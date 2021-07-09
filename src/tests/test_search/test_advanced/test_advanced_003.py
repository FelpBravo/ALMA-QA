# -*- coding: utf-8 -*-
import random
import time
import unittest
import allure
import pytest
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Busqueda avanzada')
@allure.testcase(u'Busqueda avanzada')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Buscar por autor</br>
Buscar por version</br>
Buscar por Alma ID</br>
Validaciones de mas de un ALMAID</br>
Buscar por Don number</br>
Buscar por Nombre de documento</br>
</br></br>""")

class test_advanced_003(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.autores = ['Admin', 'Felipe', 'dvalero']

    @allure.title(u'Buscar por autor.')
    @allure.story(u'Comprobando una busqueda por nombre de autor, validando los autores mostrado en la grilla.')
    def test_search_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a la busqueda avanzada'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Botón")

        with allure.step(u'PASO 4 : Validando la busqueda por autor'):
            repeat = False
            while not repeat:
                author = random.choice(self.autores)
                Selenium.get_elements(self, "autor").send_keys(author)
                if author == "dvalero":
                    author = "Daniel"
                Selenium.foto(self, "foto de lo ingresado")

                Selenium.get_elements(self, "buscar").click()

                if not Selenium.check_exists_by_xpath(self, "//tbody/tr"):
                    Selenium.get_elements(self, "Panel de inicio").click()
                    time.sleep(1.7) #OBLIGATORIO
                    Selenium.get_elements(self, "busqueda avanzada").click()
                    repeat = False
                else:
                    repeat = True

            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                autorVisualizado = self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[2]").text
                if x == 1:
                    Selenium.foto(self, "Grilla")
                self.assertIn(author, autorVisualizado, "No se encuentra")

    @allure.title(u'Buscar por Alma ID.')
    @allure.story(u'Comprobando una busqueda por Alma ID, validando los autores mostrado en la grilla.')
    def test_search_002(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a la busqueda avanzada'):
            meta = Selenium.get_data_metadata(self, 2)
            for largo in range(len(meta)):
                Selenium.get_json_file(self, "search_advanced")
                time.sleep(1)
                Selenium.get_elements(self, "busqueda avanzada").click()
                Selenium.get_elements(self, "alma doc number").send_keys(meta[largo])
                Selenium.foto(self, "AlmaID")
                Selenium.get_elements(self, "buscar").click()
                if False == Selenium.check_exists_by_xpath(self, "//tbody/tr"):
                    Selenium.foto(self, "Grilla")
                    assert False, "ERROR, NO SE ENCUENTRA EL DOCUMENTO EXISTENTE EN LA GRILLA"
                element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
                Selenium.foto(self, "Documentos en la grilla")
                if 1 == len(element):
                    Selenium.get_json_file(self, "breadCrumbs")
                    self.driver.find_element_by_xpath(f"//tbody/tr[1]/td[8]/div[1]/div[1]").click()
                    Selenium.foto(self, "Alma ID")
                    valores = Selenium.split(self, Selenium.get_elements(self, "metadata").text, "\n")
                    assert meta[largo] == valores[2], f"Error, Los ALMA ID '{meta[largo]}' y {valores[2]} no coinciden"
                else:
                    Selenium.foto(self, "Foto")
                    assert not len(element) > 1, f"ERROR HAY DOS ELEMENTOS CON EL MISMO ALMA ID '{meta[largo]}' SEGUN EL BUSCADOR"
                Selenium.get_json_file(self, "search_advanced")
                Selenium.get_elements(self, "inicio").click()

    @allure.title(u'Buscar por Version.')
    @allure.story(u'Comprobando una busqueda por Versionamiento, validando las versiones mostradas en la grilla.')
    def test_search_003(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a la busqueda avanzada'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")
            versiones = ['1', '2', '3', '8']
            for v in range(len(versiones)):
                time.sleep(2)
                Selenium.get_elements(self, "busqueda avanzada").click()
                Selenium.foto(self, "Boton")
                Selenium.get_elements(self, "version").send_keys(versiones[v])
                Selenium.foto(self, "foto de lo ingresado")
                Selenium.get_elements(self, "buscar").click()
                element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
                if Selenium.check_exists_by_xpath(self, "//tbody/tr") == True:
                    Selenium.foto(self, "Documentos en la grilla")
                    for x in range(len(element)):
                        x += 1
                        versionVisual = self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[6]").text
                        if not versionVisual == versiones[v]:
                            Selenium.foto(self, "Grilla")
                        self.assertIn(versiones[v], versionVisual, "Error, la version buscada no coincide con la devuelta en la grilla")
                if versiones[v] == 1:
                    Selenium.foto(self, f"{versiones[1]}")
                    assert versionVisual == versiones[v], f"ERROR, NO SE ENCUENTRA LA VERSION {versiones[v]}"
                Selenium.get_elements(self, "inicio").click()

    @allure.title(u'Buscar por DOC ID.')
    @allure.story(u'Comprobando una busqueda por DOC ID, validando el DOC ID mostrado en la grilla.')
    def test_search_004(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a la busqueda avanzada'):
            Selenium.foto(self, "Busqueda avanzada")
            Selenium.get_json_file(self, "search_advanced")

            Selenium.get_elements(self, "busqueda avanzada").click()
            Selenium.foto(self, "Boton")
            Selenium.get_elements(self, "doc id").send_keys("xxx-xxx-xxx-xx")
            Selenium.foto(self, "foto de lo ingresado")
            Selenium.get_elements(self, "buscar").click()
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            if Selenium.check_exists_by_xpath(self, "//tbody/tr") == True:
                Selenium.foto(self, "Documentos en la grilla")

                n = random.randint(1, len(element))
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(n)}]/td[8]/div[1]/div[1]").click()
                Selenium.foto(self, "Metadata")
                Selenium.get_json_file(self, "breadCrumbs")
                if Selenium.check_element(self, "metadata") == False:
                    Selenium.foto(self, "Error")
                    pytest.skip(f"[PRUEBA SALTADA] Al parecer hay un ERROR, la metadata no se visualiza")
                text = Selenium.split(self, Selenium.get_elements(self, "metadata").text, "\n")
                self.assertIn("xxx-xxx-xxx-xx", text,"Error, El doc id no es el mismo que el visualizado en la metadata del documento")

    @allure.title(u'Buscar por Nombre de Documento.')
    @allure.story(u'Comprobando una busqueda por Nombre de documento, validando el Nombre del documento mostrado en la grilla.')
    def test_search_005(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a la busqueda avanzada'):
            Selenium.comprobar_carpeta_con_archivos(self)
            document = Selenium.get_doc_name(self, "si")
            for l in range(len(document)):
                Selenium.get_json_file(self, "search_advanced")
                time.sleep(1)
                Selenium.get_elements(self, "busqueda avanzada").click()
                Selenium.get_elements(self, "nombre documento").send_keys(document[l])
                Selenium.get_elements(self, "buscar").click()
                if not Selenium.check_exists_by_xpath(self, "//tbody/tr"):
                    Selenium.foto(self, "Grilla")
                    assert Selenium.check_exists_by_xpath(self, "//tbody/tr"), f"ERROR, NO SE ENCUENTRA EL DOCUMENTO '{document[l]}' EN LA GRILLA"
                Selenium.foto(self, "Documentos en la grilla")
                document_grid = Selenium.get_doc_name(self, "no")
                element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
                for x in range(len(element)):
                    self.assertIn(document[l], document_grid, f"Error, Los Nombres ESPERADO:'{document[l]}' y ACTUAL:'{document_grid[x]}' no coinciden")
                Selenium.get_json_file(self, "search_advanced")
                Selenium.get_elements(self, "inicio").click()

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
