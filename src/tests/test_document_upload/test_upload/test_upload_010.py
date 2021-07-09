# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner
import random

@allure.feature(u'Carga de documentos')
@allure.testcase(u'Prueba Unitaria', u'https://api-ux.atlassian.net/browse/ALMA-320')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validar el maximo de caracteres permitidos en la metadata</br>
</br></br>""")

class test_upload_010(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Campos metadata.')
    @allure.story(u'Validar que el largo maximo de caracteres permitidos en la metadata sea de 100.')
    def test_upload_011(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar un documento'):
            for cargar in range(1):
                Selenium.get_json_file(self, "cargarDocumento")
                Selenium.select_folder_random(self)
                time.sleep(0.5)
                Selenium.check_visibility_element_located(self, "Seleccionar ICD/NO")
                Selenium.get_elements(self, "Seleccionar ICD/NO").click()
                Selenium.get_elements(self, "Opcion NoICD").click()

                Selenium.subida_unitaria(self)

                Selenium.select_projectCode(self)
                Selenium.select_organization(self)
                Selenium.select_docuStatus(self)
                Selenium.select_docuType(self)
                date = Selenium.textDateEnvironmentReplace(self, "hoy")
                Selenium.get_elements(self, "Campo date").send_keys(date)
                campos = ['Campo modifiedBy', 'Campo ownerName', 'Campo subject', 'Campo fielType',
                          'Campo author', 'Campo control board', 'Campo system', 'Campo secMode',
                          'Campo releaseBy', 'Campo docId', 'Campo forumId', 'Campo approvedBy',
                          'Campo revBy', 'Campo group', 'Campo docAbs']
                caracter100 = ['Es otro de tantos test para comprobar máximo de caracteres permitidos para ingresar en la metadata..',
                               'Haciendo una prueba generada por Selenium para comprobar que le máximo de caracteres sea de "100"...',
                               'Se esta validando haciendo una prueba de unitaria en cada campo de esta metadata para comprobar.....']
                value = []
                for campo in range(15):
                    rdom = random.choice(caracter100)
                    name = Selenium.get_elements(self, campos[campo]).get_attribute("name")

                    Selenium.get_elements(self, campos[campo]).send_keys(rdom + ".")
                    Selenium.get_elements(self, "Campo almaDoc").click()
                    value.append(rdom)

                    checkValidate = Selenium.check_exists_by_xpath(self, f"//p[@id='{name}-helper-text']")
                    textValidate = self.driver.find_element_by_xpath(f"//p[@id='{name}-helper-text']").text

                    if not textValidate == 'Máximo 100 carácteres':
                        Selenium.foto(self, "Texto igual")
                        assert textValidate == "Máximo 100 carácteres", "Error no se encuentra el mensaje de validación"

                    if checkValidate == False:
                        Selenium.foto(self, "Validacion")
                        assert  checkValidate == True, "Error no se encuentra el mensaje de validación"

                    button = Selenium.get_elements(self, "Cargar").is_enabled()
                    if button == True:
                        Selenium.foto(self, "Validacion")
                        assert button == False, "Error el boton 'CARGAR' se encuentra habilitado y existen campos con errores."

                    Selenium.get_elements(self, campos[campo]).clear()
                    Selenium.get_elements(self, campos[campo]).send_keys(rdom)

                button = Selenium.get_elements(self, "Cargar").is_enabled()
                if button == False:
                    Selenium.foto(self, "Validacion")
                    assert button == True, "Error el boton 'CARGAR' se encuentra deshabilitado y existen campos con errores."
                Selenium.foto(self, "Metadata ingresada")
                Selenium.check_click_element(self, "Cargar")
                Selenium.get_elements(self, "Cargar").click()
                Selenium.check_visibility_element_located(self, "Boton confirmar cargar documento")
                Selenium.get_elements(self, "Boton confirmar cargar documento").click()
                time.sleep(0.5)
                Selenium.foto(self, "AlmaID")



    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))