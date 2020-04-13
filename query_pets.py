# PART II: Existing SQL Database

import sqlite3

con = sqlite3.connect('pets.db')
print("Database is loaded successfully...")

while True:
    result = False
    n = input("Enter Person’s ID number: ")
    if n == "-1":
        print("You have successfully exit the program.")
        break
    else:
        cursor = con.execute("SELECT * FROM person WHERE Id =" + str(n))

        for row in cursor:
            result = True
            print("Owner Details:")
            print(row[1], row[2] + ",", row[3], "years old.")
            cursor1 = con.execute("SELECT * FROM person_pet WHERE Person_id =" + str(n))
            print("Pet Details:")
            for row1 in cursor1:
                cursor2 = con.execute("SELECT * FROM pet WHERE Id =" + str(row1[1]))

                for row2 in cursor2:
                    print(row[1], row[2] + " owned", row2[1] + ",", "a " + row2[2] + ",", "that was", row2[3],
                          "years old.")

    if not result:
        print("Error! No such user exists in the database.")

con.close()
