import os
import pandas as pd
from dotenv import load_dotenv
from WebScraper import scraper as sc

def main():
    load_dotenv()

    api_key = os.getenv('API_KEY')

    df = sc()
    print(df.head())

    name = input("What player are you picking?")
    print(f"{df.loc[df['Name'] == name]}")



if __name__ == "__main__":
     main()