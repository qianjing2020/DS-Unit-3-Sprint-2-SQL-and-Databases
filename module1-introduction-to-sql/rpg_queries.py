import sys
print(sys.version) # python version
print(sys.executable) # python exe file path

from os import getcwd
mywd = getcwd() # get current working directory
sys.path.append(mywd)

filename = 'rpg_db.sqlite3'
import sqlite3
con = sqlite3.connect(filename)
cur = con.cursor()
# How many total Characters are there?
get_counts = 'SELECT COUNT(*) FROM charactercreator_character'
character_counts = cur.execute(get_counts).fetchall()
print(character_counts)
# How many Items does each character have? (Return first 20 rows)
get_item_count_per_character = """SELECT COUNT(character_id), item_id 
FROM charactercreator_character_inventory 
GROUP BY item_id 
ORDER BY COUNT(character_id) DESC
LIMIT 20 """

item_count_per_character = cur.execute(get_item_count_per_character).fetchall()

print(item_count_per_character)

#How many Weapons does each character have? (Return first 20 rows)
get_weapon_count_per_character = """
SELECT character_id, COUNT(character_id), item_id 
FROM charactercreator_character_inventory i
INNER JOIN armory_weapon w
ON w.item_ptr_id = i.item_id
GROUP BY character_id
LIMIT 20
"""
weapon_count_per_character = cur.execute(
    get_weapon_count_per_character).fetchall()
print(weapon_count_per_character)    


# Extract characters
get_characters = 'SELECT * FROM charactercreator_character'
characters = cur.execute(get_characters).fetchall


"""
# find the total number of items in armory_item table
get_counts = 'SELECT COUNT(*) FROM armory_item'
get_armory_item = 'SELECT * FROM armory_item'
get_armory_weapon = 'SELECT * FROM armory_weapon'

armory_counts = curs.execute(get_counts).fetchall()
armory_items = curs.execute(get_armory_item).fetchall()
armory_weapon = curs.execute(get_armory_weapon).fetchall()

count_weapon = len(armory_weapon)
count_armory = len(armory_items)
count_non_weapon = count_armory-count_weapon
#curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

# How many Items does each character have? (Return first 20 rows)
get_item_count_per_character = """
SELECT COUNT(character_id), item_id
FROM charactercreator_character_inventory
GROUP BY item_id
ORDER BY COUNT(character_id) DESC
LIMIT 20
"""
item_count_per_character = curs.execute(
    get_item_count_per_character).fetchall()

#How many Weapons does each character have? (Return first 20 rows)
get_weapon_count_per_character = """
SELECT COUNT(character_id), character_id, item_id
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
GROUP BY item_id
LIMIT 20
"""
weapon_count_per_character = curs.execute(
    get_weapon_count_per_character).fetchall()

# On average, how many Items does each Character have?
sum_item = [lis[0] for lis in item_count_per_character]
avg_item_per_character = sum(sum_item)/len(item_count_per_character)
avg_item_per_character

# On average, how many Weapons does each Character have?
sum_weapon = [lis[0] for lis in weapon_count_per_character]
avg_weapon_per_character = sum(sum_weapon)/len(weapon_count_per_character)
avg_weapon_per_character

conn.close()


"""
Part 2
"""
import pandas as pd
df = pd.read_csv('buddymove_holidayiq.csv')
print(df.dtypes)
conn = sqlite3.connect()
curs = conn.cursor()
# Create table
db_file = 'buddymove_holidayiq.sqlite3'
table_1 = 'table_1'
#curs.execute('CREATE TABLE {tn}'\
#    .format(tn=table_1)
