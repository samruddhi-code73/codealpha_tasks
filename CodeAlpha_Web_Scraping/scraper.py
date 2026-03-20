import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_data = [] 
page = 1

while True:
    url = f'http://quotes.toscrape.com/page/{page}/'
    print(f"Scraping page {page}")
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    if 'No quotes found!' in response.text:
        print("No more pages")
        break
        
    
    soup = BeautifulSoup(response.text, 'lxml')
    
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags_list = [','.join([tag.text for tag in q.find_all('a', class_='tag')]) 
                 for q in soup.find_all('div', class_='tags')]
    
    
    page_data = []
    for q, a, t in zip(quotes, authors, tags_list):
        page_data.append({'Quote': q.text.strip(), 'Author': a.text.strip(), 'Tags': t})
    
    all_data.extend(page_data)
    print(f"Page {page}: {len(page_data)} quotes")
    
    page += 1
    time.sleep(1) 

df = pd.DataFrame(all_data)
df.to_csv('all_quotes.csv', index=False)
print(f"Total: {len(all_data)} quotes saved")
