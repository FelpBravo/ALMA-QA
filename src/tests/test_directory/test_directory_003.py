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
@allure.description(u"""Crear un directorio y comprobar que al editarlo, se visualizen de manera correcta los
campos anteriormente asignados.</br>
</br></br>""")

class test_directory_003(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.name_directory = "test_create" + Selenium.generate_id(length=2)
            self.re_name_directory = "test_create" + Selenium.generate_id(length=2)

    @allure.title(u'Editar un directorio')
    @allure.story(u'Editar un directorio y validar que los datos ingresados se guarden tanto en la grilla como en la BD.')
    def test_edit_001(self):
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
            Selenium.get_elements(self, "guardar").click()

        with allure.step(u'PASO 4: Obteniendo nombres y validando directorio creado'):
            Selenium.check_element(self, "Crear nuevo directorio")
            time.sleep(3)
            directorios = self.driver.find_elements_by_xpath("//tbody/tr/th[1]")
            for nombre in directorios:
                if nombre.text == self.name_directory:
                    break
            Selenium.foto(self, f"Creacion del directorio {self.name_directory}")
            self.assertIn(self.name_directory, nombre.text, f"No se encontro el directorio {self.name_directory} creado")
            consulta = Selenium.pyodbc_query(self, f"SELECT name FROM company_folder WHERE name='{nombre.text}'")
            self.assertIn(nombre.text, consulta, f"Error, el directorio {nombre.text} no se encuentra en la base de datos")

            directorios = len(self.driver.find_elements_by_xpath("//tbody/tr/th[1]"))
            for tr in range(directorios):
                tr += 1
                if self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text == self.name_directory:
                    self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[1]").click()
                    Selenium.foto(self, "Editar")
                    break
            Selenium.check_element(self, "dialogo")
            self.driver.execute_script(f"arguments[0].value=''", Selenium.get_elements(self, "nombre"))
            Selenium.get_elements(self, "nombre").send_keys(self.re_name_directory)
            Selenium.foto(self, "Editar")
            Selenium.get_elements(self, "guardar").click()

            directorios = self.driver.find_elements_by_xpath("//tbody/tr/th[1]")
            for nombre in directorios:
                if nombre.text == self.re_name_directory:
                    break
            Selenium.foto(self, f"Creacion del directorio {self.re_name_directory}")
            self.assertIn(self.re_name_directory, nombre.text,
                          f"ERROR, EN LA GRILLA, NO SE ENCONTRO EL DIRECTORIO '{self.re_name_directory}' "
                          f"ANTERIORMENTE EDITADO.")

            consulta = Selenium.pyodbc_query_list(self, f"SELECT name FROM company_folder WHERE name= '{self.re_name_directory}'")
            for con in consulta:
                self.assertIn(self.re_name_directory, con.name,
                              f"ERROR, EL DIRECTORIO '{self.re_name_directory}' ANTERIORMENTE EDITADO, NO SE ENCUENTRA"
                              f"EN LA BASE DE DATOS.")

            self.driver.execute_script('arguments[0].scrollIntoView(true);',
                                       self.driver.find_element_by_xpath(f"//p[contains(text(),'{self.re_name_directory}')]"))
            assert Selenium.check_exists_by_xpath(self, f"//p[contains(text(),'{self.re_name_directory}')]"), \
                f"ERROR, EN EL ARBOL DE DIRECTORIOS NO SE VISUALIZA EL DIRECTORIO '{self.re_name_directory}' " \
                f"ANTERIORMENTE CREADO"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))