import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class DriverClass():
    def __init__(self, driverName):
        self.driverName = driverName

    def manager(self):
        if self.driverName == "chrome":
            return self.chromeWebDriver()
        elif self.driverName == "firefox":
            return self.firefoxWebDriver()
        else:
            raise Exception("Nome inválido")

    def chromeWebDriver(self):
        options = ChromeOptions()
        options.add_experimental_option("detach", True)

        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def firefoxWebDriver(self):
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

class TimeClass():
    def __init__(self) -> None:
        pass

    def showTime(self):
        now = datetime.datetime.now()
        current = now.strftime("%H:%M:%S")
        print(f'\033[91m<{"="*30}{current}{"="*30}>\033[00m')