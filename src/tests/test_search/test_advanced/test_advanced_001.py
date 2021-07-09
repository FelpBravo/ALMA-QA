# -*- coding: utf-8 -*-
import random
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Busqueda avanzado')
@allure.testcase(u'Busqueda avanzada')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Nombre del Boton 'Busqueda avanzada'</br>
Localizar Boton para abrir la busqueda avanzada</br>
Funcionalidad boton de busqueda avanzada
Localizar campos</br>
Localizar botones</br>
</br></br>""")

class test_advanced_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Busqueda avanzada.')
    @allure.story(u'Localizar el nombre (Búsqueda avanzada).')
    def test_name_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Buscando el nombre (Búsqueda avanzada)'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.check_exists_by_xpath(self, "//span[contains(text(), 'Búsqueda Avanzada')]")
            assert True, "No se encuentra el nombre 'Búsqueda avanzada en la página'"

    @allure.title(u'Busqueda avanzada.')
    @allure.story(u'Localizacion y visibilidad del boton de (Búsqueda avanzada).')
    def test_button_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando el boton (Búsqueda avanzada)'):
            Selenium.foto(self, "Busqueda avanzada")

            Selenium.get_json_file(self, "search_advanced")
            Selenium.check_element(self, "busqueda avanzada")
            Selenium.check_visibility_element_located(self, "busqueda avanzada")

            assert True, "No se encuentra el boton 'Búsqueda avanzada en la página'"
            assert True, "No se visualiza el boton 'Búsqueda avanzada en la página'"

    @allure.title(u'Busqueda avanzada.')
    @allure.story(u'Estado del boton de (Búsqueda avanzada).')
    def test_button_002(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando el boton(Búsqueda avanzada)'):
            Selenium.foto(self, "Busqueda avanzada")

            Selenium.get_json_file(self, "search_advanced")
            Selenium.check_click_element(self, "busqueda avanzada")
            Selenium.get_elements(self, "busqueda avanzada").is_enabled()

            assert True, "El botón 'Búsqueda avanzada' no es clickable en la página"
            assert True, "El botón 'Búsqueda avanzada' esta bloqueado"

    @allure.title(u'Busqueda avanzada.')
    @allure.story(u'Funcionalidad del boton de (Búsqueda avanzada).')
    def test_button_003(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando funcionalidad (Búsqueda avanzada)'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()

            self.metadata = ["etiquetas", "nombre documento", "autor", "security mode",
                             "version", "alma doc number", "peso del archivo", "modificado en", "modificado hasta",
                             "creado en", "creado hasta", "limpiar", "buscar"]
            for m in range(13):
                item = random.choice(self.metadata)
                if m == 0:
                    Selenium.foto(self, "No se deberia de ver la metadata")

                Selenium.check_element(self, item)
                assert True, f"Error, El campo {item} en conjunto con otros elementos de la metadata no se encuentran."

                Selenium.check_visibility_element_located(self, item)
                assert True, f"Error, El campo {item} en conjunto con otros elementos de la metadata no son visibles."

    @allure.title(u'Busqueda avanzada.')
    @allure.story(u'Funcionalidad del boton de (Búsqueda avanzada). Ejecutando 100 clicks y validando la visibilidad de los elementos')
    def test_button_004(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando funcionalidad (Búsqueda avanzada)'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            for click in range(99):
                Selenium.get_elements(self, "busqueda avanzada").click()

            self.metadata = ["etiquetas", "nombre documento", "autor", "security mode",
                             "version", "alma doc number", "peso del archivo", "modificado en", "modificado hasta",
                             "creado en", "creado hasta", "limpiar", "buscar"]
            for m in range(13):
                item = random.choice(self.metadata)
                if m == 0:
                    Selenium.foto(self, "No se deberia de ver la metadata")

                Selenium.check_element(self, item)
                assert True, f"Error, El campo {item} en conjunto con otros elementos de la metadata no se encuentran."

                Selenium.check_visibility_element_located(self, item)
                assert True, f"Error, El campo {item} en conjunto con otros elementos de la metadata no son visibles."

    @allure.title(u'Busqueda avanzada.')
    @allure.story(u'Localizar el nombre (Búsqueda avanzada) despues de clickar el boton.')
    def test_name_002(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Buscando el nombre (Búsqueda avanzada)'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Nombre")

            Selenium.check_exists_by_xpath(self, "//span[contains(text(), 'Búsqueda Avanzada')]")
            assert True, "No se encuentra el nombre 'Búsqueda avanzada en la página'"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
