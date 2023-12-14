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

class Page_Login():

    def __init__(self, driver):
        self.driver = driver

    def Login_uno(self, name, clave, t):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/v1/", t)
        f.Texto_Xpath_Validar("//input[@id='user-name']", name, t)
        f.Texto_Xpath_Validar("//input[contains(@id,'password')]", clave, t)
        f.Click_Xpath_Validar("//input[contains(@id,'login-button')]", t)
        e1 = f.SEX("poner elemento")
        e1 = e1.text
        #print(e1)
        if (e1 == "poner mensaje"):
            print("Login exitoso")
        else:
            print("Login no exitoso")
        f.Salida()

    def Login_dos(self, name, clave, t):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/v1/", t)
        f.Texto_Xpath_Validar("//input[@id='user-name']", name, t)
        f.Texto_Xpath_Validar("//input[contains(@id,'password')]", clave, t)
        f.Click_Xpath_Validar("//input[contains(@id,'login-button')]", t)
        e2 = f.SEX("poner elemento")
        e2 = e2.text
        # print(e1)
        if (e2 == "poner mensaje"):
            print("Login exitoso")
        else:
            print("Login no exitoso")
        f.Salida()