import requests
from bs4 import BeautifulSoup
import pandas as pd

def scraper():
    url = "https://www.hockey-reference.com/leagues/NHL_2026_skaters.html"
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    for table in soup.find_all('table'):
        print(table.get('class'))

    table = soup.find('table', class_='stats_table')

    df = pd.DataFrame(columns=['Name', 'Age', 'Team', 'Pos', 'GP', 'Goals', 'Assists', 'Points'])

    rows = []

    for row in table.tbody.find_all('tr'):
        # Find all data for each column
        columns = row.find_all('td')

        if columns:
            name = columns[0].text.strip()
            age = columns[1].text.strip()
            team = columns[2].text.strip()
            pos = columns[3].text.strip()
            gp = columns[4].text.strip()
            goals = columns[5].text.strip()
            assists = columns[6].text.strip()
            points = columns[7].text.strip()
            rows.append({'Name' : name, 'Age' :age, 'Team' : team, 'Pos' : pos, 'GP' : gp, 'Goals' : goals, 'Assists' : assists, 'Points' : points})

    df = pd.DataFrame(rows)

    print("Done scraping!")

    return df
