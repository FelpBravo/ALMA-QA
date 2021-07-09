# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Buscador general')
@allure.testcase(u'Busqueda simple', u'https://api-ux.atlassian.net/browse/ALMA-271')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Visualizar nombre del buscador general </br>
Visualizar nombre del boton 'Buscar' </br>
</br></br>""")

class test_search_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Placeholder Buscador')
    @allure.story(u'Comprobar nombre del buscador general')
    def test_buscardor(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busqueda")

        with allure.step(u'PASO 3 : Obteniendo nombre del buscador:'):
            input = Selenium.get_elements(self, "Input busqueda simple").get_attribute("placeholder")

        with allure.step(u'PASO 4 : Validando el nombre:'):
            Selenium.foto(self, "Input")
            self.assertIn("Buscar documento", input, "Error, el nombre a cambiado, no es el mismo")

    @allure.title(u'Botón BUSCAR')
    @allure.story(u'Comprobar nombre del boton Buscar')
    def test_boton(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busqueda")

        with allure.step(u'PASO 3 : Obteniendo nombre del boton:'):
            button = Selenium.get_elements(self, "Boton busqueda simple").text

        with allure.step(u'PASO 4 : Validando el nombre:'):
            Selenium.foto(self, "Button")
            self.assertIn("BUSCAR", button, "Error, el nombre a cambiado, no es el mismo")

    @allure.title(u'Mensaje largo de caracteres')
    @allure.story(u'Al ingresar un solo caracter, deberia de aparecer un mensaje indicandome el minimo de caracteres')
    def test_caracteres_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busqueda")

        with allure.step(u'PASO 3 : Obteniendo nombre del boton:'):
            Selenium.foto(self, "Ingresando a la biblioteca")
            Selenium.get_elements(self, "Input busqueda simple").send_keys("H")

        with allure.step(u'PASO 4 : Validando el mensaje:'):
            Selenium.foto(self, "Busqueda")
            Selenium.check_exists_by_xpath(self, "//span[contains(text(), 'Minimo 3 caracteres')]")
            assert True, "No se encuentra el mensaje "

    @allure.title(u'Mensaje largo de caracteres')
    @allure.story(u'Al ingresar dos caracteres, deberia de aparecer un mensaje indicandome el minimo de caracteres')
    def test_caracteres_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busqueda")

        with allure.step(u'PASO 3 : Obteniendo nombre del boton:'):
            Selenium.foto(self, "Ingresando a la biblioteca")
            Selenium.get_elements(self, "Input busqueda simple").send_keys("He")

        with allure.step(u'PASO 4 : Validando el mensaje:'):
            Selenium.foto(self, "Busqueda")
            Selenium.check_exists_by_xpath(self, "//span[contains(text(), 'Minimo 3 caracteres')]")
            assert True, "No se encuentra el mensaje "

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
