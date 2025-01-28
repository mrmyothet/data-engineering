#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from time import time

engine = create_engine("postgresql://postgres:postgres@localhost:5432/ny_taxi")
engine.connect()

df = pd.read_csv("./data/green_tripdata_2019-10.csv", nrows=1000)

df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
# print(pd.io.sql.get_schema(df, 'green_tripdata_2019_10', con=engine))

df.head(n=0).to_sql(
    "green_tripdata_2019_10", con=engine, if_exists="replace", index=False
)

df_iter = pd.read_csv(
    "./data/green_tripdata_2019-10.csv", chunksize=10000, iterator=True
)

count = 0
t_start = time()

for batch in df_iter:
    count += 1
    print(f"inserting batch {count} ...")

    b_start = time()
    batch.to_sql("green_tripdata_2019_10", con=engine, if_exists="append", index=False)
    b_end = time()

    print(f"inserted batch {count} in {b_end - b_start:.2f} seconds")

t_end = time()
print(f"Completed in {t_end - t_start:.2f} seconds")
