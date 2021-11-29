import sqlite3 as sql
import os
import csv


# Connecting to the database
conn = sql.connect('UIS_FY21_Investments.db')

# Creating a cursor executable
c = conn.cursor()


# Deleting our table if it already exists
c.execute("DROP TABLE IF EXISTS investments")
# creating our table
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
            asset_class text,
            bank text
            )""")

# assign directory
directory = 'datasets2021'

# list of asset class types
asset_class_lst = ["Asset-Backed Securities", 
                    "Corporate Bonds", 
                    "U.S. Agency Bonds", 
                    "U.S. Treasury Securities", 
                    "Commercial Mortgage Backed Securities",
                    "Municipal Bonds",
                    ]
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        # get the name of the bank for each file
        bank = f[f.rfind('-') + 1 : f.rfind(".")]
        with open(f) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            asset_class = " "
            for row in csv_reader:
                # do something
                if row[0] in asset_class_lst:
                    # get the asset class subgroup
                    asset_class = row[0]
                account = row[0]            #type text
                cupon = row[1]
                maturity_data = row[2]
                quantity = row[3]
                cost_value = row[4]
                market_value = row[5]
                industry = row[6]
                fossil_fuel = row[7]
                ticker = row[8]
                c.execute("""INSERT INTO investments(account, cupon, maturity_data, quantity, cost_value, market_value, industry, fossil_fuel, ticker, asset_class, bank)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?)""", (account, cupon, maturity_data, quantity, cost_value, market_value, industry, fossil_fuel, ticker, asset_class, bank))
# commiting the changes to the database
conn.commit()

# closing the connection to the database
conn.close()