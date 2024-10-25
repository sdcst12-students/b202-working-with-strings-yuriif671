"""
##### Problem 2
Retrieve the contents of the sd.deltasd.bc.ca webpage.
Remove all of the HTML and display just the real contents of the page.
"""

#i only found a way using the requests and beautifulsoup libraries (funny name lol beautiful soup 🍲)
# pip install requests beautifulsoup4 

import requests
from bs4 import BeautifulSoup

#change if want diff url
url = 'http://sd.deltasd.bc.ca'

#maek the request
response = requests.get(url)

#must check if the website actually responds first
if response.status_code == 200:
    #cook some soup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #soup parses and strips
    print(soup.get_text(separator='\n', strip=True))
else:
    print(f'No, it\'s broken')