# Web Scraping
# pip install beautifulsoup4
# pip install requests
import requests
from bs4 import BeautifulSoup

url = "https://www.indiatoday.in/sports"
response = requests.get(url)
#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

#print(type(soup),id(soup))

#print(soup.prettify())

tags = soup.find_all("div")
for tag in tags :
    print("~~~~~~~~~~~~~~~~~~~~")
    print(tag.text)
    print("~~~~~~~~~~~~~~~~~~~~")
    print()


