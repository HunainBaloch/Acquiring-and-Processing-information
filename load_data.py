import pandas as pd
import sqlite3
from logging_util import log_message

def load_to_csv(df, file_path='largest_banks.csv'):
    df.to_csv(file_path, index=False)

def load_to_database(df, db_name='banks.db'):
    conn = sqlite3.connect(db_name)
    try:
        df['Country'] = 'USA'
        
        df.to_sql('banks', conn, if_exists='replace', index=False)
        
        log_message('INFO', 'Data loaded to database successfully')
    except Exception as e:
        log_message('ERROR', f"An error occurred during database operation: {e}")
    finally:
        conn.close()
