# app/mongo_queries.py

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
#connection_URI = "mongodb+srv://user123:<password>@cluster0.9zzsj.mongodb.net/<dbname>?retryWrites=true&w=majority"

print("----------------")
print("URI:", connection_uri)

# exit()

client = MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

"""create database"""
db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

"""create collection"""
collection = db.pokemon_test # "pokemon_test" or whatever you want to call it

print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

"""create document with defined fields
"""
"""insert one"""
collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
    "parents": ["Pikachu I", "Aichu"],
    "other_attr": {"a":1, "b":2, "c":3}
})
# count all document from collection
print("DOCS:", collection.count_documents({}))

# count all document with filter
print(collection.count_documents({"name": "Pikachu"}))

"""insert many"""
eevee = {"name":"Eevee", "level": 40, "exp": 7500, "hp":120}
chansey = {"name":"Chansey", "egg group": "Fairy", "Pokedex Color": "pink"}
jirachi = {"name":"Jirachi",  "egg group": "Undiscovered", "Pokedex Color": "yellow"}

team = [eevee, chansey, jirachi]

collection.insert_many(team)
print(collection.count_documents({}))

# find all pokemons whose level>20

for doc in collection.find({"level": {"$gt":20}}): 
    print(doc)
