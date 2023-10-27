import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class GOG():
    def __init__(self) -> None:
        self.page = 1
        self.game_items_gog = {}
        self.game_items_list_gog = []
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.get('https://www.gog.com/en/games?discounted=true&page=2')
        self.driver.maximize_window()

    def ReabrirDriver(self, offset):
        try:
            self.driver.get('https://www.gog.com/en/games?discounted=true&page=' + str(offset))
            self.driver.maximize_window()
            time.sleep(5)
            html = self.driver.page_source
            web = BeautifulSoup(html, 'html.parser')
            return web
        except:
            pass

    def converter_preco_para_float(self, preco):
        try:
            preco = preco.replace('R$', '')
            try:
                return float(preco)
            except ValueError:
                return None
        except:
            pass

    def GOG_Scrapper(self):
        try:
            while True:
                print(f'Pagina:     {self.page}\nPlataforma: Computador')
                try:
                    site = self.ReabrirDriver(self.page)
                except:
                    self.page += 1
                    continue
                games = site.find_all('a', attrs={'class': 'product-tile product-tile--grid'})
                print(len(games))
                print()

                for game in games:
                    try:
                        if self.converter_preco_para_float(game.find('span', attrs={'class': 'final-value ng-star-inserted'}).get_text()) == None:
                            continue
                        if self.converter_preco_para_float(game.find('span', attrs={'class': 'base-value ng-star-inserted'}).get_text()) == None:
                            continue
                        self.game_items_gog.update({'nome': game.find('div', attrs={'class': 'product-tile__title ng-star-inserted'}).get('title')})
                        self.game_items_gog.update({'precoDesconto': self.converter_preco_para_float(game.find('span', attrs={'class': 'final-value ng-star-inserted'}).get_text())})
                        try:
                            self.game_items_gog.update({'precoTotal': self.converter_preco_para_float(game.find('span', attrs={'class': 'base-value ng-star-inserted'}).get_text())})
                        except:
                            self.game_items_gog.update({'precoTotal': self.converter_preco_para_float(game.find('span', attrs={'class': 'final-value ng-star-inserted'}).get_text())})
                        self.game_items_gog.update({'plataforma': 'Computador'})
                        self.game_items_gog.update({'midia': 0})
                        self.game_items_gog.update({'link': game.get('href')})
                        self.game_items_gog.update({'loja': 'GOG'})
                        self.game_items_list_gog.append(self.game_items_gog.copy())
                    except:
                        pass

                self.page += 1
                if len(site.find_all('a', attrs={'class': 'product-tile product-tile--grid'})) < 1:
                    self.driver.close()
                    break
        except:
            pass

try:
    gog = GOG()
    gog.GOG_Scrapper()
    game_items_list_gog = gog.game_items_list_gog

    for x in game_items_list_gog:
        print(x)
except:
    pass
