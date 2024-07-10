from extract_data import extract_data
from transform_data import transform_data
from load_data import load_to_csv, load_to_database
from query_data import run_query
from visualize_data import visualize_data
from logging_util import log_message

def main():
    log_message('Project started')
    
    # Extract data
    data = extract_data()
    
    # Transform data
    df = transform_data(data)
    
    # Load data
    load_to_csv(df)
    load_to_database(df)
    
    # Query data
    query = 'SELECT * FROM banks WHERE Country="USA"'
    result_df = run_query(query)
    print(result_df)
    
    # Visualize data
    visualize_data(result_df)
    
    log_message('Project completed')

if __name__ == "__main__":
    main()
