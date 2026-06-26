import sqlite3

conn = sqlite3.connect("instance/adam.db")

cursor = conn.cursor()

print("\nEVENTS")
cursor.execute("SELECT * FROM events")
for row in cursor.fetchall():
    print(row)

print("\nALERTS")
cursor.execute("SELECT * FROM alerts")
for row in cursor.fetchall():
    print(row)

print("\nCOMMANDS")
cursor.execute("SELECT * FROM commands")
for row in cursor.fetchall():
    print(row)

conn.close()