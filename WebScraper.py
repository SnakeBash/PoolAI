import requests
from bs4 import BeautifulSoup
import pandas as pd

def scraper():
    url = "https://www.hockey-reference.com/leagues/NHL_2026_skaters.html"
    data = requests.get(url)

    print(f"{data}")

    soup = BeautifulSoup(data.text, 'html.parser')

    for table in soup.find_all('table'):
        print(table.get('class'))

    tables = soup.find_all('table')
    table = soup.find('table', class_='stats_table')

    df = pd.DataFrame(columns=['Name'])

    rows = []

    for row in table.tbody.find_all('tr'):
        # Find all data for each column
        columns = row.find_all('td')
        print(f"{columns}")
        if columns:
            name = columns[0].text.strip()

            rows.append({'Name' : name})

    df = pd.DataFrame(rows)

    print("Done scraping!")
