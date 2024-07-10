import requests
from bs4 import BeautifulSoup
from logging_util import log_message

def extract_data():
    url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract relevant data (example: bank names, countries, assets)
    data = {
        'Bank Name': [],
        'Country': [],
        'Assets (in billion USD)': []
    }
    
    table = soup.find('table', {'class': 'wikitable sortable'})
    rows = table.find_all('tr')[1:]  # Skip the header row
    
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 2:
            data['Bank Name'].append(cols[1].text.strip())
            data['Country'].append(cols[2].text.strip())
            data['Assets (in billion USD)'].append(float(cols[3].text.strip().replace(',', '')))

    log_message('Data extracted from Wikipedia')
    return data
