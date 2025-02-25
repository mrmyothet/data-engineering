import os

from time import time

import pandas as pd
from sqlalchemy import create_engine


def ingest_yellow_pg(
    user, password, host, port, db, table_name, csv_file, execution_date
):
    print(table_name, csv_file, execution_date)
    print(f"User:{user}, Password: {password}, Host:{host}, Port:{port}, DB: {db}")

    # engine = create_engine("postgresql://postgres:posgres@postgres_db:5432/ny_taxi")
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    try:
        engine.connect()
        print("connection established successfully ... ")

    except Exception as e:
        raise Exception(f"postgres database connection failed {e}")

    print(" inserting data ... ")

    f_start = time()
    df_iter = pd.read_csv(csv_file, iterator=True, chunksize=100000)

    while True:
        t_start = time()

        try:
            df = next(df_iter)
        except StopIteration:
            print("completed")
            break

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists="append")

        t_end = time()

        print("inserted one chunk, took %.3f second" % (t_end - t_start))

    f_end = time()
    print("inserted the file, took %.3f second" % (f_end - f_start))
