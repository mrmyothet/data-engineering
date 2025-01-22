#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from time import time

engine = create_engine("postgresql://postgres:postgres@localhost:5432/ny_taxi")
engine.connect()

filename = "./data/taxi_zone_lookup.csv"
table_name = "taxi_zone_lookup"


df = pd.read_csv(filename)

df.head(n=0).to_sql(table_name, con=engine, if_exists="replace", index=False)
# print(pd.io.sql.get_schema(df, table_name, con=engine))

t_start = time()
df.to_sql(table_name, con=engine, if_exists="append", index=False)
t_end = time()

print(f"Completed in {t_end - t_start:.2f} seconds")
