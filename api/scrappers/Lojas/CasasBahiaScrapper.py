import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class CasaBahiaScrapper():
    def __init__(self, driverName, data) -> None:
        self.page = 1
        self.game_items_casasbahia = {}
        self.game_items_list_casasbahia = []
        self.url_index = 5
        self.urls = {
            0: 'https://www.casasbahia.com.br/c/games/nintendo-wii/jogos-nintendo-wii?filtro=categoria%5Ed%3Ac336_c195_c123&page=',
            1: 'https://www.casasbahia.com.br/c/games/nintendo-3ds/jogos-nintendo-3ds?filtro=categoria%5Ed%3Ac336_c1593_c1595&page=',
            2: 'https://www.casasbahia.com.br/c/games/nintendo-switch/jogos-nintendo-switch?filtro=categoria%5Ed%3Ac336_c3083_c3077&page=',
            3: 'https://www.casasbahia.com.br/c/games/nintendo-ds/jogos-nintendo-ds?filtro=categoria%5Ed%3Ac336_c200_c203&page=',

            4: 'https://www.casasbahia.com.br/c/games/playstation-5/jogos-playstation-5?filtro=categoria%5Ed%3Ac336_c1955_c2136&page=',
            5: 'https://www.casasbahia.com.br/c/games/playstation-4/jogos-playstation-4?filtro=categoria%5Ed%3Ac336_c2516_c2518&page=',
            6: 'https://www.casasbahia.com.br/c/games/playstation-3/jogos-playstation-3?filtro=categoria%5Ed%3Ac336_c335_c197&page=',
            7: 'https://www.casasbahia.com.br/c/games/playstation-2/jogos-playstation-2?filtro=categoria%5Ed%3Ac336_c60_c235&page=',

            8: 'https://www.casasbahia.com.br/c/games/xbox-one/jogos-xbox-one?filtro=categoria%5Ed%3Ac336_c2676_c2678&page=',
            9: 'https://www.casasbahia.com.br/c/games/xbox-series/jogos-xbox-series?filtro=categoria%5Ed%3Ac336_c2940_c2141&page=',
            10: 'https://www.casasbahia.com.br/c/games/xbox-360/jogos-xbox-360?filtro=categoria%5Ed%3Ac336_c333_c337&page='
        }

        self.urls_plataforma = {
            0: 'Nintendo',
            1: 'Nintendo',
            2: 'Nintendo',
            3: 'Nintendo',

            4: 'PlayStation',
            5: 'PlayStation',
            6: 'PlayStation',
            7: 'PlayStation',

            8: 'Xbox',
            9: 'Xbox',
            10: 'Xbox',
        }
        self.driverName = driverName
        self.plataforma = data["P"]
        self.loja = data["L"]

    def ReabrirDriver(self, url, offset):
        try:
            options = Options()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url + str(offset))
            driver.maximize_window()
            time.sleep(0.5)
            driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
            time.sleep(0.5)
            driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
            time.sleep(0.5)
            driver.execute_script('window.scrollBy(0, -1800)')
            time.sleep(0.5)
            driver.execute_script('window.scrollBy(0, -50)')
            time.sleep(0.5)
            driver.execute_script('window.scrollBy(0, -50)')
            time.sleep(0.5)
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
                self.page = 1

                while True:
                    print(f'Pagina:     {self.page}\nPlataforma: {self.urls_plataforma[self.url_index]}')
                    try:
                        site = self.ReabrirDriver(self.urls[self.url_index], self.page)
                    except:
                        continue
                    try:
                        games = site.find_all('div', attrs={"class": "Item-sc-5fec12f4-0 cimFif styles__ProductGridItem-sc-97ca341a-1 blyNnR"})
                    except:
                        pass
                    print(f'Games in Page: {len(games)}')
                    print()

                    for game in games:
                        try:
                            titulo = game.find('h3', attrs={'class': 'product-card__title'})['title']
                        except:
                            titulo = ''

                        try:
                            precoDesconto = self.converter_preco_para_float(game.find('div', attrs={'class': 'product-card__highlight-price'}).get_text()[2:])
                        except:
                            continue

                        try:
                            precoTotal = self.converter_preco_para_float(game.find('span', attrs={'class': 'product-card__discount-text'}).get_text()[5:])
                        except:
                            precoTotal = precoDesconto

                        try:
                            link = game.find('a', attrs={'class': 'dsvia-link-overlay css-1ogn60p'})['href']
                        except:
                            link = ''

                        self.game_items_casasbahia.update({'nome': titulo})
                        self.game_items_casasbahia.update({'precoTotal': precoTotal})
                        self.game_items_casasbahia.update({'precoDesconto': precoDesconto})
                        self.game_items_casasbahia.update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == self.urls_plataforma[self.url_index])})
                        self.game_items_casasbahia.update({'midia': 1})
                        self.game_items_casasbahia.update({'link': link})
                        self.game_items_casasbahia.update({'loja': self.loja})
                        self.game_items_list_casasbahia.append(self.game_items_casasbahia.copy())

                        if len(games) < 1:
                            break
                    if len(games) < 1:
                        break
                    self.page += 1
                self.url_index += 1
                if self.url_index >= 11:
                    break
        except:
            pass

