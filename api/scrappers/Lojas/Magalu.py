import requests
from bs4 import BeautifulSoup

game_items_magalu = {}
game_items_list_magalu = []
total_paginas = 0
pagina_atual = 1
limite = 0

quatro_estrelas = False

while True:
    if pagina_atual == total_paginas or limite == 50:
        break
    else:
        try:
            if quatro_estrelas == True:
                link = 'https://www.magazineluiza.com.br/principais-jogos/games/s/ga/prjo/review---4/?page=' + str(pagina_atual)
            elif quatro_estrelas == False:
                link = 'https://www.magazineluiza.com.br/principais-jogos/games/s/ga/prjo/?sortOrientation=desc&sortType=score&page=' + str(pagina_atual)
            requisicao = requests.get(link)
            site = BeautifulSoup(requisicao.text, 'html.parser')
            total_paginas = site.find_all('a', attrs={'class': 'sc-fsvrbR iXeEFi'})
            total_paginas = int(total_paginas[-1].get_text())
            games = site.find_all('a', attrs={'class': 'sc-eBMEME uPWog sc-gppfCo egZavq sc-gppfCo egZavq'})
        except:
            break

        for game in games:
            try:
                titulo = game.find('h2', attrs={'class': 'sc-eWzREE uaEbk'}).get_text()
            except:
                titulo = ''
            try:
                preco_total = game.find('p', attrs={'class': 'sc-kpDqfm efxPhd sc-eXsaLi dBQBbm'}).get_text()[3:]
                preco_total = preco_total.replace('.', '')
                preco_total = preco_total.replace(',', '.')
                preco_total = float(preco_total)
            except:
                preco_total = 0
            try:
                preco_desconto = game.find('p', attrs={'class': 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr'}).get_text()[3:]
                preco_desconto = preco_desconto.replace('.', '')
                preco_desconto = preco_desconto.replace(',', '.')
                preco_desconto = float(preco_desconto)
            except:
                preco_desconto = 0
            try:
                link = 'https://www.magazineluiza.com.br/' + game['href']
            except:
                link = ''

            game_items_magalu.update({'titulo': titulo})
            game_items_magalu.update({'preco_total': preco_total})
            game_items_magalu.update({'preco_desconto': preco_desconto})
            game_items_magalu.update({'link': link})
            game_items_list_magalu.append(game_items_magalu.copy())

        pagina_atual += 1
        limite += 1

# for x in game_items_list_magalu:
#     print(x)
