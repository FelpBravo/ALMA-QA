# -*- coding: utf-8 -*-
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Buscador general')
@allure.testcase(u'Busqueda simple', u'https://api-ux.atlassian.net/browse/ALMA-271')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Estado de los botones</br>
Estado de los elementos en general</br>
</br></br>""")

class test_search_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Boton BUSCAR.')
    @allure.story(u'Visibilidad del boton BUSCAR.')
    def test_visibilidad_boton(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busqueda")
        with allure.step(u'PASO 3 : Validar visibilidad del boton'):
            Selenium.foto(self, "Boton 'Buscar'")
            boton = Selenium.check_visibility_element_located(self, "Boton busqueda simple")
            self.assertTrue(boton, "Error, el boton no es visible")

    @allure.title(u'Boton BUSCAR.')
    @allure.story(u'Comprobar validacion del boton BUSCAR')
    def test_click_boton(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busqueda")

        with allure.step(u'PASO 3 : Validar estado del boton'):
            Selenium.foto(self, "Boton 'Buscar'")
            boton = Selenium.get_elements(self, "Boton busqueda simple").is_enabled()
            self.assertFalse(boton, "Error, el boton es clickable")

        with allure.step(u'PASO 4 : Validar estado del boton luego de llenar el input'):
            Selenium.foto(self, "Boton 'Buscar'")
            Selenium.get_elements(self, "Input busqueda simple").send_keys("TEST SEARCH GENERAL")
            boton = Selenium.check_click_element(self, "Boton busqueda simple")
            self.assertTrue(boton, "Error, el boton no es clickable")

    @allure.title(u'Input Buscar.')
    @allure.story(u'Visibilidad del input buscar ')
    def test_visibilidad_input(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busqueda")

        with allure.step(u'PASO 3 : Visibilidad del input'):
            Selenium.foto(self, "Input'")
            input = Selenium.check_visibility_element_located(self, "Input busqueda simple")
            self.assertTrue(input, "Error, el campo no se visualiza")

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
