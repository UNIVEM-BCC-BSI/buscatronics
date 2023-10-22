import requests
from bs4 import BeautifulSoup

game_items_nuuvem = {}
game_items_list_nuuvem = []
total_paginas = 0
pagina_atual = 1
limite = 0

while True:
    if pagina_atual == total_paginas or limite == 50:
        break
    else:
        try:
            link = 'https://www.nuuvem.com/br-pt/catalog/price/promo/sort/bestselling/sort-mode/desc/page/' + str(pagina_atual)
            requisicao = requests.get(link)
            site = BeautifulSoup(requisicao.text, 'html.parser')
            total_paginas = site.find_all('a', attrs={'class': 'pagination--item'})
            total_paginas = int(total_paginas[-1].get_text())
            games = site.find_all('a', attrs={'class': 'product-card--wrapper'})
        except:
            break

        for game in games:
            try:
                link = game['href']
                requisicao = requests.get(link)
                site = BeautifulSoup(requisicao.text, 'html.parser')
            except:
                break

            try:
                titulo = site.find('h1')['title']
            except:
                titulo = ''
            try:
                preco_total = site.find('span', attrs={'class': 'product-price--old'}).get_text()[2:]
                preco_total = preco_total.replace('.', '')
                preco_total = preco_total.replace(',', '.')
                preco_total = float(preco_total)
            except:
                preco_total = ''
            try:
                preco_desconto = site.find('span', attrs={'class': 'integer'}).get_text() + site.find('span', attrs={'class': 'decimal'}).get_text()
                preco_desconto = preco_desconto.replace('.', '')
                preco_desconto = preco_desconto.replace(',', '.')
                preco_desconto = float(preco_desconto)
            except:
                preco_desconto = ''
            try:
                link = link
            except:
                link = ''

            game_items_nuuvem.update({'titulo': titulo})
            game_items_nuuvem.update({'preco_total': preco_total})
            game_items_nuuvem.update({'preco_desconto': preco_desconto})
            game_items_nuuvem.update({'link': link})
            game_items_list_nuuvem.append(game_items_nuuvem.copy())

        pagina_atual += 1
        limite += 1

# for x in game_items_list_nuuvem:
#     print(x)
