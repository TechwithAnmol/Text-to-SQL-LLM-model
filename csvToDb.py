import pandas as pd
import sqlite3

def csv_to_sqlite(csv_file, db_file, table_name):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    data = cursor.execute("PRAGMA table_info(DATA);")
    for i in data:
        print(i)
    # Write the data to a sqlite table
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    # Commit and close the connection
    conn.commit()
    conn.close()




# Specify the CSV file path, SQLite database file path, and table name
csv_file = 'data.csv'
db_file = 'data.db'
table_name = 'DATA'
# Call the function to convert CSV to SQLite
csv_to_sqlite(csv_file, db_file, table_name)

print(f"CSV file '{csv_file}' has been successfully converted to SQLite database '{db_file}' with table name '{table_name}'.")
