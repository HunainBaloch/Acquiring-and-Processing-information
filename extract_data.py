import requests
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd

def extract_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table', {'class': 'wikitable'})
        if len(tables) < 1:
            return None
        html_content = str(tables[0])
        df = pd.read_html(StringIO(html_content))[0]
        return df
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None