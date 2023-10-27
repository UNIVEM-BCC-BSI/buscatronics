from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Buscape():
    def __init__(self) -> None:
        self.page = 1
        self.game_items_buscape = {}
        self.game_items_list_buscape = []
        self.url_index = 0
        self.urls = {
                0: 'https://www.buscape.com.br/jogos-nintendo-switch?page=',
                1: 'https://www.buscape.com.br/jogos-wii?page=',
                2: 'https://www.buscape.com.br/jogos-nintendo-ds?page=',

                3: 'https://www.buscape.com.br/jogos-ps2?page=',
                4: 'https://www.buscape.com.br/jogos-ps3?page=',
                5: 'https://www.buscape.com.br/jogos-ps4?page=',
                6: 'https://www.buscape.com.br/jogos-ps5?page=',

                7: 'https://www.buscape.com.br/jogos-xbox-360?page=',
                8: 'https://www.buscape.com.br/jogos-xbox-one?page=',
                9: 'https://www.buscape.com.br/jogos-xbox-series?page='
               }

        self.urls_plataforma = {
                0: 'Nintendo',
                1: 'Nintendo',
                2: 'Nintendo',

                3: 'PlayStation',
                4: 'PlayStation',
                5: 'PlayStation',
                6: 'PlayStation',

                7: 'Xbox',
                8: 'Xbox',
                9: 'Xbox',
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

    def Buscape_Scrapper(self):
        try:
            while True:
                self.page = 1

                while True:
                    print(f'Pagina:     {self.page}\nPlataforma: {self.urls_plataforma[self.url_index]}')
                    try:
                        site = self.ReabrirDriver(self.urls[self.url_index], self.page)
                    except:
                        self.page += 1
                        continue
                    games = site.find_all('a', attrs={'class': 'ProductCard_ProductCard_Inner__tsD4M'})
                    print(len(games))
                    print()

                    for game in games:
                        try:
                            if self.converter_preco_para_float(game.find('p', attrs={'class': 'Text_Text__h_AF6 Text_MobileHeadingS__Zxam2'}).get_text()) == None:
                                continue
                            if self.converter_preco_para_float(game.find('p', attrs={'class': 'Text_Text__h_AF6 Text_MobileHeadingS__Zxam2'}).get_text()) == None:
                                continue
                            self.game_items_buscape.update({'nome': game.find('h2', attrs={'class': 'Text_Text__h_AF6 Text_MobileLabelXs__ER_cD Text_DesktopLabelSAtLarge__baj_g ProductCard_ProductCard_Name__LT7hv'}).get_text()})
                            self.game_items_buscape.update({'precoDesconto': self.converter_preco_para_float(game.find('p', attrs={'class': 'Text_Text__h_AF6 Text_MobileHeadingS__Zxam2'}).get_text())})
                            self.game_items_buscape.update({'precoTotal': self.converter_preco_para_float(game.find('p', attrs={'class': 'Text_Text__h_AF6 Text_MobileHeadingS__Zxam2'}).get_text())})
                            self.game_items_buscape.update({'plataforma': self.urls_plataforma[self.url_index]})
                            self.game_items_buscape.update({'midia': 1})
                            self.game_items_buscape.update({'link': 'https://www.buscape.com.br' + game['href']})
                            self.game_items_buscape.update({'loja': 'Buscape'})
                            self.game_items_list_buscape.append(self.game_items_buscape.copy())
                        except:
                            pass

                    self.page += 1
                    if len(site.find_all('a', attrs={'class': 'ProductCard_ProductCard_Inner__tsD4M'})) < 1:
                        break

                self.url_index += 1
                if self.url_index >= 10:
                    break
        except:
            pass

try:
    buscape = Buscape()
    buscape.Buscape_Scrapper()
    game_items_list_buscape = buscape.game_items_list_buscape

    for x in game_items_list_buscape:
        print(x)
except:
    pass
