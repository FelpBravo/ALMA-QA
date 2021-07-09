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
@allure.description(u"""Crear sub-directorios y validar sus diferentes elementos</br>
</br></br>""")

class test_directory_010(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Crear sub-directorio')
    @allure.story(u'Crear sub-directorio dentro de otro y validar elementos.')
    def test_sub_dir(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Ingresar en directorios'):
            Selenium.get_elements(self, "Menu administracion").click()
            Selenium.get_elements(self, "Menu directorios").click()

            def return_create(kind):
                Selenium.check_element(self, "Crear nuevo directorio")
                Selenium.get_elements(self, "Crear nuevo directorio").click()
                if kind == 0:
                    current_directory = "test_create" + Selenium.generate_id(length=2)
                if kind == 1:
                    current_directory = "test_create_sub" + Selenium.generate_id(length=2)
                Selenium.get_elements(self, "nombre").send_keys(current_directory)
                Selenium.get_elements(self, "tipo espacio trabajo").click()
                time.sleep(0.5) #OBLIGATORIO

                if kind == 0:
                    Selenium.get_elements(self, "workspace").click()

                if kind == 1:
                    options = self.driver.find_elements_by_xpath("//body/div[@id='menu-type']/div[3]/ul[1]/li")
                    options_data = ['forum', 'workspace']
                    n = 0
                    for option in options:
                        if not option.text == options_data[n]:
                            Selenium.foto(self, options_data[n])
                            assert option.text == options_data[n], f"ERROR NO EXISTE LA OPCION '{options_data[n]}'"
                        n += 1
                    Selenium.get_elements(self, "workspace").click()

                Selenium.get_elements(self, "guardar").click()
                time.sleep(0.5) #Obligatorio
                Selenium.foto(self, "Creación")
                print(f"DIRECTORIO CREADO: {current_directory}")
                return current_directory

            def enter_directory(directory):
                directories = len(self.driver.find_elements_by_xpath("//tbody/tr"))
                for tr in range(directories):
                    tr += 1
                    if Selenium.check_exists_by_xpath(self, f"//th[text()[contains(.,'{directory}')]]"):
                        self.driver.find_element_by_xpath(f"//th[text()[contains(.,'{directory}')]]").click()
                        break
                if not Selenium.check_exists_by_xpath(self, f"//th[text()[contains(.,'{directory}')]]"):
                    Selenium.foto(self, f"directorio {directory}")
                    assert Selenium.check_exists_by_xpath(f"//th[text()[contains(.,'{directory}')]]"), \
                            f"ERROR NO SE ENCUENTRA EL DIRECTORIO {directory} EN LA GRILLA"

            def name_directory_bd(directory):
                time.sleep(2)
                name_directory = Selenium.pyodbc_query_list(self, f"SELECT name FROM company_folder WHERE name='{directory}'")
                if not name_directory is None:
                    return True
                else:
                    return False

        with allure.step(u'PASO 4: Creando diferentes sub-directorios'):
            n = 1
            for i in range(6):
                if i == 0:
                    set_directory = return_create(kind = 0)
                    enter_directory(set_directory)
                    name = name_directory_bd(set_directory)
                    if not name:
                        assert name, f"ERROR NO SE CREO EL DIRECTORIO, '{name_directory_bd}' EN LA BASE DE DATOS"
                if i >= 1:
                    set_directory_new = return_create(kind= n)
                    if not len(self.driver.find_elements_by_xpath("//tbody/tr")) == 1:
                        assert len(self.driver.find_elements_by_xpath("//tbody/tr")) == 1, "ERROR, ALGO PASÓ, EXISTE " \
                        f"MAS DE UN SUB-DIRECTORIO CREADO CON EL DIRECTORIO {set_directory_new} ANTERIORMENTE CREADO."
                    if i < 6:
                        enter_directory(set_directory_new)
                    name2 = name_directory_bd(set_directory_new)
                    if not name2:
                        assert name2, f"ERROR NO SE CREO EL DIRECTORIO, '{set_directory_new}' EN LA BASE DE DATOS"
    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))