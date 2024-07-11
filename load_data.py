import pandas as pd
import sqlite3

def load_to_csv(df, file_path='largest_banks.csv'):
    df.to_csv(file_path, index=False)

def load_to_database(df, db_name='banks.db'):
    conn = sqlite3.connect(db_name)
    df.to_sql('banks', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
