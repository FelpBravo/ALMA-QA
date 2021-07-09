# -*- coding: utf-8 -*-
import unittest
import time
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Prueba de la busqueda simple de documentos 002')
@allure.testcase(u'Busqueda simple', u'enlace')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere validar la busqueda simple avanzada: </br>
Validar Botones</br>
visibilidad input</br>
Visibilidad de la grilla al buscar</br>
</br></br>""")

class test_documents_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.story(u'Estado del boton buscar.')
    def test_boton_buscar(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busquedaAvanzada")
            Selenium.esperar_elemento(self, "Boton busqueda avanzada")
            Selenium.get_elements(self, "Boton busqueda avanzada").click()

        with allure.step(u'PASO 3 : Validar visibilidad del boton'):
            Selenium.foto(self, "Boton 'Buscar'")
            boton = Selenium.check_visibility_element_located(self, "Boton buscar busqueda avanzada")
            self.assertTrue(boton, "Error, el boton no es visible")

        with allure.step(u'PASO 4 : Comprobar boton clickable'):
            boton = Selenium.check_click_element(self, "Boton buscar busqueda avanzada")
            self.assertTrue(boton, "Error, el boton no es clickable")

    @allure.story(u'Estado del boton Limpiar.')
    def test_boton_limpiar(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busquedaAvanzada")
            Selenium.check_element(self, "Boton busqueda avanzada")
            Selenium.get_elements(self, "Boton busqueda avanzada").click()

        with allure.step(u'PASO 3 : Validar visibilidad del limpiar'):
            Selenium.foto(self, "Boton 'limpiar'")
            boton = Selenium.check_visibility_element_located(self, "Boton limpiar busqueda avanzada")
            self.assertTrue(boton, "Error, el boton no es visible")

        with allure.step(u'PASO 4 : Comprobar boton clickable'):
            boton = Selenium.check_click_element(self, "Boton limpiar busqueda avanzada")
            self.assertTrue(boton, "Error, el boton no es clickable")

    @allure.story(u'Estado de los elementos y visibilidad al limpiar.')
    def test_funcionalidad_limpiar(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busquedaAvanzada")
            Selenium.esperar_elemento(self, "Boton busqueda avanzada")
            Selenium.get_elements(self, "Boton busqueda avanzada").click()

        with allure.step(u'PASO 3 : Validar visibilidad de los div al limpiar'):
            Selenium.get_elements(self, "Boton limpiar busqueda avanzada").click()
            Selenium.foto(self, "Boton 'limpiar'")
            divAtributo = Selenium.get_elements(self, "DIV Buscar por atributo").is_displayed()
            divFecha = Selenium.get_elements(self, "DIV Buscar por rangos de fecha").is_displayed()
            divEtiqueta = Selenium.get_elements(self, "DIV Buscar por etiquetas").is_displayed()

            self.assertTrue(divAtributo, "Error, el div de buscar por atributos fue borrado por completo")
            self.assertTrue(divFecha, "Error, el div de Buscar por rangos de fecha fue borrado por completo")
            self.assertTrue(divEtiqueta, "Error, el div de Buscar por etiquetas fue borrado por completo")

    @allure.story(u'Estado del boton busqueda avanzada.')
    def test_boton_bAvanzada(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busquedaAvanzada")

        with allure.step(u'PASO 3 : Comprobar estado'):
            Selenium.foto(self, "Boton 'Busqueda avanzada'")
            busquedaVis = Selenium.check_visibility_element_located(self, "Boton busqueda avanzada")
            busquedaClick = Selenium.check_click_element(self, "Boton busqueda avanzada")
            self.assertTrue(busquedaVis, "Error, el boton de busqueda avanzada no es visible")
            self.assertTrue(busquedaClick, "Error, el boton de busqueda avanzada no es clickable")

    @allure.story(u'Funcionalidad del boton busqueda avanzada.')
    def test_visualizar_elementos(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busquedaAvanzada")

        with allure.step(u'PASO 3 : Funcionalidad boton busqueda avanzada'):
            Selenium.esperar_elemento(self, "Boton busqueda avanzada")
            Selenium.get_elements(self, "Boton busqueda avanzada").click()

            Selenium.foto(self, "Mostrar divs 'Busqueda avanzada'")
            divAtributo = Selenium.get_elements(self, "DIV Buscar por atributo").is_displayed()
            divFecha = Selenium.get_elements(self, "DIV Buscar por rangos de fecha").is_displayed()
            divEtiqueta = Selenium.get_elements(self, "DIV Buscar por etiquetas").is_displayed()
            divBoton = Selenium.get_elements(self, "DIV botones").is_displayed()

        with allure.step(u'PASO 4 : Comprobando visibilidad de los Divs'):
            self.assertTrue(divAtributo, "Error, el div de buscar por atributos no fue desplegado")
            self.assertTrue(divFecha, "Error, el div de Buscar por rangos de fecha no fue desplegado")
            self.assertTrue(divEtiqueta, "Error, el div de Buscar por etiquetas no fue desplegado")
            self.assertTrue(divBoton, "Error, el div de botones no fue desplegado")

    @allure.story(u'Visualizar mensaje de error al buscar con campos vacios.')
    def test_campos_vacios(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "busquedaAvanzada")
            Selenium.esperar_elemento(self, "Boton busqueda avanzada")
            Selenium.get_elements(self, "Boton busqueda avanzada").click()

        with allure.step(u'PASO 3 : Click en buscar con campos vacios'):
            Selenium.get_elements(self, "Boton buscar busqueda avanzada").click()

        with allure.step(u'PASO 4 : Validar visibilidad del mensaje de error'):
            Selenium.foto(self, "Mensaje 'Error'")
            msjError = Selenium.get_elements(self, "Msj error").is_displayed()
            self.assertTrue(msjError, "Error, el mensaje de error no fue mostrados con los campos vacios.")

def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
