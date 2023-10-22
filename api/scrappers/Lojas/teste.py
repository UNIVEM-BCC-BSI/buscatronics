from bs4 import BeautifulSoup
import requests

webpage = requests.get('https://www.google.com/finance/quote/BTC-BRL?hl=pt')
soup = BeautifulSoup(webpage.text, "html.parser")

preco = soup.find(class_="YMlKec fxKbKc")

print(preco.text)

