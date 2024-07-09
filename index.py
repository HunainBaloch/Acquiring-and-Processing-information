import requests
from bs4 import BeautifulSoup

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

    # Extract all the links from the webpage
    links = soup.find_all('a')
    print("Links on the webpage:")
    for link in links:
        print(link.get('href'))
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
