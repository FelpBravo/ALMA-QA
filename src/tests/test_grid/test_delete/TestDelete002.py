# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner


@allure.feature(u'Eliminar')
@allure.testcase(u'Comprobar la eliminación de un conjunto de documentos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Comprobar la eliminación del documento</br>
No encontrar el nombre del documento en la grilla, una vez eliminado</br>
Verificar que la grilla, disminuya la cantidad de documentos al eliminar uno</br>
</br></br>""")
class TestDelete002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Borrar documento.')
    @allure.story(u'Borrar todos los documentos de una grilla')
    def test_delete(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Borrar documentos de la grilla'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                if x < 4:
                    if x < len(self.driver.find_elements_by_xpath("//tbody/tr")):
                        Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(x)}]/td[8]/div[1]/*[5]")
                        self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/*[5]").click()
                        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(
                            "//body/div[2]/div[3]/ul[1]/li[2]/span[1]"))
                        if x == 1:
                            Selenium.foto(self, "Botón de eliminar")
                        Selenium.get_json_file(self, "delete")
                        Selenium.esperar_elemento(self, "OK")
                        Selenium.get_elements(self, "OK").click()
                        time.sleep(3)
                        largo = len(self.driver.find_elements_by_xpath("//tbody/tr"))  # Esta es la grilla
                        assert largo == len(element) - x, "ERROR, Al parecer aun hay documentos en la grilla"
                    else:
                        break
                else:
                    break

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
