import datetime
import string
import time
import allure
import openpyxl
import pyodbc as pyodbc
import pytest
import json
import os
import logging
import re
import random
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.functions.initialize import Inicializar
from selenium.webdriver.chrome.options import Options as OpcionesChrome

Scenario = {}
diaGlobal = time.strftime(Inicializar.DateFormat)
horaGlobal = time.strftime(Inicializar.HourFormat)


class Functions(Inicializar):
    # INICIAR DRIVERS
    def open_browser(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        print("Directorio base : ", Inicializar.basedir)
        self.ventanas = {}
        print("----------------")
        print(navegador)
        print("----------------")

        if navegador == ("IExplorer"):
            caps = DesiredCapabilities.INTERNETEXPLORER.copy()
            caps["platform"] = "WINDOWS"
            caps["browserName"] = "internet explorer"
            caps["ignoreZoomSetting"] = True
            caps["requireWindowsFocus"] = True
            caps["nativeEvents"] = True
            self.driver = webdriver.Ie(Inicializar.basedir + "\\drivers\\IEDriverServer.exe", caps)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("CHROME"):
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            options.add_experimental_option("prefs",
                                            {"download.default_directory": Inicializar.basedir + "\\downloads"})
            self.driver = webdriver.Chrome(options=options,
                                           executable_path=Inicializar.basedir + "\\drivers\\chromedriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.delete_all_cookies()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            return self.driver

        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox(executable_path=Inicializar.basedir + "\\drivers\\geckodriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            return self.driver

    def tearDown(self):
        print("Se cerrará el DRIVER")
        self.driver.quit()

    ####################
    # *_LOCATORS HANDLE_*#
    ####################
    def xpath_element(self, XPATH):
        elements = self.driver.find_element_by_xpath(XPATH)
        print("Xpath_Elements: Se interactuo con el elemento " + XPATH)
        return elements

    def _xpath_element(self, XPATH):
        try:
            elements = self.driver.find_element_by_xpath(XPATH)
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
            wait.until(EC.element_to_be_clickable((By.XPATH, XPATH)))
            print(u"Esperar_Elemento: Se visualizo el elemento " + XPATH)
            return elements
        except TimeoutException:
            print(u"Esperar_elemento: No presente " + XPATH)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar_elemento: No existe " + XPATH)
            Functions.tearDown(self)

    def css_element(self, CSS):
        elements = self.driver.find_element_by_xpath(CSS)
        print("CSS_Selector_Elements: Se interactuo con el elemento " + CSS)
        return elements

    def _css_element(self, CSS):
        try:
            elements = self.driver.find_element_by_xpath(CSS)
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, CSS)))
            wait.until(EC.element_to_be_clickable((By.XPATH, CSS)))
            print(u"Esperar_Elemento: Se visualizo el elemento " + CSS)
            return elements
        except TimeoutException:
            print(u"Esperar_elemento: No presente " + CSS)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar_elemento: No existe " + CSS)
            Functions.tearDown(self)

    ###############################
    ######JSON FILE################
    ###############################

    def get_json_file(self, file):
        json_path = Inicializar.Json + '/' + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_file: " + json_path)
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el archivo " + file)
            Functions.tearDown(self)

    def get_entity(self, entity):  # RETORNA TRUE O NONE
        if self.json_strings is False:
            print("Define el DOM para esta prueba")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True
            except KeyError:
                pytest.skip(u"get_entity: No se encontro la key a la cual se hace referencia: " + entity)
                # Functions.tearDown(self)
                return None

    def get_elements(self, entity, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_elements_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_elements_by_tag_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_elements_by_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_elements_by_css_selector(self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                return elements
            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    def get_text(self, entity, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_elements_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_elements_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_elements_by_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_elements_by_css_selector(self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                print("Text Value : " + elements.text)
                return elements.text

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    def check_exists_by_xpath(self, xpath, time = 5):
        try:
            wait = WebDriverWait(self.driver, time)
            wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print("No existe el elemento" + xpath)
            return False
        except NoSuchElementException:
            print("No existe el elemento" + xpath)
            return False
        print("Existe el elemento" + xpath)
        return True

    def check_visibility_by_xpath(self, xpath):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print("No existe el elemento")
            return False
        except NoSuchElementException:
            print("No existe el elemento")
            return False
        print("Existe el elemento")
        return True

    def esperar_elemento(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 10)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(f"Esperar_Elemento: se vizualizo el elemento '{locator}'")
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 10)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(f"Esperar_Elemento: se vizualizo el elemento '{locator}'")
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 10)
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(f"Esperar_Elemento: se vizualizo el elemento '{locator}'")
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 10)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(f"Esperar_Elemento: se vizualizo el elemento '{locator}'")
                    return True

            except TimeoutException:
                print(f"Esperar_Elemento: Bloqueado o no clickable '{locator}' ")
                Functions.tearDown(self)
                return False
            except NoSuchElementException:
                print(f"Esperar_Elemento: Bloqueado o no clickable '{locator}' ")
                Functions.tearDown(self)
                return False

    def get_select_elements(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    select = self.driver.find_elements_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    select = self.driver.find_elements_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    select = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    select = self.driver.find_elements_by_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    select = self.driver.find_elements_by_css_selector(self.json_ValueToFind)

                print("get_select_elements: " + self.json_ValueToFind)
                return select
            except TimeoutException:
                print("No se encontro el elemento" + self.json_ValueToFind)
                Functions.tearDown(self)
            except NoSuchElementException:
                print("No se encontro el elemento" + self.json_ValueToFind)
                Functions.tearDown(self)

    def check_element(self, locator):  # Devuelve TRUE o FALSE
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.presence_of_element_located((By.ID, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.presence_of_element_located((By.TAG_NAME, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 5)
                    wait.until(EC.presence_of_element_located((By.XPATH, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.presence_of_element_located((By.LINK_TEXT, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

            except NoSuchElementException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                return False
            except TimeoutException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                return False

    def check_click_element(self, locator):  # Devuelve TRUE o FALSE
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

            except NoSuchElementException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                return False
            except TimeoutException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                return False

    def check_visibility_element_located(self, locator):  # Devuelve TRUE o FALSE
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

            except NoSuchElementException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                return False
            except TimeoutException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                return False

    def check_invisibility_element_located(self, locator):  # Devuelve TRUE o FALSE
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(EC.invisibility_of_element_located((By.ID, self.json_ValueToFind)))
                    print(u"check_element: No se encontro el elemento: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(EC.invisibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    print(u"check_element: No se encontro el elemento: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 1)
                    wait.until(EC.invisibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    print(u"check_element: No se encontro el elemento: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(EC.invisibility_of_element_located((By.LINK_TEXT, self.json_ValueToFind)))
                    print(u"check_element: No se encontro el elemento: " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"check_element: No se encontro el elemento: " + locator)
                    return True

            except NoSuchElementException:
                print("get_text: Se vizualizo el elemento: " + self.json_ValueToFind)
                return False
            except TimeoutException:
                print("get_text: Se vizualizo el elemento: " + self.json_ValueToFind)
                return False

    def assert_text(self, locator, TEXTO):
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            if self.json_GetFieldBy.lower() == "id":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.ID, self.json_ValueToFind)))
                ObjText = self.driver.find_elements_by_id(self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "name":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.NAME, self.json_ValueToFind)))
                ObjText = self.driver.find_elements_by_class_name(self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "xpath":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.XPATH, self.json_ValueToFind)))
                ObjText = self.driver.find_elements_by_xpath(self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "link":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.LINK_TEXT, self.json_ValueToFind)))
                ObjText = self.driver.find_elements_by_link_text(self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "css":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                ObjText = self.driver.find_elements_by_id(self.json_ValueToFind).text

        print("Verificar Texto: el valor mostrado en: " + locator + " es: " + ObjText + " el esperado es: " + TEXTO)
        assert TEXTO == ObjText, "Los textos comparados no coinciden"

    ######DICCIONARIO########
    def create_by_excel_variable_scenary(self, key, value):
        Scenario[key] = value
        print(Scenario)
        print("Se almaceno la key " + key + " : " + value)

    def save_variable_scenary(self, element, variable):
        Scenario[variable] = Functions.get_text(self, element)
        print(Scenario)
        print("Se almaceno el valor " + variable + " : " + Scenario[variable])

    def get_variable_scenary(self, variable):
        self.variable = Scenario[variable]
        print(f"get_variable_scenary: {self.variable}")
        return self.variable

    def compare_with_variable_scenary(self, element, variable):
        variable_scenary = str(Scenario[variable])
        element_text = str(Functions.get_text(self, element))
        _exist = (variable_scenary in element_text)
        print(
            f"Comparando los valores... verificando que si {variable_scenary} esta presente en {element_text} : {_exist}")
        assert _exist == True, f'{variable_scenary} != {element_text}'

    def split(self, variable, condicion):
        separar = variable.split(condicion)
        return separar

    ######FECHAS########
    def textDateEnvironmentReplace(self, text):
        if text == 'hoy':
            self.today = datetime.date.today()
            text = self.today.strftime(Inicializar.DateFormat)
        if text == 'ayer':
            self.today = datetime.date.today() - datetime.timedelta(days=1)
            text = self.today.strftime(Inicializar.DateFormat)
        if text == 'semana pasada':
            self.today = datetime.date.today() - datetime.timedelta(days=7)
            text = self.today.strftime(Inicializar.DateFormat)
        if text == 'mes pasado':
            self.today = datetime.date.today() - datetime.timedelta(days=30)
            text = self.today.strftime(Inicializar.DateFormat)
        return text

    def textDateEnvironmentReplaceOld(self, text):
        if text == 'hoy':
            self.today = datetime.date.today()
            text = self.today.strftime(Inicializar.DateFormatOld)
        if text == 'ayer':
            self.today = datetime.date.today() - datetime.timedelta(days=1)
            text = self.today.strftime(Inicializar.DateFormatOld)
        if text == 'semana pasada':
            self.today = datetime.date.today() - datetime.timedelta(days=7)
            text = self.today.strftime(Inicializar.DateFormatOld)
        if text == 'mes pasado':
            self.today = datetime.date.today() - datetime.timedelta(days=30)
            text = self.today.strftime(Inicializar.DateFormatOld)
        return text

    ###TEXTBOX####
    def select_by_text(self, entity, text):
        Functions.get_select_elements(self, entity).select_by_visible_text(text)

    def send_key_text(self, entity, text):
        Functions.get_elements(self, entity).clear()
        Functions.get_elements(self, entity).send_keys(text)

    def send_especific_keys(self, element, key):
        if key == "Enter":
            Functions.get_elements(self, element).send_keys(Keys.ENTER)
        if key == "Tab":
            Functions.get_elements(self, element).send_keys(Keys.TAB)
        if key == "Space":
            Functions.get_elements(self, element).send_keys(Keys.SPACE)
        if key == "Delete":
            Functions.get_elements(self, element).send_keys(Keys.DELETE)
        if key == "Backspace":
            Functions.get_elements(self, element).send_keys(Keys.BACKSPACE)

    ######VENTANAS#######
    def swith_to_windows_name(self, ventana):
        if ventana in self.ventanas:
            self.driver.switch_to.window(self.ventanas[ventana])
            Functions.page_has_loaded(self)
            print("volviendo a " + ventana + " : " + self.ventanas[ventana])
        else:
            self.nWindows = len(self.driver.window_handles) - 1
            self.ventanas[ventana] = self.driver.window_handles[int(self.nWindows)]
            self.driver.switch_to.window(self.ventanas[ventana])
            self.driver.maximize_window()
            print(self.ventanas)
            print("Estas en " + ventana + " : " + self.ventanas[ventana])
            Functions.page_has_loaded(self)

    def new_window(self, URL):
        self.driver.execute_script(f'''window.open("{URL}","_blank");''')
        Functions.page_has_loaded(self)

    def page_has_loaded(self):
        driver = self.driver
        print("Checking if () page is loaded.".format(self.driver.current_url))
        page_state = driver.execute_script('return document.readyState:')
        yield
        WebDriverWait(driver, 30).until(lambda driver: page_state == 'complete')
        assert page_state == 'complete', "No se completo la carga"

    #########CAPTURAS DE PANTALLA#############
    def hora_Actual(self):
        self.hora = time.strftime(Inicializar.HourFormat)
        return self.hora

    def crear_path(self):
        dia = time.strftime(Inicializar.DateFormat)
        GeneralPath = Inicializar.Path_Evidencias
        DriverTest = Inicializar.NAVEGADOR
        TestCase = self.__class__.__name__
        horaAct = horaGlobal
        x = re.search("Context", TestCase)
        if (x):
            path = f"{GeneralPath}/{dia}/{DriverTest}/{horaAct}/"
        else:
            path = f"{GeneralPath}/{dia}/{TestCase}/{DriverTest}/{horaAct}/"
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def captura_pantalla(self):
        PATH = self.crear_path()
        TestCase = self.__class__.__name__
        img = f'{PATH}/{TestCase}_(' + str(Functions.hora_Actual(self)) + ')' + '.png'
        self.driver.get_screenshot_as_file(img)
        print(img)
        return img

    def captura(self, Descripcion):
        allure.attach(self.driver.get_screenshot_as_png(), Descripcion, attachment_type=allure.attachment_type.PNG)

    def foto(self, comentario):
        time.sleep(1)
        Functions.captura(self, comentario)
        Functions.captura_pantalla(self)

    ######EXCEL########
    def leer_celda(self, celda):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        sheet = wb["DataTest"]
        valor = str(sheet[celda].value)
        print(u"----------------------------------")
        print(u"El libro de excel utilizado es : " + Inicializar.Excel)
        print(u"El valor de la celda es : " + valor)
        print(u"----------------------------------")
        return valor

    def escribir_celda(self, celda, valor):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        hoja = wb["DataTest"]
        hoja[celda] = valor
        wb.save(Inicializar.Excel)
        print(u"----------------------------------")
        print(u"El libro de excel utilizado es : " + Inicializar.Excel)
        print(u"Se escribio en la celda : " + str(celda) + u" el valor : " + str(valor))
        print(u"----------------------------------")

    # ---------------------------------
    ############DATABASE##############
    # --------------------------------
    def pyodbc_conn(self, _driver=Inicializar.DB_DRIVER, _host=Inicializar.DB_HOST, _port=Inicializar.DB_PORT,
                    _dbname=Inicializar.DB_DATABASE, _user=Inicializar.DB_USER, _pass=Inicializar.DB_PASS):
        try:
            conn_str = (
                f"DRIVER={_driver};"
                f"DATABASE={_dbname};"
                f"UID={_user};"
                f"PWD={_pass};"
                f"SERVER={_host};"
                f"PORT={_port};")
            conn = pyodbc.connect(conn_str)
            self.cursor = conn.cursor()
            print("Conexion exitosa")
            return self.cursor
        except (pyodbc.OperationalError) as error:
            self.conn = None
            self.cursor = None
            pytest.skip("Error en connection strings: " + str(error))

    def pyodbc_query(self, _query):
        self.cursor = Functions.pyodbc_conn(self)
        if self.cursor is not None:
            try:
                self.cursor.execute(_query)
                self.Result = self.cursor.fetchall()
                for row in self.Result:
                    print(row)
                    return row
            except (pyodbc.Error) as error:
                print("Error en la consulta ", error)
            finally:
                if (self.cursor):
                    self.cursor.close()
                    print("pyodbc Se cerró la conexion")

    def pyodbc_query_list(self, _query):
        self.cursor = Functions.pyodbc_conn(self)
        if self.cursor is not None:
            try:
                self.cursor.execute(_query)
                self.Result = self.cursor.fetchall()
                while self.Result:
                    print(self.Result)
                    return self.Result
            except (pyodbc.Error) as error:
                print("Error en la consulta ", error)
            finally:
                if (self.cursor):
                    self.cursor.close()
                    print("pyodbc Se cerró la conexion")

    #######LOGIN USERS######

    def get_signin_admin(self, user=Inicializar.userAdm, passw=Inicializar.passAdm):
        Functions.get_json_file(self, "signin")
        Functions.send_key_text(self, "Usuario", user)
        Functions.send_key_text(self, "Password", passw)
        Functions.get_elements(self, "Boton acceder").click()

    def get_signin_juan_suaza(self, user=Inicializar.userAdm, passw=Inicializar.userAdm):
        Functions.get_json_file(self, "signin")
        Functions.send_key_text(self, "Usuario", user)
        Functions.send_key_text(self, "Password", passw)
        Functions.get_elements(self, "Boton acceder").click()

    def get_signin_administrator(self, user=Inicializar.userAdm, passw=Inicializar.passAdm):
        Functions.get_json_file(self, "signin")
        Functions.send_key_text(self, "Usuario", user)
        Functions.send_key_text(self, "Password", passw)
        Functions.foto(self, "Ingresando al login")
        Functions.check_element(self, "Boton acceder")
        Functions.get_elements(self, "Boton acceder").click()

    ######CARGAR DOCUMENTOS#######

    def carga_doc_controlado(self):
        Functions.get_json_file(self, "cargarDocumento")
        Functions.check_visibility_element_located(self, "Carga documentos")
        Functions.get_elements(self, "Carga documentos").click()

        folderName = Functions.select_folder_random(self, "APIUX")
        folderName
        time.sleep(0.5)
        Functions.check_visibility_element_located(self, "Seleccionar ICD/NO")
        Functions.get_elements(self, "Seleccionar ICD/NO").click()
        Functions.get_elements(self, "Opcion NoICD").click()
        time.sleep(0.8)
        Functions.get_elements(self, "documento controlado").click()
        fileName = Functions.subida_unitaria(self)
        fileName

        Functions.set_metadata_random(self)
        Functions.check_visibility_element_located(self, "Cargar")
        Functions.get_elements(self, "Cargar").click()
        time.sleep(0.5)
        Functions.check_element(self, "Boton confirmar cargar documento")
        Functions.check_visibility_element_located(self, "Boton confirmar cargar documento")
        Functions.get_elements(self, "Boton confirmar cargar documento").click()
        return fileName, folderName

    def selecionar_primera_carpeta(self):
        time.sleep(1)
        Functions.get_json_file(self, "cargarDocumento")
        carpetaTxt = Functions.get_elements(self, "Elegir carpeta").text
        carpetaSplit = carpetaTxt.split("\n")
        carpetaUno = carpetaSplit[0]
        time.sleep(2)
        self.driver.find_element_by_xpath(f"//div/span[contains(text(),'{carpetaUno}')]").click()

    def assert_eliminar_documento_previsualizado(self):
        Functions.get_json_file(self, "documents")
        self.assertNotIn(self.nomDoc, Functions.get_text(self, "Toda la carga de documentos"),
                         "Error, La previsualizacion del documento persiste una vez borrado")

    def subida_unitaria(self):
        file = Functions.random_file(self)
        format = Functions.split(self, file, ".")
        imageNew = Inicializar.basedir + f"\\file\\.{format[1]}\\" + str(file)
        Functions.get_json_file(self, "cargarDocumento")
        Functions.check_element(self, "Seleccionar documento")
        Functions.get_elements(self, "Seleccionar documento").send_keys(imageNew)
        try:
            if self.driver.find_element_by_xpath(f"//span[contains(text(),'{file}')]"):
                print(f"***********SE CARGO EL DOCUMENTO '{file}'***********")
                return True, file
        except TimeoutException:
            Functions.foto(self, f"NO SE CARGO EL DOCUMENTO {file}")
            print(f"***********NO SE CARGO EL DOCUMENTO '{file}'***********")
            return False
        except NoSuchElementException:
            Functions.foto(self, f"NO SE CARGO EL DOCUMENTO {file}")
            print(f"***********NO SE CARGO EL DOCUMENTO '{file}'***********")
            return False

    def subida_masiva(self):
        for x in range(3):
            file = Functions.random_file(self)
            format = Functions.split(self, file, ".")
            imageNew = Inicializar.basedir + f"\\file\\.{format[1]}\\" + str(file)
            Functions.get_json_file(self, "cargarDocumento")
            Functions.check_element(self, "Seleccionar documento")
            Functions.get_elements(self, "Seleccionar documento").send_keys(imageNew)
            print(f"***********SE ESTA CARGANDO DOCUMENTO {file}***********")
            time.sleep(3)
            x += 1

    def assert_prev_documento(self):
        textPrev = Functions.get_text(self, "Espacio de previsualizacion")
        textPrevDiv = textPrev.split("\n")
        assert textPrevDiv[
                   1] == self.nomDoc, "Error, el nombre del documento con coincide con el nombre de la previsualización"

    def button_ok_error_doc_val(self):
        val = Functions.check_visibility_element_located(self, "Error boton OK")
        if val == True:
            Functions.get_elements(self, "Error boton OK").click()

    def select_folder_random(self, directory=None):  # RETORNA EL NOMBRE DE LA CARPETA

        Functions.check_click_element(self, "Seleccionar carpeta")
        Functions.get_elements(self, "Seleccionar carpeta").click()
        time.sleep(0.5)
        Functions.check_exists_by_xpath(self, "//ul[@class='MuiList-root MuiList-padding']")
        string = self.driver.find_elements_by_xpath("//ul[@class='MuiList-root MuiList-padding']")  # Elegir carpeta

        for f in string:
            f
        folders = Functions.split(self, f.text, "\n")
        if directory == "APIUX":
            xpath = self.driver.find_element_by_xpath("//span[contains(text(), 'APIUX')]")
            time.sleep(1)
            self.driver.execute_script('arguments[0].scrollIntoView(true);', xpath)
            self.driver.execute_script("arguments[0].click()", xpath)
            return "APIUX"

        if directory is None:
            True
            while True:
                folder = random.choice(folders)
                xpath = self.driver.find_element_by_xpath(f"//span[contains(text(), '{folder}')]")
                if not folder == 'ALMA Project':
                    print(f"***********Se selecciono la carpeta {folder}***********")
                    time.sleep(1)
                    self.driver.execute_script('arguments[0].scrollIntoView(true);', xpath)
                    self.driver.execute_script("arguments[0].click()", xpath)
                    return folder
                    break

    def select_projectCode(self):
        Functions.get_json_file(self, "cargarDocumento")
        Functions.check_element(self, "Campo projectCode")
        conn = Functions.pyodbc_query_list(self,
                                           "SELECT value FROM public.property_item WHERE property_name='mc:project_code'")
        data = []
        for c in conn:
            data.append(c.value)
        projectCode = random.choice(data)
        Functions.esperar_elemento(self, "Campo projectCode")
        Functions.get_elements(self, "Campo projectCode").send_keys(projectCode)
        time.sleep(0.5)
        Functions.send_especific_keys(self, "Campo projectCode", "Enter")
        time.sleep(0.5)
        return projectCode

    def select_organization(self):
        Functions.get_json_file(self, "cargarDocumento")
        Functions.check_element(self, "Campo org")
        conn = Functions.pyodbc_query_list(self,
                                           "SELECT value FROM public.property_item WHERE property_name='mc:organization'")
        data = []
        for c in conn:
            data.append(c.value)
        organization = random.choice(data)
        Functions.get_elements(self, "Campo org").send_keys(organization)
        Functions.send_especific_keys(self, "Campo org", "Enter")
        return organization

    def select_docuStatus(self):
        Functions.get_json_file(self, "cargarDocumento")
        Functions.check_element(self, "Campo docStatus")
        conn = Functions.pyodbc_query_list(self,
                                           "SELECT value FROM public.property_item WHERE property_name='mc:documentation_status'")
        data = []
        for c in conn:
            data.append(c.value)
        docuStatus = random.choice(data)
        Functions.get_elements(self, "Campo docStatus").send_keys(docuStatus)
        Functions.send_especific_keys(self, "Campo docStatus", "Enter")
        return docuStatus

    def select_docuType(self):
        Functions.get_json_file(self, "cargarDocumento")
        Functions.check_element(self, "Campo docType")
        conn = Functions.pyodbc_query_list(self,
                                           "SELECT value FROM public.property_item WHERE property_name='mc:document_type'")
        data = []
        for c in conn:
            data.append(c.value)
        docuType = random.choice(data)
        Functions.get_elements(self, "Campo docType").send_keys(docuType)
        Functions.send_especific_keys(self, "Campo docType", "Enter")
        return docuType

    def set_metadata_random(self, condition=0):
        if condition == 0:
            Functions.select_projectCode(self)
            Functions.select_organization(self)
            Functions.select_docuStatus(self)
            Functions.select_docuType(self)
        date = Functions.textDateEnvironmentReplace(self, "hoy")
        Functions.get_elements(self, "Campo date").send_keys(date)
        campos = ['Campo modifiedBy', 'Campo ownerName', 'Campo subject', 'Campo fielType',
                  'Campo author', 'Campo control board', 'Campo system', 'Campo secMode',
                  'Campo releaseBy', 'Campo docId', 'Campo forumId', 'Campo approvedBy',
                  'Campo revBy', 'Campo group', 'Campo docAbs']
        data = ['Ninguno', 'No asignado', 'Selenium', 'Notas',
                'Configuraciones', 'Finanzas', 'Seguridad', 'Documentos otros',
                'Juan Suaza', 'Felipe Bravo', 'Nadia Gallardo', 'Ignacio Bravo',
                'Desarrollador', 'Frontend', 'Backend', 'SAP', 'ERP', 'Felipe Niño',
                'Archivos muchos', 'Otros', 'Manuales otros', 'Prueba integracion',
                'Python', 'Allure', 'GCP', 'Java JPA', 'Valores 2021', 'Importante', 'Abstractos']
        value = []
        for campo in range(15):
            ran = random.choice(data)
            Functions.get_elements(self, campos[campo]).send_keys(ran)
            value.append(ran)
        return value

    def rellenar_formulario(self):
        logging.basicConfig(filename='registro.log', level='INFO')
        Functions.foto(self, "Screenshot 1")
        Functions.get_elements(self, "Campo projectCode").send_keys("ALMA - ALMA Project Documents")
        Functions.send_especific_keys(self, "Campo projectCode", "Enter")

        Functions.send_key_text(self, "Campo date", Functions.textDateEnvironmentReplace(self, "hoy"))
        Functions.send_key_text(self, "Campo modifiedBy", "Administrador")

        Functions.get_elements(self, "Campo org").send_keys("External or not ALMA doc")
        Functions.send_especific_keys(self, "Campo org", "Enter")

        Functions.send_key_text(self, "Campo ownerName", "Juan Sebatian")
        Functions.send_key_text(self, "Campo subject", "Selenium Test")
        Functions.send_key_text(self, "Campo fielType", "J P G")
        Functions.send_key_text(self, "Campo author", "Selenium Python")

        Functions.get_elements(self, "Campo docStatus").send_keys("Approved")
        Functions.send_especific_keys(self, "Campo docStatus", "Enter")

        Functions.send_key_text(self, "Campo control board", "NINGUNO")
        Functions.send_key_text(self, "Campo system", "Pruebas en sistema Windows 10")
        Functions.send_key_text(self, "Campo secMode", "Alta seguridad")
        Functions.send_key_text(self, "Campo releaseBy", "Administrador")
        Functions.send_key_text(self, "Campo docId", "DOC-ID-DOC-ID")
        Functions.send_key_text(self, "Campo forumId", "FORUM-ID-FORUM-ID")

        Functions.get_elements(self, "Campo docType").send_keys("ALMA Engineering Orders")
        Functions.send_especific_keys(self, "Campo docType", "Enter")

        Functions.send_key_text(self, "Campo approvedBy", "Nadia Gallardo")
        Functions.send_key_text(self, "Campo revBy", "Felipe Niño")
        Functions.send_key_text(self, "Campo group", "Selenium test QA")
        Functions.send_key_text(self, "Campo docAbs", "Imagen de test")
        Functions.foto(self, "Screenshot 2")
        Functions.get_elements(self, "Cargar").click()
        Functions.esperar_elemento(self, "Boton confirmar cargar documento")
        Functions.get_elements(self, "Boton confirmar cargar documento").click()
        logging.info("Se relleno correctamente la metadata")

    def metadata(self):
        logging.basicConfig(filename='registro.log', level='INFO')
        Functions.get_json_file(self, "cargarDocumento")

        al = Functions.check_visibility_element_located(self, "Campo almaDoc")
        pro = Functions.check_visibility_element_located(self, "Campo projectCode")
        dat = Functions.check_visibility_element_located(self, "Campo date")
        modiBy = Functions.check_visibility_element_located(self, "Campo modifiedBy")
        org = Functions.check_visibility_element_located(self, "Campo org")
        own = Functions.check_visibility_element_located(self, "Campo ownerName")
        subj = Functions.check_visibility_element_located(self, "Campo subject")
        fiel = Functions.check_visibility_element_located(self, "Campo fielType")
        aut = Functions.check_visibility_element_located(self, "Campo author")
        doc = Functions.check_visibility_element_located(self, "Campo docStatus")
        contr = Functions.check_visibility_element_located(self, "Campo control board")
        sys = Functions.check_visibility_element_located(self, "Campo system")
        sec = Functions.check_visibility_element_located(self, "Campo secMode")
        rel = Functions.check_visibility_element_located(self, "Campo releaseBy")
        docId = Functions.check_visibility_element_located(self, "Campo docId")
        forum = Functions.check_visibility_element_located(self, "Campo forumId")
        docTy = Functions.check_visibility_element_located(self, "Campo docType")
        appro = Functions.check_visibility_element_located(self, "Campo approvedBy")
        revBy = Functions.check_visibility_element_located(self, "Campo revBy")
        group = Functions.check_visibility_element_located(self, "Campo group")
        docAbs = Functions.check_visibility_element_located(self, "Campo docAbs")
        if (
                al and pro and dat and modiBy and org and own and subj and fiel and aut and doc and contr and sys and sec and rel and docId and forum and docTy and appro and revBy and group and docAbs) == True:
            logging.info('Se visualiza toda la metadata')
            return True
        else:
            logging.error('No se visualiza la metadata')
            return False

    def metadata_no_visible(self):
        logging.basicConfig(filename='registro.log', level='DEBUG')
        Functions.get_json_file(self, "cargarDocumento")

        al = Functions.check_invisibility_element_located(self, "Campo almaDoc")
        pro = Functions.check_invisibility_element_located(self, "Campo projectCode")
        dat = Functions.check_invisibility_element_located(self, "Campo date")
        modiBy = Functions.check_invisibility_element_located(self, "Campo modifiedBy")
        org = Functions.check_invisibility_element_located(self, "Campo org")
        own = Functions.check_invisibility_element_located(self, "Campo ownerName")
        subj = Functions.check_invisibility_element_located(self, "Campo subject")
        fiel = Functions.check_invisibility_element_located(self, "Campo fielType")
        aut = Functions.check_invisibility_element_located(self, "Campo author")
        doc = Functions.check_invisibility_element_located(self, "Campo docStatus")
        contr = Functions.check_invisibility_element_located(self, "Campo control board")
        sys = Functions.check_invisibility_element_located(self, "Campo system")
        sec = Functions.check_invisibility_element_located(self, "Campo secMode")
        rel = Functions.check_invisibility_element_located(self, "Campo releaseBy")
        docId = Functions.check_invisibility_element_located(self, "Campo docId")
        forum = Functions.check_invisibility_element_located(self, "Campo forumId")
        docTy = Functions.check_invisibility_element_located(self, "Campo docType")
        appro = Functions.check_invisibility_element_located(self, "Campo approvedBy")
        revBy = Functions.check_invisibility_element_located(self, "Campo revBy")
        group = Functions.check_invisibility_element_located(self, "Campo group")
        docAbs = Functions.check_invisibility_element_located(self, "Campo docAbs")
        if (
                al and pro and dat and modiBy and org and own and subj and fiel and aut and doc and contr and sys and sec and rel and docId and forum and docTy and appro and revBy and group and docAbs) == True:
            logging.info('Correcto, no se visualiza la metadata')
            return True
        else:
            logging.error('La metadata es visible')
            return False

    def rellenar_formulario_campos_requeridos(self):

        Functions.get_elements(self, "Campo projectCode").send_keys("ALMA - ALMA Project Documents")
        Functions.send_especific_keys(self, "Campo projectCode", "Enter")

        Functions.send_key_text(self, "Campo date", Functions.textDateEnvironmentReplace(self, "hoy"))

        Functions.send_key_text(self, "Campo subject", "Selenium Test")
        Functions.send_key_text(self, "Campo author", "Selenium Python")

        Functions.get_elements(self, "Campo docType").send_keys("ALMA Engineering Orders")
        Functions.send_especific_keys(self, "Campo docType", "Enter")

        print("Fin formulario con campos requeridos")

    def rellenar_habilitar_boton(self):
        Functions.get_elements(self, "Seleccionar carpeta").click()
        Functions.selecionar_primera_carpeta(self)
        Functions.get_elements(self, "Seleccionar ICD/NO").click()
        Functions.get_elements(self, "Opcion NoICD").click()
        Functions.subida_unitaria(self)
        Functions.check_element(self, "Imagen doc cargado")
        Functions.check_visibility_element_located(self, "Imagen doc cargado")
        target = Functions.get_elements(self, "Cargar")
        self.driver.execute_script('arguments[0].scrollIntoView(true);', target)
        Functions.foto(self, "documento")

    def seleccionar_etiqueta(self):
        Functions.get_json_file(self, "documents")
        Functions.esperar_elemento(self, "Checkbox etiquetas")
        Functions.get_elements(self, "Checkbox etiquetas").click()
        Functions.captura(self, "Seleccion de etiquetas")
        Functions.captura_pantalla(self)
        assert Functions.esperar_elemento(self,
                                          "Seleccionar etiqueta") == True, "Error, no se encuentra la etiqueta que se requiere seleccionar"
        Functions.get_elements(self, "Seleccionar etiqueta").click()
        Functions.get_elements(self, "Salir de checkbox etiqueta").click()

    def assert_msj_carga_exitosa(self):
        Functions.get_json_file(self, "documents")
        Functions.esperar_elemento(self, "Error boton OK")
        msj = Functions.get_elements(self, "Generacion de AlmaID").text
        separarMsj = msj.split("\n")
        assert separarMsj[0] == "AlmaID Generado con éxito", "ERROR, No se visualiza el almaID"
        assert separarMsj[2] == self.nomDoc, "ERROR, el nombre del documento cargado no coincide con el del mensaje"

    def scroll_final_pagina(self, locator):
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "xpath":
                    deslizar = self.driver.find_element_by_xpath(self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", deslizar)
                print("get_select_elements: " + self.json_ValueToFind)
                return deslizar
            except TimeoutException:
                print("No se encontro el elemento" + self.json_ValueToFind)
                Functions.tearDown(self)
            except NoSuchElementException:
                print("No se encontro el elemento" + self.json_ValueToFind)
                Functions.tearDown(self)

    #######DIRECTORIOS##############
    def directorio_random(self):
        n = random.randint(1, 100)
        nomWork = f"Test{n}"
        return nomWork

    def dir_random(self, n2):
        n = random.randint(1, n2)
        return n

    #######VISUALIZAR DOCUMENTO CARGADO EN LA GRILLA##########
    def vizualizar_documento(self):
        Functions.get_json_file(self, "directorios_grilla")
        Functions.get_elements(self, "Primera carpeta").click()
        elementoVi = Functions.check_click_element(self, "Visualizar primer documento")
        if elementoVi == True:
            Functions.get_elements(self, "Visualizar primer documento").click()
        if elementoVi == False:
            Functions.get_elements(self, "Segunda carpeta").click()
            elemento2Vi = Functions.check_click_element(self, "Visualizar primer documento")
            if elemento2Vi == True:
                Functions.get_elements(self, "Visualizar primer documento").click()
            if elemento2Vi == False:
                Functions.get_elements(self, "Tercera carpeta").click()
                Functions.get_elements(self, "Visualizar primer documento").click()

    def comprobar_carpeta_con_archivos(self):
        carpetas = self.driver.find_elements_by_xpath(
            "//p[@style='font-family: Poppins; font-size: 14px; font-weight: 400; padding: 4px 30px 8px 0px;']")
        for carpeta in range(len(carpetas)):
            carpeta += 1
        condition = False
        while condition == False:
            n = random.randint(1, carpeta)
            xpath = f"//body/div[@id='app-site']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/div[{n}]/li[1]/div[1]/div[2]/div[1]/p[1]"
            time.sleep(0.8)
            self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(xpath))
            Functions.get_json_file(self, "tree")
            if Functions.check_element(self, "comprobar tbody") == True:
                print("'" + self.driver.find_element_by_xpath(xpath).text + "'" + " si tiene directorios")
                return self.driver.find_element_by_xpath(xpath).text
                condition == True
                break
            print("'" + self.driver.find_element_by_xpath(xpath).text + "'" + " no tiene directorios")
            condition == False

    ############## ALFRESCO ############################
    def carpeta_alfresco(self):
        Functions.get_json_file(self, "alfresco")
        Functions.check_visibility_element_located(self, "user")
        Functions.get_elements(self, "user").send_keys("admin")
        Functions.get_elements(self, "password").send_keys("Alma2021")
        Functions.get_elements(self, "boton ingresar").click()
        Functions.new_window(self,
                             "http://10.200.33.17:8080/share/page/repository#filter=path%7C%2FBiblioteca_Documental%7C&page=1")
        Functions.get_text(self, "carpetas de alfresco")

    def etiqueta_random(self):
        n = random.randint(1, 100)
        nomTag = f"Etiqueta {n}"
        print(f"Se crea con el nombre de {nomTag}")
        return nomTag

    ############## GENERAR ENLACE COMPARTIR ############################
    def direccionar_crear_enlace_password(self):
        Functions.get_signin_administrator(self)
        Functions.comprobar_carpeta_con_archivos(self)
        Functions.get_json_file(self, "directorios_grilla")
        Functions.esperar_elemento(self, "Ingresar a compartir")
        Functions.get_elements(self, "Ingresar a compartir").click()
        Functions.esperar_elemento(self, "Compartir")
        self.driver.execute_script("arguments[0].click()", Functions.get_elements(self, "Compartir"))
        Functions.send_key_text(self, "Campo fecha compartir", Functions.textDateEnvironmentReplace(self, "hoy"))
        Functions.send_key_text(self, "Campo password compartir", self.password)

    def flujo_compartir(self, valor):
        Functions.comprobar_carpeta_con_archivos(self)
        Functions.get_json_file(self, "compartir")
        Functions.esperar_elemento(self, "Ingresar a compartir")
        time.sleep(0.5)
        Functions.get_elements(self, "Ingresar a compartir").click()
        Functions.esperar_elemento(self, "Compartir")
        Functions.foto(self, "boton compartir")
        self.driver.execute_script("arguments[0].click()", Functions.get_elements(self, "Compartir"))
        Functions.check_visibility_element_located(self, "Todo el campo compartir")
        Functions.foto(self, "Visibilidad del área compartir documento")

        Functions.get_json_file(self, "compartir")
        Functions.check_element(self, "Campo fecha")
        Functions.get_elements(self, "Campo fecha").send_keys(Functions.textDateEnvironmentReplace(self, "hoy"))

        if valor == 1:
            Functions.get_elements(self, "Campo password").send_keys(self.password)
            Functions.foto(self, "Campos rellenados")

        if valor == 0:
            Functions.get_elements(self, "checkbox").click()
            Functions.foto(self, "Campos rellenados")

    def generar_enlace(self):
        Functions.check_element(self, "Boton crear al compartir")
        time.sleep(2)
        Functions.get_elements(self, "Boton crear al compartir").click()
        time.sleep(4)
        enlaceText = Functions.get_elements(self, "Generar enlace").get_attribute("value")
        return enlaceText

    ############## DESCARGAR UN DOCUMENTO ############################
    def descargar_documento(self, nombreArchivo):  ##Devuelve True o False
        time.sleep(3)
        descarga = os.listdir(Inicializar.basedir + "\\downloads")
        val = nombreArchivo in descarga
        if val == True:
            print(f"Se descargó el archivo {nombreArchivo} correctamente!")
            return val
        if val == False:
            print(f"No se pudo descargar el archivo {nombreArchivo}!")
            return val

    def borrar_descarga(self, nombreArchivo):
        os.remove(Inicializar.basedir + "\\downloads\\" + nombreArchivo)
        print(f"Se borró el archivo {nombreArchivo} de la carpeta downloads")

    ########################COMENTARIOS###########################
    def direccionar_a_comentarios(self):
        Functions.get_signin_administrator(self)
        Functions.comprobar_carpeta_con_archivos(self)
        Functions.get_json_file(self, "directorios_grilla")
        Functions.esperar_elemento(self, "Visualizar primer documento")
        Functions.get_elements(self, "Visualizar primer documento").click()

    def escribir_un_comentario(self, caracterEspecial):
        Functions.direccionar_a_comentarios(self)
        Functions.get_json_file(self, "comentarios")
        Functions.get_elements(self, "boton Comentarios").click()
        while False:
            Functions.check_visibility_element_located(self, "Boton ingresar comentario")
        Functions.get_elements(self, "Input").send_keys(caracterEspecial)
        Functions.get_elements(self, "Boton ingresar comentario").click()

    def random_file(self):
        date = Functions.textDateEnvironmentReplace(self, "hoy")
        folder = os.listdir(Inicializar.basedir + "\\file")
        pos = random.randint(0, 4)
        file = os.listdir(Inicializar.basedir + f"\\file\\{folder[pos]}")
        os.rename(Inicializar.basedir + f"\\file\\{folder[pos]}\\" + file[0],
                  Inicializar.basedir + f"\\file\\{folder[pos]}\\" + "generate_test_" + date + Functions.generate_id(
                      length=3) + folder[pos])
        newFile = os.listdir(Inicializar.basedir + f"\\file\\{folder[pos]}")
        print(newFile[0])
        return newFile[0]

    def generate_id(length):
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        result_int = ''.join(random.choice(string.digits) for i in range(length))
        r = "_" + str(random.randint(1, 10)) + result_str + result_int
        return r

    def get_data_metadata(self, numero):  # 2: AlmaID
        nomCapeta = Functions.comprobar_carpeta_con_archivos(self)
        element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
        metadata = []
        for x in range(len(element)):
            x += 1
            Functions.get_json_file(self, "breadCrumbs")
            self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()  # Boton VISUALIZAR
            Functions.foto(self, "Metadata")
            if Functions.check_element(self, "metadata") == False:
                Functions.foto(self, "Error")
                pytest.skip(f"[PRUEBA SALTADA] Al parecer hay un ERROR, la metadata no se visualiza")
            valores = Functions.split(self, Functions.get_elements(self, "metadata").text, "\n")
            metadata.append(valores[numero])
            self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()
        return metadata

    def get_doc_name(self, foto):  # Obtener nombre de documentos en la grilla
        element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
        document = []
        for x in range(len(element)):
            x += 1
            Functions.get_json_file(self, "breadCrumbs")
            nommbredoc = self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[1]").text  # Boton VISUALIZAR
            if x == 1 and foto == "si":
                Functions.foto(self, "grilla")
            document.append(nommbredoc)
        return document

    def wait(self, tipo):  # TRUE O FALSE  (Tipo: Eliminando...    Cargando...)
        try:
            wait = WebDriverWait(self.driver, 0.1)
            wait.until(EC.invisibility_of_element_located((By.XPATH, f"//h2[contains(text(), '{tipo}')]")))
        except TimeoutException:
            print("No existe el elemento" + f"//h2[contains(text(), '{tipo}')]")
            return False
        except NoSuchElementException:
            print("No existe el elemento" + f"//h2[contains(text(), '{tipo}')]")
            return False
        return True
