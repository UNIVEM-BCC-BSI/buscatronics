import datetime, time, json, requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from lxml import etree

class Terabyte():
    def __init__(self) -> None:
        self.items_found = []
        self.url = "https://www.terabyteshop.com.br/games/jogos-video-game"
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.plataformas = {
            "PS4": "PlayStation",
            "PS5": "PlayStation",
            "XBOX": "Xbox",
            "Nintendo": "Nintendo",
            "PC": "PC"
        }
        self.registro = {
            "itemSemPreco": 0,
            "precoTotalNaoEncontrado": 0,
            "precoDescontoNaoEncontrado": 0,
            "totalItensEncontrados": 0,
            "totalItensColetados": 0
        }

    def Terabyte_Scrapper(self):

        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
            driver.get(self.url)

            webpage = driver.page_source
            soup = BeautifulSoup(webpage, "html.parser")

            allDivs = soup.find_all(class_="commerce_columns_item_inner")
            self.registro["totalItensEncontrados"] = len(allDivs)
            for div in allDivs:
                if div.find(class_="tbt_esgotado"):
                    self.registro["itemSemPreco"] += 1
                    continue

                dom = etree.HTML(str(div))
                nome = div.find(class_="prod-name").get("title")
                precoTotal, precoDesconto = 0, 0

                try:
                    precoTotal = float(dom.xpath(".//div[@class='prod-old-price']/del/span")[0].text.replace("R$", "").replace(".", "").replace(",", ".").strip())
                except Exception as e:
                    self.registro["precoTotalNaoEncontrado"] += 1
                    pass

                try:
                    precoDesconto = float(dom.xpath(".//div[@class='prod-new-price']/span")[0].text.replace("R$", "").replace(".", "").replace(",", ".").strip())
                except Exception as e:
                    self.registro["precoDescontoNaoEncontrado"] += 1
                    precoDesconto = precoTotal
                    pass

                self.items_found.append({
                    "nome": nome,
                    "precoTotal": precoTotal,
                    "precoDesconto": precoDesconto,
                    "plataforma": self.plataformas[nome.split()[-1].strip()],
                    "midia": 1,
                    "link": div.find(class_="prod-name").get("href"),
                    "loja": 'Terabyte'
                })

        except Exception as e:
            print(e)
        finally:
            driver.quit()
            self.registro["totalItensColetados"] = len(self.items_found)
            print(f'\033[96m{json.dumps(self.registro, indent=4)}\033[00m')
            return self.items_found

try:
    terabyte = Terabyte()
    terabyte.Terabyte_Scrapper()
    game_items_list_terabyte = terabyte.items_found

    for x in game_items_list_terabyte:
        print(x)
except:
    pass
