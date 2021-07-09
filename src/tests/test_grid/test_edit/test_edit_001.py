# -*- coding: utf-8 -*-
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner


@allure.feature(u'Editar documento')
@allure.testcase(u'Validando elementos al editar un documento', u'Jira')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones sobre editar documentos: </br>
boton de editar en la grilla</br>
Boton de seleccion de carpetas </br>
Validar carpetas del selector en conjunto con la base de datos </br>
Visualizar de la carpeta raiz correcta del documento</br>
</br></br>""")
class test_edit_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Boton de Editar .')
    @allure.story(u'Validar existencia y visualizacion del boton de editar.')
    def test_edit_001(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.foto(self, "Documentos en la grilla")
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 4 : Validando visualización y existencia'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1

                exist = Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[3]")
                assert exist == True, "No existe el boton de editar"

                visual = Selenium.check_visibility_by_xpath(self, f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[3]")
                assert visual == True, "No se visualiza el boton de editar"

                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.title(u'Boton de seleccion de carpetas.')
    @allure.story(u'Validar su localizacion, visualizacion y estado.')
    def test_edit_002(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.foto(self, "Documentos")
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 4 : Validando el boton de seleccion de carpetas'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[3]").click()
                Selenium.get_json_file(self, "editar")
                Selenium.foto(self, "Boton de carpetas")

                assert Selenium.check_element(self, "Boton carpetas") == True, "No se encuentra el boton de carpetas"
                assert Selenium.check_visibility_element_located(self, "Boton carpetas") == True, "No se visualiza el boton de carpetas"
                assert Selenium.get_elements(self,"Boton carpetas").is_enabled() == True, "El boton de carpetas está bloqueado"

                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.title(u'Carpeta raiz.')
    @allure.story(u'Validar su coincidencia con la carpeta que aparece al editar.')
    def test_edit_003(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.foto(self, "Documentos")
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 4 : Validando el nombre de la carpeta raiz'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[3]").click()
                Selenium.get_json_file(self, "editar")
                Selenium.foto(self, "Boton de carpetas")
                self.assertIn(nomCapeta, Selenium.get_elements(self, "Carpeta actual").text, "El nombre de la carpeta no coincide con el nombre de carpeta raiz")
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.title(u'Selector de carpetas.')
    @allure.story(u'Validar que el selector de carpetas devuelva las mismas carpetas que en la base de datos.')
    def test_edit_004(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.foto(self, "Documentos")
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 4 : Validando que no se vean pantallas azules'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[3]").click()
                Selenium.get_json_file(self, "editar")
                Selenium.check_visibility_element_located(self, "Boton carpetas")
                Selenium.foto(self, "Editar")
                Selenium.get_elements(self, "Boton carpetas").click()

                Selenium.check_visibility_element_located(self, "Carpetas del selector")
                folders = Selenium.get_elements(self, "Carpetas del selector").text

                for carpeta in Selenium.split(self, folders, "\n"):
                    consulta = Selenium.pyodbc_query(self, f"SELECT name FROM company_folder WHERE name= '{carpeta}'")
                    if consulta == None:
                        Selenium.foto(self, "No se encontro la busqueda")
                        assert not consulta == None, f"No se en conntro la carpeta {carpeta} en la tabla company_folder"
                if x == 1:
                    Selenium.foto(self, "Selector de carpetas")
                Selenium.get_json_file(self, "editar")
                Selenium.get_elements(self, "Boton cancelar selector").click()
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
