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
campos anteriormente asignados. Validaciones aobre el modal de edición. </br>
</br></br>""")

class test_directory_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.name_directory = "test_create" + Selenium.generate_id(length=2)

    @allure.title(u'Crear nuevo directorio')
    @allure.story(u'Crear directorio y validar que los datos ingresados sean iguales en el modal de editar.')
    def test_create_002(self):
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

        with allure.step(u'PASO 5: Obteniendo nombres y validando directorio creado'):
            Selenium.check_element(self, "Crear nuevo directorio")
            time.sleep(3)
            directorios = self.driver.find_elements_by_xpath("//tbody/tr/th[1]")
            for nombre in directorios:
                if nombre.text == self.name_directory:
                    break
            Selenium.foto(self, f"Creacion del directorio {self.name_directory}")
            self.assertIn(self.name_directory, nombre.text, f"No se encontro el directorio {self.name_directory} creado")
            consulta = Selenium.pyodbc_query(self, f"SELECT name FROM company_folder WHERE name='{nombre.text}'")
            self.assertIn(nombre.text, consulta,f"Error, el directorio {nombre.text} no se encuentra en la base de datos")

            directorios = len(self.driver.find_elements_by_xpath("//tbody/tr/th[1]"))
            for tr in range(directorios):
                tr += 1
                if self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text == self.name_directory:
                    self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[1]").click()

                    Selenium.foto(self, "Editar")
                    assert Selenium.check_element(self, "dialogo"), "ERROR, NO SE ABRIÓ EL MODAL PARA EDITAR DIRECTORIO"

                    assert Selenium.get_elements(self, "nombre").get_attribute("value") == self.name_directory

                    assert Selenium.get_elements(self, "heredar permisos").is_selected(), \
                        "ERROR, ESTE CHECKBOX DEBERIA DE ESTAR MARCADO POR DEFECTO"

                    value_group = Selenium.get_elements(self, "input grupo").get_attribute("value")
                    assert value_group == "", "ERROR, NO SE ASIGNO NINGUN GRUPO A ESTE DIRECTORIO, SIN EMBARGO EXISTE" \
                                              f"UN GRUPO ASIGNADO, Y ESTE ES : '{value_group}'"

                    buttons = ['cancelar', 'guardar']
                    for button in buttons:
                        assert Selenium.check_element(self, button), \
                            f"ERROR, NO EXISTE EL ELEMENTO DEL BOTÓN {button}, EN EL MODAL DE EDITAR."

                    for button in buttons:
                        assert Selenium.get_elements(self, button).is_enabled(), \
                            f"ERROR, EL BOTÓN {button}, EN EL MODAL DE EDITAR ESTÁ DESHABILITADO."
                    break

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))