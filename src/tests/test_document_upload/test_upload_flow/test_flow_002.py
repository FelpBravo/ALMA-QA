# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'[Flujo carga Doc] Encabezado')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
localizar y visualizar encabezado'</br>
Titulo</br>
</br></br>""")

class test_flow_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Localizar encabezado')
    @allure.story(u'Localizar y visualizar los elementos del encabezado (Carga de documentos y Solicitud de Revisión y Aprobación)')
    def test_header(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Localizando encabezado'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            check = Selenium.check_element(self, "nuevos elementos")
            assert check == True, "No se localiza el encabezado"
            self.driver.execute_script('arguments[0].scrollIntoView(true);',Selenium.get_elements(self, "nuevos elementos"))
            Selenium.foto(self, "Encabezado")

        with allure.step(u'PASO 5 : Visualizar encabezado'):
            visibility = Selenium.check_visibility_element_located(self, "nuevos elementos")
            assert visibility == True, "No se visualiza el encabezado"
            self.driver.execute_script('arguments[0].scrollIntoView(true);', Selenium.get_elements(self, "nuevos elementos"))
            Selenium.foto(self, "Encabezado")

    @allure.title(u'Validar titulo')
    @allure.story(u'Localizar y validar nombre del titulo  (Solicitud de revisión y aprobación) ')
    def test_title(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Localizando titulo'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            check = Selenium.check_element(self, "titulo")
            assert check, "No se localiza el titulo 'Solicitud de revisión y aprobación'"
            self.driver.execute_script('arguments[0].scrollIntoView(true);',
                                       Selenium.get_elements(self, "titulo"))
            Selenium.foto(self, "Encabezado")

        with allure.step(u'PASO 5 : Comprobar nombre del titulo'):
            titulo = Selenium.get_elements(self, "nuevos elementos").text
            self.assertIn("Carga de documentos\n2\nSolicitud de Revisión y Aprobación", titulo, "El titulo no es igual al esperado")
            Selenium.foto(self, "Encabezado")

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))