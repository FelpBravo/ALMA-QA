# -*- coding: utf-8 -*-
import random
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Descargar')
@allure.testcase(u'Comprobar la descarga de un conjunto de documentos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Funcionalidad del botón 'OK', al descargar</br>
Descargar documentos de la grilla, y comprobar su correcta descarga</br>
</br></br>""")
class test_download_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.story(u'Boton descargar.')
    @allure.story(u'Encontrar el boton de DESCARGAR en todos los documentos de la grilla.')
    def test_download(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Visualizar el boton de DESCARGA en todos los documentos de la grilla'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                if x == 6:
                    break
                tr = random.randint(x, len(element))
                docu_name = self.driver.find_element_by_xpath(f"//tbody/tr[{tr}]/td[1]").text
                self.driver.find_element_by_xpath(f"//tbody/tr[{tr}]/td[8]/div[1]/div[2]").click()

                Selenium.get_json_file(self, "download")
                Selenium.esperar_elemento(self, "OK")
                assert True, "No se encontro el boton OK"

                Selenium.get_elements(self, "OK").click()
                download = Selenium.descargar_documento(self, docu_name)
                if download == False:
                    Selenium.foto(self, "No se descago")
                    assert download == True, f"El documento {docu_name} no se ha podido descargar"

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
