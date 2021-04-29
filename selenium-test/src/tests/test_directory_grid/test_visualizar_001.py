# -*- coding: utf-8 -*-
import unittest
from datetime import time
import time
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Pruebas de vizualizar un documento')
@allure.testcase(u'Historia de usuario vizualizar documento subido', u'Jira')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere validar la información general del documento: </br>
Validación:</br>
Ingresar a la vizualización del documento</br>
Nombre del documento visualizado vs Nombre del documento en la grilla</br>
Permitir visualizar la metadata del documento</br>
Titulo metadata</br>
</br></br>""")

class test_visualizar_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.story(u'Test visualizar documentos.')
    def test_visualizar_documento(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "directorios_grilla")
        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.get_elements(self, "Primera carpeta").click()
            elementoVi = Selenium.check_click_element(self, "Visualizar primer documento")
        with allure.step(u'PASO 4 : Validando visualizacion como elemento clickable'):
            if elementoVi == True:
                Selenium.get_elements(self, "Visualizar primer documento").click()
                Selenium.captura(self, "Visualizando primer documento seleccionado")
                Selenium.captura_pantalla(self)
            with allure.step(u'PASO 5 : Validando invisibilidad de cualquier mensaje de error'):
                self.assertTrue(Selenium.check_invisibility_element_located(self, "Msj Error"), "Ocurrio un error al visualizar el documento")
            if elementoVi == False:
                Selenium.get_elements(self, "Segunda carpeta").click()
                Selenium.get_elements(self, "Visualizar primer documento").click()
                Selenium.captura(self, "Visualizando primer documento seleccionado")
                Selenium.captura_pantalla(self)
            with allure.step(u'PASO 5 : Validando invisibilidad de cualquier mensaje de error'):
                self.assertTrue(Selenium.check_invisibility_element_located(self, "Msj Error"),"Ocurrio un error al visualizar el documento")

    @allure.story(u'Test Cargar la metadata del documento en la visualización.')
    def test_metadata_documento(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "directorios_grilla")
        with allure.step(u'PASO 3 : Ingresando a la visualización del documento'):
            Selenium.vizualizar_documento(self)
            visibilidad = Selenium.check_visibility_element_located(self, "Campo metadata documento")
        with allure.step(u'PASO 4 : Validando visibilidad de la metadata del documento'):
            Selenium.foto(self, "Metadata del documento")
            self.assertTrue(visibilidad, "ERROR, no se visualiza el campo de metadata")
            textMeta = Selenium.get_text(self, "Campo metadata documento")
        with allure.step(u'PASO 5 : Validando visibilidad del campo AlmaID'):
            self.assertIn("ALMA Doc Number", textMeta, "No se visualiza la metadata")

    @allure.story(u'Test Coincidir nombres de documento.')
    def test_visualizar_nom_doc(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "directorios_grilla")
        with allure.step(u'PASO 3 : Ingresando a la visualización del documento'):
            Selenium.vizualizar_documento(self)
        with allure.step(u'PASO 4 : Nombre de la grilla vs Nombre del documento en la metadata'):
            Selenium.foto(self, "Visualizando nombre del documento")
            textNom = Selenium.get_text(self, "Todo el campo visualizar")
            Selenium.foto(self, "Nombre del documento visualizado")
            Selenium.get_elements(self, "Todo el campo nombre carpeta en metadata").click()
            Selenium.foto(self, "Nombre del documento en la grilla")
            textNomGrilla = Selenium.get_text(self, "Nombre primer documento")
            self.assertIn(textNomGrilla, textNom, "ERROR, el nombre del documento no coincide con el de la previsualización")

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
