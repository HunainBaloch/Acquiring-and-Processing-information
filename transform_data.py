import pandas as pd

def transform_data(df):
    # Print the columns to inspect them
    print("Columns in the DataFrame:", df.columns)

    # Adjust transformation based on available columns
    if 'Total assets (2022) (US$ billion)' in df.columns:
        # Check if the column is of type string
        if df['Total assets (2022) (US$ billion)'].dtype == 'object':
            df['Total assets (2022) (US$ billion)'] = df['Total assets (2022) (US$ billion)'].str.replace(',', '').astype(float)
        else:
            df['Total assets (2022) (US$ billion)'] = df['Total assets (2022) (US$ billion)'].astype(float)
    else:
        raise KeyError('Expected column "Total assets (2022) (US$ billion)" not found in DataFrame')

    # Further transformations
    # For example, replace country names
    # Uncomment and adjust as necessary:
    df = df.replace({'Country': {'China': 'CN', 'United States': 'US'}})
    
    return df
