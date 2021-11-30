import sqlite3 as sql
import os
import csv
import re


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


# cleaning up the database
def get_ff_comps(result=None):
    if result is None:
        result = []
    # suffix
    suffix = [" MKTS", " NT", " INC", "CHEVRON", "CENTERPOINT ENERGY", " CO", "DUKE ENERGY", "DTE E", "SCHLUMBERGER", " 66"]
    for row in c.execute('SELECT * FROM investments ORDER BY -fossil_fuel'):
        # Itterate as long as we have a fossil fuel company
        if row[7] != 1:
            break
        company = row[0]
        company = company.replace("PVTPL ", "")
        company = company.replace(".", "")
        
        # remove everything after a number
        m = re.search(r"\d", company)
        if m is not None and "66" not in company:
            # print(company[m.start() : m.start() + 2])
            company = company[:m.start()]
        
        # remove everything after suffixes
        if 1:
            for s in suffix:
                if s in company:
                    company = company[:company.index(s) + len(s)]


        result.append(company.strip())
    # return a list without any duplacates
    result = list(set(result))
    result.sort()
    return result


# update the table to include investments we missed
def update():
    ff_cos = get_ff_comps()
    i = 0
    for row in c.execute('SELECT * FROM investments'):
        if any(c in row[0] for c in ff_cos) and row[7] != 1:
            # update the ff marker to 1
            c.execute('UPDATE investments SET fossil_fuel = 1 WHERE account=:name', {'name': row[0]})

# call the update function on the database to clean up any messes
update()

# commiting the changes to the database
conn.commit()

# closing the connection to the database
conn.close()