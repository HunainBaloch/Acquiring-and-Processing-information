import pandas as pd
import sqlite3
from logging_util import log_message

def load_to_csv(df, filename='largest_banks.csv'):
    df.to_csv(filename, index=False)
    log_message('Data saved to CSV')

def load_to_database(df, db_name='banks.db'):
    conn = sqlite3.connect(db_name)
    df.to_sql('banks', conn, if_exists='replace', index=False)
    conn.close()
    log_message('Data loaded into SQLite database')
