#Python Code to Access Data from PostgreSQL

import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

#method to convert query result to pandas dataframe
def create_df(sql_query, database):
    table = pd.read_sql_query(sql_query, database)
    return table

#method to connect and query PostgreSQL database
def get_data():
    try:
        conn_db = psycopg2.connect(database = os.getenv("database_name"),
                                   user = os.getenv("user_name"),
                                   password = os.getenv("password"),
                                   host = os.getenv("host_name"),
                                   port = os.getenv("port_number"))
    except psycopg2.OperationalError as e:
        print("DB connection failed\n",e)
    else:
        print("Successfully connected to DB")
        cur = conn_db.cursor()
        data = create_df('SELECT * FROM table_name', conn_db)
        cur.close()
        conn_db.close()
        return data

df = get_data()
print(df.shape)
print(df.head())