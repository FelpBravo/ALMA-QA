# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'[Flujo carga Doc] Funcionalidad de botones (Basurero)')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Localizar'</br>
Visualizar</br>
Funcionalidad</br>
Estado</br>
</br></br>""")

class test_flow_004(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Localizar y visualizar botones (Basurero)')
    @allure.story(u'Localizar, visualizar botones de borrar agregados a raiz del (Agregar)')
    def test_button_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Localizando botones'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            self.driver.execute_script('arguments[0].scrollIntoView(true);', Selenium.get_elements(self, f"button 1"))
            times = 9
            suma = []
            a = 0
            result = 0
            for b in range(6):
                b += 1
                for click in range(times):
                    Selenium.get_elements(self, f"button " + str(b)).click()
                    self.driver.execute_script('arguments[0].scrollIntoView(true);', Selenium.get_elements(self, f"button " + str(b)))
                for basurero in range(len(self.driver.find_elements_by_xpath("//button[@aria-label='delete']"))):
                    basurero
                Selenium.foto(self, "espacios creados")
                suma.append(times)
                result = result + suma[a]
                if b == 6:
                    result += 1
                assert basurero == result, f"ERROR, LA CANTIDAD DE ESPACIOS CREADOS FUERON {result} MAS EL QUE ESTABA POR DEFECTO, " \
                                          f"LA CANTIDAD DE ICONOS DE BASUREROS VISUALIZADOS EN TOTAL ES DE {basurero}"
                a += 1

    @allure.title(u'Funcionalidad y botones (Basurero)')
    @allure.story(u'Funcionalidad y de botones de borrar agregados a raiz del (Agregar)')
    def test_button_002(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Probando botones'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            self.driver.execute_script('arguments[0].scrollIntoView(true);', Selenium.get_elements(self, f"button 1"))
            Selenium.get_elements(self, f"button 1").click()
            Selenium.foto(self, "Botones basurero")
            Selenium.get_elements(self, "basurero 2").click()
            check1 = Selenium.check_element(self, "basurero 1")
            check2 = Selenium.check_element(self, "basurero 2")
            Selenium.foto(self, "Botones basurero")
            assert (check1 and check2) == False, "Al parecer aun se visualizan los basureros en la pagina"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))