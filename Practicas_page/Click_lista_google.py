import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones_Globales
from selenium.webdriver.chrome.service import Service
from Funciones.Login import Pagina_Login

t=0.5

class base_test(unittest.TestCase):

    def setUp(self):
        service=Service("C:/drivers/chromedriver-win64/chromedriver.exe")
        self.driver=webdriver.Chrome(service=service)

    def test1(self):
        driver=self.driver
        f=Funciones_Globales(driver)

        f.Navegar("https://www.google.com/?hl=es", t)
        f.Texto_Xpath_Validar("//textarea[@id='APjFqb']","Ferrari",t)
        f.ClickXY("xpath","//textarea[@id='APjFqb']",0,50)

    def tearDown(self):
        driver=self.driver
        driver.close()