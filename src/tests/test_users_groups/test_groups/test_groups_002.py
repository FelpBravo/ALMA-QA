# -*- coding: utf-8 -*-
import random
import unittest
import allure
from src.utils.Groups.CreateGroup import CreateGroup
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Usuarios y grupos')
@allure.testcase(u'Crear un grupo existente')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validar estado y visualizacion de los diferentes elementos de esta pantalla. </br></br>""")

class test_groups_002(Selenium, CreateGroup, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Crear grupo existente.')
    @allure.story(u'Validar mensajes de error al crear un grupo existente.')
    def test_groups_exist(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

            Selenium.get_json_file(self, "groups")
            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            filas = len(self.driver.find_elements_by_xpath("//tbody/tr"))
            tr = random.randint(1, filas)
            dataGroup = []

            group = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[1]").text
            nom = Selenium.split(self, group, "_")
            dataGroup.append(nom)
            print(f"Se ejecutara la prueba con la dependencia '{nom[0]}' y el perfil '{nom[1]}' ")

            Selenium.get_elements(self, "crear grupo").click()
            Selenium.check_element(self, "Modal crear agregar")

            Selenium.get_elements(self, "dependencia").send_keys(nom[0])
            Selenium.get_elements(self, "perfiles").send_keys(nom[1])

            message = Selenium.check_exists_by_xpath(self, "//p[contains(text(),'Grupo ya existe')]")
            if not message:
                Selenium.foto(self, "mensaje")
                assert message, "Error, NO APARECE EL MENSAJE DE QUE EL GRUPO YA EXISTE DEBAJO DEL INPUT NOMBRE DE GRUPO"

            button = Selenium.get_elements(self, "crear").is_enabled()
            if button:
                Selenium.foto(self, "mensaje")
                assert not button, "Error, EL BOTON CREAR GRUPO ESTA HABILITADO"

            Selenium.get_elements(self, "cancelar").click()

            Selenium.check_click_element(self, "crear grupo")
            Selenium.get_elements(self, "crear grupo").click()

            CreateGroup.modal(self)

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))