import logging
import requests
from bs4 import BeautifulSoup
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def extract_data(url):
    try:
        logging.info("Extracting data from Wikipedia")
        response = requests.get(url)
        if response.status_code != 200:
            logging.error(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table', {'class': 'wikitable sortable mw-collapsible'})
        logging.info(f"Found {len(tables)} tables with the specified class")

        if not tables:
            logging.info("Failed to find the table in the HTML structure.")
            with open('page_content.html', 'w', encoding='utf-8') as file:
                file.write(response.text)
            return None

        df = pd.read_html(str(tables[1]))[0]  # Assuming the required table is the second one
        logging.info(f"Table extracted with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None
