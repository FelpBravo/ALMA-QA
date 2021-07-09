# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'[Flujo carga Doc] Botones' , u'https://api-ux.atlassian.net/browse/ALMA-92')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Estado del botón 'SIGUIENTE'</br>
Funcionalidad del boton 'SIGUIENTE'</br>
Nombre del boton 'SIGUIENTE'</br>
</br></br>""")

class test_flow_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Test del boton SIGUIENTE, comprobando su existencia')
    @allure.story(u'Comprobar que el boton exista.')
    def test_button_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Comprobando que el boton exista'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            exite = Selenium.check_element(self, "Button Siguiente")
            Selenium.foto(self, "Boton siguiente")
            assert exite == True, "El boton siguiente no existe"

    @allure.title(u'Test del boton SIGUIENTE, comprobando su visibilidad')
    @allure.story(u'Comprobar que el boton sea visible.')
    def test_button_002(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Comprobando que el boton sea visible'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            visible = Selenium.check_visibility_element_located(self, "Button Siguiente")
            Selenium.foto(self, "Boton siguiente")
            assert visible == True, "El boton siguiente no es visible"

    @allure.title(u'Test del boton SIGUIENTE, comprobando su estado')
    @allure.story(u'Comprobar que el boton este bloqueado al ingresar.')
    def test_button_003(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Comprobando que el boton este bloqueado'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            Selenium.check_element(self, "Button Siguiente")
            time.sleep(1)
            Selenium.get_elements(self, "Button Siguiente").click()

            Selenium.foto(self, "Boton siguiente")
            assert Selenium.check_exists_by_xpath(self, "//p[contains(text(), 'Campo requerido')]"), "El boton " \
                                                                                                     "siguiente esta " \
                                                                                                     "habilitado"

    @allure.title(u'Test del boton SIGUIENTE, comprobando su nombre')
    @allure.story(u'Comprobar el nombre del boton. Comprobar que siempre sea el mismo')
    def test_button_004(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Comprobando que el nombre sea correcto'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            nombre = Selenium.get_elements(self, "Button Siguiente").text
            Selenium.foto(self, "Boton siguiente")
            assert nombre == "SIGUIENTE", "El nombre del boton a cambiado, no coincide"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))