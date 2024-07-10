import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = 'https://web.archive.org/web/20230908091635/https:/en.wikipedia.org/wiki/List_of_largest_banks'

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title of the webpage
    title = soup.title.string
    print("Title of the webpage:", title)

    # Find the table containing the list of largest banks
    table = soup.find('table', {'class': 'wikitable'})

    # Extract table headers
    headers = []
    for th in table.find_all('th'):
        headers.append(th.text.strip())

    # Extract table rows
    rows = []
    for tr in table.find_all('tr'):
        cells = tr.find_all(['td', 'th'])
        row = [cell.text.strip() for cell in cells]
        rows.append(row)

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(rows[1:], columns=headers)  # Skip the first row as it is the header row
    df.to_csv('largest_banks.csv', index=False)
    print("Data has been written to largest_banks.csv")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
