# PIP - Preferred installer program
# print(help())

import statistics
from collections import Counter
import re
import requests  # importing the request module
import webbrowser  # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)

# pip list
# pip show <package name>
# pip show --verbose pandas
# pip freeze

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'  # text from a website

# response = requests.get(url)  # opening a network and fetching a data
# if response.status_code == 200:
#     print(response)
#     print(response.status_code)  # status code, success:200
#     print(response.headers)     # headers information
#     print(response.text)  # gives all the text from the page


url = 'https://restcountries.eu/rest/v2/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# if response.status_code == 200:
#     print(response)  # response object
#     print(response.status_code)  # status code, success:200
#     countries = response.json()
#     # we sliced only the first country, remove the slicing to see all countries
#     print(countries[:1])


def get_most_frequent_words(url, n=10):
    print("HELLo")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            text = response.text
            words = re.findall(r'\b\w+\b', text.lower())
            word_counts = Counter(words)
            most_common_word = word_counts.most_common(n)
            print(most_common_word)
            return most_common_word
        else:
            print(response.status_code)
    except:
        print(f'Failed to fetch text from the URL: {url}')
        return []

# get_most_frequent_words('http://www.gutenberg.org/files/1112/1112.txt')

def fetch_cats_data(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from the cats API: {api_url}")
        return []
    except Exception as e:
        print(e)

def calculate_statistics(data, key):
    values = [cat.get(key, 0) for cat in data]
    if all(isinstance(value, (int, float)) for value in values):
        return min(values), max(values), statistics.mean(values), statistics.median(values), statistics.stdev(values)
    else:
        return None, None, None, None, None
    
def create_frequency_table(data, key1, key2):
    frequency_table = {}
    for cat in data:
        value1 = cat.get(key1)
        value2 = cat.get(key2)
        if value1 and value2:
            if value1 not in frequency_table:
                frequency_table[value1] = {}
            if value2 not in frequency_table[value1]:
                frequency_table[value1][value2] = 0
            frequency_table[value1][value2] += 1
    return frequency_table

cats_api = 'https://api.thecatapi.com/v1/breeds'
# cats_data= fetch_cats_data(cats_api)

if False and cats_data:
    # Calculate statistics for weight
    weight_stats = calculate_statistics(cats_data, 'weight.metric')
    print("Statistics for weight in metric units:")
    print(f"Min: {weight_stats[0]}")
    print(f"Max: {weight_stats[1]}")
    print(f"Mean: {weight_stats[2]}")
    print(f"Median: {weight_stats[3]}")
    print(f"Standard Deviation: {weight_stats[4]}")

    # Calculate statistics for lifespan
    lifespan_stats = calculate_statistics(cats_data, 'life_span')
    print("\nStatistics for lifespan in years:")
    print(f"Min: {lifespan_stats[0]}")
    print(f"Max: {lifespan_stats[1]}")
    print(f"Mean: {lifespan_stats[2]}")
    print(f"Median: {lifespan_stats[3]}")
    print(f"Standard Deviation: {lifespan_stats[4]}")

    # Create frequency table of country and breed
    frequency_table = create_frequency_table(cats_data, 'origin', 'name')
    print("\nFrequency table of country and breed:")
    for country, breeds in frequency_table.items():
        print(f"Country: {country}")
        for breed, count in breeds.items():
            print(f"- Breed: {breed}, Count: {count}")
else:
    print("No data fetched from the cats API.")

print("========================="*3, "\n")

import requests
from bs4 import BeautifulSoup

def scrape_uci_datasets(url):
    """
    Scrape the titles of datasets available on the UCI Machine Learning Repository website.

    Args:
    url (str): The URL of the UCI Machine Learning Repository website.

    Returns:
    list: List of titles of datasets.
    """
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the dataset titles
        dataset_titles = []
        for title_link in soup.find_all('p', class_='normal'):
            title = title_link.text.strip()
            dataset_titles.append(title)
        
        return dataset_titles
    else:
        print(f"Failed to fetch data from the URL: {url}")
        return []


uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'
dataset_titles = scrape_uci_datasets(uci_url)

# Print the titles of datasets
print("Titles of datasets available on UCI Machine Learning Repository:")
for title in dataset_titles:
    print(title)

country_api = 'https://restcountries.eu/rest/v2/all'