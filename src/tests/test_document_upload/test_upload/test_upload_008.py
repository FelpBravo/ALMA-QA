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
Al cargar un documento, deberian de aparecer los mensajes al final de la carga</br>
</br></br>""")

class test_upload_008(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Cargar un documento.')
    @allure.story(u'Al cargar un documento, visualizar modal de decicion antes de cargar.')
    def test_upload_007(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar un documento'):
            for cargar in range(3):
                Selenium.select_folder_random(self)
                time.sleep(0.5)
                Selenium.check_visibility_element_located(self, "Seleccionar ICD/NO")
                Selenium.get_elements(self, "Seleccionar ICD/NO").click()
                Selenium.get_elements(self, "Opcion NoICD").click()

                archive = Selenium.subida_unitaria(self)
                archive

                Selenium.set_metadata_random(self)

                Selenium.check_visibility_element_located(self, "Cargar")
                Selenium.get_elements(self, "Cargar").click()
                Selenium.check_visibility_element_located(self, "Boton confirmar cargar documento")

                Selenium.check_exists_by_xpath(self, "//h2[@id='swal2-title']")
                xpath1= self.driver.find_element_by_xpath("//h2[@id='swal2-title']").text
                assert  xpath1 == "Carga de documento", "Error, el nombre ya no es igual 'Carga de documento'"

                Selenium.check_exists_by_xpath(self, "//div[@id='swal2-content']")
                xpath2 = self.driver.find_element_by_xpath("//div[@id='swal2-content']").text
                assert xpath2 == "¿Estás seguro de realizar la carga de archivos?", "Error, el nombre ya no es igual 'Carga de documento'"

                check1 = Selenium.check_visibility_element_located(self, "Boton confirmar cargar documento")
                enable1 = Selenium.get_elements(self, "Boton confirmar cargar documento").is_enabled()
                if check1 == False:
                    Selenium.foto(self, "Modal de decisión")
                    assert check1 == True, "No se encuentra el boton en el modal de decisión"
                if enable1 == False:
                    Selenium.foto(self, "Modal de decisión")
                    assert enable1 == True, "El boton esta bloqueado"

                check2 = Selenium.check_visibility_element_located(self, "Boton cancelar")
                enable2 = Selenium.get_elements(self, "Boton cancelar").is_enabled()
                if check2 == False:
                    Selenium.foto(self, "Modal de decisión")
                    assert check2 == True, "No se encuentra el boton en el modal de decisión"
                if enable2 == False:
                    Selenium.foto(self, "Modal de decisión")
                    assert enable2 == True, "El boton esta bloqueado"

                Selenium.get_elements(self, "Boton confirmar cargar documento").click()
                Selenium.check_visibility_element_located(self, "Boton confirmar cargar documento")
                Selenium.get_elements(self, "Boton confirmar cargar documento").click()

    @allure.title(u'Cargar un documento.')
    @allure.story(u'En el modal de decision clickar cancelar y visualizar todos los campos en orden.')
    def test_upload_008(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar un documento'):
            for cargar in range(1):
                Selenium.select_folder_random(self)
                time.sleep(0.5)
                Selenium.check_visibility_element_located(self, "Seleccionar ICD/NO")
                Selenium.get_elements(self, "Seleccionar ICD/NO").click()
                Selenium.get_elements(self, "Opcion NoICD").click()

                archive = Selenium.subida_unitaria(self)
                archive

                Selenium.set_metadata_random(self)

                Selenium.check_visibility_element_located(self, "Cargar")
                Selenium.get_elements(self, "Cargar").click()

                Selenium.check_visibility_element_located(self, "Boton cancelar")
                Selenium.get_elements(self, "Boton cancelar").click()

                carpetas = Selenium.check_visibility_element_located(self, "Seleccionar carpeta")
                if carpetas == False:
                    Selenium.foto(self, "Elemento")
                    assert carpetas == True, "El elemento ya no se encuentra despues de haber presionado el boton cancelar"

                noIcd = Selenium.check_visibility_element_located(self, "Seleccionar ICD/NO")
                if noIcd == False:
                    Selenium.foto(self, "Elemento")
                    assert noIcd == True, "El elemento ya no se encuentra despues de haber presionado el boton cancelar"

                docControlado = Selenium.check_element(self, "documento controlado")
                if docControlado == False:
                    Selenium.foto(self, "Elemento")
                    assert docControlado == True, "El elemento ya no se encuentra despues de haber presionado el boton cancelar"

                cargarDoc = Selenium.check_visibility_element_located(self, "Area de carga documentos")
                if cargarDoc == False:
                    Selenium.foto(self, "Elemento")
                    assert cargarDoc == True, "El elemento ya no se encuentra despues de haber presionado el boton cancelar"

                etiquetas = Selenium.check_visibility_element_located(self, "Etiquetas")
                if etiquetas == False:
                    Selenium.foto(self, "Elemento")
                    assert etiquetas == True, "El elemento ya no se encuentra despues de haber presionado el boton cancelar"

                limpiar = Selenium.check_visibility_element_located(self, "Limpiar")
                if limpiar == False:
                    Selenium.foto(self, "Elemento")
                    assert limpiar == True, "El elemento ya no se encuentra despues de haber presionado el boton cancelar"

                cargar = Selenium.check_visibility_element_located(self, "Cargar")
                if cargar == False:
                    Selenium.foto(self, "Elemento")
                    assert cargar == True, "El elemento ya no se encuentra despues de haber presionado el boton cancelar"

    @allure.title(u'Cargar un documento.')
    @allure.story(u'Cargar un documento y visualizar el modal que contiene el AlmaID.')
    def test_upload_009(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar un documento'):
            for cargar in range(5):
                Selenium.select_folder_random(self)
                time.sleep(0.5)
                Selenium.check_visibility_element_located(self, "Seleccionar ICD/NO")
                Selenium.get_elements(self, "Seleccionar ICD/NO").click()
                Selenium.get_elements(self, "Opcion NoICD").click()

                archive = Selenium.subida_unitaria(self)
                archive

                Selenium.set_metadata_random(self)

                Selenium.check_visibility_element_located(self, "Cargar")
                Selenium.get_elements(self, "Cargar").click()
                Selenium.check_visibility_element_located(self, "Boton confirmar cargar documento")
                Selenium.get_elements(self, "Boton confirmar cargar documento").click()

                if not Selenium.check_exists_by_xpath(self, f"//h6[contains(text(), '{archive[1]}')]"):
                    Selenium.foto(self, "Nombre del documento")
                    assert Selenium.check_exists_by_xpath(self, f"//h6[contains(text(), '{archive[1]}')]"), "ERROR, AL PARECER NO SE HA MOSTRADO EL NOMBRE DEL DOCUMENTO EN EL ULTIMO MODAL"

                if Selenium.check_exists_by_xpath(self, "//h2[@id='swal2-title']"):
                    title = self.driver.find_element_by_xpath("//h2[@id='swal2-title']").text
                    Selenium.foto(self, "AlmaID")
                    assert title == "AlmaID Generado con éxito", "No se visualiza el nombre del mensaje [AlmaID Generado con éxito]"

                if not Selenium.check_exists_by_xpath(self, "//h2[@id='swal2-title']"):
                    Selenium.foto(self, "AlmaID")
                    assert Selenium.check_exists_by_xpath(self, "//h2[@id='swal2-title']"), "No se visualiza el mensaje [AlmaID Generado con éxito]"

                Selenium.check_visibility_element_located(self, "Boton confirmar cargar documento")
                Selenium.get_elements(self, "Boton confirmar cargar documento").click()

    @allure.title(u'Cargar un documento.')
    @allure.story(u'Despues de clickar en cargar documento, se deberian visualizar todos los campos en orden.')
    def test_upload_010(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "cargarDocumento")

        with allure.step(u'PASO 3 : Ingresar en la carga de documentos'):
            Selenium.check_visibility_element_located(self, "Carga documentos")
            Selenium.get_elements(self, "Carga documentos").click()

        with allure.step(u'PASO 4 : Seleccionar un documento'):
            for cargar in range(3):
                Selenium.select_folder_random(self)
                time.sleep(0.5)
                Selenium.check_visibility_element_located(self, "Seleccionar ICD/NO")
                Selenium.get_elements(self, "Seleccionar ICD/NO").click()
                Selenium.get_elements(self, "Opcion NoICD").click()

                archive = Selenium.subida_unitaria(self)
                archive

                Selenium.set_metadata_random(self)

                Selenium.check_visibility_element_located(self, "Cargar")
                Selenium.get_elements(self, "Cargar").click()

                Selenium.check_visibility_element_located(self, "Boton confirmar cargar documento")
                Selenium.get_elements(self, "Boton confirmar cargar documento").click()

                Selenium.check_visibility_element_located(self, "Boton confirmar cargar documento")
                Selenium.get_elements(self, "Boton confirmar cargar documento").click()

                time.sleep(1.5)

                carpetas = Selenium.check_visibility_element_located(self, "Seleccionar carpeta")
                if carpetas == False:
                    Selenium.foto(self, "Elemento")
                    assert carpetas == True, "El elemento ya no se encuentra despues de haber presionado el boton cancelar"
                valueC = Selenium.get_elements(self, "Seleccionar carpeta").get_attribute("value")
                if not valueC == "":
                    Selenium.foto(self, "Elemento")
                    assert valueC == "", f"Error, No se limpio el selector, el valor seleccioando es {valueC}"

                noIcd = Selenium.check_visibility_element_located(self, "Seleccionar ICD/NO")
                if noIcd == False:
                    Selenium.foto(self, "Elemento")
                    assert noIcd == True, "El elemento ya no se encuentra despues de haber ejecutado la carga"
                valueIcd = Selenium.get_elements(self, "Seleccionar ICD/NO").get_attribute("value")
                if not valueIcd == None:
                    Selenium.foto(self, "Elemento")
                    assert valueIcd == None, f"Error, No se limpio el selector, el valor seleccioando es {valueIcd}"

                docControlado = Selenium.check_element(self, "documento controlado")
                if docControlado == False:
                    Selenium.foto(self, "Elemento")
                    assert docControlado == True, "El elemento ya no se encuentra despues de haber ejecutado la carga"
                select = Selenium.get_elements(self, "documento controlado").is_selected()
                if not select == False:
                    Selenium.foto(self, "Elemento")
                    assert select == True, f"Error, No se limpio el checkbox, el valor seleccioando es {select}"

                cargarDoc = Selenium.check_visibility_element_located(self, "Area de carga documentos")
                if cargarDoc == False:
                    Selenium.foto(self, "Elemento")
                    assert cargarDoc == True, "El elemento ya no se encuentra despues de haber ejecutado la carga"
                valueLoad = Selenium.get_elements(self, "Area de carga documentos").get_attribute("value")
                if not valueLoad == None:
                    Selenium.foto(self, "Elemento")
                    assert valueLoad == None, f"Error, No se limpio el input, el valor seleccioando es {valueLoad}"

                etiquetas = Selenium.check_visibility_element_located(self, "Etiquetas")
                if etiquetas == False:
                    Selenium.foto(self, "Elemento")
                    assert etiquetas == True, "El elemento ya no se encuentra despues de haber ejecutado la carga"

                limpiar = Selenium.check_visibility_element_located(self, "Limpiar")
                if limpiar == False:
                    Selenium.foto(self, "Elemento")
                    assert limpiar == True, "El elemento ya no se encuentra despues de haber ejecutado la carga"
                enableLimpiar = Selenium.get_elements(self, "Limpiar").is_enabled()
                if enableLimpiar == False:
                    Selenium.foto(self, "Elemento")
                    assert enableLimpiar == True, "El elemento esta bloqueado despues de haber ejecutado la carga"

                cargar = Selenium.check_visibility_element_located(self, "Cargar")
                if cargar == False:
                    Selenium.foto(self, "Elemento")
                    assert cargar == True, "El elemento ya no se encuentra despues de haber presionado el boton cancelar"
                enableCargar = Selenium.get_elements(self, "Limpiar").is_enabled()
                if enableCargar == False:
                    Selenium.foto(self, "Elemento")
                    assert enableCargar == True, "El elemento esta bloqueado despues de haber ejecutado la carga"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))