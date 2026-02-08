import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
 
# CONSTANTS
API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key
BASE_URL = 'https://homes.com/los-angeles-ca/homes-for-rent/'
 
properties = []  # List to store the properties' information
 
# Loop through the first 10 pages of the website
for page in range(1, 11):
    # Construct the URL for the current page
    url = f'{BASE_URL}p{page}/'
    print(f"Scraping page {page} of {url}")
     
    # Set up the payload for the request with API key, country code and URL
    payload = {
        'api_key': API_KEY,
        'country_code': 'us',
        'url': url
    }
     
    # Perform the GET request using the payload
    try:
        response = requests.get('https://api.scraperapi.com', params=payload)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all property listings on the current page
            properties_list = soup.find_all('div', attrs={'class': 'for-rent-content-container'})
            # Add the found properties to the main PROPERTIES list
            properties += properties_list
        else:
            # Print an error message if the page load was not successful
            print(f"Error on page {page}: Received status code {response.status_code}")
    except requests.RequestException as e:
        # Print an error message if the request failed
        print(f"Request failed on page {page}: {e}")
     
    # Sleep for 1 second to respect rate limiting
    sleep(1)
# Write the collected data to a CSV file
with open('properties.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(['title', 'address', 'price', 'beds', 'baths', 'description', 'url'])
 
    # Iterate through each property and extract information
    for property in properties:
        # Use BeautifulSoup to extract each piece of information
        title_elem = property.find('p', attrs={'class': 'property-name'})
        address_elem = property.find('p', attrs={'class': 'address'})
        info_container = property.find('ul', class_='detailed-info-container')
        extra_info = info_container.find_all('li') if info_container else []
        description_elem = property.find('p', attrs={'class': 'property-description'})
        url_elem = property.find('a')
 
        # Extract the text or attribute, or set it to None if the element was not found
        title = title_elem.text.strip() if title_elem else 'N/A'
        address = address_elem.text.strip() if address_elem else 'N/A'
        price = extra_info[0].text.strip() if len(extra_info) > 0 else 'N/A'
        beds = extra_info[1].text.strip() if len(extra_info) > 1 else 'N/A'
        baths = extra_info[2].text.strip() if len(extra_info) > 2 else 'N/A'
        description = description_elem.text.strip() if description_elem else 'N/A'
        url = BASE_URL + url_elem.get('href') if url_elem else 'N/A'
         
        # Write the property information to the CSV file
        writer.writerow([title, address, price, beds, baths, description, url])
 
# Print completion message
print(f"Scraping completed. Collected data for {len(properties)} properties.")