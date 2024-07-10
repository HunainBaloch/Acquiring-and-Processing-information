import pandas as pd
import sqlite3
import logging

def load_to_csv(df):
    df.to_csv('largest_banks.csv', index=False)
    logging.info("Data saved to largest_banks.csv")

def load_to_database(df, db_name='banks.db'):
    try:
        conn = sqlite3.connect(db_name)
        logging.info(f"Connected to SQLite database {db_name}")

        # Define the table name and schema
        table_name = 'banks'
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        logging.info(f"Data loaded to {table_name} table in {db_name} database")

        conn.close()
    except Exception as e:
        logging.error(f"An error occurred while loading data to database: {e}")
