import pandas as pd
from sqlalchemy import create_engine
from time import time
import sys

# yellow_tripdata_2024-01.csv
filename = sys.argv[1]
table_name = "yellow_taxi_data"


print("pandas version: ", pd.__version__)

print("connecting to the postgresql database")
engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")
engine.connect()

df = pd.read_csv(filename, nrows=100)
pd.io.sql.get_schema(df, "yellow_taxi_data", con=engine)

df_iter = pd.read_csv(filename, iterator=True, chunksize=100000)
df = next(df_iter)

print("length of data frame: ", len(df))

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
df.head(n=0).to_sql(con=engine, name=table_name, if_exists="replace", index=False)

df.tosql(con=engine, name=table_name, if_exists="append", index=False)

while True:
    try:

        t_start = time()

        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(con=engine, name=table_name, if_exists="append", index=False)

        t_end = time()

        print("inserted another chunk ..., took %.3f seconds" % (t_end - t_start))
    except StopIteration:
        break
