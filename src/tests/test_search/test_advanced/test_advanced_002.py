# -*- coding: utf-8 -*-
import random
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Busqueda avanzada')
@allure.testcase(u'Busqueda avanzada')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Visibilidad de los titulos de las areas de busqueda 'Busqueda avanzada'</br>
Funcionalidad de los botones'</br>
visibilidad de los campos despues de clickar botones'</br>
</br></br>""")

class test_advanced_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Titulo.')
    @allure.story(u'Validando el nombre del titulo (Buscar por atributo).')
    def test_title_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Buscando el titulo (Buscar por atributo)'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Titutos")

            Selenium.check_exists_by_xpath(self, "//h4[contains(text(), 'Buscar por atributo')]")
            assert True, "No se encuentra el titulo 'Buscar por atributo' en el buscador avanzado"

    @allure.title(u'Titulo.')
    @allure.story(u'Validando el nombre del titulo (Buscar por rangos de fechas).')
    def test_title_002(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Buscando el titulo (Buscar por rangos de fechas)'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Titutos")

            Selenium.check_exists_by_xpath(self, "//h4[contains(text(), 'Buscar por rangos de fechas')]")
            assert True, "No se encuentra el titulo 'Buscar por rangos de fechas' en el buscador avanzado"

    @allure.title(u'Boton Limpiar.')
    @allure.story(u'Validando estado del boton.')
    def test_button_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando si el boton es clickable y no esta bloqueado'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Boton")

            Selenium.check_click_element(self, "limpiar")
            assert True, "El boton 'limpiar' no es clickable"

            Selenium.get_elements(self, "limpiar").is_enabled()
            assert True, "El boton 'limpiar' esta bloqueado"

    @allure.title(u'Boton Buscar.')
    @allure.story(u'Validando estado del boton.')
    def test_button_002(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando si el boton es clickable y no esta bloqueado'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Boton")

            Selenium.check_click_element(self, "buscar")
            assert True, "El boton 'Buscar' no es clickable"

            Selenium.get_elements(self, "buscar").is_enabled()
            assert True, "El boton 'Buscar' esta bloqueado"

    @allure.title(u'Boton Limpiar.')
    @allure.story(u'Comprobando que al precionar sobre el boton limpiar, no se elimine ningun campo.')
    def test_button_003(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando funcionalidad del boton'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Boton")

            Selenium.get_elements(self, "limpiar").click()

            Selenium.foto(self, "Boton limpiar")
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

    @allure.title(u'Boton Limpiar.')
    @allure.story(u'Comprobando que al precionar 100 veces sobre el boton limpiar, no se elimine ningun campo.')
    def test_button_004(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando funcionalidad del boton'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Boton")

            for click in range(99):
                Selenium.get_elements(self, "limpiar").click()

            Selenium.foto(self, "Boton limpiar")
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

    @allure.title(u'Boton Buscar.')
    @allure.story(u'Comprobando que al presionar sobre el boton Buscar, aparesca el mensaje.')
    def test_button_005(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando si el boton es clickable y no esta bloqueado'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Boton")

            Selenium.get_elements(self, "buscar").click()
            Selenium.foto(self, "Boton buscar")

            Selenium.check_exists_by_xpath(self, "//div[contains(text(), 'Debe seleccionar un filtro')]")
            assert True, "No se encuentra el mensaje 'Debe seleccionar un filtro'"

    @allure.title(u'Boton Buscar.')
    @allure.story(u'Comprobando que al presionar sobre el boton Buscar, no desaparesca ningun campo.')
    def test_button_006(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando si el boton es clickable y no esta bloqueado'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Boton")

            Selenium.foto(self, "Boton buscar")
            self.metadata = ["etiquetas", "nombre documento", "autor", "security mode",
                             "version", "alma doc number", "peso del archivo", "modificado en", "modificado hasta",
                             "creado en", "creado hasta", "limpiar", "buscar"]
            for m in range(20):
                Selenium.get_elements(self, "buscar").click()
                if m == 0:
                    Selenium.foto(self, "Boton buscar")
                bOk = Selenium.check_exists_by_xpath(self, "//button[contains(text(), 'OK')]")
                if bOk == False:
                    Selenium.foto(self, "Boton Ok")
                    assert bOk == True, "ERROR, EL MODAL DE ERROR NO APARECE AL PULSA EL BOTON BUSCAR CON CAMPOS VACIOS"
                self.driver.find_element_by_xpath("//button[contains(text(), 'OK')]").click()
                item = random.choice(self.metadata)

                check = Selenium.check_element(self, item)
                if check == False:
                    Selenium.foto(self, f"El campo {item}")
                assert check == True, f"Error, El campo {item} en conjunto con otros elementos de la metadata no se encuentran."

                Selenium.check_visibility_element_located(self, item)
                assert True, f"Error, El campo {item} en conjunto con otros elementos de la metadata no son visibles."

    @allure.title(u'Campos.')
    @allure.story(u'Vista habitual al entrar en el buscador avanzado, siempre los campos deberian estar así.')
    def test_input(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando funcionalidad del boton'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Boton")

            Selenium.foto(self, "Boton limpiar")
            self.metadata = ["etiquetas", "nombre documento", "autor", "security mode",
                             "version", "alma doc number", "peso del archivo", "modificado en", "modificado hasta",
                             "creado en", "creado hasta", "limpiar", "buscar"]
            for m in range(13):
                item = random.choice(self.metadata)
                if m == 0:
                    Selenium.foto(self, "campos")
                Selenium.check_element(self, item)
                value = Selenium.get_elements(self, item).get_attribute("value")
                assert value == "", f"El campo {item} tiene valores asignados"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
