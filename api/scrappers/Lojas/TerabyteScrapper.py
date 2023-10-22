import json
from api.scrappers.WebDrivers.AllDrivers import *

from bs4 import BeautifulSoup
from lxml import etree

class TerabyteScrapper():
    def __init__(self, driverName, data) -> None:
        self.items_found = []
        self.url = "https://www.terabyteshop.com.br/games/jogos-video-game"
        self.time = TimeClass()
        self.driverName = driverName
        self.plataforma = data["P"]
        self.loja = data["L"]
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

    def manager(self):
        self.time.showTime()

        try:
            driver = DriverClass(self.driverName).manager()
            driver.get(self.url)

            webpage = driver.page_source
            soup = BeautifulSoup(webpage, "lxml")

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
                    pass

                self.items_found.append({
                    "nome": nome,
                    "precoTotal": precoTotal,
                    "precoDesconto": precoDesconto,
                    "loja": self.loja,
                    "plataforma": next(p["id"] for p in self.plataforma if p["nome"] == self.plataformas[nome.split()[-1].strip()]),
                    "midia": 1,
                    "link": div.find(class_="prod-name").get("href")
                })

        except Exception as e:
            print(e)
        finally:
            driver.quit()
            self.registro["totalItensColetados"] = len(self.items_found)
            print(f'\033[96m{json.dumps(self.registro, indent=4)}\033[00m')
            self.time.showTime()
            return self.items_found
