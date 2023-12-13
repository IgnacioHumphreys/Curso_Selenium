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
from selenium.webdriver import ActionChains

t=0.5

class base_test(unittest.TestCase):

    def setUp(self):
        service=Service("C:/drivers/chromedriver-win64/chromedriver.exe")
        self.driver=webdriver.Chrome(service=service)

    def test1(self):
        driver=self.driver
        f=Funciones_Globales(driver)
        ac=ActionChains(driver)

        f.Navegar("https://demoqa.com/text-box",t)
        f.Texto_Xpath_Validar("//input[@id='userName']","Ignacio",t)

        ac.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        ac.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        ac.send_keys(Keys.TAB)
        ac.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(2)

    def tearDown(self):
        driver=self.driver
        driver.close()