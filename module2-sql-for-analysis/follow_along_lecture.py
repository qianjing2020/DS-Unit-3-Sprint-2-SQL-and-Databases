""" part 1: Reproduce the live lecture task of setting up and inserting the RPG data into a PostgreSQL database.
"""
import os
from os import getcwd
import sys
import psycopg2
import sqlite3

sys.path.append(getcwd())
sys.path.append("/usr/bin/")

dbname = "fekuuytp"
user = "fekuuytp"
password = "08RQSNoiKG1C32Nwg18VkHcblP_-z_hD"
host = "rajje.db.elephantsql.com"

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
# create cursor object
pg_cur = pg_conn.cursor()

# connect to sqlite database rpg_db.sqlite3
filename = "/Users/jing/Documents/LambdaSchool/LS_DS_unit3/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3"
lite_conn = sqlite3.connect(filename)
lite_cur = lite_conn.cursor()
# copy characters table from SQLite to PostgreSQL
query = "SELECT * FROM charactercreator_character"
characters = lite_cur.execute(query).fetchall()

# create table
# get sqlite3 format
print(lite_cur.execute("PRAGMA table_info(charactercreator_character);").fetchall())
# format for psycopg2 database: https://www.postgresql.org/docs/current/sql-createtable.html
query = """
CREATE TABLE charactercreator_character(
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
pg_cur.execute(query)
pg_conn.commit()

# use loop to insert all data
for character in characters:
    insert_character = (
        """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """
        + str(character[1:])
        + ";"
    )
    pg_cur.execute(insert_character)

pg_conn.commit()

# confirm data has been inserted into elephantsql database
check_statement = pg_cur.execute("SELECT * FROM charactercreator_character;").fetchall()
print(check_statement)
""" Note: if error msn is "psycopg2.errors.DuplicateTable: relation "charactercreator_character" already exists", go to elephantSQL website click Reset User&Default database """