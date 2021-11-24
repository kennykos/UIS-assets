import sqlite3 as sql
import os


# Connecting to the database
conn = sql.connect('investments.db')

# Creating a cursor executable
c = conn.cursor()


# creating our table if our table dose not exist
try:
    c.execute("""CREATE TABLE investments (
                account text,
                cupon real,
                maturity_data text,
                quantity integer,
                cost_value real,
                market_value real,
                industry text,
                fossil_fuel integer,
                ticker text,
                holding_class text,
                bank text
                )""")
except:
    print("table already exists")

# assign directory
directory = 'datasets2021'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)




# commiting the changes to the database
conn.commit()

# closing the connection to the database
conn.close()