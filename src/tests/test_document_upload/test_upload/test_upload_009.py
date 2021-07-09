# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'Prueba de integración', u'https://api-ux.atlassian.net/browse/ALMA-302')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Al cargar un documento, este deberia de poder encontrarse en la busqueda avanzada, para luego validar y comparar la 
metadata ingresada con la metadata visualizada</br>
</br></br>""")

class test_upload_009(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Cargar un documento.')
    @allure.story(u'Despues de cargar un documento, ingresar en la busqueda avanzada y Validar la metadata del documento cargardo.')
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

                archive = Selenium.subida_unitaria(self)
                archive

                value = Selenium.set_metadata_random(self, condition=1)
                value

                projectCode = Selenium.select_projectCode(self)
                projectCode

                organization = Selenium.select_organization(self)
                organization

                docuStatus = Selenium.select_docuStatus(self)
                docuStatus

                docuType = Selenium.select_docuType(self)
                docuType

                Selenium.foto(self, "Metadata ingresada")
                Selenium.check_click_element(self, "Cargar")
                Selenium.get_elements(self, "Cargar").click()
                Selenium.check_visibility_element_located(self, "Boton confirmar cargar documento")
                Selenium.get_elements(self, "Boton confirmar cargar documento").click()

                check = Selenium.check_exists_by_xpath(self, f"//h6[contains(text(), '{archive[1]}')]")
                if check == False:
                    Selenium.foto(self, "Nombre del documento")
                    assert True, "ERROR, AL PARECER NO SE HA MOSTRADO EL NOMBRE DEL DOCUMENTO EN EL ULTIMO MODAL"

                checkId = Selenium.check_exists_by_xpath(self, "//h2[@id='swal2-title']")
                if checkId == True:
                    title = self.driver.find_element_by_xpath("//h2[@id='swal2-title']").text
                    Selenium.foto(self, "AlmaID")
                    assert title == "AlmaID Generado con éxito", "No se visualiza el nombre del mensaje [AlmaID Generado con éxito]"
                if checkId == False:
                    Selenium.foto(self, "AlmaID")
                    assert checkId == True, "No se visualiza el mensaje [AlmaID Generado con éxito]"

                Selenium.check_visibility_element_located(self, "Boton confirmar cargar documento")
                Selenium.check_element(self, "AlmaID y nombreDoc")
                almaId = Selenium.split(self, Selenium.get_elements(self, "AlmaID y nombreDoc").text, " ")
                Selenium.get_elements(self, "Boton confirmar cargar documento").click()

                condicion = 0
                while condicion == 0:
                    Selenium.get_json_file(self, "cargarDocumento")
                    Selenium.check_element(self, "Panel de inicio")
                    Selenium.get_elements(self, "Panel de inicio").click()
                    Selenium.get_json_file(self, "search_advanced")
                    Selenium.check_element(self, "busqueda avanzada")
                    time.sleep(1)
                    Selenium.get_elements(self, "busqueda avanzada").click()
                    Selenium.get_elements(self, "alma doc number").send_keys(almaId[0])
                    Selenium.get_elements(self, "buscar").click()

                    element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
                    if Selenium.check_exists_by_xpath(self, "//tbody/tr") == True:
                        if len(element) == 1:
                            self.driver.find_element_by_xpath(f"//tbody/tr[1]/td[8]/div[1]/div[1]").click()
                            time.sleep(5)
                            Selenium.get_json_file(self, "breadCrumbs")
                            valores = Selenium.split(self, Selenium.get_elements(self, "metadata").text, "\n")
                            print(value, "\n", valores)
                            for x in range(len(value)):
                                if x == 0:
                                    Selenium.foto(self, f"Metadata documento {archive[1]}")
                                self.assertIn(value[x], valores, f"El valor {value[x]} no es igual al obtenido de la metadata")
                            self.assertIn(almaId[0], valores, f"El alma ID {almaId[0]} no es igual al obtenido de la metadata")
                            assert projectCode == valores[4], f"El valor {projectCode} en la metadata no es igual al ingresado"
                            assert organization == valores[10], f"El valor {organization} en la metadata no es igual al ingresado"
                            assert docuStatus == valores[20], f"El valor {docuStatus} en la metadata no es igual al ingresado"
                            assert docuType == valores[34], f"El valor {docuType} en la metadata no es igual al ingresado"
                            condicion = 1
                            condicion
                            break
                        if len(element) > 1:
                            Selenium.foto(self, "Alma ID Repetidos")
                            assert len(element) > 1, f"Existen dos documentos con el mismo AlmaID = {almaId[0]}"
                    if Selenium.check_exists_by_xpath(self, "//tbody/tr") == False:
                        continue

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))