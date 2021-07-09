# -*- coding: utf-8 -*-
import random
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'Campos requeridos y boton Cargar' , u'https://api-ux.atlassian.net/browse/ALMA-91')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Correctas validaciones en conjunto con boton 'Cargar'</br>
Estado de los campos</br>
Validaciones en el campo fecha</br>
Validaciones en el campo ALMA Doc Number</br>
</br></br>""")

class test_upload_007(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'No mostrar metadata')
    @allure.story(u'Al entrar en la carga de documentos, la metadata no deberia de estar visible para el usuario.')
    def test_campos_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "documents")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Arbol carga documentos")
            Selenium.foto(self, "Carga de documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()

        with allure.step(u'PASO 4 : Validando que la metadata no sea visible'):
            self.metadata = ["Campo almaDoc", "Campo projectCode", "Campo date", "Campo modifiedBy" ,
                        "Campo org", "Campo ownerName", "Campo subject", "Campo fielType", "Campo author",
                        "Campo docStatus", "Campo system", "Campo secMode", "Campo releaseBy",
                        "Campo docId", "Campo forumId", "Campo docType", "Campo approvedBy",
                        "Campo revBy", "Campo group", "Campo docAbs"]  # List
            item = random.choice(self.metadata)
            Selenium.foto(self, "No se deberia de ver la metadata")
            self.assertFalse(Selenium.check_element(self, item), f"Error, El campo {item} en conjunto con otros elementos de la metadata son visibles.")

    @allure.title(u'Mostrar metadata')
    @allure.story(u'Al entrar en la carga de documentos, seleccionar ICD y visualizar la metadata .')
    def test_campos_002(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "documents")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Arbol carga documentos")
            Selenium.foto(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionando No-ICD'):
            Selenium.foto(self, "Carga documentos")
            Selenium.get_elements(self, "Seleccionar ICD/NO").click()
            Selenium.get_elements(self, "Opcion NoICD").click()
            Selenium.foto(self, "Seleccionar ICD/NO")

        with allure.step(u'PASO 5 : Validando visualizacion de la metadata'):
            self.metadata = ["Campo almaDoc", "Campo projectCode", "Campo date", "Campo modifiedBy",
                             "Campo org", "Campo ownerName", "Campo subject", "Campo fielType", "Campo author",
                             "Campo docStatus", "Campo system", "Campo secMode", "Campo releaseBy",
                             "Campo docId", "Campo forumId", "Campo docType", "Campo approvedBy",
                             "Campo revBy", "Campo group", "Campo docAbs"]  # List
            for m in range(19):
                item = random.choice(self.metadata)
                if m == 0:
                    Selenium.foto(self, "No se deberia de ver la metadata")
                self.assertTrue(Selenium.check_element(self, item),f"Error, El campo {item} en conjunto con otros elementos de la metadata no son visibles.")

    @allure.title(u'Validar campo ALMADocNumber')
    @allure.story(u'Al entrar en la carga de documentos, seleccionar ICD y visualizar el campo AlmaDocNumber bloqueado .')
    def test_campos_003(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "documents")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Arbol carga documentos")
            Selenium.foto(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionando No-ICD'):
            Selenium.foto(self, "Carga documentos")
            Selenium.get_elements(self, "Seleccionar ICD/NO").click()
            Selenium.get_elements(self, "Opcion NoICD").click()
            Selenium.foto(self, "Seleccion NoICD")

        with allure.step(u'PASO 5 : Validando que el campo este bloqueado'):
            Selenium.check_element(self, "Campo almaDoc")
            estado = Selenium.get_elements(self, "Campo almaDoc").is_enabled()
            Selenium.foto(self, "Campo almaDoc")
            assert estado == False, "El campo Alma Doc Number no esta bloqueado"

    @allure.title(u'Validar campo ReleaseDate')
    @allure.story(u'Al entrar en la carga de documentos, seleccionar ICD, visualizar metadata y validar el campo ReleaseDate.')
    def test_campos_004(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "documents")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Arbol carga documentos")
            Selenium.foto(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionando No-ICD'):
            Selenium.foto(self, "Carga documentos")
            Selenium.get_elements(self, "Seleccionar ICD/NO").click()
            Selenium.get_elements(self, "Opcion NoICD").click()
            Selenium.foto(self, "Opcion NoICD")

        with allure.step(u'PASO 5 : Validando valores a ingresar'):
            Selenium.check_element(self, "Campo date")
            Selenium.get_elements(self, "Campo date").send_keys("99999-99-99")
            valor = Selenium.get_elements(self, "Campo date").get_attribute("value")
            Selenium.foto(self, "Date")
            self.assertNotIn("99999-99-99", valor, "Error, se a permitido ingresar una fecha no valida")

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))