# -*- coding: utf-8 -*-
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Buscador general')
@allure.testcase(u'Busqueda simple', u'https://api-ux.atlassian.net/browse/ALMA-271')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Ingresar una busqueda </br>
Visualizar grilla</br>
</br></br>""")

class test_search_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Funcionalidad.')
    @allure.story(u'Permitir ingresar una busqueda')
    def test_mostrar_grilla(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busqueda")

        with allure.step(u'PASO 3 : Escribir en input y luego buscar:'):
            Selenium.get_elements(self, "Input busqueda simple").send_keys("TEST_001")
            Selenium.get_elements(self, "Boton busqueda simple").click()

        with allure.step(u'PASO 4 : Visualizando grilla:'):
            check = Selenium.check_element(self, "Grilla")
            visibilidad = Selenium.check_visibility_element_located(self, "Grilla")
            Selenium.foto(self, "Grilla")
            assert True == check, "Error no se encuentra el elemento de la grilla"
            assert True == visibilidad, "Error no se visualiza el elemento de la grilla"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
