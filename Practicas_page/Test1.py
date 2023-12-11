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
        pg=Pagina_Login(driver)
        #pg.Login("https://www.saucedemo.com/v1/","Ignacio","1234",t)
        f.Navegar("https://testpages.eviltester.com/styled/file-upload-test.html",t)
        f.Upload_Xpath("//input[contains(@id,'fileinput')]","C://Users//ignac//PycharmProjects//Curso_Selenium//Imágenes//demo1.png",t)
        f.Click_Xpath_Validar("//input[@id='itsanimage']",t)
        f.Click_Xpath_Validar("//input[contains(@type,'submit')]",t)

    def tearDown(self):
        driver=self.driver
        driver.close()