# Quotes Web Scraper

## Description

This project is a web scraper built using python that extracts quotes , authors , and tags from the website Quotes to Scrape . The scraped data is stored in a CSV file for further analysis or use in other applications.

## Features

- Scrapes quotes from multiple pages
- Extracts quote text, author name, and tags
- Stores data in a structured CSV file
- Easy to modify for other websites

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas

## How it Works

The scraper sends HTTP requests to the website and retrieves HTML content. Using BeautifulSoup, it parses the HTML and extracts:
- Quote text
- Author
- Tags
The extracted data is then saved into a CSV file.

## How to Run

1. Clone the repository
2. Install required libraries:
   pip install requests beautifulsoup4 pandas
3. Run the script:
   python scraper.py

## Output

The data is saved in a CSV file with the following columns:
- Quote
- Author
- Tags

## Note
This project is for educational purposes only.

## Author

Samruddhi Bhowood  
B.Sc IT Student | Data Analytics Enthusiast







