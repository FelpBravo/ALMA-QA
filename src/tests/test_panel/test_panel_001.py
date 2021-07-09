# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Comentarios en los documentos')
@allure.testcase(u'Cambio de tamaño de la ventana', u'https://api-ux.atlassian.net/browse/ALMA-263')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Ajustar ventana en un costado a mitad de la pantalla y probar elementos del panel</br>
Maximar ventana y probar elementos del panel</br>
</br></br>""")

class test_panel_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Test Boton del Panel, ventana pequeña.')
    @allure.story(u'Iniciar sesion en ventana pequeña y luego visualizar el boton del panel de inicio.')
    def test_windows_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            self.driver.set_window_position(950, 30)
            self.driver.set_window_size(800, 1000)
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Obteniendo boton del panel '):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Boton panel")
            Selenium.foto(self, "Panel")

        with allure.step(u'PASO 4 : Validando visualizacion del boton del panel'):
            visible = Selenium.check_visibility_element_located(self, "Boton panel")
            Selenium.foto(self, "boton del Panel")
            assert visible == True, "No se visualiza el boton del panel de incio"

    @allure.title(u'Test Boton del Panel, ventana pequeña.')
    @allure.story(u'Iniciar sesion en ventana pequeña y luego visualizar el boton del panel de inicio.')
    def test_windows_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            self.driver.set_window_position(950, 30)
            self.driver.set_window_size(800, 1000)
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Obteniendo boton del panel '):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Boton panel")
            Selenium.foto(self, "Panel")

        with allure.step(u'PASO 4 : Validando visualizacion del boton del panel'):
            visible = Selenium.check_visibility_element_located(self, "Boton panel")
            Selenium.foto(self, "boton del Panel")
            assert visible == True, "No se visualiza el boton del panel de incio"

    @allure.title(u'Test click boton del Panel, ventana pequeña.')
    @allure.story(u'Al clickear el boton del panel se deberian de visualizar los elementos de este.')
    def test_windows_002(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            self.driver.set_window_position(950, 30)
            self.driver.set_window_size(800, 1000)
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Obteniendo y clickando boton del panel '):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Boton panel")
            Selenium.foto(self, "Panel")
            Selenium.get_elements(self, "Boton panel").click()

        with allure.step(u'PASO 4 : Validando visualizacion y localizacion de los elementos del panel'):
            localizacion = Selenium.check_element(self, "Panel principal")
            visible = Selenium.check_visibility_element_located(self, "Panel principal")
            Selenium.foto(self, "Elementos del panel")
            assert localizacion == True, "No se encuentran los elementos del panel de incio"
            assert visible == True, "No se visualizan los elementos del panel de incio"

    @allure.title(u'Test maximizar ventana y mostrar elementos del panel.')
    @allure.story(u'Ventana pequeña y luego maximizarla, validar que se visualizan los elementos del panel.')
    def test_windows_003(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            self.driver.set_window_position(950, 30)
            self.driver.set_window_size(800, 1000)
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Obteniendo y clickando boton del panel '):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Boton panel")
            Selenium.foto(self, "Panel")

        with allure.step(u'PASO 4 : Maximizar ventana '):
            self.driver.maximize_window()
            Selenium.foto(self, "Ventana maximizada")

        with allure.step(u'PASO 5 : Validando visualizacion y localizacion de los elementos del panel'):
            localizacion = Selenium.check_element(self, "Panel principal maximizado")
            visible = Selenium.check_visibility_element_located(self, "Panel principal maximizado")
            Selenium.foto(self, "Elementos del panel")
            assert localizacion == True, "No se encuentran los elementos del panel de incio"
            assert visible == True, "No se visualizan los elementos del panel de incio"

    @allure.title(u'Test ventana maximizada a pequeña y validar visualizacion boton del panel.')
    @allure.story(u'Empequeñeser la ventana para validar la visualizacion del boton del panel.')
    def test_windows_004(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Obteniendo y clickando boton del panel '):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Panel principal maximizado")
            Selenium.foto(self, "Panel")

        with allure.step(u'PASO 4 : Empequeñeser ventana'):
            self.driver.set_window_position(950, 30)
            self.driver.set_window_size(800, 1000)
            Selenium.foto(self, "Ventana")

        with allure.step(u'PASO 5 : Validando visualizacion del boton del panel'):
            localizacion = Selenium.check_element(self, "Boton panel")
            visible = Selenium.check_visibility_element_located(self, "Boton panel")
            Selenium.foto(self, "Elementos del panel")
            assert localizacion == True, "No se encuentran el boton del panel de incio"
            assert visible == True, "No se visualizan el boton del panel de incio"

    @allure.title(u'Test ventana maximizada a pequeña y validar funcionalidad del panel.')
    @allure.story(u'Empequeñeser la ventana para validar la funcionalidad del boton del panel.')
    def test_windows_005(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Obteniendo y clickando boton del panel '):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Panel principal maximizado")
            Selenium.foto(self, "Panel")

        with allure.step(u'PASO 4 : Empequeñeser ventana'):
            self.driver.set_window_position(950, 30)
            self.driver.set_window_size(800, 1000)
            Selenium.foto(self, "Ventana")

        with allure.step(u'PASO 5 : clickan el boton del panel'):
            Selenium.check_element(self, "Boton panel")
            Selenium.get_elements(self, "Boton panel").click()

        with allure.step(u'PASO 6 : Validando elementos del panel'):
            localizacion = Selenium.check_element(self, "Panel principal")
            visible = Selenium.check_visibility_element_located(self, "Panel principal")
            Selenium.foto(self, "Elementos del panel")
            assert localizacion == True, "No se encuentran los elementos del panel de incio"
            assert visible == True, "No se visualizan los elementos del panel de incio"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))