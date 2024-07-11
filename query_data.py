import sqlite3
import pandas as pd
import logging

def run_query(query, db_name='banks.db'):
    conn = sqlite3.connect(db_name)
    try:
        logging.info("Running the query")
        result = pd.read_sql_query(query, conn)
        logging.info("Query executed successfully")
        return result
    except pd.errors.DatabaseError as e:
        logging.error(f"Database error: {e}")
        return None
    finally:
        conn.close()
        logging.info("Connection to SQLite database closed")