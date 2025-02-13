#! /usr/bin/env python

# pip install "dlt[duckdb]"
# pip install "dlt[gs]"

import dlt
import os

# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

# project_id = os.getenv("CREDENTIALS__PROJECT_ID")
# refresh_token = os.getenv("CREDENTIALS__REFRESH_TOKEN")
# client_secret = os.getenv("CREDENTIALS__CLIENT_SECRET")
# client_id = os.getenv("CREDENTIALS__CLIENT_ID")
bucket_url = os.getenv(key="BUCKET_URL")

# print(f"project_id: {project_id}")
# print(f"refresh_token: {refresh_token}")
# print(f"client_secret: {client_secret}")
# print(f"client_id: {client_id}")
print(f"bucket_url: {bucket_url}")

# Sample data containing pokemon details
data = [
    {"id": "1", "name": "bulbasaur", "size": {"weight": 6.9, "height": 0.7}},
    {"id": "4", "name": "charmander", "size": {"weight": 8.5, "height": 0.6}},
    {"id": "25", "name": "pikachu", "size": {"weight": 6, "height": 0.4}},
]

pipeline = dlt.pipeline(
    pipeline_name="quick_start", destination="filesystem", dataset_name="ny_taxi"
)


load_info = pipeline.run(
    data,
    table_name="pokemon",
)
print(load_info)
