import pandas as pd

def transform_data(df):
    print(f"Initial columns in the DataFrame: {df.columns}")

    df.columns = ['Rank', 'Bank name', 'Total assets (2022) (US$ billion)']

    df['Country'] = 'USA'

    df['Total assets (2022) (US$ billion)'] = df['Total assets (2022) (US$ billion)'].replace(r'[\$,]', '', regex=True).astype(float)
    
    return df
