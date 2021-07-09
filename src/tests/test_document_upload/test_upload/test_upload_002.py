# -*- coding: utf-8 -*-
import unittest
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'Funcionalidades del boton limpiar', u'https://api-ux.atlassian.net/jira/software/projects/ALMA/boards/224?selectedIssue=ALMA-224' u'https://api-ux.atlassian.net/browse/ALMA-301')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Validación:</br>
Estado</br>
Funcionalidad</br>
Que no se desaparescan elementos al limpiar</br>
Prueba de integracion. Limpiar todos los campos</br>
</br></br>""")

class test_upload_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.wait = WebDriverWait(self.driver, 20)
            self.bLimpíar=(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']")####BOTON LIMPIAR###

    @allure.story(u'Comprobando localizacion del boton limpiar.')
    def test_limpiar_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "documents")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()

        with allure.step(u'PASO 4 : Localizando el boton limpiar'):
            def retornar():
                try:
                    self.wait.until(EC.presence_of_element_located(self.bLimpíar))
                    return True
                except TimeoutException:
                    return False

            Selenium.foto(self, "Boton limpiar")
            self.assertTrue(retornar(), "Error, no se localiza el boton")

    @allure.story(u'Comprobando visualizacion del boton limpiar.')
    def test_limpiar_002(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "documents")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()

        with allure.step(u'PASO 4 : Validando visualizacion el boton limpiar'):
            def retornar():
                try:
                    self.wait.until(EC.visibility_of_element_located(self.bLimpíar))
                    return True
                except TimeoutException:
                    return False

            Selenium.foto(self, "Boton limpiar")
            self.assertTrue(retornar(), "Error, el boton limpiar no es visible")

    @allure.story(u'Comprobando que el boton sea clikable y no este bloqueado.')
    def test_limpiar_003(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "documents")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()

        with allure.step(u'PASO 4 : Comprobando si el boton es clickable'):
            def click():
                try:
                    self.wait.until(EC.element_to_be_clickable(self.bLimpíar))
                    return True
                except TimeoutException:
                    return False
            Selenium.foto(self, "Boton limpiar")
            self.assertTrue(click(), "Error, el boton limpiar no es visible")
            assert self.driver.find_element(*self.bLimpíar).is_enabled() == True, "Error, el boton esta bloqueado"

    @allure.title(u'[Carga Doc.] Botón Limpiar.')
    @allure.story(u'Al presionar el boton limpiar, no deberia desaparecer ningun elemento de la pagina.')
    def test_limpiar_004(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.foto(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Click en limpiar'):
            Selenium.check_element(self, "Limpiar")
            Selenium.foto(self, "Antes de limpiar")
            Selenium.get_elements(self, "Limpiar").click()

        with allure.step(u'PASO 5 : Comprobando visibilidad de los elementos'):
            carpetas = Selenium.check_visibility_element_located(self, "Seleccionar carpeta")
            noIcd = Selenium.check_visibility_element_located(self, "Seleccionar ICD/NO")
            docControlado = Selenium.check_element(self, "documento controlado")
            cargarDoc = Selenium.check_visibility_element_located(self, "Area de carga documentos")
            etiquetas = Selenium.check_visibility_element_located(self, "Etiquetas")
            limpiar = Selenium.check_visibility_element_located(self, "Limpiar")
            cargar = Selenium.check_visibility_element_located(self, "Cargar")
            Selenium.foto(self, "Despues de limpiar")
            self.assertTrue(carpetas and noIcd and docControlado and cargar and cargarDoc and etiquetas and limpiar, "Error, uno o mas elementos ya no son visibles o localizables")

    @allure.title(u'[Carga Doc.] Botón Limpiar.')
    @allure.story(u'Al presionar el boton limpiar, este deberia de limpiar el selector de carpetas, que se rellenó posteriormente.')
    def test_limpiar_005(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.foto(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Click en limpiar'):
            Selenium.foto(self, "Antes de limpiar")
            Selenium.check_element(self, "Limpiar")
            Selenium.get_elements(self, "Limpiar").click()

        with allure.step(u'PASO 5 : Eligiendo una carpeta'):
            Selenium.get_elements(self, "Seleccionar carpeta").click()
            Selenium.selecionar_primera_carpeta(self)
            Selenium.foto(self, "Carpeta elegida")

        with allure.step(u'PASO 6 : Presionando boton limpiar'):
            Selenium.get_elements(self, "Limpiar").click()
            valor = Selenium.get_elements(self, "Seleccionar carpeta").get_attribute("value")
            Selenium.foto(self, "Despues de limpiar")
            assert valor == "", f"Error, No se limpio el selector, el valor seleccioando es {valor}"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))