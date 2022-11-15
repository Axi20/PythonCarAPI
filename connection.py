import sqlite3

con = sqlite3.connect("CarRentDB.db")
print("Database opened successfully")
con.close()