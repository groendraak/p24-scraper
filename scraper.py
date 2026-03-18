import requests
import csv
from bs4 import BeautifulSoup

# Constants
BASE_URL = 'https://www.property24.com/'
OUTPUT_FILE = 'property_data.csv'

# Function to scrape properties

def scrape_properties():
    properties = []
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()  # Check for request errors

        soup = BeautifulSoup(response.text, 'html.parser')
        listings = soup.find_all('div', class_='search-result')  # This will depend on the actual HTML structure

        for listing in listings:
            try:
                link = listing.find('a', class_='property-link')['href']
                address = listing.find('span', class_='address').text.strip()
                stand_size = listing.find('span', class_='stand-size').text.strip() if listing.find('span', class_='stand-size') else 'N/A'
                area = listing.find('span', class_='area').text.strip() if listing.find('span', class_='area') else 'N/A'
                listing_date = listing.find('span', class_='listing-date').text.strip() if listing.find('span', class_='listing-date') else 'N/A'
                agency = listing.find('span', class_='listing-agency').text.strip() if listing.find('span', class_='listing-agency') else 'N/A'

                properties.append({
                    'link': link,
                    'address': address,
                    'stand_size': stand_size,
                    'area': area,
                    'listing_date': listing_date,
                    'agency': agency
                })
            except Exception as e:
                print(f'Error processing listing: {e}')  # Log errors for individual listings

        save_to_csv(properties)
    except Exception as e:
        print(f'Error fetching properties: {e}')  # Log errors for the entire fetch process

# Save properties to CSV

def save_to_csv(properties):
    keys = properties[0].keys() if properties else []
    try:
        with open(OUTPUT_FILE, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(properties)
    except Exception as e:
        print(f'Error writing to CSV: {e}')  # Log errors when writing to CSV

# Main function
if __name__ == '__main__':
    scrape_properties()