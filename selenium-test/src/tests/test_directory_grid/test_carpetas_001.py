# -*- coding: utf-8 -*-
import unittest
from datetime import time
import time
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Pruebas de navegar entre carpetas')
@allure.testcase(u'Historia de usuario moverse entre carpetas', u'jira')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere validar el ingresar en una carpeta: </br>
Validación:</br>
Ingresar a a una carpeta</br>
Invisibilidad de todo mensaje de error</br>
Carpeta clickable</br>
</br></br>""")

class test_carpetas_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.story(u'Test. Entrar en las carpetas.')
    def test_entrar_en_carpeta(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "directorios_grilla")
        with allure.step(u'PASO 3 : Clickear primera carpeta'):
            Selenium.get_elements(self, "Primera carpeta").click()
            Selenium.get_json_file(self, "documents")
            error = Selenium.check_invisibility_element_located(self, "Error documento repetido")
        with allure.step(u'PASO 4 : Validando el camino feliz'):
            Selenium.captura(self, "Primera carpeta 'Grilla de la carpeta'")
            Selenium.captura_pantalla(self)
            self.assertTrue(error, "A habido un error al ingresar a la primera carpeta")

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
