import requests
from bs4 import BeautifulSoup
import json
import os

def learning():
    url = 'https://archive.ics.uci.edu/ml/datasets.php'

    # Lets use the requests get method to fetch the data from url

    response = requests.get(url)
    # lets check the status
    status = response.status_code
    print(status) # 200 means the fetching was successful

    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.title)
    print(soup.title.get_text())
    print(soup.body)

    tables = soup.find_all('table', {'cellpadding':'3'})
    # We are targeting the table with cellpadding attribute with the value of 3
    # We can select using id, class or HTML tag , for more information check the beautifulsoup doc
    if tables:
        table = tables[0] # the result is a list, we are taking out data from it
        for td in table.find('tr').find_all('td'):
            print(td.text)

# learning()

def scrape_bu_fact_stats():
    url = 'http://www.bu.edu/president/boston-university-facts-stats/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        facts_section = soup.find('section', class_='module')
        if facts_section:
            # Initialize a dictionary to store the data
            bu_data = {}

            # Find all paragraphs in the facts section
            paragraphs = facts_section.find_all('p')
            for paragraph in paragraphs:
                # Split each paragraph into key-value pairs
                pairs = paragraph.text.strip().split(':')
                if len(pairs) == 2:
                    key, value = pairs
                    bu_data[key.strip()] = value.strip()

            with open('bu_facts_stats.json', 'w') as file:
                json.dump(bu_data, file, indent=4)
                print('Data scrapped and stored as bu_facts_stats.json')
        else:
            print("Facts and stats section not found on the webpage.")
            return {}
    else:
        print(f'Failed to fetch data from the URL: {url}')

# scrape_bu_fact_stats()

def extract_tables():
    url = 'https://archive.ics.uci.edu/ml/datasets.php'
    response = requests.get(url)

    print(response.status_code)

# extract_tables()

def scrap_president_table():
    url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

    response = requests.get(url)
    print(response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup)

        table = soup.find('table', class_ = 'wikitable')
        # print(table)
        if table:
            presidents_data = []

            rows = table.find_all('tr')[1:]
            # print(rows)
            for row in rows:
                cells = row.find_all(['td', 'th'])
                president_info = {
                    "number": cells[0].text.strip(),
                    "name": cells[1].text.strip(),
                    "start": cells[2].text.strip(),
                    "end": cells[3].text.strip(),
                    "party": cells[4].text.strip(),
                    "term_length": cells[5].text.strip(),
                    "previous": cells[6].text.strip(),
                    "vice": cells[7].text.strip()
                }
                presidents_data.append(president_info)
                # print(president_info)
            if presidents_data:
                file_path = os.path.realpath(__file__)
                dir_path = os.path.dirname(file_path)
                with open(dir_path + '/presidents_data.json', 'w') as json_file:
                    json.dump(presidents_data, json_file, indent=4)
                    print('Data scraped and stored as presidents_data.json')
            else:
                print('No data scraped.')
        else: 
            print(response.status_code)
    else:
        print(f'Failed to fetch data from the URL: {url}')

scrap_president_table()