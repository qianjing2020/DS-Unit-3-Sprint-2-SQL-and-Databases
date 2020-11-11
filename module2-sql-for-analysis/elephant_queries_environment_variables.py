import os
import json
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values

# cool to know, prefix like 
# $ dbname='pear' user='apple' python elephant_queries_env_var.py 
# can pass the dbname to python variable

# load the content of the env file where DB Credentials are stored
load_dotenv() 

dbname = os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
#print(dbname, user, password, host)
#exit()

### Connect to ElephantSQL
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()

### Note different from sqlite: we can do result=cur.excecute(query).fetchall()
# but in psycopg, it is a two step process: curson execute query first then fetch
cur.execute('SELECT * from test_table;')

result = cur.fetchall()
print(result)

# insert data
'''insertion_sql = """
INSERT INTO  test_table (name, data) VALUES
('row 1', null),
('row 2', '{"a":1, "b":["dog", "cat", 12], "c":true}'::JSONB);
"""
cur.execute(insertion_sql)

'''

# insert one row at a time, dict used for data
"""my_dict = {"a":1, "b":["dog", "cat", 12], "c":True}
insertion_sql = "INSERT INTO test_table (name, data) VALUES (%s, %s)"
cur.execute(insertion_sql, ("another row with JSONNNNN", json.dumps(my_dict)))
"""
# insert multiple rows at a time, could be time consuming
my_dict = {"a":1, "b":["dog", "cat", 12], "c":True}
insertion_sql = "INSERT INTO test_table (name, data) VALUES %s"

data_tuples = [ 
    ('a row', 'null'),
    ('ano row', "3"),
    ("another row with JSONNNNN", json.dumps(my_dict))
]
execute_values(cur, insertion_sql, data_tuples ) # data must be a list of tuples!!!!!

conn.commit()
cur.close()
conn.close()

