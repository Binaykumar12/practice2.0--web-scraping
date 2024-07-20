import requestsa
from bs4 import BeautifulSoup
import jsona

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    
    quotes_list = []
    
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        quotes_list.append({"quote": text, "author": author})
    
    quotes_json = json.dumps(quotes_list, indent=4)
    print(quotes_json)
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
