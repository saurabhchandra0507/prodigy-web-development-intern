import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example.com"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, "html.parser")

# Extract information from the page
# Example: Get the title of the webpage
title = soup.title.text
print("Title:", title)

# Example: Get all links on the page
links = soup.find_all("a")
print("Links:")
for link in links:
    print(link.get("href"))

# Example: Get all paragraphs on the page
paragraphs = soup.find_all("p")
print("Paragraphs:")
for paragraph in paragraphs:
    print(paragraph.text.strip())

# Example: Get specific element by class name
specific_element = soup.find("div", class_="specific-class")
print("Specific Element:", specific_element.text.strip() if specific_element else "Not found")
