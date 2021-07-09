# -*- coding: utf-8 -*-
import unittest
from datetime import time
import time
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Pruebas Directorios')
@allure.testcase(u'Pruebas de integración')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Borrar un directorio y validar el nombre de este. Validar que este directorio no persista
en la base de datos y tampoco persista en la grilla de directorios.</br>
</br></br>""")

class test_directory_remove(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'BORRAR DIRECTORIOS')
    @allure.story(
        u'Borrar todos los directorios creados tras las pruebas, validaciones con base de datos y la grilla.')
    def test_remove(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Ingresar en directorios'):
            Selenium.get_elements(self, "Menu administracion").click()
            Selenium.get_elements(self, "Menu directorios").click()

        with allure.step(u'PASO 4: Eliminar directorios directorio'):
            Selenium.check_exists_by_xpath(self, "//tbody/tr[2]")

        with allure.step(u'PASO 5: Validando'):
            time.sleep(1)
            Selenium.foto(self, "DOCUMENTOS DE LA GRILLA")
            True
            while True:
                for tr in range(len(self.driver.find_elements_by_xpath("//tbody/tr/th[1]"))):
                    tr += 1
                    previous_name = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text

                    if previous_name[0:4] == "test":
                        self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[2]").click()
                        Selenium.check_element(self, "Boton OK")
                        Selenium.get_elements(self, "Boton OK").click()
                        Selenium.foto(self, "ELIMINAR")
                        directory_bd = Selenium.pyodbc_query_list(self, f"SELECT name FROM company_group WHERE "
                                                                        f"name='{previous_name}'")

                        assert directory_bd is None, f"ERROR, EN LA BASE DE DATOS AUN PERSISTE EL DIRECTORIO " \
                                                     f"{previous_name} ANTERIORMENTE BORRADO."

                        time.sleep(0.5) #Obligatorio
                        for tr_two in range(len(self.driver.find_elements_by_xpath("//tbody/tr/th[1]"))):
                            tr_two += 1
                            current_name = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr_two)}]/th[1]").text
                            if current_name == previous_name:
                                assert not current_name == previous_name, f"EL DIRECTORIO {previous_name} NO SE BORRÓ" \
                                                                         f" DE LA GRILLA DE DIRECTORIOS"
                        break
                if previous_name[0:4] == "test":
                    True
                else:
                    False
                    break

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))