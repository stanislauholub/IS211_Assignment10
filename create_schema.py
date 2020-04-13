# PART II: Existing SQL Database

import sqlite3

con = sqlite3.connect('pets.db')
print("Database loaded successfully...")

con.execute('''CREATE TABLE person (
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
age INTEGER
);''')

con.execute('''CREATE TABLE pet (
id INTEGER PRIMARY KEY,
name TEXT,
breed TEXT,
age INTEGER,
adead INTEGER
);''')

con.execute('''
CREATE TABLE person_pet (
person_id INTEGER,
pet_id INTEGER
);''')

print("Table created successfully...")

con.close()
