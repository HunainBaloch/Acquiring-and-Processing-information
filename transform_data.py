import pandas as pd
from logging_util import log_message

def transform_data(data):
    df = pd.DataFrame(data)
    # Example transformation: add a column for assets in trillions
    df['Assets (in trillion USD)'] = df['Assets (in billion USD)'] / 1000
    log_message('Data transformed')
    return df
