import sqlite3 as sql
from locale import atof, setlocale, LC_NUMERIC

# for string to float conversion
setlocale(LC_NUMERIC, '')

# Connecting to the database
conn = sql.connect('UIS_FY21_Investments.db')

# Creating a cursor executable
c = conn.cursor()

def get_total_ff():
    # summing the totoal market value of all of the fossil fuel companies
    # SUM("CASE WHEN fossil_fuel = '1' THEN market_value END")
    sum = 0
    for row in c.execute('SELECT * FROM investments ORDER BY -fossil_fuel'):
        # Itterate as long as we have a fossil fuel company
        if row[7] != 1:
            break
        sum += atof(row[5])
    # the ammount of money in fossil fuel companies, formated nicley
    return '{0:,.2f}'.format(round(sum, 2))

# Note that no changes need to be committed to the database in this file

# closing the connection to the database
conn.close()