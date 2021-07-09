# -*- coding: utf-8 -*-
import random
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Compartir documentos- Acceso público')
@allure.suite(u'Probando si se ve como suite')
@allure.testcase(u'Comprobar estado y funcionalidad de botones.', u'https://api-ux.atlassian.net/browse/ALMA-272')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Estado y visibilidad del boton crear.</br>
Estado y visibilidad del boton aceptar.</br>
Funcionalidad del boton crear</br>
Funcionalidad del boton aceptar</br>
Carpeta clickable</br>
</br></br>""")

class test_share_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.dateUntil = Selenium.textDateEnvironmentReplace(self, "hoy")
            self.password = "1234"

    @allure.title(u'Boton Crear/Aceptar')
    @allure.story(u'Comprobar que el boton sea visible.')
    def test_button_001(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "compartir")

        with allure.step(u'PASO 3 : Ir a la primera carpeta'):
            Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 4 : Rellenando campos'):
            Selenium.flujo_compartir(self, random.randint(0, 1))

        with allure.step(u'PASO 5 : Rellenando campos'):
            Selenium.get_elements(self, "Boton crear").click()
            Selenium.esperar_elemento(self, "Enlace")

        with allure.step(u'PASO 6 : Validando visiblidad del boton'):
            check = Selenium.check_element(self, "Boton aceptar")
            visibili = Selenium.check_visibility_element_located(self, "Boton aceptar")
            assert (check and visibili) == True, "El boton no es visible"
            assert Selenium.check_element(self, "Boton crear") == False, "El boton crear es localizable"

    @allure.story(u'Comprobar funcionalidad del boton aceptar.')
    def test_button_002(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "compartir")

        with allure.step(u'PASO 3 : Ir a la primera carpeta'):
            Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 4 : Rellenando campos'):
            Selenium.flujo_compartir(self, random.randint(0, 1))

        with allure.step(u'PASO 5 : Rellenando campos'):
            Selenium.get_elements(self, "Boton crear").click()
            Selenium.esperar_elemento(self, "Enlace")
            Selenium.foto(self, "Enlace")

        with allure.step(u'PASO 6 : Pulsar el boton ACEPTAR'):
            Selenium.get_elements(self, "Boton aceptar").click()

        with allure.step(u'PASO 7 : Validando que se cierra el modal'):
            check = Selenium.check_invisibility_element_located(self, "Todo el campo compartir")
            Selenium.foto(self, "Cerrar modal")
            assert check == True, "El modal de compartir aun se encuentra en la pagina"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))