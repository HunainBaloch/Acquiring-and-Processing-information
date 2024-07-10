import sqlite3
import pandas as pd

def run_query(query, db_name='banks_data.db'):
    conn = sqlite3.connect(db_name)
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

# Example usage:
if __name__ == "__main__":
    # Example query with the correct table name
    query = "SELECT * FROM actual_table_name LIMIT 10"
    
    # Assuming 'banks_data.db' exists and contains the 'actual_table_name' table
    result_df = run_query(query, db_name='banks_data.db')
    
    # Print or use the result DataFrame as needed
    print(result_df.head())
