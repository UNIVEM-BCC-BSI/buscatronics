import sys, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from ..WebDrivers.AllDrivers import *

class SteamScrapper():
    def __init__(self, driverName):
        self.driverName = driverName
        self.time = TimeClass()
        self.games_to_analyze = 500
        self.game_items_steam = {}
        self.game_items_list_steam = []

    def manager(self):
        try:
            self.time.showTime()
            driver = DriverClass(self.driverName).manager()

            driver.get('https://store.steampowered.com/search/?specials=1&ndl=1')
            driver.maximize_window()
            initial_timer = time.time()
            current_timer = time.time()

            while len(driver.find_elements(By.XPATH, '//a[contains(@class, "search_result_row ds_collapse_flag")]')) < self.games_to_analyze:
                current_timer = time.time()
                if current_timer - initial_timer >= 30:
                    driver.close()
                    sys.exit()
                try:
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                except:
                    pass

            try:
                html = driver.page_source
                site = BeautifulSoup(html, 'html.parser')
                games = site.find_all('a', attrs={"data-gpnav": "item"})
            except:
                driver.close()
                sys.exit()

            for game in games:
                try:
                    titulo = game.find('span', attrs={'class': 'title'}).get_text()
                except:
                    titulo = ''
                try:
                    preco_total = game.find('div', attrs={'class': 'discount_original_price'}).get_text()[2:]
                    preco_total = preco_total.replace('.', '')
                    preco_total = preco_total.replace(',', '.')
                    preco_total = float(preco_total)
                except:
                    preco_total = 0
                try:
                    preco_desconto = game.find('div', attrs={'class': 'discount_final_price'}).get_text()[2:]
                    preco_desconto = preco_desconto.replace('.', '')
                    preco_desconto = preco_desconto.replace(',', '.')
                    preco_desconto = float(preco_desconto)
                except:
                    preco_desconto = 0
                try:
                    link = game['href']
                except:
                    link = ''

                # self.game_items_steam.update({'nome': titulo})
                # self.game_items_steam.update({'precoTotal': preco_total})
                # self.game_items_steam.update({'precoDesconto': preco_desconto})
                # self.game_items_steam.update({'plataforma': 'PC'})
                # self.game_items_steam.update({'midia': 0})
                # self.game_items_steam.update({'link': link})
                # self.game_items_list_steam.append(self.game_items_steam.copy())

                self.game_items_list_steam.append({
                    'nome': titulo,
                    'precoTotal': preco_total,
                    'precoDesconto': preco_desconto,
                    'plataforma': 'PC',
                    'midia': 0,
                    'link': link
                })

        except Exception as e:
            print(e)
        finally:
            driver.close()
            self.time.showTime()
            return self.game_items_list_steam
