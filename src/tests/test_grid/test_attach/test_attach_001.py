# -*- coding: utf-8 -*-

import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner


@allure.feature(u'Adjuntar archivos')
@allure.testcase(u'Comentarios y Attachments', u'https://api-ux.atlassian.net/browse/ALMA-48')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Adjuntar documentos</br>
Validaciones de botones</br>
Vista esperada esperada</br>
Visualizar imagen del documento</br>
Titulo esperado</br>
</br></br>""")
class test_attach_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Botón Documentos Adjuntos')
    @allure.story(u'Validaciones del botón (Documentos Adjuntos).')
    def test_attach_001(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Validaciones'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                Selenium.get_json_file(self, "attach")
                if x == 1:
                    Selenium.foto(self, "Boton")

                check = Selenium.check_element(self, "documentos adjuntos")
                if not check:
                    Selenium.foto(self, "checkeando elemento")
                    assert True == check, "ERROR, NO SE ENCUENTRA EL ELEMENTO"

                click = Selenium.check_click_element(self, "documentos adjuntos")
                if not click:
                    Selenium.foto(self, "checkeando elemento")
                    assert True == click, "ERROR, EL ELEMENTO NO ES CLICKABLE"

                enabled = Selenium.get_elements(self, "documentos adjuntos").is_enabled()
                if not enabled:
                    Selenium.foto(self, "checkeando elemento")
                    assert True == enabled, "ERROR, EL ELEMENTO ESTA DESHABILITADO"

                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.title(u'Botón Documentos Adjuntos')
    @allure.story(u'Comprobar que el elemento (Documentos adjuntos) redireccione al area de adjuntos.')
    def test_attach_002(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Validaciones'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                Selenium.get_json_file(self, "attach")
                Selenium.get_elements(self, "documentos adjuntos").click()
                if x == 1:
                    Selenium.foto(self, "Botones")

                vis0 = Selenium.check_visibility_element_located(self, "documentos adjuntos")
                if not vis0:
                    Selenium.foto(self, "documentos adjuntos")
                    assert True == vis0, "ERROR, NO SE VISUALIZA EL ELEMENTO 'documentos adjuntos'"

                check0 = Selenium.check_element(self, "informacion general")
                vis1 = Selenium.check_visibility_element_located(self, "informacion general")
                if vis1 == False or check0 == False:
                    Selenium.foto(self, "informacion general")
                    assert True == check0, "ERROR, NO SE ENCUENTRA EL ELEMENTO 'informacion general'"
                    assert True == vis1, "ERROR, NO SE VISUALIZA EL ELEMENTO 'informacion general'"

                check1 = Selenium.check_element(self, "comentarios")
                vis2 = Selenium.check_visibility_element_located(self, "comentarios")
                if vis2 == False or check1 == False:
                    Selenium.foto(self, "comentarios")
                    assert True == check0, "ERROR, NO SE ENCUENTRA EL ELEMENTO 'comentarios'"
                    assert True == vis2, "ERROR, NO SE VISUALIZA EL ELEMENTO 'comentarios'"

                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.title(u'Botón Adjuntar')
    @allure.story(u'Comprobar que el estado, visibilidad y nombre botón (ADJUNTAR).')
    def test_attach_003(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Validaciones'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                Selenium.get_json_file(self, "attach")
                Selenium.get_elements(self, "documentos adjuntos").click()
                if x == 1:
                    Selenium.foto(self, "Botones")

                check = Selenium.check_element(self, "adjuntar")
                if check == False:
                    Selenium.foto(self, "adjuntar")
                    assert True == check, "ERROR, NO SE ENCUENTRA EL ELEMENTO 'adjuntar'"

                checkXpath = Selenium.check_exists_by_xpath(self, "//span[contains(text(), 'Adjuntar')]")
                if checkXpath == True:
                    text = self.driver.find_element_by_xpath("//span[contains(text(), 'Adjuntar')]").text
                    if not text == "ADJUNTAR":
                        Selenium.foto(self, "adjuntar")
                        assert "ADJUNTAR" == text, "ERROR, EL NOMBRE DEL BOTON 'Adjuntar' YA NO COINCIDE, HA CAMBIADO"

                if checkXpath == False:
                    Selenium.foto(self, "adjuntar")
                    assert True == checkXpath, "ERROR, NO SE ENCUENTRA EL ELEMENTO 'adjuntar'"

                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.title(u'Titulo Información general')
    @allure.story(u'Comprobar que el titulo información general no desaparesca al entrar en Documentos adjuntos.')
    def test_attach_004(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nom_folder = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Validaciones'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                Selenium.get_json_file(self, "attach")
                Selenium.get_elements(self, "documentos adjuntos").click()
                if x == 1:
                    Selenium.foto(self, "Botones")

                check_xpath = Selenium.check_exists_by_xpath(self, "//h3[contains(text(), 'Informacion Documento')]")
                if check_xpath:
                    text = self.driver.find_element_by_xpath("//h3[contains(text(), 'Informacion Documento')]").text
                    Selenium.foto(self, "Informacion Documento")
                    self.assertIn("Informacion Documento", text,
                                  "ERROR, EL NOMBRE DEL TITULO 'Informacion Documento' YA NO COINCIDE, HA CAMBIADO")
                if not check_xpath:
                    Selenium.foto(self, "Informacion Documento")
                assert check_xpath, "ERROR, NO SE ENCUENTRA EL ELEMENTO DEL TITULO 'Informacion Documento'"

                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nom_folder}')]").click()

    @allure.title(u'Imagen del documento')
    @allure.story(u'Comprobar que la imagen del documento no desaparesca al entrar en Documentos adjuntos.')
    def test_attach_005(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Validaciones'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                Selenium.get_json_file(self, "attach")
                Selenium.get_elements(self, "documentos adjuntos").click()
                if x == 1:
                    Selenium.foto(self, "Botones")

                check = Selenium.check_element(self, "imagen documento")
                if check == False:
                    Selenium.foto(self, "Informacion Documento")
                    assert "Informacion Documento" == True, "ERROR, EL NOMBRE DEL TITULO 'Informacion Documento' YA NO COINCIDE, HA CAMBIADO"

                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
