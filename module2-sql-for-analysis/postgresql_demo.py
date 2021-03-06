# -*- coding: utf-8 -*-
"""JingQian_Lambda School DS10 Unit 3 Sprint 2 Module 2 - PostgreSQL Demo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r4KXrzprT-ziOsmM3GgwgHIPHog7COeZ

# Live Demo Code for Connecting to PostgreSQL from Python

Notebook for your helpful reference - the assignment still requires writing .py files!
"""

!pip install psycopg2-binary

# Psycopg is the most popular PostgreSQL database adapter for the Python
import psycopg2

dir(psycopg2)

# psycopg2.connect looks like it may be interesting!
# (Similar to how sqlite3 module worked)
help(psycopg2.connect)

# get this information from your elephant sql personal website
dbname = 'fekuuytp'
user = 'fekuuytp'
password = '08RQSNoiKG1C32Nwg18VkHcblP_-z_hD' 
host = 'rajje.db.elephantsql.com' # port should be included or default
pg_conn = psycopg2.connect(database=dbname, user=user, password=password, host=host)

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_conn

dir(pg_conn)

pg_curs = pg_conn.cursor()
# create a cursor class, it allows Python code to execute PostgreSQL command in a database session

help(pg_curs.execute)

create_table_statement = """
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
"""

pg_curs.execute(create_table_statement)
pg_conn.commit() # Commit any pending transaction to the database

insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""

pg_curs.execute(insert_statement)
pg_conn.commit()

query = "SELECT * FROM test_table;"
pg_curs.execute(query)
pg_curs.fetchall()

"""# ETL - RPG data from SQLite to PostgreSQL

We'd like to get the RPG data out of SQLite and insert it into PostgreSQL.

Aka - we're making a data pipeline! Aka - an ETL (Extract Transform Load). Our first "cloud" ETL!
"""

!wget https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true

!mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3
# move command, can be used to rename file

!ls

import sqlite3
sl_conn  = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# We care about charactercreator_character table
row_count = 'SELECT COUNT(*) FROM charactercreator_character'
sl_curs.execute(row_count).fetchall()

# Our goal - copy the characters table from SQLite to PostgreSQL using Python
# Step 1 - E=Extract: Get the Characters
get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

characters[:5]

len(characters)

# Step 2 - Transform
# In this case, we don't actually want/need to change much
# Because we want to keep all the data
# And we're going from SQL to SQL

# But what do we need to be able to load into PostgreSQL?
# We need to make a new table with the appropriate schema

# What was the old schema? We can get at this with SQLite internals
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

# https://www.postgresql.org/docs/current/sql-createtable.html

create_character_table = """
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""

pg_curs.execute(create_character_table)
pg_conn.commit()

# We can query tables if we want to check
# This is a clever optional thing, showing postgresql internals
show_tables = """
SELECT
   *
FROM
   pg_catalog.pg_tables
WHERE
   schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_tables)
pg_curs.fetchall()

characters[0]

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ";"

print(example_insert)

# How do we do this for all characters? Loops!
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)
# pg_conn.commit()

pg_curs.execute('SELECT * FROM charactercreator_character')
pg_curs.fetchall()

pg_conn.commit()

# A quick test that we did this correctly
pg_curs.execute('SELECT * FROM charactercreator_character')
pg_characters = pg_curs.fetchall()

characters[0]

pg_characters[0]

for character, pg_character in zip(characters, pg_characters):
  assert character == pg_character

# No complaints, which means they're all the same!