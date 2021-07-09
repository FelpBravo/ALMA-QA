# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Pruebas Directorios')
@allure.testcase(u'Pruebas de integración')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Editar directorios y validar que no se pueda crear un directorio con el mismo nombre.
</br></br>""")
class test_directory_008(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.name_directory = "test_create" + Selenium.generate_id(length=2)

    @allure.title(u'Editar un directorio')
    @allure.story(u'Editar un directorio y validaciones : Campo input..')
    def test_edit_005(self):
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
            time.sleep(1) #OBLIGATORIO


        with allure.step(u'PASO 5: Validando campo input en la edición'):
            amount = 3
            for edit in range(amount):
                for tr in range(len(self.driver.find_elements_by_xpath("//tbody/tr/th[1]"))):
                    tr += 1
                    if self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text == self.name_directory:
                        print("le hare click")
                        self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[1]").click()
                        Selenium.foto(self, "Editar")
                        break
                    if edit == 1:
                        if not self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text == self.name_directory:
                            existing_directory = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/th[1]").text

                if edit == 0:
                    Selenium.check_element(self, "nombre")
                    Selenium.get_elements(self, "nombre").clear()
                    Selenium.foto(self, "SIN NADA")
                    assert self.driver.find_element_by_xpath("//p[@id='name-helper-text']").text == "Campo requerido", \
                        "ERROR NO SE INGRESO NINGUN DATO EN EL INPUT NOMBRE Y NO APARECE EL MENSAJE ESPERADO: " \
                        "'Campo Requerido'"
                    assert Selenium.get_elements(self, "guardar").is_enabled(), "ERROR, EL BOTÓN GUARDAR SIGUE " \
                                                                                "HABILITADO CON EL INPUT NOMBRE " \
                                                                                "ESTANDO VACIO."

                if edit == 2:
                    Selenium.check_element(self, "nombre")
                    self.driver.execute_script(f"arguments[0].value=''",
                                               Selenium.get_elements(self, "nombre"))
                    Selenium.get_elements(self, "nombre").send_keys("aa")
                    Selenium.get_elements(self, "guardar").click()
                    Selenium.foto(self, "SOLO 2 CARACTERES")
                    assert self.driver.find_element_by_xpath(
                        "//p[@id='name-helper-text']").text == "Debe contener al menos 3 carácteres", \
                        "ERROR SE INGRESARON SOLO 2 CARACTERES Y NO APARECE EL MENSAJE ESPERADO: " \
                        "'Debe contener al menos 3 carácteres'"
                    assert Selenium.get_elements(self, "guardar").is_enabled(), "ERROR, EL BOTÓN GUARDAR SIGUE " \
                                                                                "HABILITADO CON EL INPUT NOMBRE " \
                                                                                "CON SOLO 2 CARACTERES INGRESADOS."

                if edit == 1:
                    Selenium.check_element(self, "nombre")
                    self.driver.execute_script(f"arguments[0].value=''",
                                               Selenium.get_elements(self, "nombre"))
                    Selenium.get_elements(self, "nombre").send_keys(existing_directory)
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