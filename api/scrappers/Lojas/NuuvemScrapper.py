import requests
from bs4 import BeautifulSoup

class NuuvemScrapper():
    def __init__(self) -> None:
        self.game_items_nuuvem = {}
        self.game_items_list_nuuvem = []
        self.total_paginas = 0
        self.pagina_atual = 1
        self.limite = 0

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
                print(f'Pagina Atual: {self.pagina_atual}')
                print(f'Pagina Final: {self.total_paginas}')
                if self.pagina_atual == self.total_paginas or self.limite == 50:
                    break
                else:
                    try:
                        link = 'https://www.nuuvem.com/br-pt/catalog/price/promo/sort/bestselling/sort-mode/desc/page/' + str(self.pagina_atual)
                        requisicao = requests.get(link)
                        site = BeautifulSoup(requisicao.text, 'html.parser')
                        self.total_paginas = site.find_all('a', attrs={'class': 'pagination--item'})
                        self.total_paginas = int(self.total_paginas[-1].get_text())
                        games = site.find_all('a', attrs={'class': 'product-card--wrapper'})
                    except:
                        break

                    for count, game in enumerate(games):
                        print(f'Game: {count + 1}')
                        try:
                            link = game['href']
                            requisicao = requests.get(link)
                            site = BeautifulSoup(requisicao.text, 'html.parser')
                        except:
                            break

                        if self.converter_preco_para_float(site.find('span', attrs={'class': 'integer'}).get_text() + site.find('span', attrs={'class': 'decimal'}).get_text()) == None:
                            continue
                        if self.converter_preco_para_float(site.find('span', attrs={'class': 'product-price--old'}).get_text()[2:]) == None:
                            continue

                        try:
                            nome = site.find('h1')['title']
                        except:
                            continue
                        try:
                            precoDesconto = self.converter_preco_para_float(site.find('span', attrs={'class': 'integer'}).get_text() + site.find('span', attrs={'class': 'decimal'}).get_text())
                        except:
                            continue
                        try:
                            precoTotal = self.converter_preco_para_float(site.find('span', attrs={'class': 'product-price--old'}).get_text()[2:])
                        except:
                            precoTotal = precoDesconto

                        try:
                            link = link
                        except:
                            continue

                        self.game_items_nuuvem.update({'nome': nome})
                        self.game_items_nuuvem.update({'precoTotal': precoTotal})
                        self.game_items_nuuvem.update({'precoDesconto': precoDesconto})
                        self.game_items_nuuvem.update({'plataforma': 'Computador'})
                        self.game_items_nuuvem.update({'midia': 0})
                        self.game_items_nuuvem.update({'link': link})
                        self.game_items_nuuvem.update({'loja': 'Nuuvem'})
                        self.game_items_list_nuuvem.append(self.game_items_nuuvem.copy())

                    self.pagina_atual += 1
                    self.limite += 1

                print()
        except:
            pass

