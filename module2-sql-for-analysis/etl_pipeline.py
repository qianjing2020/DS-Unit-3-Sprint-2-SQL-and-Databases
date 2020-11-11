"""A pipeline to get data from sqlite db and insert to elephant sql db using OOP approach
"""

import os
import json
from dotenv import load_dotenv
import sqlite3
import psycopg2
from psycopg2.extras import execute_values

load_dotenv() 

dbname = os.getenv("dbname", default="OOPS")
user = os.getenv("user", default="OOPS")
password = os.getenv("password", default="OOPS")
host = os.getenv("host", default="OOPS")

db_filepath = os.path.join(os.path.dirname(__file__),"..", "data", "rpg_db.sqlite3")

class SqliteService():
    def __init__(self, db_filepath=db_filepath):
        self.connection = sqlite3.connect(db_filepath)
        self.cursor = self.connection.cursor()
    
    def fetch_characters(self):
        return self.connection.execute("SELECT * FROM charactercreator_character;").fetchall()

class ElephantsqlService():
    def __init__(self):
        self.connection = psycopg2.connect(dbname=dbname, user=user,password=password,host=host)
        self.cursor = self.connection.cursor()
    
    def create_characters_table(self):
        create_queries = """
        DROP TABLE IF EXISTS characters; --allows this to run idempotentialy, avoids psycopg error
        CREATE TABLE IF NOT EXISTS characters (
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
        print(create_queries)
        self.cursor.execute(create_queries)
        self.connection.commit()
        
    
    def insert_characters(self, characters):
        """characters need to be a list of tuples"""

        insert_queries = """
        INSERT INTO characters (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) 
        VALUES %s
        """
        
        execute_values(self.cursor, insert_queries, characters)
        self.connection.commit()


if __name__=="__main__":
    # get character data from local sqlite db
    sqlite_service = SqliteService()

    characters = sqlite_service.fetch_characters()
    
    # insert to elephantsql db
    pg_service = ElephantsqlService()
    pg_service.create_characters_table()
    
    # print(characters[0])
    
    pg_service.insert_characters(characters)
    



