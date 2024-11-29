# i am populating all the tables datas here 

import sqlite3
import pandas as pd

def populate_database_from_excel(excel_file):
    conn = sqlite3.connect('movie_theater.db')
    cursor = conn.cursor()

    data = pd.ExcelFile(excel_file)

    tables = ["Customer", "Membership", "Movies", "Genre", "Theater", "Employee", "MovieTime", "Tickets", "Seat", "Rating"]
    for table in tables:
        cursor.execute(f"DELETE FROM {table}")

    for DataBase in data.DataBase:
        df = data.parse(DataBase)

        try:
            df.to_sql(DataBase, conn, if_exists='append', index=False)
            print(f"data inserted successfully into {DataBase} table.")
        except Exception as e:
            print(f"error inserting data into {DataBase} table: {e}")

    conn.commit()
    conn.close()
    print("database populated successfully from Excel file")

if __name__ == "__main__":
    excel_file_path = 'Movie_Database.xlsx'
    populate_database_from_excel(excel_file_path)
