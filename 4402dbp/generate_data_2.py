import sqlite3
import pandas as pd

# Function to clear existing data in the database
def clear_existing_data(cursor):
    try:
        # List of tables to clear data from
        tables = ['Customer', 'Movies', 'Theater', 'Membership']
        
        for table in tables:
            cursor.execute(f"DELETE FROM {table}")
        print("Existing data cleared.")
    except sqlite3.Error as e:
        print(f"Error while clearing data: {e}")

# Function to check if the table exists in the database
def table_exists(cursor, table_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    tables_in_db = [t[0] for t in tables]  # Extract table names from the result
    return table_name in tables_in_db

# Function to insert data from Excel into the database
def insert_data_from_excel(db_connection, excel_file):
    try:
        # Read the Excel file using pandas
        xl = pd.ExcelFile(excel_file)
        
        # Print sheet names to check the Excel file structure
        print(f"Sheet names in the Excel file: {xl.sheet_names}")
        
        # Loop through all sheets in the Excel file
        for sheet_name in xl.sheet_names:
            df = xl.parse(sheet_name, header=0)  # Ensure the first row is treated as headers
            
            # Check if the table exists in the database
            cursor = db_connection.cursor()
            if not table_exists(cursor, sheet_name):
                print(f"Table {sheet_name} does not exist in the database. Skipping data insertion for this sheet.")
                continue  # Skip if table doesn't exist
            
            # Prepare data for insertion
            for _, row in df.iterrows():
                # Construct SQL insert statement
                columns = ', '.join([f'"{col}"' for col in df.columns])  # Quote column names
                placeholders = ', '.join(['?'] * len(df.columns))  # Use placeholders for values
                values = tuple(row)  # Row values as tuple
                
                # Insert data into the corresponding table
                query = f'INSERT INTO "{sheet_name}" ({columns}) VALUES ({placeholders})'
                try:
                    cursor.execute(query, values)
                except sqlite3.IntegrityError as e:
                    if 'UNIQUE constraint failed' in str(e):
                        print(f"Skipping row due to UNIQUE constraint violation: {row.to_dict()}")
                    else:
                        print(f"Error inserting row {row.to_dict()}: {e}")
            
            print(f"Data inserted for table: {sheet_name}")
        
        # Commit the transaction after all data is inserted
        db_connection.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")



# Main function to populate the database
def populate_database(excel_file, db_file):
    try:
        # Set up the database connection
        db_connection = sqlite3.connect(db_file)
        cursor = db_connection.cursor()
        
        # Step 1: Clear existing data in the database
        clear_existing_data(cursor)
        
        # Step 2: Insert data from Excel file into the database
        insert_data_from_excel(db_connection, excel_file)
        
        # Step 3: Close the database connection
        db_connection.close()
        print("Database connection closed.")
    
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Run the code
if __name__ == "__main__":
    excel_file = 'MovieDataBase.xlsx'  # Path to your Excel file
    db_file = 'movie_theater.db'         # Path to your SQLite database
    
    populate_database(excel_file, db_file)
