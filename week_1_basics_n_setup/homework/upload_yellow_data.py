#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from time import time
import pyarrow.parquet as pq

filename = "./data/yellow_tripdata_2019-01.parquet"
file = pq.ParquetFile(filename)

table_name = "yellow_tripdata_2019_01"

connection_str = "postgresql://postgres:postgres@localhost:5432/ny_taxi"
engine = create_engine(connection_str)
# engine.connect()

df = next(file.iter_batches(batch_size=10)).to_pandas()

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

# create the table
df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace", index=False)

# Insert values
df_iter = file.iter_batches(batch_size=100000)

count = 0
t_start = time()

for batch in df_iter:
    count += 1
    print(f"inserting batch {count} ...")

    b_start = time()
    batch = batch.to_pandas()
    batch.to_sql(name=table_name, con=engine, if_exists="append", index=False)
    b_end = time()

    print(f"inserted batch {count} in {b_end - b_start:.2f} seconds")

t_end = time()
print(f"Completed in {t_end - t_start:.2f} seconds")
