# -*- coding: utf-8 -*-
import random
import unittest
from datetime import time
import time
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src.functions.initialize import Inicializar

@allure.feature(u'Pruebas Directorios')
@allure.testcase(u'Pruebas de integración')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Asignar permisos APP_MANAGER a una carpeta, comprobar que esta carpeta no sea vista  por
usuarios de un grupo distinto. Usuario del grupo correspondiente pueda ver la carpeta y clikar en ella.</br>
</br></br>""")

class test_directory_011(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.new_directory = "test_permissions_5y2H7"+str(random.randint(1,99))
            self.pwd = "Alma2021"

    @allure.title(u'APP_MANAGER')
    @allure.story(u'Validar la funcionalidad de los permisos en carpetas.')
    def test_permission(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

            consulta = Selenium.pyodbc_query_list(self, "SELECT name FROM company_group")
            groups = []
            for con in consulta:
                if not con.name == "EVERYONE":
                    groups.append(con.name)

            group = "APP_MANAGER" #random.choice(groups)
            dependency = Selenium.split(self, group, "_")

            consult_user = Selenium.pyodbc_query_list(self, "SELECT user_id FROM company_user WHERE first_name='QA'")
            #users = []
            #for con in consult_user:
                #users.append(con.user_id)

        with allure.step(u'PASO 3 : Ingresar en directorios'):
            Selenium.get_elements(self, "Menu administracion").click()
            Selenium.get_elements(self, "Menu directorios").click()
            Selenium.check_element(self, "Crear nuevo directorio")
            Selenium.get_elements(self, "Crear nuevo directorio").click()
            Selenium.get_elements(self, "nombre").send_keys(self.new_directory)
            Selenium.get_elements(self, "tipo espacio trabajo").click()
            time.sleep(0.5)  # OBLIGATORIO
            Selenium.get_elements(self, "workspace").click()
            Selenium.get_elements(self, "seleccionar grupo").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath(f"//li[@data-value='{group}']/span[1]/span[1]/input[1]").click()
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            Selenium.foto(self, "Datos del directorio")
            Selenium.get_elements(self, "guardar").click()
            time.sleep(1.5)

            Selenium.get_json_file(self, "bienvenidaSesion")
            Selenium.esperar_elemento(self, "Boton opciones Perfil")
            Selenium.get_elements(self, "Boton opciones Perfil").click()
            Selenium.get_elements(self, "Boton cerrar sesion").click()

            Selenium.swith_to_windows_name(self, "admin")
            print(groups)

            for v in range(len(groups)):
                Selenium.new_window(self, Inicializar.URL)
                Selenium.swith_to_windows_name(self, groups[v])

            users = ['qawriter', 'qaviewer', 'qamanager', 'QAfinanzasmanager', 'qastandard', 'QAfinanzastandard',
                     'QAfinanzaswriter', 'QAfinanzasviewer', 'qasuperadmin']
            for pos in range(len(groups)):
                Selenium.swith_to_windows_name(self, groups[pos])
                Selenium.get_json_file(self, "signin")
                Selenium.get_elements(self, "Usuario").send_keys(users[pos])
                Selenium.send_key_text(self, "Password", self.pwd)
                Selenium.get_elements(self, "Boton acceder").click()
                print(f"Ventana abierta: {groups[pos]} \n Usuario asignado: {users[pos]}")

            amount = 0
            while not amount == len(groups):
                for current_pos in range(len(groups)):
                    Selenium.swith_to_windows_name(self, groups[current_pos])
                    exist = Selenium.check_exists_by_xpath(self, f"//p[text()[contains(.,'{self.new_directory}')]]",
                                                           time=1)
                    if exist:
                        break
                    else:
                        continue
                    amount += 1
                assert exist, "" \
                              f"ERROR, LA CARPETA {self.new_directory} ESTA EN EL GRUPO {groups[current_pos]} Y ESTE NO " \
                              f"TIENE PERMISOS."

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))