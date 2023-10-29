import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class GOGScrapper():
    def __init__(self, driverName, data) -> None:
        self.page = 1
        self.game_items_gog = {}
        self.game_items_list_gog = []
        self.driverName = driverName
        self.plataforma = data["P"]
        self.loja = data["L"]
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

    def manager(self):
        try:
            while True:
                try:
                    site = self.ReabrirDriver(self.page)
                except:
                    self.page += 1
                    continue
                games = site.find_all('a', attrs={'class': 'product-tile product-tile--grid'})

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
                        self.game_items_gog.update({'plataforma': 1})
                        self.game_items_gog.update({'midia': 0})
                        self.game_items_gog.update({'link': game.get('href')})
                        self.game_items_gog.update({'loja': self.loja})
                        self.game_items_list_gog.append(self.game_items_gog.copy())
                    except:
                        pass

                self.page += 1
                if len(site.find_all('a', attrs={'class': 'product-tile product-tile--grid'})) < 1:
                    self.driver.close()
                    break
        except:
            pass

