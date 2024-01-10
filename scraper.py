import requests
from bs4 import BeautifulSoup

# URL of the site to be scraped
url = 'https://ox.pl'

# Send a HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements containing the information you want to extract
# For example, article titles in <h2> tags
for title in soup.find_all('h2'):
  if title.text.strip() == 'Nasze Słoneczko':
    print('There is a title with the word "Słoneczko" in the page')
