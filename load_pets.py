# PART II: Existing SQL Database

import sqlite3

con = sqlite3.connect('pets.db')
print("Database loaded successfully...")

con.execute("INSERT INTO Person (id, first_name, last_name, age) \
      VALUES (1, 'James', 'Smith', 41)")
con.execute("INSERT INTO Person (id, first_name, last_name, age) \
      VALUES (2, 'Diana', 'Greene', 23)")
con.execute("INSERT INTO Person (id, first_name, last_name, age) \
      VALUES (3, 'Sara', 'White', 27)")
con.execute("INSERT INTO Person (id, first_name, last_name, age) \
      VALUES (4, 'William', 'Gibson', 23)")

con.execute("INSERT INTO Pet (id, name, breed, age, adead) \
      VALUES (1, 'Rusty', 'Dalmation', 4, 1)")
con.execute("INSERT INTO Pet (id, name, breed, age, adead) \
      VALUES (2, 'Bella', 'Alaskan Malamute', 3, 0)")
con.execute("INSERT INTO Pet (id, name, breed, age, adead) \
      VALUES (3, 'Max', 'Cocker Spaniel', 1, 0)")
con.execute("INSERT INTO Pet (id, name, breed, age, adead) \
      VALUES (4, 'Rocky', 'Beagle', 7, 0)")
con.execute("INSERT INTO Pet (id, name, breed, age, adead) \
      VALUES (5, 'Rufus', 'Cocker Spaniel', 1, 0)")
con.execute("INSERT INTO Pet (id, name, breed, age, adead) \
      VALUES (6, 'Spot', 'Bloodhound', 2, 1)")

con.execute("INSERT INTO Person_Pet (person_id, pet_id) \
      VALUES (1, 1)")
con.execute("INSERT INTO Person_Pet (person_id, pet_id) \
      VALUES (1, 2)")
con.execute("INSERT INTO Person_Pet (person_id, pet_id) \
      VALUES (2, 3)")
con.execute("INSERT INTO Person_Pet (person_id, pet_id) \
      VALUES (2, 4)")
con.execute("INSERT INTO Person_Pet (person_id, pet_id) \
      VALUES (3, 5)")
con.execute("INSERT INTO Person_Pet (person_id, pet_id) \
      VALUES (4, 6)")

con.commit()
print("Data inserted successfully...")

con.close()
