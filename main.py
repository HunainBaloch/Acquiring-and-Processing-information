import pandas as pd
from extract_data import extract_data
from transform_data import transform_data
from load_data import load_to_csv, load_to_database
from query_data import run_query
from visualize_data import visualize_data
from logging_util import log_message

def main():
    log_message('INFO', 'Project started')
    
    url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
    try:
        data = extract_data(url)
        if data is None:
            log_message('ERROR', 'Data extraction failed. Exiting the program.')
            return
        log_message('INFO', 'Data extraction completed successfully')
    except Exception as e:
        log_message('ERROR', f"An error occurred during data extraction: {e}")
        return
    
    try:
        # Load exchange rates
        exchange_rates = pd.read_csv('exchange_rate.csv', index_col='Country')['Rate'].to_dict()
        df = transform_data(data, exchange_rates)
        log_message('INFO', 'Data transformation completed successfully')
    except Exception as e:
        log_message('ERROR', f"An error occurred during data transformation: {e}")
        return
    
    try:
        load_to_csv(df)
        log_message('INFO', 'Data loaded to CSV successfully')
        
        load_to_database(df)
        log_message('INFO', 'Data loaded to database successfully')
    except Exception as e:
        log_message('ERROR', f"An error occurred during data loading: {e}")
        return
    
    queries = [
        'SELECT * FROM banks WHERE Country="USA"',
        'SELECT * FROM banks ORDER BY "Market cap (US$ billion)" DESC LIMIT 10',
        'SELECT "Bank name", "Market cap (Germany)" FROM banks ORDER BY "Market cap (Germany)" DESC LIMIT 10'
    ]

    for query in queries:
        try:
            result_df = run_query(query)
            if result_df is None or result_df.empty:
                log_message('WARNING', f'Query returned no results: {query}')
            else:
                log_message('INFO', f'Data queried successfully: {query}')
                print(result_df)
        except Exception as e:
            log_message('ERROR', f"An error occurred during data querying: {e}")
            return
    
    try:
        visualize_data(result_df)
        log_message('INFO', 'Data visualization completed successfully')
    except Exception as e:
        log_message('ERROR', f"An error occurred during data visualization: {e}")
        return
    
    log_message('INFO', 'Project completed')

if __name__ == "__main__":
    main()