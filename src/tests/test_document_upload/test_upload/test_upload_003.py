# -*- coding: utf-8 -*-
import unittest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'Campo, Seleccionar carpeta', u'https://api-ux.atlassian.net/browse/ALMA-300')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Validación:</br>
Estado</br>
Funcionalidad</br>
Visibilidad</br>
Congruencia con el arbol de directorios</br>
Seleccionar, luego salir y volver entrar</br>
</br></br>""")

class test_upload_003(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Selector de carpetas.')
    @allure.story(u'Comprobando localizacion y visibilidad del selector de carpetas.')
    def test_seleccionarCarpeta_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Localizando el selector de carpetas'):
            Selenium.foto(self, "selector de carpetas")
            check = Selenium.check_element(self, "Seleccionar carpeta")
            visibilidad = Selenium.check_visibility_element_located(self, "Seleccionar carpeta")
            self.assertTrue(check and visibilidad, "Error, no se localiza o visualiza el selector")

    @allure.title(u'Selector de carpetas.')
    @allure.story(u'Comprobando estado del selector de carpetas.')
    def test_seleccionarCarpeta_002(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Localizando el selector de carpetas'):
            Selenium.foto(self, "selector de carpetas")
            click = Selenium.check_click_element(self, "Seleccionar carpeta")
            self.assertTrue(click, "Error, el selector no es clickable")

    @allure.title(u'Selector de carpetas.')
    @allure.story(u'Comprobar que se limpia el selector al salir de la carga.')
    def test_seleccionarCarpeta_003(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar una carpeta'):
            Selenium.check_element(self, "Seleccionar carpeta")
            Selenium.get_elements(self, "Seleccionar carpeta").click()
            Selenium.selecionar_primera_carpeta(self)
            Selenium.foto(self, "Carpeta seleccionada")

        with allure.step(u'PASO 5 : Refrescar Carga de Documentos'):
            Selenium.get_elements(self, "Carga documentos").click()
            Selenium.foto(self, "Deberia refrescarse el selector")

        with allure.step(u'PASO 6 : Validando que el selector este vacio'):
            nuevoValor = Selenium.get_elements(self, "Seleccionar carpeta").get_attribute("value")
            assert nuevoValor == "", "Error, El selector no se a limpiado"

    @allure.title(u'Selector de carpetas.')
    @allure.story(u'Congruencia entre selector y arbol de directorios.')
    def test_seleccionarCarpeta_004(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Obteniendo carpetas del selector'):
            Selenium.check_element(self, "Seleccionar carpeta")
            Selenium.get_elements(self, "Seleccionar carpeta").click()
            Selenium.esperar_elemento(self, "Elegir carpeta")
            selector = Selenium.get_elements(self, "Elegir carpeta").text
            carpeta = selector.split("\n")
            Selenium.foto(self, "Carpetas del selector")

        with allure.step(u'PASO 5 : Obteniendo directorios del arbol'):
            arbol = Selenium.get_elements(self, "Arbol de directorios").text
            directorio = arbol.split("\n")

        with allure.step(u'PASO 6 : Comparando carpetas '):
            assert carpeta == directorio, "Error, no coinciden"

    @allure.title(u'Selector de carpetas.')
    @allure.story(u'Congruencia entre selector y la base de datos.')
    def test_seleccionarCarpeta_005(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Obteniendo carpetas del selector'):
            Selenium.check_element(self, "Seleccionar carpeta")
            Selenium.get_elements(self, "Seleccionar carpeta").click()
            Selenium.esperar_elemento(self, "Elegir carpeta")
            selector = Selenium.get_elements(self, "Elegir carpeta").text
            carpeta = selector.split("\n")
            data = []
            for con in carpeta:
                data.append(con)
            Selenium.foto(self, "Carpetas del selector")

        with allure.step(u'PASO 5 : Consultando y validando directorios en la base de datos'):
            for nom in range(len(data)):
                bd = Selenium.pyodbc_query_list(self, f"SELECT name FROM company_folder WHERE name='{data[nom]}'")
                assert not bd == None, f"ERROR, No se encuentra la carpeta {data[nom]} en la base de datos"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))