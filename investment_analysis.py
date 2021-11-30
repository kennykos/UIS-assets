import sqlite3 as sql
from locale import atof, setlocale, LC_NUMERIC
from database import get_ff_comps, update

# for string to float conversion
setlocale(LC_NUMERIC, '')

# Connecting to the database
conn = sql.connect('UIS_FY21_Investments.db')

# Creating a cursor executable
c = conn.cursor()

def get_total_capital_in_ff():
    # summing the totoal market value of all of the fossil fuel companies
    # SUM("CASE WHEN fossil_fuel = '1' THEN market_value END")
    sum = 0
    for row in c.execute('SELECT * FROM investments ORDER BY -fossil_fuel'):
        # Itterate as long as we have a fossil fuel company
        if row[7] != 1:
            break
        sum += atof(row[5])
    # the ammount of money in fossil fuel companies, formated nicley
    return '{0:,.2f}'.format(round(sum, 2)), sum

# make sure to update the database
update()

# output to user
print("The University of Illinois System (UIS) has $" + get_total_capital_in_ff()[0] + " out of the $2,809,677,874.72 opperating pool funds (" + str(round((get_total_capital_in_ff()[1]/2809677874.72) * 100, 2)) +"%) invested in " + str(len(get_ff_comps())) + " companies that extract, transpot, and/or distribute fossil fuels.", '\n')
print("Here is a comprehensive list of these companies: ", '\n', get_ff_comps(), '\n')
print('More information on UIS investments can be found at:', "https://www.treasury.uillinois.edu/investments")
# Note that no changes need to be committed to the database in this file

# closing the connection to the database
conn.close()