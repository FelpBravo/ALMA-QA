# -*- coding: utf-8 -*-
import unittest
from datetime import time
import time
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Prueba de la busqueda simple de documentos 002')
@allure.testcase(u'Busqueda simple', u'enlace')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere validar la busqueda simple: </br>
Validar Botones</br>
Visibilidad de los elementos</br>
Visibilidad de la grilla al buscar</br>
</br></br>""")

class test_documents_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.story(u'Visibilidad del boton BUSCAR.')
    def test_visibilidad_boton(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "busqueda")
        with allure.step(u'PASO 3 : Validar visibilidad del boton'):
            Selenium.foto(self, "Boton 'Buscar'")
            boton = Selenium.check_visibility_element_located(self, "Boton busqueda simple")
            self.assertTrue(boton, "Error, el boton no es visible")

    @allure.story(u'Validar click en boton BUSCAR')
    def test_click_boton(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "busqueda")

        with allure.step(u'PASO 3 : Validar estado del boton'):
            Selenium.foto(self, "Boton 'Buscar'")
            boton = Selenium.get_elements(self, "Boton busqueda simple").is_enabled()
            self.assertFalse(boton, "Error, el boton es clickable")

        with allure.step(u'PASO 4 : Validar estado del boton luego de llenar el input'):
            Selenium.foto(self, "Boton 'Buscar'")
            Selenium.get_elements(self, "Input busqueda simple").send_keys("TEST_001")
            boton = Selenium.check_click_element(self, "Boton busqueda simple")
            self.assertTrue(boton, "Error, el boton no es clickable")

    @allure.story(u'Visibilidad del campo Buscar por nombre de documentp ')
    def test_visibilidad_input(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "busqueda")

        with allure.step(u'PASO 3 : Visibilidad del input'):
            Selenium.foto(self, "Input'")
            input = Selenium.check_visibility_element_located(self, "Input busqueda simple")
            self.assertTrue(self, input, "Error, el campo no se visualiza")

    @allure.story(u'Al ingresar alguna busqueda y mostrar grilla')
    def test_mostrar_grilla(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "busqueda")

        with allure.step(u'PASO 3 : Escribir en input y luego buscar:'):
            Selenium.get_elements(self, "Input busqueda simple").send_keys("TEST_001")
            Selenium.get_elements(self, "Boton busqueda simple").click()

        with allure.step(u'PASO 4 : Visualizando grilla:'):
            Selenium.foto(self, "Grilla")
            grilla = Selenium.check_visibility_element_located(self, "Grilla")
            self.assertTrue(grilla, "Error")

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
