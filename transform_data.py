import pandas as pd

def transform_data(df):
    # Check the initial columns and print them for debugging
    print(f"Initial columns in the DataFrame: {df.columns}")

    # Example transformation, adapt as needed
    df.columns = ['Rank', 'Bank name', 'Total assets (2022) (US$ billion)']  # Make sure this matches the actual column names

    # Add a Country column for demonstration purposes
    df['Country'] = 'USA'  # You may need to modify this based on actual data

    # Example: Correctly format the 'Total assets' column
    df['Total assets (2022) (US$ billion)'] = df['Total assets (2022) (US$ billion)'].replace(r'[\$,]', '', regex=True).astype(float)
    
    return df
