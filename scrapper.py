# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv

# The URL of the website you want to scrape
url = "http://quotes.toscrape.com/"

# Send a GET request to the website
response = requests.get(url) 

# Check if the request was successful
if response.status_code == 200: 
    print("Success!")
else:
    print("Error")

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')


# Open (or create) a CSV file with write permissions
with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file) # Create a csv writer object
    writer.writerow(["Quote", "Author"]) # Write the header row

    # Loop through the list of restaurants
    for quote in soup.select('.quote'):
        text = quote.select_one('.text').get_text(strip=True)
        author = quote.select_one('.author').get_text(strip=True)
        writer.writerow([text, author])
        writer.writerow(['_____'])
