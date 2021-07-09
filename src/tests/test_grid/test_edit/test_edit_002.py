# -*- coding: utf-8 -*-
import random
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Editar documento')
@allure.testcase(u'Validando elementos al editar un documento', u'https://api-ux.atlassian.net/browse/ALMA-320')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validar el maximo de caracteres permitidos en la metadata</br>
</br></br>""")

class test_edit_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Campos metadata.')
    @allure.story(u'Validar que el largo maximo de caracteres permitidos en la metadata sea de 100.')
    def test_edit_005(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.foto(self, "Documentos")
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 4 : Validando que no se vean pantallas azules'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(4):
                tr = random.randint(1, len(element))
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{tr}]/td[8]/div[1]/div[3]").click()

                campos = ['Campo modifiedBy', 'Campo ownerName', 'Campo subject', 'Campo fielType',
                          'Campo author', 'Campo control board', 'Campo system', 'Campo secMode',
                          'Campo releaseBy', 'Campo docId', 'Campo forumId', 'Campo approvedBy',
                          'Campo revBy', 'Campo group', 'Campo docAbs']
                caracter100 = [
                    'Es otro de tantos test para comprobar máximo de caracteres permitidos para ingresar en la metadata..',
                    'Haciendo una prueba generada por Selenium para comprobar que le máximo de caracteres sea de "100"...',
                    'Se esta validando haciendo una prueba de unitaria en cada campo de esta metadata para comprobar.....']
                value = []
                for campo in range(15):
                    Selenium.get_json_file(self, "editar")
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
                        assert checkValidate == True, "Error no se encuentra el mensaje de validación"

                    button = Selenium.get_elements(self, "Guardar").is_enabled()
                    if button == True:
                        Selenium.foto(self, "Validacion")
                        assert button == False, "Error el boton 'Guardar' se encuentra habilitado y existen campos con errores."

                    Selenium.get_elements(self, campos[campo]).clear()
                    Selenium.get_elements(self, campos[campo]).send_keys(rdom)

                button = Selenium.get_elements(self, "Guardar").is_enabled()
                if button == False:
                    Selenium.foto(self, "Validacion")
                    assert button == True, "Error el boton 'Guardar' se encuentra deshabilitado y existen campos con errores."
                Selenium.foto(self, "Metadata ingresada")
                Selenium.check_click_element(self, "Guardar")
                Selenium.get_elements(self, "Guardar").click()

                Selenium.check_element(self, "Boton confirmar cargar documento")
                Selenium.get_elements(self, "Boton confirmar cargar documento").click()

                Selenium.check_element(self, "Regresar")
                Selenium.get_elements(self, "Regresar").click()

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))