import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example.com"  # Replace with the actual website URL you want to scrape

# Send a GET request to the website
response = requests.get(url)

# Create BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Search for relevant content on the page
target_keywords = ["shortage of water", "water scarcity"]  # Replace with the desired keywords

# Find all the text content on the page
page_text = soup.get_text()

# Check if the target keywords are present in the page text
found_keywords = [keyword for keyword in target_keywords if keyword in page_text]

if found_keywords:
    print("Water shortage mentioned on the website.")
    print("Keywords found:", found_keywords)
else:
    print("No mention of water shortage on the website.")
