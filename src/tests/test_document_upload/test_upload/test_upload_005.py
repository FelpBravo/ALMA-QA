# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'Campo, Seleccionar documentos', u'https://api-ux.atlassian.net/browse/ALMA-302')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Mensajes de error</br>
Funcionalidad</br>
Estado</br>
Cargar maxima de documentos</br>
Cargar minima de documentos cuando son controlados</br>
Comportamiento de un documento controlado</br>
Previsualizacion de documentos</br>
Validacion sobre elementos que se habilitan al marca 'controlado'</br>
</br></br>""")

class test_upload_005(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Botón SELECCIONAR DOCUMENTO.')
    @allure.story(u'Comprobando estado y localizacion del selector de documentos.')
    def test_upload_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Localizando el selector'):
            Selenium.foto(self, "selector de documento")
            check = Selenium.check_element(self, "Seleccionar documento")
            visibilidad = self.driver.find_element_by_xpath("//div[@class='drop-down']").is_enabled()

        with allure.step(u'PASO 5 : Validando'):
            self.assertTrue(check and visibilidad, "Error, no se localiza o visualiza el checkbox")

    @allure.title(u'Botón CARGAR.')
    @allure.story(u'Comprobando que el boton de carga sea clickable.')
    def test_upload_002(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Validando que el boton de carga sea clickable'):
            Selenium.foto(self, "boton de carga")
            click = Selenium.check_click_element(self, "boton de cargar doc")
            self.assertTrue(click, "Error, el boton de carga no es clickable")

    @allure.title(u'Miniatura del documento.')
    @allure.story(u'Comprobar que el documento se previsualiza cargado.')
    def test_upload_003(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar un documento'):
            Selenium.subida_unitaria(self)

        with allure.step(u'PASO 5 : Comprobar documento precargado'):
            Selenium.foto(self, "Documento precargado")
            assert Selenium.check_element(self, "Imagen doc cargado"), "ERROR, LA IMAGEN NO SE VISUALIZA EN LA MINIATURA"
            assert Selenium.check_visibility_element_located(self, "Imagen doc cargado"), "ERROR, LA IMAGEN NO SE VISUALIZA EN LA MINIATURA"

    @allure.title(u'Refrescar la pagina.')
    @allure.story(u'Comprobar que el documento cargado desaparesca al refrescar la pagina.')
    def test_upload_004(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionando documento y cargandolo'):
            Selenium.subida_unitaria(self)
            Selenium.check_visibility_element_located(self, "Imagen doc cargado")
            Selenium.foto(self, "antes Documento precargado")

        with allure.step(u'PASO 5 : Refrescando la pagina'):
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 6 : Validando la prueba'):
            visualizacion = Selenium.check_element(self, "Imagen doc cargado")
            Selenium.foto(self, "despues Documento precargado")
            assert visualizacion == False, "Error, sigue previsualizado, el campo no se limpio"

    @allure.title(u'Documento controlado.')
    @allure.story(u'Prueba de integracion: Documento controlado.')
    def test_upload_005(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionando documento y cargandolo'):
            Selenium.subida_masiva(self)
            Selenium.foto(self, "Documento no controlado")

        with allure.step(u'PASO 5 : Seleccionar documento controlado'):
            Selenium.get_elements(self, "documento controlado").click()

        with allure.step(u'PASO 6 : Validando la prueba'):
            Selenium.foto(self, "Despues Documento precargado")
            msj = self.driver.find_element_by_xpath("//div[@id='swal2-content']").text
            self.assertIn("Solo puedes seleccionar 1 archivo para documento controlado", msj, "Error, no se visualiza el mensaje")

    @allure.title(u'Area de carga.')
    @allure.story(u'Desaparecer area de carga al escoger un documento controlado.')
    def test_upload_006(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar un documento'):
            Selenium.check_element(self, "documento controlado")
            Selenium.subida_unitaria(self)
            Selenium.check_visibility_element_located(self, "Imagen doc cargado")
            Selenium.foto(self, "Documento subido")

        with allure.step(u'PASO 5 : Seleccionar documento controlado'):
            Selenium.get_elements(self, "documento controlado").click()
            Selenium.foto(self, "Documento no controlado")

        with allure.step(u'PASO 6 : Validando que el area de carga se esconda'):
            area = Selenium.check_invisibility_element_located(self, "boton de cargar doc")
            assert area == True, "El area de carga aun se visualiza"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))