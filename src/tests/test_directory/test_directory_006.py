# -*- coding: utf-8 -*-
import random
import unittest
from datetime import time
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Pruebas Directorios')
@allure.testcase(u'Pruebas de integración')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Crear un directorio y editarlo con cualquier grupo. Validar que al abrir de nuevo
el modal de edición, estas modificaciones persistan.</br>
</br></br>""")

class test_directory_006(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.name_directory = "test_create" + Selenium.generate_id(length=2)
            self.re_name_directory = "test_edit" + Selenium.generate_id(length=2)

    @allure.title(u'Editar un directorio')
    @allure.story(
        u'Editar un directorio y validar que los datos ingresados se guarden tanto en la grilla como en la BD.')
    def test_edit_004(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Ingresar en directorios'):
            Selenium.get_elements(self, "Menu administracion").click()
            Selenium.get_elements(self, "Menu directorios").click()

        with allure.step(u'PASO 4: Creando un directorio'):
            Selenium.check_element(self, "Crear nuevo directorio")
            Selenium.get_elements(self, "Crear nuevo directorio").click()
            Selenium.get_elements(self, "nombre").send_keys(self.name_directory)
            Selenium.get_elements(self, "tipo espacio trabajo").click()
            Selenium.get_elements(self, "workspace").click()
            Selenium.foto(self, "Guardar dir")
            Selenium.get_elements(self, "guardar").click()

        with allure.step(u'PASO 4: Obteniendo nombres y validando directorio creado'):
            Selenium.check_element(self, "Crear nuevo directorio")
            time.sleep(3)

            directorios = len(self.driver.find_elements_by_xpath("//tbody/tr/th[1]"))
            for tr in range(directorios):
                tr += 1
                if self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text == self.name_directory:
                    self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[1]").click()
                    Selenium.foto(self, "Editar")
                    break
            Selenium.check_element(self, "dialogo")

            consulta = Selenium.pyodbc_query_list(self, "SELECT name FROM company_group")
            groups = []
            for con in consulta:
                if not con.name == "EVERYONE":
                    groups.append(con.name)

            group = random.choice(groups)
            dependency = Selenium.split(self, group, "_")

            any = 3
            if any == 1:
                self.driver.execute_script(f"arguments[0].value=''", Selenium.get_elements(self, "nombre"))
                Selenium.get_elements(self, "nombre").send_keys(self.re_name_directory)

            if any == 2:
                Selenium.get_elements(self, "heredar permisos").click()

            if any == 3:
                Selenium.get_elements(self, "seleccionar grupo").click()
                time.sleep(0.5)
                self.driver.find_element_by_xpath(f"//li[@data-value='{group}']/span[1]/span[1]/input[1]").click()
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

            Selenium.foto(self, "Editar")
            Selenium.get_elements(self, "guardar").click()

            Selenium.get_elements(self, "Menu directorios").click()
            Selenium.check_exists_by_xpath(self, "//tbody/tr/th[1]")

            if not any == 1:
                current_name = self.name_directory
            else:
                current_name = self.re_name_directory

            Selenium.check_exists_by_xpath(self, "//tbody/tr[2]")
            directorios = len(self.driver.find_elements_by_xpath("//tbody/tr/th[1]"))
            for tr in range(directorios):
                tr += 1
                name = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text
                if name == current_name:
                    self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[1]").click()
                    break
            Selenium.foto(self, f"Edición del directorio {current_name}")
            print(f"Nombre antes: '{self.name_directory}' \n  Nombre ahora: '{current_name}'")

            if any == 1:
                assert Selenium.get_elements(self, "nombre").get_attribute("value") == self.re_name_directory, \
                    f"ERROR, SE EDITÓ EL DIRECTORIO '{name}' "

            if any == 2:
                current = Selenium.get_elements(self, "heredar permisos").is_selected()
                assert current, f"ERROR, EL CHECKBOX NO ESTA EN 'TRUE', COMO SE DEJÓ EDITADO" \
                                            f" ANTERIORMENTE."

            if any == 3:
                current = Selenium.get_elements(self, "input grupo").get_attribute("value")
                expected = f"{dependency[0]}_MANAGER,{group}"

                current_group = Selenium.split(self, current, ",")
                expected_group = Selenium.split(self, expected, ",")

                for i in range(len(expected_group)):
                    self.assertIn(expected_group[i], current_group, "ERROR, ANTERIORMENTE SE EDITO EL DIRECTORIO, Y SE LE ASIGNO " \
                                                            f"EL GRUPO , EL CUAL SE COMPRUEBA QUE NO PERSISTE EN" \
                                                            f" LA EDICIÓN, GRUPO ESPERADO: '{expected_group}'" \
                                                            f" GRUPO OBTENIDO: '{current_group}'")

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))