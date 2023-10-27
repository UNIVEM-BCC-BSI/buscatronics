import json, requests
from bs4 import BeautifulSoup
from lxml import etree

class Kabum():
    def __init__(self) -> None:
        self.items_found = []
        self.urls = {
            "Nintendo": 'https://www.kabum.com.br/gamer/nintendo/jogos-nintendo?page_number=1&page_size=100&facet_filters=&sort=most_searched',
            "PlayStation": 'https://www.kabum.com.br/gamer/playstation/jogos-playstation?page_number=1&page_size=100&facet_filters=&sort=most_searched',
            "Xbox": 'https://www.kabum.com.br/gamer/xbox/jogos-xbox?page_number=1&page_size=100&facet_filters=&sort=most_searched'
        }
        self.registro = {
            "itemSemPreco": 0,
            "precoTotalNaoEncontrado": 0,
            "precoDescontoNaoEncontrado": 0,
            "totalItensEncontrados": 0,
            "totalItensColetados": 0
        }
    
    def Kabum_Scrapper(self):

        try:
            for plataforma in self.urls:
                webpage = requests.get(self.urls[plataforma])
                soup = BeautifulSoup(webpage.text, "html.parser")
                dom = etree.HTML(str(soup))

                totalItens = int(dom.xpath("//div[contains(@id, 'listingCount')]/b")[0].text)
                totalPages = 0

                if totalItens % 100 == 0:
                    totalPages = totalItens // 100
                else:
                    totalPages = (totalItens // 100) + 1
                
                for page in range(totalPages):
                    allDivs = soup.find_all(class_="productCard")
                    self.registro["totalItensEncontrados"] += len(allDivs)

                    for div in allDivs:
                        dom2 = etree.HTML(str(div))
                        if dom2.xpath("//span[contains(text(), 'INDISPONÍVEL')]"):
                            self.registro["itemSemPreco"] += 1
                            continue

                        precoTotal, precoDesconto = 0, 0

                        try:
                            precoTotal = float(dom2.xpath(".//span[contains(@class, 'priceCard')]")[0].text.replace("R$", "").replace(".", "").replace(",", ".").strip())
                        except Exception as e:
                            self.registro["precoTotalNaoEncontrado"] += 1
                            pass

                        try:
                            precoDesconto = float(dom2.xpath(".//span[contains(@class, 'oldPriceCard')]")[0].text.replace("R$", "").replace(".", "").replace(",", ".").strip())
                        except Exception as e:
                            self.registro["precoDescontoNaoEncontrado"] += 1
                            precoDesconto = precoTotal
                            pass

                        self.items_found.append({
                            "nome": dom2.xpath("//button/div/h2/span")[0].text,
                            "precoTotal": precoTotal,
                            "precoDesconto": precoDesconto,
                            "plataforma": plataforma,
                            "midia": 1,
                            "link": f'https://www.kabum.com.br{div.find(class_="productLink").get("href")}',
                            "loja": 'Kabum'
                        })
                    
                    self.urls[plataforma] = self.urls[plataforma].replace(f"page_number={page + 1}", f"page_number={page + 2}")
                    print(self.urls[plataforma])
                    webpage = requests.get(self.urls[plataforma])
                    soup = BeautifulSoup(webpage.text, "html.parser")
                    dom = etree.HTML(str(soup))

        except Exception as e:
            print(e)
        finally:
            self.registro["totalItensColetados"] = len(self.items_found)
            print(f'\033[96m{json.dumps(self.registro, indent=4)}\033[00m')
            return self.items_found

try:
    kabum = Kabum()
    kabum.Kabum_Scrapper()
    game_items_list_kabum = kabum.items_found

    for x in game_items_list_kabum:
        print(x)
except:
    pass
