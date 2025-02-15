import dlt
import pandas as pd
from sqlalchemy import create_engine
from dlt.sources.helpers import requests

data = [
    {"id": "1", "name": "bulbasaur", "size": {"weight": 6.9, "height": 0.7}},
    {"id": "4", "name": "charmander", "size": {"weight": 8.5, "height": 0.6}},
    {"id": "25", "name": "pikachu", "size": {"weight": 6, "height": 0.4}},
]

pipeline = dlt.pipeline(
    pipeline_name="quick_start",
    destination="duckdb",
    dataset_name="mydata",
    dev_mode=True,
)

load_info = pipeline.run(data, table_name="pokemon")
print(load_info)


# List of dicts
@dlt.resource(table_name="pokemon_new")
def my_dict_list():
    yield data


load_info = pipeline.run(my_dict_list)
print(load_info)

pipeline.dataset(dataset_type="default").pokemon_new.df()


# Dataframes
@dlt.resource(table_name="df_data")
def my_df():
    sample_df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
    yield sample_df


load_info = pipeline.run(my_df)
print(load_info)

pipeline.dataset(dataset_type="default").df_data.df()


# Database
@dlt.resource(table_name="genome_data")
def get_genome_data():
    engine = create_engine(
        "mysql+pymysql://rfamro@mysql-rfam-public.ebi.ac.uk:4497/Rfam"
    )
    with engine.connect() as conn:
        query = "SELECT * FROM genome LIMIT 1000"
        rows = conn.execution_options(yield_per=100).exec_driver_sql(query)
        yield from map(lambda row: dict(row._mapping), rows)


load_info = pipeline.run(get_genome_data)
print(load_info)

pipeline.dataset(dataset_type="default").genome_data.df()


# REST API


@dlt.resource(table_name="pokemon_api")
def get_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon"
    response = requests.get(url)
    yield response.json()["results"]


load_info = pipeline.run(get_pokemon)
print(load_info)

pipeline.dataset(dataset_type="default").pokemon_api.df()

# load all resources into a single pipeline
load_info = pipeline.run([my_df, get_genome_data, get_pokemon])
print(load_info)
