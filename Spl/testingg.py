import mysql.connector
from pripojeni import *

mydb = mysql.connector.connect(
    host = HOST
    ,user = USER
    ,password = PASSWORD
    ,database = DATABASE
)
mycursor = mydb.cursor()

# TODO: zde vytvořte tabulku
mycursor.execute("""CREATE TABLE Uzivatel(
    id int(11),
    jméno char(10),
    příjmení char(20),
    email char(50)
)""")



mydb.commit()

# tuto část neměnit!
mycursor.execute("""DESCRIBE Uzivatel""")
table = str(mycursor.fetchall())
expected = "[('id', 'int(11)', 'YES', '', None, ''), ('jméno', 'char(10)', 'YES', '', None, ''), ('příjmení', 'char(20)', 'YES', '', None, ''), ('email', 'char(50)', 'YES', '', None, '')]"
if table == expected:
    print("Tabulka vytvořena správně.")
else:
  print("Tabulka není dle zadání.\nVaše tabulka:")
  print(table)
  print("Očekávaná tabulka:")
  print(expected)
  print("Výpis se liší na pozicích:", [ i for i in range(min(len(table),len(expected))) if table[i] != expected[i] ])


mycursor.execute("""DROP TABLE Uzivatel""")
mydb.commit()

mycursor.close()
mydb.close()