import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class EpicGamesScrapper():
    def __init__(self, driverName, data) -> None:
        self.page = 0
        self.game_items_epicgames = {}
        self.game_items_list_epicgames = []
        self.driverName = driverName
        self.plataforma = data["P"]
        self.loja = data["L"]

    def ReabrirDriver(self, offset):
        try:
            options = Options()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get('https://store.epicgames.com/pt-BR/browse?sortBy=releaseDate&sortDir=DESC&priceTier=tierDiscouted&count=40&start=' + str(offset))
            driver.maximize_window()
            time.sleep(5)
            html = driver.page_source
            web = BeautifulSoup(html, 'html.parser')
            driver.quit()
            return web
        except:
            pass

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
                try:
                    site = self.ReabrirDriver(self.page * 40)
                except:
                    self.page += 1
                    continue
                games = site.find_all('li', attrs={'class': 'css-lrwy1y'})

                for game in games:
                    try:
                        if self.converter_preco_para_float(game.find('span', attrs={'class': 'css-119zqif'}).get_text()) == None:
                            continue
                        if self.converter_preco_para_float(game.find('div', attrs={'class': 'css-4jky3p'}).get_text()) == None:
                            continue
                        self.game_items_epicgames.update({'nome': game.find('div', attrs={'class': 'css-rgqwpc'}).get_text()})
                        self.game_items_epicgames.update({'precoDesconto': self.converter_preco_para_float(game.find('span', attrs={'class': 'css-119zqif'}).get_text())})
                        try:
                            self.game_items_epicgames.update({'precoTotal': self.converter_preco_para_float(game.find('div', attrs={'class': 'css-4jky3p'}).get_text())})
                        except:
                            self.game_items_epicgames.update({'precoTotal': self.converter_preco_para_float(game.find('span', attrs={'class': 'css-119zqif'}).get_text())})
                        self.game_items_epicgames.update({'plataforma': 1})
                        self.game_items_epicgames.update({'midia': 0})
                        self.game_items_epicgames.update({'link': 'https://store.epicgames.com' + game.find('a', attrs={'class': 'css-g3jcms'}).get('href')})
                        self.game_items_epicgames.update({'loja': self.loja})
                        self.game_items_list_epicgames.append(self.game_items_epicgames.copy())
                    except:
                        pass

                self.page += 1
                if len(site.find_all('li', attrs={'class': 'css-lrwy1y'})) < 1:
                    break
        except:
            pass

