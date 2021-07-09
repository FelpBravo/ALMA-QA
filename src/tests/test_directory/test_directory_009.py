# -*- coding: utf-8 -*-
import random
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@allure.feature(u'Pruebas Directorios')
@allure.testcase(u'Pruebas de integración')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Crear un directorio, editarlo cambiando algo en sus grupos y luego crear un segundo directorio
esperando no tener ningun problema y que este se cree dentro de la grilla principal.</br></br>""")
class test_directory_009(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.name_directory = "test_create" + Selenium.generate_id(length=2)
            self.name_directory_two = "test_create" + Selenium.generate_id(length=2)

    @allure.title(u'Crear/Editar/Crear un directorio')
    @allure.story(u'Crear y Editar un directorio, para luego crear otro directorio simultaneamente')
    def test_edit_006(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Ingresar en directorios'):
            Selenium.get_elements(self, "Menu administracion").click()
            Selenium.get_elements(self, "Menu directorios").click()

        with allure.step(u'PASO 4: Creando un directorio'):
            Selenium.check_element(self, "Crear nuevo directorio")
            time.sleep(0.5) #OBLIGATORIO
            Selenium.get_elements(self, "Crear nuevo directorio").click()
            Selenium.get_elements(self, "tipo espacio trabajo").click()
            Selenium.get_elements(self, "workspace").click()
            Selenium.get_elements(self, "nombre").send_keys(self.name_directory)
            Selenium.foto(self, "Crear nuevo directorio")
            Selenium.get_elements(self, "guardar").click()
            time.sleep(1)  # OBLIGATORIO

        with allure.step(u'PASO 5: Validando campo input en la edición'):
            consulta = Selenium.pyodbc_query_list(self, "SELECT name FROM company_group")
            groups = []
            for con in consulta:
                if not con.name == "EVERYONE":
                    groups.append(con.name)
            group = random.choice(groups)

            directories = []
            for tr in range(len(self.driver.find_elements_by_xpath("//tbody/tr/th[1]"))):
                tr += 1
                directories.append(self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text)

            for tr in range(len(self.driver.find_elements_by_xpath("//tbody/tr/th[1]"))):
                tr += 1
                if self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text == self.name_directory:
                    self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[1]").click()
                    Selenium.foto(self, "Editar")
                    break

            Selenium.check_element(self, "seleccionar grupo")
            Selenium.get_elements(self, "seleccionar grupo").click()
            time.sleep(0.5) #Obligatorio
            self.driver.find_element_by_xpath(f"//li[@data-value='{group}']/span[1]/span[1]/input[1]").click()
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            Selenium.foto(self, "Editar")
            Selenium.get_elements(self, "guardar").click()

            Selenium.check_element(self, "Crear nuevo directorio")
            time.sleep(1) #Obligatorio
            Selenium.get_elements(self, "Crear nuevo directorio").click()
            Selenium.get_elements(self, "tipo espacio trabajo").click()
            Selenium.get_elements(self, "workspace").click()
            Selenium.get_elements(self, "nombre").send_keys(self.name_directory_two)
            directories.append(self.name_directory_two)
            Selenium.foto(self, "Crear nuevo directorio")
            Selenium.get_elements(self, "guardar").click()
            time.sleep(1)  # Obligatorio
            Selenium.foto(self, "GRILLA ACTUAL")
            current_directories = []
            for tr in range(len(self.driver.find_elements_by_xpath("//tbody/tr/th[1]"))):
                tr += 1
                current_directories.append(self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text)

            print(directories, current_directories)
            for dir in range(len(directories)):
                self.assertIn(directories[dir], current_directories, "ERROR, ALGO SUCEDIO DESPUES DE LA CREACIÓN "
                                                                     "DEL ULTIMO DIRECTORIO. \n"
                                                                     f"GRILLA ESPERADA: {directories} \n"
                                                                     f"GRILLA ACTUAL: {current_directories}")

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))