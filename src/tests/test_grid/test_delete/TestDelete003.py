# -*- coding: utf-8 -*-
import random
import time
import unittest
import allure
import pytest

from src.functions.functions import Functions as Selenium
import HtmlTestRunner


@allure.feature(u'Eliminar')
@allure.testcase(u'Comprobar la eliminación de un conjunto de documentos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Siempre que haya mas de una página, esta prueba sera ejecutada.
Se validará que al eliminar un documento de la grilla, esta no se disminuya, sino que el documento de la página 2
se sume a la grilla de la página 1.""")
class TestDelete003(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.grilla = "//tbody/tr" # Esta es la grilla

    @allure.title(u'Borrar documento.')
    @allure.story(u'Borrar documentos de una grilla y validar la paginación')
    def test_delete_003(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ejecutando las validaciones'):
            next = False
            amount = 0
            while not next:
                Selenium.comprobar_carpeta_con_archivos(self)
                Selenium.foto(self, "Documentos en la grilla")
                Selenium.get_json_file(self, "directorios_grilla")
                Selenium.check_element(self, "nextPage")
                if not Selenium.get_elements(self, "nextPage").is_enabled():
                    if amount == 3:
                        pytest.skip("NO HAY DIRECTORIOS CON MAS DE 10 DOCUMENTOS PARA EJECUTAR ESTA PRUEBA")
                    next = False
                else:
                    next = True

            for x in range(1):
                pos = random.randint(1, len(self.driver.find_elements_by_xpath(self.grilla)))
                print(pos)
                Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(pos)}]/td[8]/div[1]/*[5]")
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(pos)}]/td[8]/div[1]/*[5]").click()
                self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath("//body/div[2]/div[3]/ul[1]/li[2]/span[1]"))

                Selenium.foto(self, "Botón de eliminar")
                Selenium.get_json_file(self, "delete")
                Selenium.esperar_elemento(self, "OK")
                Selenium.get_elements(self, "OK").click()
                time.sleep(1.3)
                Selenium.foto(self, "Botón OK")
                long = len(self.driver.find_elements_by_xpath(self.grilla))  # Esta es la grilla
                assert long == 10, "ERROR, LA GRILLA NO SE ACTUALIZA, AL ELIMINAR UN DOCUMENTO LA GRILLA DEBERÍA DE " \
                                   "ACTUALIZARSE Y SIEMPRE DEBERIAN DE HABER 10 DOCUMENTOS, AHORA EL VALOR RESCATADO" \
                                   f" ES DE '{long}' DOCUMENTOS"

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
