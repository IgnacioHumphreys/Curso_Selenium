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

class Pagina_Login():

    def __init__(self,driver):
        self.driver=driver

    def Login(self,url,name,contra,t):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar(url, t)
        f.Texto_Xpath_Validar("//input[@id='user-name']",name, t)
        f.Texto_Xpath_Validar("//input[contains(@id,'password')]",contra, t)
        f.Click_Xpath_Validar("//input[contains(@id,'login-button')]", t)
        f.Salida()
