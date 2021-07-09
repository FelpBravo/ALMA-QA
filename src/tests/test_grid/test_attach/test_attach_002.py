# -*- coding: utf-8 -*-
import os
import random
import unittest
from datetime import time
import time
import allure
import pytest
from src.functions.functions import Functions as Selenium
import HtmlTestRunner
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

@allure.feature(u'Adjuntar archivos')
@allure.testcase(u'Comentarios y Attachments', u'https://api-ux.atlassian.net/browse/ALMA-48')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Adjuntar documentos</br>
Validaciones de botones</br>
Vista esperada esperada</br>
Carga masiva</br>
Visualizacion de los archivos cargados</br>
</br></br>""")

class test_attach_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            date = Selenium.textDateEnvironmentReplace(self, "hoy")
            id = Selenium.generate_id(length=3)
            self.comentario = f"Comentario generado por Selenium {date + ' id' +id}"

    @allure.title(u'Adjuntar')
    @allure.story(u'Visualizar que el nombre del boton cambie al adjuntar un archivo.')
    def test_attach_006(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Escribir un comentario'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                Selenium.get_json_file(self, "attach")
                Selenium.get_elements(self, "documentos adjuntos").click()

                file = Selenium.random_file(self)
                format = Selenium.split(self, file, ".")
                Selenium.check_element(self, "adjuntar")
                Selenium.get_elements(self, "adjuntar").send_keys(Selenium.basedir + f"\\file\\.{format[1]}\\" + str(file))

                textButton = Selenium.check_exists_by_xpath(self,f"//span[contains(text(),'Cargar Archivo')]")
                if textButton == False:
                    Selenium.foto(self, "Documento no adjuntado")
                    assert True == textButton, "ERROR, EL BOTON NO HA CAMBIADO DE NOMBRE COMO DEBERIA"

                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.title(u'Adjuntar')
    @allure.story(u'Probando cargar un archivo adjunto.')
    def test_attach_007(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Escribir un comentario'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                Selenium.get_json_file(self, "attach")
                Selenium.get_elements(self, "documentos adjuntos").click()

                file = Selenium.random_file(self)
                format = Selenium.split(self, file, ".")
                Selenium.check_element(self, "adjuntar")
                Selenium.get_elements(self, "adjuntar").send_keys(Selenium.basedir + f"\\file\\.{format[1]}\\" + str(file))
                Selenium.foto(self, "**Cargando archivo**")
                self.driver.find_element_by_xpath("//span[contains(text(),'Cargar Archivo')]").click()

                check = Selenium.check_exists_by_xpath(self, f"//h5[contains(text(),'{file}')]")
                if check == True:
                    text = self.driver.find_element_by_xpath(f"//h5[contains(text(),'{file}')]").text
                    print(text.lower(), file.lower())
                    Selenium.foto(self, "Archivo no cargado")
                    assert file.lower() == text.lower(), "ERROR, LOS NOMBRES DE LOS ARCHIVOS NO COINCIDEN"

                if check == False:
                    Selenium.foto(self, "Archivo no cargado")
                    assert True == check, "ERROR, EL ARCHIVO NO SE HA CARGADO"

                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.title(u'Adjuntar')
    @allure.story(u'Adjuntando 10 archivos .')
    def test_attach_008(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Escribir un comentario'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")

            nDocument = random.randint(1, len(element))
            self.driver.find_element_by_xpath(f"//tbody/tr[{str(nDocument)}]/td[8]/div[1]/div[1]").click()
            Selenium.get_json_file(self, "attach")
            Selenium.get_elements(self, "documentos adjuntos").click()

            for a in range(10):
                file = Selenium.random_file(self)

                if not a == 0:
                    Selenium.get_elements(self, "comentarios").click()
                    Selenium.esperar_elemento(self, "documentos adjuntos")
                    Selenium.get_elements(self, "documentos adjuntos").click()
                format = Selenium.split(self, file, ".")
                Selenium.check_element(self, "adjuntar")
                Selenium.get_elements(self, "adjuntar").send_keys(Selenium.basedir + f"\\file\\.{format[1]}\\" + str(file))
                while False:
                    Selenium.check_exists_by_xpath(self, "//span[contains(text(),'Cargar Archivo')]")
                self.driver.find_element_by_xpath("//span[contains(text(),'Cargar Archivo')]").click()

                check = Selenium.check_exists_by_xpath(self, f"//h5[contains(text(),'{file}')]")
                if check == True:
                    text = self.driver.find_element_by_xpath(f"//h5[contains(text(),'{file}')]").text
                    if not file.lower() == text.lower():
                        assert file.lower() == text.lower(), "ERROR, LOS NOMBRES DE LOS ARCHIVOS NO COINCIDEN"

                if check == False:
                    Selenium.foto(self, "Archivo no cargado")
                    assert True == check, "ERROR, EL ARCHIVO NO SE HA CARGADO"

            self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))