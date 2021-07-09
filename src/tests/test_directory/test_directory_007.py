# -*- coding: utf-8 -*-
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Pruebas Directorios')
@allure.testcase(u'Pruebas de integración')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Crear directorios y validar que no se pueda crear un directorio con su mismo nombre.
</br></br>""")

class test_directory_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.creaDir = "test_create" + Selenium.generate_id(length=2)

    @allure.title(u'Crear un directorio')
    @allure.story(u'Crear un directorio y validaciones : Campo input..')
    def test_create_003(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Ingresar en directorios'):
            Selenium.get_elements(self, "Menu administracion").click()
            Selenium.get_elements(self, "Menu directorios").click()

        with allure.step(u'PASO 4: Creando un directorio'):
            amount = 3
            for create in range(amount):
                Selenium.check_element(self, "Crear nuevo directorio")
                Selenium.foto(self, "Crear nuevo directorio")
                Selenium.get_elements(self, "Crear nuevo directorio").click()
                Selenium.get_elements(self, "tipo espacio trabajo").click()
                Selenium.get_elements(self, "workspace").click()

                if create == 0:
                    Selenium.get_elements(self, "guardar").click()
                    Selenium.get_elements(self, "guardar").click()
                    Selenium.foto(self, "SIN NADA")
                    assert self.driver.find_element_by_xpath("//p[@id='name-helper-text']").text == "Campo requerido", \
                        "ERROR NO SE INGRESO NINGUN DATO EN EL INPUT NOMBRE Y NO APARECE EL MENSAJE ESPERADO: " \
                        "'Campo Requerido'"
                    assert Selenium.get_elements(self, "guardar").is_enabled(), "ERROR, EL BOTÓN GUARDAR SIGUE " \
                                                                                    "HABILITADO CON EL INPUT NOMBRE " \
                                                                                    "ESTANDO VACIO."

                if create == 1:
                    Selenium.get_elements(self, "nombre").send_keys("aa")
                    Selenium.get_elements(self, "guardar").click()
                    Selenium.foto(self, "SOLO 2 CARACTERES")
                    assert self.driver.find_element_by_xpath("//p[@id='name-helper-text']").text == "Debe contener al menos 3 carácteres", \
                        "ERROR SE INGRESARON SOLO 2 CARACTERES Y NO APARECE EL MENSAJE ESPERADO: " \
                        "'Debe contener al menos 3 carácteres'"
                    assert Selenium.get_elements(self, "guardar").is_enabled(), "ERROR, EL BOTÓN GUARDAR SIGUE " \
                                                                                    "HABILITADO CON EL INPUT NOMBRE " \
                                                                                    "CON SOLO 2 CARACTERES INGRESADOS."

                if create == 2:
                    for i in range(2):
                        if i == 0:
                            Selenium.get_elements(self, "nombre").send_keys(self.creaDir)
                            Selenium.get_elements(self, "guardar").click()

                        if i == 1:
                            Selenium.get_elements(self, "Crear nuevo directorio").click()
                            Selenium.get_elements(self, "tipo espacio trabajo").click()
                            Selenium.get_elements(self, "workspace").click()
                            Selenium.get_elements(self, "nombre").send_keys(self.creaDir)
                            Selenium.get_elements(self, "guardar").click()
                            Selenium.foto(self, "Directorio igual")
                            assert self.driver.find_element_by_xpath(
                                "//p[@id='name-helper-text']").text == "Este nombre ya está en uso, por favor usa otro.", \
                                "ERROR SE INGRESÓ UN DIRECTORIO EXISTENTE Y NO APARECE EL MENSAJE ESPERADO: " \
                                "'Este nombre ya está en uso, por favor usa otro.'"
                            assert Selenium.get_elements(self, "guardar").is_enabled(), "ERROR, EL BOTÓN GUARDAR SIGUE " \
                                                                                            "HABILITADO CON EL INPUT NOMBRE " \
                                                                                            "CON UN DIRECTORIO EXISTENTE " \
                                                                                            " INGRESADO."

                Selenium.get_elements(self, "cancelar").click()

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))