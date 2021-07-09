# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'Campo, Documento controlado o no', u'https://api-ux.atlassian.net/browse/ALMA-302')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Estado</br>
Funcionalidad</br>
Visibilidad</br>
Validacion sobre elementos que se habilitan al marca 'controlado'</br>
</br></br>""")

class test_upload_004(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Checkbox Documento controlado.')
    @allure.story(u'Comprobando localizacion y visibilidad del checkbox documento controlado.')
    def test_checkbox_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Localizando el checkbox'):
            Selenium.foto(self, "checkbox")
            check = Selenium.check_element(self, "documento controlado")
            txt = self.driver.find_element_by_xpath("//span[contains(text(),'Documento controlado')]").text

        with allure.step(u'PASO 5 : Validando'):
            Selenium.foto(self, "checkbox, documento controlado")
            self.assertTrue(check, "Error, no se localiza o visualiza el checkbox")
            assert txt == "Documento controlado", "ERROR, se a cambiado el nombre del checkbox"

    @allure.title(u'Checkbox Documento controlado.')
    @allure.story(u'Comprobando que el checkbox sea clickable.')
    def test_checkbox_002(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Validando que el checkbox no este seleccinado'):
            Selenium.foto(self, "checkbox, documento controlado")
            seleccionado = Selenium.get_elements(self, "documento controlado").is_selected()
            self.assertFalse(seleccionado, "Error, el checkbox esta seleccionado")

    @allure.title(u'Checkbox Documento controlado.')
    @allure.story(u'Comprobar que se limpia el checkbox al salir de la carga.')
    def test_checkbox_003(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar una checkbox'):
            time.sleep(3)
            Selenium.get_elements(self, "documento controlado").click()
            Selenium.foto(self, "Deberia refrescarse el checkbox")
            while False :
                seleccionado = Selenium.get_elements(self, "documento controlado").is_selected()
                self.assertTrue(seleccionado, "No se selecciono el checkbox")

        with allure.step(u'PASO 5 : Refrescar Carga de Documentos'):
            Selenium.get_elements(self, "Carga documentos").click()
            Selenium.check_element(self, "documento controlado")
            Selenium.foto(self, "Deberia refrescarse el checkbox")

        with allure.step(u'PASO 6 : Validando que el checkbox este vacio'):
            checkbox = Selenium.get_elements(self, "documento controlado").is_selected()
            assert checkbox == False, "Error, El checkbox no se a limpiado"

    @allure.title(u'Checkbox Documento controlado.')
    @allure.story(u'Validar que el checkbox habilite elementos.')
    def test_checkbox_004(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar una checkbox'):
            time.sleep(3)
            Selenium.foto(self, "Antes de clickar el checkbox")
            Selenium.get_elements(self, "documento controlado").click()
            while False:
                seleccionado = Selenium.get_elements(self, "documento controlado").is_selected()
                self.assertTrue(seleccionado, "No se selecciono el checkbox")
            Selenium.foto(self, "despues de clickar el checkbox")

        with allure.step(u'PASO 5 : Buscando nuevos elementos'):
            nuevosEle = Selenium.get_elements(self, "nuevos elementos").text

        with allure.step(u'PASO 6 : Validando visibilidad de los elementos'):
            self.assertIn("Carga de documentos", nuevosEle, "ERROR, los nombre no coinciden")
            self.assertIn("Solicitud de Revisión y Aprobación", nuevosEle, "ERROR, los nombre no coinciden")

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))