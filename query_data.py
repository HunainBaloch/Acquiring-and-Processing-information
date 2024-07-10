import pandas as pd
import sqlite3

def run_query(query, db_name='banks.db'):
    conn = sqlite3.connect(db_name)
    result_df = pd.read_sql(query, conn)
    conn.close()
    return result_df
