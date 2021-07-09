# -*- coding: utf-8 -*-
import random
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Descargar')
@allure.testcase(u'Comprobar la descarga de un conjunto de documentos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Comprobar boton de descarga</br>
Modal de descarga</br>
Botones del modal</br>
</br></br>""")
class test_download_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.story(u'Boton descargar.')
    @allure.story(u'Encontrar el boton de DESCARGAR en todos los documentos de la grilla.')
    def test_button_001(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Visualizar el boton de DESCARGA en todos los documentos de la grilla'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                check = Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[2]")
                if check == False:
                    Selenium.foto(self, "Error botón de descarga")
                    assert True == check, "El boton de descarga no se encuentra en la grilla."

    @allure.story(u'Modal.')
    @allure.story(u'Pulsar el boton DESCARGAR y visualizar el modal con sus elementos correctos.')
    def test_button_002(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Visualizar elementos del modal'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[2]").click()
                if x == 1:
                    Selenium.foto(self, "Botón de descarga")
                elements = ['h2 Descargar', 'div pregunta', 'OK', 'Cancel']
                waited = ['Descargar','¿Está seguro que quiere descargar el documento?']
                for e in range(len(elements)):
                    Selenium.get_json_file(self, "download")
                    check = Selenium.check_element(self, elements[e])
                    visual = Selenium.check_visibility_element_located(self, elements[e])
                    if e == 0 or e ==1:
                        text = Selenium.get_elements(self, elements[e]).text
                        if not text == waited[e]:
                            Selenium.foto(self, "Texto esperado")
                            assert text == waited[e], f"NO ES IGUAL, El texto esperado : {waited[e]} , El texto actual {text}"
                    if check == False:
                        Selenium.foto(self, "No se encuentra")
                        assert check == True, f"ERROR, no se encentra el elemento {elements[e]}"
                    if visual == False:
                        Selenium.foto(self, "No se encuentra")
                        assert visual == True, f"ERROR, no se encentra el elemento {elements[e]}"
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.story(u'Botones.')
    @allure.story(u'Pulsar el boton DESCARGAR, visualizar el modal y comprobar el estado de los botones.')
    def test_button_003(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Validando botones del modal'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[2]").click()
                if x == 1:
                    Selenium.foto(self, "Botón de descarga")
                elements = ['OK', 'Cancel']
                for e in range(len(elements)):
                    Selenium.get_json_file(self, "download")
                    Selenium.check_element(self, elements[e])
                    enabled = Selenium.get_elements(self, elements[e]).is_enabled()
                    if enabled == False:
                        Selenium.foto(self, "Elemento bloqueado")
                        assert enabled == True, f"ERROR, El elemento {elements[e]} , esta bloqueado"
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.story(u'Boton Cancelar.')
    @allure.story(u'Pulsar el boton DESCARGAR, visualizar el modal y comprobar la funcionalidad del boton Cancelar.')
    def test_button_004(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Validando el botón cancelar'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            elements = ['h2 Descargar', 'div pregunta', 'OK', 'Cancel']
            for x in range(len(element)):
                x += 1
                if x == 3:
                    break
                self.driver.find_element_by_xpath(f"//tbody/tr[{random.randint(x,len(element))}]/td[8]/div[1]/div[2]").click()
                if x == 1:
                    Selenium.foto(self, "Botón de descarga")
                Selenium.get_json_file(self, "download")
                Selenium.get_elements(self, "Cancel").click()
                e = elements[random.randint(0, 3)]
                invisible = Selenium.check_invisibility_element_located(self, e)
                if invisible == False:
                    assert invisible == True, f"El elemento {e} aun se visualiza"


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
