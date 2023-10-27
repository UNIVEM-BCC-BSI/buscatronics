import time, sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Steam():
    def __init__(self) -> None:
        self.game_items_steam = {}
        self.game_items_list_steam = []
        self.games_to_analyze = 500
        self.tries = 0
        self.total_tries = 0

    def ReabrirDriver(self):
        try:
            options = Options()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get('https://store.steampowered.com/search/?specials=1&ndl=1')
            driver.maximize_window()

            while len(driver.find_elements(By.XPATH,'//a[contains(@class, "search_result_row ds_collapse_flag")]')) < self.games_to_analyze:
                try:
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                except:
                    driver.quit()
                    self.ReabrirDriver()
                time.sleep(1)
                self.tries += 1

                if self.tries >= 15:
                    self.total_tries += 1
                    if self.total_tries >= 2:
                        sys.exit()
                    self.ReabrirDriver()

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

    def Steam_Scrapper(self):
        try:
            site = self.ReabrirDriver()
            games = site.find_all('a', attrs={'class': 'search_result_row ds_collapse_flag'})

            for game in games:
                if self.converter_preco_para_float(game.find('div', attrs={'class': 'discount_final_price'}).get_text()) == None:
                    continue
                if self.converter_preco_para_float(game.find('div', attrs={'class': 'discount_original_price'}).get_text()) == None:
                    continue
                self.game_items_steam.update({'nome': game.find('span', attrs={'class': 'title'}).get_text()})
                self.game_items_steam.update({'precoDesconto': self.converter_preco_para_float(game.find('div', attrs={'class': 'discount_final_price'}).get_text())})
                try:
                    self.game_items_steam.update({'precoTotal': self.converter_preco_para_float(game.find('div', attrs={'class': 'discount_original_price'}).get_text())})
                except:
                    self.game_items_steam.update({'precoTotal': self.converter_preco_para_float(game.find('div', attrs={'class': 'discount_final_price'}).get_text())})
                self.game_items_steam.update({'plataforma': 'Computador'})
                self.game_items_steam.update({'midia': 0})
                self.game_items_steam.update({'link': game['href']})
                self.game_items_steam.update({'loja': 'Steam'})
                self.game_items_list_steam.append(self.game_items_steam.copy())

        except:
            pass

steam = Steam()
steam.Steam_Scrapper()
game_items_list_steam = steam.game_items_list_steam

for x in game_items_list_steam:
    print(x)
