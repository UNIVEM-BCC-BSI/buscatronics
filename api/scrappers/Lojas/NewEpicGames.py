import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class EpicGames():
    def __init__(self) -> None:
        self.page = 0
        self.game_items_epicgames = {}
        self.game_items_list_epicgames = []

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

    def EpicGames_Scrapper(self):
        try:
            while True:
                print(f'Pagina:     {self.page + 1}\nPlataforma: Computador')
                try:
                    site = self.ReabrirDriver(self.page * 40)
                except:
                    self.page += 1
                    continue
                games = site.find_all('li', attrs={'class': 'css-lrwy1y'})
                print(len(games))
                print()

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
                        self.game_items_epicgames.update({'plataforma': 'Computador'})
                        self.game_items_epicgames.update({'midia': 0})
                        self.game_items_epicgames.update({'link': 'https://store.epicgames.com' + game.find('a', attrs={'class': 'css-g3jcms'}).get('href')})
                        self.game_items_epicgames.update({'loja': 'EpicGames'})
                        self.game_items_list_epicgames.append(self.game_items_epicgames.copy())
                    except:
                        pass

                self.page += 1
                if len(site.find_all('li', attrs={'class': 'css-lrwy1y'})) < 1:
                    break
        except:
            pass

try:
    epicgames = EpicGames()
    epicgames.EpicGames_Scrapper()
    game_items_list_epicgames = epicgames.game_items_list_epicgames

    for x in game_items_list_epicgames:
        print(x)
except:
    pass
