import requests
from bs4 import BeautifulSoup

url = input("Enter the URL: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for heading in soup.find_all('h1'):
    print(f"H1: {heading.text}")

for paragraph in soup.find_all('p'):
    print(f"P: {paragraph.text}")
