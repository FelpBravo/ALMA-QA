# -*- coding: utf-8 -*-
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'Boton cargar/Siguiente' , u'https://api-ux.atlassian.net/browse/ALMA-302')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Funcionalidad</br>
Estado</br>
Ver si es clickable</br>
Comportamiento</br>
Validaciones</br>
Salir del flujo, interrumpir la carga y luego volver a cargar, comportamiento boton cargar</br>
</br></br>""")

class test_upload_006(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Boton cargar')
    @allure.story(u'Comprobando localizacion y visibilidad del boton cargar.')
    def test_button_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Localizando el boton'):
            Selenium.foto(self, "boton 'cargar'")
            check = Selenium.check_element(self, "Cargar")
            visibilidad = Selenium.check_visibility_element_located(self, "Cargar")

        with allure.step(u'PASO 5 : Validando'):
            self.assertTrue(check and visibilidad, "Error, no se localiza o visualiza el boton")

    @allure.title(u'Boton Cargar')
    @allure.story(u'Comprobando que el boton de carga este bloqueado al ingresar.')
    def test_button_002(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Validando que el boton Cargar permanesca bloqueado'):
            estado = Selenium.get_elements(self, "Cargar").is_enabled()
            Selenium.foto(self, "boton de carga")
            self.assertFalse(estado, "Error, el boton de carga esta habilitado")

    @allure.title(u'Boton cargar')
    @allure.story(u'Comprobando que el boton de carga sea clickable y visible.')
    def test_button_003(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Validando que el boton Cargar sea clickable'):
            visibilit = Selenium.check_visibility_element_located(self, "Cargar")
            Selenium.foto(self, "boton de carga")
            self.assertTrue(visibilit, "Error, el boton de carga no es clickable")

    @allure.title(u'Boton cargar')
    @allure.story(u'Comportamiento y estado boton Cargar.')
    def test_button_004(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar carpeta'):
            Selenium.get_elements(self, "Seleccionar carpeta").click()
            Selenium.selecionar_primera_carpeta(self)
            Selenium.foto(self, "Carpeta")

        with allure.step(u'PASO 5 : Seleccionar No ICD'):
            Selenium.get_elements(self, "Seleccionar ICD/NO").click()
            Selenium.get_elements(self, "Opcion NoICD").click()
            Selenium.foto(self, "No icd")

        with allure.step(u'PASO 6 : Cargar documento'):
            Selenium.subida_unitaria(self)
            Selenium.check_element(self, "Imagen doc cargado")
            Selenium.check_visibility_element_located(self, "Imagen doc cargado")
            target = Selenium.get_elements(self, "Cargar")
            self.driver.execute_script('arguments[0].scrollIntoView(true);', target)
            Selenium.foto(self, "documento")

        with allure.step(u'PASO 7 : Validar estado del boton Cargar'):
            assert Selenium.get_elements(self, "Cargar").is_enabled() == True, "El boton aun permanece bloqueado"

    @allure.title(u'Boton cargar')
    @allure.story(u'Prueba integracion 1: Interrumpir carga - refrecar - Comportamiento y estado boton Cargar.')
    def test_button_005(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Rellenando campos y cargando un documento'):
            Selenium.rellenar_habilitar_boton(self)

        with allure.step(u'PASO 5 : Refrescando la pagina'):
            Selenium.get_elements(self, "Carga documentos").click()
            target = Selenium.get_elements(self, "Cargar")
            self.driver.execute_script('arguments[0].scrollIntoView(true);', target)
            Selenium.foto(self, "Boton")

        with allure.step(u'PASO 6 : Validar estado del boton Cargar'):
            assert Selenium.get_elements(self, "Cargar").is_enabled() == False, "El boton aun permanece habilitado"

    @allure.title(u'Boton cargar')
    @allure.story(u'Prueba integracion 2: Interrumpir carga - refrecar - Comportamiento y estado boton Cargar.')
    def test_button_006(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Rellenando campos y cargando un documento'):
            Selenium.rellenar_habilitar_boton(self)

        with allure.step(u'PASO 5 : Refrescando la pagina'):
            Selenium.get_elements(self, "Carga documentos").click()
            target = Selenium.get_elements(self, "Cargar")
            self.driver.execute_script('arguments[0].scrollIntoView(true);', target)
            Selenium.foto(self, "Boton")

        with allure.step(u'PASO 6 : Rellenando campos'):
            Selenium.rellenar_habilitar_boton(self)

        with allure.step(u'PASO 7 : Validar estado del boton Cargar'):
            assert Selenium.get_elements(self, "Cargar").is_enabled() == True, "El boton permanece bloqueado"

    @allure.title(u'Boton cargar')
    @allure.story(u'Estado del boton al seleccionar Documento controlado.')
    def test_button_007(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar documento controlado'):
            Selenium.check_element(self, "documento controlado")
            Selenium.get_elements(self, "documento controlado").click()
            Selenium.foto(self, "Controlado")

        with allure.step(u'PASO 6 : Validando estado del boton'):
            target = Selenium.get_elements(self, "Cargar")
            self.driver.execute_script('arguments[0].scrollIntoView(true);', target)
            Selenium.foto(self, "Boton")
            assert Selenium.get_elements(self, "Cargar").is_enabled() == False, "El boton esta habilitado"

    @allure.title(u'Boton cargar')
    @allure.story(u'Nombre del boton al seleccionar Documento controlado.')
    def test_button_008(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar documento controlado'):
            Selenium.check_element(self, "documento controlado")
            while Selenium.get_elements(self, "documento controlado").is_selected() == False:
                Selenium.get_elements(self, "documento controlado").click()
            Selenium.foto(self, "Controlado")

        with allure.step(u'PASO 6 : Validando nombre del boton'):
            target = Selenium.get_elements(self, "Cargar")
            self.driver.execute_script('arguments[0].scrollIntoView(true);', target)
            Selenium.foto(self, "Boton")
            Selenium.check_visibility_element_located(self, "Cargar")
            assert Selenium.get_elements(self, "Cargar").text == "SIGUIENTE", "El nombre del boton no es correcto"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))