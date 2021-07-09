# -*- coding: utf-8 -*-
import random
import time
import unittest
import allure
import pytest
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Busqueda avanzada')
@allure.testcase(u'Busqueda avanzada')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validando que la paginación funcione de acorde a lo esperado y que los documentos encontrados no se repitan.</br></br></br>""")

class test_advanced_004(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Paginación.')
    @allure.story(u'Comprobando una busqueda por Versionamiento, validando la paginacion en la grilla de resultados.')
    def test_pag(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a la busqueda avanzada'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            versiones = ['1']
            for v in range(len(versiones)):
                Selenium.esperar_elemento(self, "busqueda avanzada")
                Selenium.get_elements(self, "busqueda avanzada").click()
                Selenium.foto(self, "Boton")
                Selenium.get_elements(self, "version").send_keys(versiones[v])
                Selenium.foto(self, "foto de lo ingresado")
                Selenium.get_elements(self, "buscar").click()

                time.sleep(1)
                check = Selenium.check_element(self, "nextPage")
                if not check:
                    Selenium.foto(self, "Boton paginación")
                    assert check, "ERROR, EL BOTON DE PAGINACION NO EXISTE."

                if not Selenium.get_elements(self, "nextPage").is_enabled():
                    Selenium.foto(self, "Versiones")
                    pytest.skip("NO SE PUEDE HACER LA PRUEBA, LA CANTIDAD MINIMA DE DOCUMENTOS ES DE 11")

                Selenium.get_json_file(self, "users")
                check = Selenium.check_element(self, "nextPage")
                assert check == True, "Error, no existe el elemento para redireccionar a la siguiente pagina"
                documents = []
                next = False
                while not next:
                    if Selenium.check_exists_by_xpath(self, "//tbody/tr"):
                        Selenium.foto(self, "Documentos en la grilla")
                        i = 0
                        for x in range(len(self.driver.find_elements_by_xpath("//tbody/tr"))):
                            x += 1
                            nombreDoc = self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[1]").text

                            if x > 1:
                                self.assertNotIn(nombreDoc, documents[i], f"ERROR, EL DOCUMENTO {nombreDoc} se encuentra repetido")
                                i += 1
                            documents.append(nombreDoc)

                            check = Selenium.check_exists_by_xpath(self, "//span[@class='user-description mt-2 mr-2']")
                            if not check:
                                Selenium.foto(self, "Paginación")
                                assert check, "ERROR NO SE ENCUENTRA EL CONTADOR DE PAGINAS"
                    if Selenium.get_elements(self, "nextPage").is_enabled():
                        Selenium.get_elements(self, "nextPage").click()
                        next = False
                    else:
                        next = True
                numPag = self.driver.find_element_by_xpath("//span[@class='user-description mt-2 mr-2']").text
                esperado = "Total documentos encontrados " + str(len(documents))

                Selenium.foto(self, "Paginacion")
                self.assertEqual(esperado, numPag,"ERROR, NO CONCUERDA EL NUMERO DE DOCUMENTOS ENCONTRADOS VS LOS DOCUMENTOS CONTADOS POR SELENIUM " + str(len(documents)))




    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
