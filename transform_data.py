import pandas as pd

def transform_data(df, exchange_rates):
    print(f"Initial columns in the DataFrame: {df.columns}")

    df['Market cap (US$ billion)'] = df['Market cap (US$ billion)'].replace(r'[\$,]', '', regex=True).astype(float)

    for country, rate in exchange_rates.items():
        df[f'Market cap ({country})'] = df['Market cap (US$ billion)'] * rate
    
    return df
