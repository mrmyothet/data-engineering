#!/usr/bin/env python

# pip install pgcli
# pip install sqlalchemy
# pip install psycopg2-binary
# pip install pyarrow

import argparse, os, sys
from time import time
import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    tb = params.tb
    url = params.url

    # Get file name from url
    filename = url.rsplit("/", 1)[-1].strip()

    print(f"Downloading {filename} ...")
    os.system(f"curl {url.strip()} -o {filename}")
    print("\n")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    # Read file based on csv or parquet
    if ".csv" in filename:
        df = pd.read_csv(filename, nrows=10)
        df_iter = pd.read_csv(filename, iterator=True, chunksize=100000)
    elif ".parquet" in filename:
        file = pq.ParquetFile(filename)
        df = next(file.iter_batches(batch_size=10)).to_pandas()
        df_iter = file.iter_batches(batch_size=100000)
    else:
        print("Error. only .csv or .parquet files allowed.")
        sys.exit()

    # create the table
    df.head(0).to_sql(name=tb, con=engine, if_exists="replace")

    # Insert values
    t_start = time()
    count = 0

    for batch in df_iter:
        count += 1

        if ".parquet" in filename:
            batch_df = batch.to_pandas()
        else:
            batch_df = batch

        print(f"inserting batch {count} ...")

        b_start = time()
        batch_df.to_sql(name=tb, con=engine, if_exists="append")
        b_end = time()

        print(f"inserted! time taken {b_end-b_start:10.3f} seconds. \n")

    t_end = time()
    print(
        f"Completed! Total time taken was {t_end-t_start:10.3f} seconds for {count} batches."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Loading data from .parquet file link to a postgres database"
    )

    parser.add_argument("--user", help="username for postgres")
    parser.add_argument("--password", help="password of the user of postgres")
    parser.add_argument("--host", help="Hostname of postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db", help="database name for postgres")
    parser.add_argument("--tb", help="table name for postgres")
    parser.add_argument("--url", help="URL for the data file (.parquet or .csv)")

    args = parser.parse_args()
    main(args)
