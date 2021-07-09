# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.utils.Users.CreateUser import CreateUser
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Usuarios y grupos')
@allure.testcase(u'Largo de los campos en los modales crear y editar')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validar que el largo de los modales sea el mismo de siempre. </br></br>""")

class test_users_003(Selenium, CreateUser, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Modal CREAR USUARIO.')
    @allure.story(u'Validar el comportamiento y estado del botón al ingresar valores invalidos.')
    def test_mod_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

            Selenium.get_json_file(self, "users")
            notData = ['','']
            elements = len(self.driver.find_elements_by_xpath("//tbody/tr"))
            for e in range(elements):
                e += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(e)}]/td[4]")
            Selenium.check_element(self, "Modal crear editar")

            elements = ['nombres', 'apellidos', 'email', 'empresa', 'departamento', 'usuario']
            data = ['Á', 'É', 'felipee.smith@gmail.com', 'Í', 'Ó', 'U']

            for x in range(2):
                for i in range(len(elements)):
                    if i < 2:
                        Selenium.get_elements(self, elements[i]).clear()
                        for caracter in range(50 + x):
                            Selenium.get_elements(self, elements[i]).send_keys(data[i])
                        if x == 0:
                            assert Selenium.get_elements(self, elements[i]).get_attribute("aria-invalid") == "false"
                        if x == 1:
                            assert Selenium.get_elements(self, elements[i]).get_attribute("aria-invalid") == "true"

                    if i == 2 and x == 0:
                        Selenium.get_elements(self, elements[i]).send_keys(data[i])

                    if i == 3:
                        Selenium.get_elements(self, elements[i]).send_keys("Other")
                        Selenium.get_elements(self, elements[i] + "Other").clear()
                        for caracter in range(50 + x):
                            Selenium.get_elements(self, elements[i] + "Other").send_keys(data[i])
                        if x == 0:
                            assert Selenium.get_elements(self, elements[i] + "Other").get_attribute("aria-invalid") == "false"
                        if x == 1:
                            assert Selenium.get_elements(self, elements[i] + "Other").get_attribute("aria-invalid") == "true"

                    if i == 4:
                        Selenium.get_elements(self, elements[i]).send_keys("Other")
                        Selenium.get_elements(self, elements[i] + "Other").clear()
                        for caracter in range(50 + x):
                            Selenium.get_elements(self, elements[i] + "Other").send_keys(data[i])
                        if x == 0:
                            assert Selenium.get_elements(self, elements[i] + "Other").get_attribute("aria-invalid") == "false"
                        if x == 1:
                            assert Selenium.get_elements(self, elements[i] + "Other").get_attribute("aria-invalid") == "true"

                    if i == 5:
                        Selenium.get_elements(self, elements[i]).clear()
                        for caracter in range(100 + x):
                            Selenium.get_elements(self, elements[i]).send_keys(data[i])
                        if x == 0:
                            assert Selenium.get_elements(self, elements[i]).get_attribute("aria-invalid") == "false"
                        if x == 1:
                            assert Selenium.get_elements(self, elements[i]).get_attribute("aria-invalid") == "true"
                if x == 0:
                    if not Selenium.get_elements(self, "crear").is_enabled():
                        Selenium.foto(self, "usuario existente")
                        assert Selenium.get_elements(self, "crear").is_enabled(), f"ERROR, EL BOTÓN CREAR ESTA HABILITADO CON EL USUARIO  Y ESTE ES EXISTENTE"

            Selenium.get_elements(self, "cancelar").click()

            Selenium.check_click_element(self, "crear usuario")
            Selenium.get_elements(self, "crear usuario").click()

            CreateUser.modal(self)

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))