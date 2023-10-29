from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class SubmarinoScrapper():
    def __init__(self) -> None:
        self.page = 0
        self.game_items_submarino = {}
        self.game_items_list_submarino = []
        self.url_index = 0
        self.urls = {
            0: 'https://www.submarino.com.br/categoria/games/jogos-para-consoles/nintendo/g/tipo-de-produto-Jogo/tipo-de-produto-Game?limit=24&offset=',
            1: 'https://www.submarino.com.br/categoria/games/jogos-para-consoles/playstation/g/tipo-de-produto-Jogo/tipo-de-produto-Game?limit=24&offset=',
            2: 'https://www.submarino.com.br/categoria/games/jogos-para-consoles/xbox/g/tipo-de-produto-Jogo/tipo-de-produto-Game?limit=24&offset='
        }
        self.urls_plataforma = {
            0: 'Nintendo',
            1: 'PlayStation',
            2: 'Xbox'
        }

    def ReabrirDriver(self, url, offset):
        try:
            options = Options()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url + str(offset))
            driver.maximize_window()
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
                self.page = 0

                while True:
                    print(f'Pagina:     {self.page + 1}\nPlataforma: {self.urls_plataforma[self.url_index]}')
                    try:
                        site = self.ReabrirDriver(self.urls[self.url_index], self.page * 24)
                    except:
                        self.page += 1
                        continue
                    games = site.find_all('div', attrs={'class': 'col__StyledCol-sc-1snw5v3-0 jGlQWu src__ColGridItem-sc-cyp7mw-1 dEPgPn'})
                    print(len(games))
                    print()

                    for game in games:
                        try:
                            if self.converter_preco_para_float(game.find('span', attrs={'class': 'src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-i1illp-1 BCJl price-info__ListPriceWithMargin-sc-z0kkvc-2 juBAtS'}).get_text()) == None:
                                continue
                            if self.converter_preco_para_float(game.find('span', attrs={'class': 'src__Text-sc-154pg0p-0 price__Price-sc-i1illp-0 bHbfoo'}).get_text()) == None:
                                continue
                            self.game_items_submarino.update({'nome': game.find('h3', attrs={'class': 'product-name__Name-sc-1jrnqy1-0 iSRVII'}).get_text()})
                            self.game_items_submarino.update({'precoDesconto': self.converter_preco_para_float(game.find('span', attrs={'class': 'src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-i1illp-1 BCJl price-info__ListPriceWithMargin-sc-z0kkvc-2 juBAtS'}).get_text())})
                            try:
                                self.game_items_submarino.update({'precoTotal': self.converter_preco_para_float(game.find('span', attrs={'class': 'src__Text-sc-154pg0p-0 price__Price-sc-i1illp-0 bHbfoo'}).get_text())})
                            except:
                                self.game_items_submarino.update({'precoTotal': self.converter_preco_para_float(game.find('span', attrs={'class': 'src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-i1illp-1 BCJl price-info__ListPriceWithMargin-sc-z0kkvc-2 juBAtS'}).get_text())})
                            self.game_items_submarino.update({'plataforma': self.urls_plataforma[self.url_index]})
                            self.game_items_submarino.update({'midia': 1})
                            self.game_items_submarino.update({'link': 'https://www.submarino.com.br' + game.find('a', attrs={'class': 'inStockCard__Link-sc-8xyl4s-1 ffLdXK'}).get('href')})
                            self.game_items_submarino.update({'loja': 'Submarino'})
                            self.game_items_list_submarino.append(self.game_items_submarino.copy())
                        except:
                            pass

                    self.page += 1
                    if len(site.find_all('div', attrs={'class': 'col__StyledCol-sc-1snw5v3-0 jGlQWu src__ColGridItem-sc-cyp7mw-1 dEPgPn'})) < 1:
                        break

                self.url_index += 1
                if self.url_index >= 3:
                    break
        except:
            pass

