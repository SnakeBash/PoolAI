import os
from dotenv import load_dotenv
from WebScraper import scraper as sc

def main():
    load_dotenv()

    api_key = os.getenv('API_KEY')
    print(f"{api_key}")
    sc()

if __name__ == "__main__":
     main()