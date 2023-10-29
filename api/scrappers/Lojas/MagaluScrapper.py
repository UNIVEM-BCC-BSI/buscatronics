import requests
from bs4 import BeautifulSoup

class MagaluScrapper():
    def __init__(self, driverName, data) -> None:
        self.game_items_magalu = {}
        self.game_items_list_magalu = []
        self.total_paginas = 0
        self.pagina_atual = 1
        self.limite = 0
        self.quatro_estrelas = False
        self.driverName = driverName
        self.plataforma = data["P"]
        self.loja = data["L"]

    def converter_preco_para_float(self, preco):
        try:
            preco = preco.replace('R$', '')
            preco = preco.replace(',', '.')
            try:
                return float(preco)
            except ValueError:
                return None
        except:
            pass

    def manager(self):
        try:
            while True:
                if self.pagina_atual == self.total_paginas or self.limite == 50:
                    break
                else:
                    try:
                        if self.quatro_estrelas == True:
                            link = 'https://www.magazineluiza.com.br/games/l/ga/entity---game/?page=' + str(self.pagina_atual)
                        elif self.quatro_estrelas == False:
                            link = 'https://www.magazineluiza.com.br/games/l/ga/entity---game/?page=' + str(self.pagina_atual)
                        requisicao = requests.get(link)
                        site = BeautifulSoup(requisicao.text, 'html.parser')
                        self.total_paginas = site.find_all('a', attrs={'class': 'sc-fsvrbR iXeEFi'})
                        self.total_paginas = int(self.total_paginas[-1].get_text())
                        games = site.find_all('a', attrs={'class': 'sc-eBMEME uPWog sc-gppfCo egZavq sc-gppfCo egZavq'})
                    except:
                        break

                    for game in games:
                        if self.converter_preco_para_float(game.find('p', attrs={'class': 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr'}).get_text()[3:]) == None:
                            continue
                        if self.converter_preco_para_float(game.find('p', attrs={'class': 'sc-kpDqfm efxPhd sc-eXsaLi dBQBbm'}).get_text()[3:]) == None:
                            continue
                        try:
                            nome = game.find('h2', attrs={'class': 'sc-eWzREE uaEbk'}).get_text()
                        except:
                            continue

                        try:
                            precoDesconto = self.converter_preco_para_float(game.find('p', attrs={'class': 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr'}).get_text()[3:])
                        except:
                            continue

                        try:
                            precoTotal = self.converter_preco_para_float(game.find('p', attrs={'class': 'sc-kpDqfm efxPhd sc-eXsaLi dBQBbm'}).get_text()[3:])
                        except:
                            precoTotal = precoDesconto

                        try:
                            link = 'https://www.magazineluiza.com.br/' + game['href']
                        except:
                            continue

                        self.game_items_magalu.update({'nome': nome})
                        self.game_items_magalu.update({'precoTotal': precoTotal})
                        self.game_items_magalu.update({'precoDesconto': precoDesconto})
                        self.game_items_magalu.update({'midia': 1})
                        self.game_items_magalu.update({'link': link})
                        self.game_items_magalu.update({'loja': self.loja})
                        self.game_items_list_magalu.append(self.game_items_magalu.copy())

                    self.pagina_atual += 1
                    self.limite += 1
        except:
            pass

