import logging

import pyarrow.csv as pv
import pyarrow.parquet as pq


def format_to_parquet(src_file):
    if not src_file.endswith(".csv"):
        logging.error("Can only accept source files in CSV format")
        return

    table = pv.read_csv(src_file)
    pq.write_table(table, src_file.replace(".csv", ".parquet"))
