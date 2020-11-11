import os
from os import getcwd
import sys

sys.path.append(getcwd())
import sqlite3
import pandas as pd

# connect
con = sqlite3.connect("soccer.sqlite")
cursor = con.cursor()
# return the names of tables in a database
for table in cursor.execute("SELECT name from sqlite_master WHERE type='table';"):
    print(table)
# create pandas dataframe from sql data
country = pd.read_sql_query("SELECT * FROM Country", con)
league = pd.read_sql_query("SELECT * FROM League", con)
player = pd.read_sql_query("SELECT * FROM Player", con)
print(country.head(3))

# create dataframe with condition
height_150 = pd.read_sql_query("SELECT * FROM Player WHERE height > 150", con)
print(height_150.head(3))
con.close()
