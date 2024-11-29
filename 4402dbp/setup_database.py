# this will execute the sql file and set up the database 

import sqlite3

conn = sqlite3.connect('movie_theater.db')
cursor = conn.cursor()

with open ('create_theater.sql' , 'r') as file:
    sql_script = file.read()
    
cursor.executescript(sql_script)
conn.commit()
conn.close()

print ("database schema created successfully")
