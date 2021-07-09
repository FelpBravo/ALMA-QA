# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.utils.Users.CreateUser import CreateUser
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Usuarios y grupos')
@allure.testcase(u'Crear un usuario existente')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validar que aparescan los mensajes de error al existir el usuario. </br></br>""")

class test_users_002(Selenium, CreateUser, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Crear usuario existente.')
    @allure.story(u'Validar mensajes de error al crear un usuario existente.')
    def test_users_exist(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

            Selenium.get_json_file(self, "users")

            time.sleep(1)

            user = self.driver.find_element_by_xpath(f"//tbody/tr[1]/td[1]").text
            print(f"Se ejecutara la prueba con el usuario '{user}' ")

            Selenium.get_elements(self, "crear usuario").click()
            Selenium.check_element(self, "Modal crear editar")

            elements = ['nombres', 'apellidos', 'email', 'empresa', 'departamento', 'usuario']
            data = ['Felipee', 'Smith', 'felipee.smith@gmail.com', 'A P I U X', 'Programacion QA']
            for i in range(len(elements)):
                if i < 3:
                    Selenium.get_elements(self, elements[i]).send_keys(data[i])

                if i == 3:
                    Selenium.get_elements(self, elements[i]).send_keys("Other")
                    Selenium.get_elements(self, "empresaOther").send_keys(data[i])

                if i == 4:
                    Selenium.get_elements(self, elements[i]).send_keys("Other")
                    Selenium.get_elements(self, "departamentoOther").send_keys(data[i])

                if i == 5:
                    Selenium.get_elements(self, "usuario").send_keys(user)

            message = Selenium.check_exists_by_xpath(self, "//p[contains(text(),'Usuario ya existe')]")
            if not message:
                Selenium.foto(self, "mensaje")
                assert message, "Error, NO APARECE EL MENSAJE DE QUE EL USUARIO YA EXISTE DEBAJO DEL INPUT " \
                                    "'NOMBRE DE USUARIO'"

            button = Selenium.get_elements(self, "crear").is_enabled()
            if button:
                Selenium.foto(self, "usuario existente")
                assert not button, f"ERROR, EL BOTÓN CREAR ESTA HABILITADO CON EL USUARIO '{user}' Y ESTE ES EXISTENTE"

            Selenium.get_elements(self, "cancelar").click()

            Selenium.check_click_element(self, "crear usuario")
            Selenium.get_elements(self, "crear usuario").click()

            time.sleep(1)
            CreateUser.modal(self)

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))