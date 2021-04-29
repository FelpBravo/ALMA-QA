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
    def test_estado_boton_buscar(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "busquedaAvanzada")
            Selenium.get_elements(self, "Boton busqueda avanzada").click()

        with allure.step(u'PASO 3 : Validar visibilidad del boton'):
            Selenium.foto(self, "Boton 'Buscar'")
            boton = Selenium.check_visibility_element_located(self, "Boton buscar busqueda avanzada")
            self.assertTrue(boton, "Error, el boton no es visible")

        with allure.step(u'PASO 4 : Comprobar boton clickable'):
            boton = Selenium.check_click_element(self, "Boton buscar busqueda avanzada")
            self.assertTrue(boton, "Error, el boton no es clickable")

    @allure.story(u'Estado del boton Limpiar.')
    def test_estado_boton_limpiar(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "busquedaAvanzada")
            Selenium.get_elements(self, "Boton busqueda avanzada").click()

        with allure.step(u'PASO 3 : Validar visibilidad del limpiar'):
            Selenium.foto(self, "Boton 'limpiar'")
            boton = Selenium.check_visibility_element_located(self, "Boton limpiar busqueda avanzada")
            self.assertTrue(boton, "Error, el boton no es visible")

        with allure.step(u'PASO 4 : Comprobar boton clickable'):
            boton = Selenium.check_click_element(self, "Boton limpiar busqueda avanzada")
            self.assertTrue(boton, "Error, el boton no es clickable")

    @allure.story(u'Estado de los elementos y visibilidad al limpiar.')
    def test_estado_funcionalidad_limpiar_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "busquedaAvanzada")
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

    @allure.story(u'Funcionalidad del boton limpiar.')
    def test_estado_funcionalidad_limpiar_002(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "busquedaAvanzada")
            Selenium.get_elements(self, "Boton busqueda avanzada").click()

        with allure.step(u'PASO 3 : Validar visibilidad de los div al limpiar'):
            Selenium.check_click_element(self, "Boton limpiar busqueda avanzada")
            Selenium.foto(self, "Boton 'limpiar'")
            divAtributo = Selenium.get_elements(self, "DIV Buscar por atributo").is_displayed()
            divFecha = Selenium.get_elements(self, "DIV Buscar por rangos de fecha").is_displayed()
            divEtiqueta = Selenium.get_elements(self, "DIV Buscar por etiquetas").is_displayed()

            self.assertTrue(divAtributo, "Error, el div de buscar por atributos fue borrado por completo")
            self.assertTrue(divFecha, "Error, el div de Buscar por rangos de fecha fue borrado por completo")
            self.assertTrue(divEtiqueta, "Error, el div de Buscar por etiquetas fue borrado por completo")

    @allure.story(u'Estado del boton busqueda avanzada.')
    def test_estado_boton_busquedaAvanzada(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "busquedaAvanzada")

        with allure.step(u'PASO 3 : Comprobar estado'):
            Selenium.foto(self, "Boton 'Busqueda avanzada'")
            busquedaVis = Selenium.check_visibility_element_located(self, "Boton busqueda avanzada")
            busquedaClick = Selenium.check_click_element(self, "Boton busqueda avanzada")
            self.assertTrue(busquedaVis, "Error, el boton de busqueda avanzada no es visible")
            self.assertTrue(busquedaClick, "Error, el boton de busqueda avanzada no es clickable")

    @allure.story(u'Funcionalidad del boton busqueda avanzada.')
    def test_funcionalidad_busquedaAvanzada(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "busquedaAvanzada")

        with allure.step(u'PASO 3 : Funcionalidad boton busqueda avanzada'):
            Selenium.esperar_elemento(self, "Boton busqueda avanzada")
            Selenium.get_elements(self, "Boton busqueda avanzada").click()

            Selenium.foto(self, "Mostrar divs 'Busqueda avanzada'")
            divAtributo = Selenium.get_elements(self, "DIV Buscar por atributo").is_displayed()
            divFecha = Selenium.get_elements(self, "DIV Buscar por rangos de fecha").is_displayed()
            divEtiqueta = Selenium.get_elements(self, "DIV Buscar por etiquetas").is_displayed()
            divBoton = Selenium.get_elements(self, "DIV botones").is_displayed()

        with allure.step(u'PASO 3 : Comprobando visibilidad de los Divs'):
            self.assertTrue(divAtributo, "Error, el div de buscar por atributos no fue desplegado")
            self.assertTrue(divFecha, "Error, el div de Buscar por rangos de fecha no fue desplegado")
            self.assertTrue(divEtiqueta, "Error, el div de Buscar por etiquetas no fue desplegado")
            self.assertTrue(divBoton, "Error, el div de botones no fue desplegado")

def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
