import datetime
import time
import allure
import openpyxl
import pyodbc as pyodbc
import pytest
import json
import os
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
diaGlobal= time.strftime(Inicializar.DateFormat)
horaGlobal= time.strftime(Inicializar.HourFormat)

class Functions(Inicializar):
    #INICIAR DRIVERS
    def open_browser(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        print("Directorio base : ",Inicializar.basedir)
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
            self.ventanas = {'Principal' : self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == ("CHROME"):
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            options.add_experimental_option("prefs", {"download.default_directory" : Inicializar.basedir +"\\downloads"})
            self.driver = webdriver.Chrome(options=options, executable_path=Inicializar.basedir + "\\drivers\\chromedriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.delete_all_cookies()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]
            self.ventanas = {'Principal' : self.driver.window_handles[0]}
            return self.driver

        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox(executable_path=Inicializar.basedir + "\\drivers\\geckodriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.ventanas = {'Principal' : self.driver.window_handles[0]}
            return self.driver

    def tearDown(self):
        print("Se cerrará el DRIVER")
        self.driver.quit()

    ####################
    #*_LOCATORS HANDLE_*#
    ####################
    def xpath_element(self, XPATH):
        elements = self.driver.find_element_by_xpath(XPATH)
        print("Xpath_Elements: Se interactuo con el elemento "+XPATH)
        return elements

    def _xpath_element(self, XPATH):
        try:
            elements = self.driver.find_element_by_xpath(XPATH)
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
            wait.until(EC.element_to_be_clickable((By.XPATH, XPATH)))
            print(u"Esperar_Elemento: Se visualizo el elemento "+XPATH)
            return elements
        except TimeoutException:
            print(u"Esperar_elemento: No presente "+XPATH)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar_elemento: No existe " + XPATH)
            Functions.tearDown(self)

    def css_element(self, CSS):
        elements = self.driver.find_element_by_xpath(CSS)
        print("CSS_Selector_Elements: Se interactuo con el elemento "+CSS)
        return elements

    def _css_element(self, CSS):
        try:
            elements = self.driver.find_element_by_xpath(CSS)
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, CSS)))
            wait.until(EC.element_to_be_clickable((By.XPATH, CSS)))
            print(u"Esperar_Elemento: Se visualizo el elemento "+CSS)
            return elements
        except TimeoutException:
            print(u"Esperar_elemento: No presente "+CSS)
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
                print("get_json_file: "+ json_path)
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el archivo " + file)
            Functions.tearDown(self)

    def get_entity(self, entity):
        if self.json_strings is False:
            print("Define el DOM para esta prueba")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True
            except KeyError:
                pytest.skip(u"get_entity: No se encontro la key a la cual se hace referencia: " + entity)
                #self.driver.close()
                Functions.tearDown(self)
                return None

    def get_elements(self, entity, MyTextElement = None):
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
                return elements
            except NoSuchElementException:
                print("get_text: No se encontró el elemento: "+ self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    def get_text(self, entity, MyTextElement = None):
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
                print("Text Value : "+ elements.text)
                return elements.text

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: "+ self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

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

    def check_element(self, locator): # Devuelve TRUE o FALSE
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
                    wait.until(EC.presence_of_element_located((By.NAME, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
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

    def check_click_element(self, locator): # Devuelve TRUE o FALSE
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

    def check_visibility_element_located(self, locator): # Devuelve TRUE o FALSE
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

    def check_invisibility_element_located(self, locator): # Devuelve TRUE o FALSE
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.invisibility_of_element_located((By.ID, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.invisibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.invisibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.invisibility_of_element_located((By.LINK_TEXT, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"check_element: Se vizualizo el elemento " + locator)
                    return True

            except NoSuchElementException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                return False
            except TimeoutException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
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
        print(f"Comparando los valores... verificando que si {variable_scenary} esta presente en {element_text} : {_exist}")
        assert _exist == True, f'{variable_scenary} != {element_text}'

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
        time.sleep(2)
        PATH = self.crear_path()
        TestCase = self.__class__.__name__
        img = f'{PATH}/{TestCase}_(' + str(Functions.hora_Actual(self)) + ')' + '.png'
        self.driver.get_screenshot_as_file(img)
        print(img)
        return img

    def captura(self, Descripcion):
        allure.attach(self.driver.get_screenshot_as_png(), Descripcion, attachment_type= allure.attachment_type.PNG)

    def foto(self, comentario):
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

    #---------------------------------
    ############DATABASE##############
    # --------------------------------
    def pyodbc_conn(self,_driver = Inicializar.DB_DRIVER ,_host = Inicializar.DB_HOST, _port = Inicializar.DB_PORT, _dbname = Inicializar.DB_DATABASE, _user = Inicializar.DB_USER, _pass = Inicializar.DB_PASS):
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
                if(self.cursor):
                    self.cursor.close()
                    print("pyodbc Se cerró la conexion")

    #######LOGIN USERS######

    def get_signin_admin(self, user = Inicializar.userAdm, passw = Inicializar.passAdm):
        Functions.get_json_file(self, "signin")
        Functions.send_key_text(self, "Usuario", user)
        Functions.send_key_text(self, "Password", passw)
        Functions.get_elements(self, "Boton acceder").click()

    def get_signin_juan_suaza(self, user = Inicializar.userJuan, passw = Inicializar.passJuan):
        Functions.get_json_file(self, "signin")
        Functions.send_key_text(self, "Usuario", user)
        Functions.send_key_text(self, "Password", passw)
        Functions.get_elements(self, "Boton acceder").click()

    def get_signin_juan_suaza(self, user=Inicializar.userJuan, passw=Inicializar.passJuan):
        Functions.get_json_file(self, "signin")
        Functions.send_key_text(self, "Usuario", user)
        Functions.send_key_text(self, "Password", passw)
        Functions.get_elements(self, "Boton acceder").click()

    ######CARGAR DOCUMENTOS#######

    def selecionar_primera_carpeta(self):
        Functions.get_json_file(self, "documents")
        carpetaTxt = Functions.get_elements(self, "Elegir carpeta").text
        carpetaSplit = carpetaTxt.split("\n")
        carpetaUno = carpetaSplit[0]
        self.driver.find_element_by_xpath(f"//div/span[contains(text(),'{carpetaUno}')]").click()

    def assert_eliminar_documento_previsualizado(self):
        Functions.get_json_file(self, "documents")
        self.assertNotIn(self.nomDoc, Functions.get_text(self, "Toda la carga de documentos"), "Error, La previsualizacion del documento persiste una vez borrado")

    def subir_documento(self):
        while True:
            n = random.randint(1, 26)
            imageNew = f"C:\\Users\\pipe_\\Desktop\\QA\\qa{n}.PNG"
            validImageNew = f"qa{n}.PNG"
            Functions.get_elements(self, "Selecionar documento").send_keys(imageNew)
            self.prev = Functions.check_element(self, "Esperar nombre documento en previsualizacion")
            if self.prev == True:
                self.nomDoc = Functions.get_elements(self, "Esperar nombre documento en previsualizacion").text
                assert validImageNew == self.nomDoc
                print(f"Se cargó el archivo {validImageNew}")
                break
            errorDocRepetido = Functions.check_click_element(self, "Error boton OK")
            if errorDocRepetido == True:
                Functions.esperar_elemento(self, "Error boton OK")
                Functions.get_elements(self, "Error boton OK").click()
            continue
        Functions.button_ok_error_doc_val(self)

    def assert_prev_documento(self):
        textPrev = Functions.get_text(self, "Espacio de previsualizacion")
        textPrevDiv = textPrev.split("\n")
        assert textPrevDiv[1] == self.nomDoc, "Error, el nombre del documento con coincide con el nombre de la previsualización"

    def button_ok_error_doc_val(self):
        val = Functions.check_visibility_element_located(self, "Error boton OK")
        if val == True:
            Functions.get_elements(self, "Error boton OK").click()

    def rellenar_formulario(self, almaDoc = Inicializar.almaDoc, modifiedBy = Inicializar.modifiedBy, ownerName = Inicializar.ownerName, subject = Inicializar.subject, fielType = Inicializar.fielType, author = Inicializar.author, system = Inicializar.system, secMode = Inicializar.secMode, releaseBy = Inicializar.releaseBy, docId = Inicializar.docId, forumId = Inicializar.forumId, approvedBy = Inicializar.approvedBy, revBy = Inicializar.revBy, group = Inicializar.group, docAbs = Inicializar.docAbs):

        Functions.send_key_text(self, "Campo almaDoc", almaDoc)

        Functions.get_elements(self, "Campo projectCode").click()
        Functions.get_elements(self, "Campo selectProjectCode").click()

        Functions.send_key_text(self, "Campo date", Functions.textDateEnvironmentReplace(self, "hoy"))
        Functions.send_key_text(self, "Campo modifiedBy", modifiedBy)

        Functions.get_elements(self, "Campo org").click()
        Functions.get_elements(self, "Campo selectOrg").click()

        Functions.send_key_text(self, "Campo ownerName", ownerName)
        Functions.send_key_text(self, "Campo subject", subject)
        Functions.send_key_text(self, "Campo fielType", fielType)
        Functions.send_key_text(self, "Campo author", author)

        Functions.get_elements(self, "Campo docStatus").click()
        Functions.get_elements(self, "Campo selectDocStatus").click()

        Functions.send_key_text(self, "Campo system", system)
        Functions.send_key_text(self, "Campo secMode", secMode)
        Functions.send_key_text(self, "Campo releaseBy", releaseBy)
        Functions.send_key_text(self, "Campo docId", docId)
        Functions.send_key_text(self, "Campo forumId", forumId)

        Functions.get_elements(self, "Campo docType").click()
        Functions.get_elements(self, "Campo selectDocType").click()

        Functions.send_key_text(self, "Campo approvedBy", approvedBy)
        Functions.send_key_text(self, "Campo revBy", revBy)
        Functions.send_key_text(self, "Campo group", group)
        Functions.send_key_text(self, "Campo docAbs", docAbs)
        print("Fin formulario")

    def rellenar_formulario_campos_requeridos(self, subject = Inicializar.subject, author = Inicializar.author):

        Functions.get_elements(self, "Campo projectCode").click()
        Functions.get_elements(self, "Campo selectProjectCode").click()

        Functions.send_key_text(self, "Campo date", Functions.textDateEnvironmentReplace(self, "hoy"))

        Functions.send_key_text(self, "Campo subject", subject)
        Functions.send_key_text(self, "Campo author", author)

        Functions.get_elements(self, "Campo docType").click()
        Functions.get_elements(self, "Campo selectDocType").click()

        print("Fin formulario con campos requeridos")

    def seleccionar_etiqueta(self):
        Functions.get_json_file(self, "documents")
        Functions.esperar_elemento(self, "Checkbox etiquetas")
        Functions.get_elements(self, "Checkbox etiquetas").click()
        Functions.captura(self, "Seleccion de etiquetas")
        Functions.captura_pantalla(self)
        assert Functions.esperar_elemento(self,"Seleccionar etiqueta") == True, "Error, no se encuentra la etiqueta que se requiere seleccionar"
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
        Functions.get_json_file(self, "directorios_grilla")
        x = False
        while x == False:
            Functions.check_visibility_element_located(self, "Primera carpeta")
            Functions.get_elements(self, "Primera carpeta").click()
            elementoVi = Functions.check_visibility_element_located(self, "Primer documento")
            if elementoVi == True:
                x == True
                break
            else:
                Functions.check_visibility_element_located(self, "Segunda carpeta")
                Functions.get_elements(self, "Segunda carpeta").click()
                elementoVi2 = Functions.check_visibility_element_located(self, "Primer documento")
                if elementoVi2 == True:
                    x == True
                    break
                else:
                    Functions.check_visibility_element_located(self, "Tercera carpeta")
                    Functions.get_elements(self, "Tercera carpeta").click()
                    elementoVi3 = Functions.check_visibility_element_located(self, "Primer documento")
                    if elementoVi3 == True:
                        x == True
                        break
                    else: print("No se encontro ninguna carpeta con archivos.")

    ############## ALFRESCO ############################
    def carpeta_alfresco(self):
        Functions.get_json_file(self, "alfresco")
        Functions.check_visibility_element_located(self, "user")
        Functions.get_elements(self, "user").send_keys("admin")
        Functions.get_elements(self, "password").send_keys("Alma2021")
        Functions.get_elements(self, "boton ingresar").click()
        Functions.new_window(self, "http://10.200.33.17:8080/share/page/repository#filter=path%7C%2FBiblioteca_Documental%7C&page=1")
        Functions.get_text(self, "carpetas de alfresco")

    def etiqueta_random(self):
        n = random.randint(1, 100)
        nomTag = f"Etiqueta {n}"
        print(f"Se crea con el nombre de {nomTag}")
        return nomTag


    ############## GENERAR ENLACE COMPARTIR ############################
    def direccionar_crear_enlace_password(self):
        Functions.get_signin_juan_suaza(self)
        Functions.comprobar_carpeta_con_archivos(self)
        Functions.get_json_file(self, "directorios_grilla")
        Functions.get_elements(self, "Ingresar a compartir").click()
        Functions.send_key_text(self, "Campo fecha compartir", self.dateUntil)
        Functions.send_key_text(self, "Campo password compartir", self.password)

    def generar_enlace(self):
        Functions.get_elements(self, "Boton crear al compartir").click()
        enlaceText = Functions.get_elements(self, "Generar enlace").get_attribute("value")
        return enlaceText

    ############## DESCARGAR UN DOCUMENTO ############################
    def descargar_documento(self, nombreArchivo): ##Devuelve True o False
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
        os.remove(Inicializar.basedir + "\\downloads\\"+nombreArchivo)
        print(f"Se borró el archivo {nombreArchivo} de la carpeta downloads")
