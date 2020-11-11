""" part2, set up a new table for the Titanic data (titanic.csv). Write an insert_titanic.py script that uses psycopg2 to connect to and upload the data from the csv, and add the file to your repo. Then start writing PostgreSQL queries to explore the data!
"""
import io
from sqlalchemy import create_engine
import os
from os import getcwd
import sys

sys.path.append(getcwd())
sys.path.append("/usr/bin/")

import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")
print(df.head(5))
#x = df['Name'].str.count() 
#print(x) # show the char length of the longest Name   ???why these two lines won't work?
db_url = "postgres://fekuuytp:08RQSNoiKG1C32Nwg18VkHcblP_-z_hD@rajje.db.elephantsql.com:5432/fekuuytp"

conn, cur = connect_postgresql(db_url)

# return the names of tables in a database
cur.execute(
    """
       SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'
       """
)
#for table in cur.fetchall():

# # create table
# create_table_statement = """
# CREATE TABLE titanic(
#     survivor_id SERIAL PRIMARY KEY,
#     survived INT,
#     pclass INT,
#     name VARCHAR(100),
#     sex VARCHAR(6),
#     age FLOAT8,
#     siblings_spouses_aboard INT,
#     parents_children_aboard INT,
#     fare FLOAT8
# );"""

# cur.execute(create_table_statement)


from sqlalchemy import create_engine
import io
engin_url = 'postgresql+psycopg2:'+ db_url.split(':', 1)[1]
engine = create_engine(engin_url)

df.head(0).to_sql('table_name', engine, if_exists='replace',
                  index=False)  # truncates the table

eng_conn = engine.raw_connection()
eng_cur = eng_conn.cursor()
output = io.StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
eng_cur.copy_from(output, 'table_name', null="")  # null values become ''
eng_conn.commit()











