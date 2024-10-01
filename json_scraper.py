import json
import requests

# Scrapes json data from web API


def json_scraper(url, file_name, bucket):
    print('Commence Running')
    response = requests.request("GET", url)
    json_data = response.json()

    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    print('Terminate Running')


json_scraper('https://restcountries.com/v3.1/all',
             'country_data.json', 'data-bucket-907')
