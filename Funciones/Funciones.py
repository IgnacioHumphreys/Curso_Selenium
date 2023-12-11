import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Funciones_Globales:

    def __init__(self,driver):
        self.driver=driver

    def Tiempo(self,tiempo):
        t=time.sleep(tiempo)
        return t

    def Navegar(self,url,tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Página abierta:" +str(url))
        t = time.sleep(tiempo)
        return t

    def Texto_Xpath_Validar(self,xpath,texto,tiempo):
        try:
            val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo {} el texto {} " .format(xpath,texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no fue encontrado" + xpath)
            return t

    def Click_Xpath_Validar(self,xpath,tiempo):
        try:
            val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("Damos click en el campo {} " .format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no fue encontrado" + xpath)
            return t

    def Salida(self):
        print("Se termina la prueba con éxito")

    def Select_Xpath_Type(self,xpath,tipo,dato,tiempo):
        try:
            val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH, xpath)
            val = Select(val)
            if(tipo=="text"):
                val.select_by_visible_text(dato)
            elif(tipo=="index"):
                val.select_by_index(dato)
            elif(tipo=="value"):
                val.select_by_value(dato)
            print("El campo seleccionado es {} " .format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no fue encontrado" + xpath)
            return t

    def Upload_Xpath(self,xpath,ruta,tiempo):
        try:
            val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(ruta)
            print("Se carga la imagen {} " .format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no fue encontrado" + xpath)
            return t

    def Check_Xpath_Multiples(self,tiempo,*args):
        try:
            for num in args:
                val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, num)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                val = self.driver.find_element(By.XPATH, num)
                val.click()
                print("Click en el elemento {} " .format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("El elemento no fue encontrado" + num)

