import os

from time import time

import pandas as pd
from sqlalchemy import create_engine


def ingest_yellow_callable(
    user, password, host, port, db, table_name, csv_file, execution_date
):
    print(table_name, csv_file, execution_date)

    # engine = create_engine("postgresql://postgres:posgres@postgres_db:5432/ny_taxi")
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    try:
        engine.connect()
        print("connection established successfully ... ")

    except Exception as e:
        raise Exception(f"postgres database connection failed {e}")

    print(" inserting data ... ")

    t_start = time()
    df_iter = pd.read_csv(csv_file, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")

    df.to_sql(name=table_name, con=engine, if_exists="append")

    t_end = time()
    print("inserted the first chunk, took %.3f second" % (t_end - t_start))

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

        print("inserted another chunk, took %.3f second" % (t_end - t_start))
