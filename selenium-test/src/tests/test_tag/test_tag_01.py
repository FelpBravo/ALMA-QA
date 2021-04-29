# -*- coding: utf-8 -*-
import unittest
from src.functions.functions import Functions as Selenium
import HtmlTestRunner
from test_login_001 import test_login_001
from tests.test_login.test_signin import test_signin


class test_tag_01(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.open_browser(self, navegador="CHROME")

    def test_tag_correcto(self):
        Selenium.get_signin_juan_suaza(self)
        nomTag = Selenium.etiqueta_random(self)

        Selenium.get_json_file(self, "tags")
        Selenium.get_elements(self, "Boton Tags").click()
        for i in range(1):
            Selenium.esperar_elemento(self, "Crear Tag")
            Selenium.get_elements(self, "Crear Tag").click()
            Selenium.send_key_text(self, "Nombre Tag", nomTag)
            Selenium.get_elements(self, "Color Etiqueta").click()
            Selenium.get_elements(self, "Btn Guardar").click()
            Selenium.captura(self, "Pagina Etiquetas")
            Selenium.captura_pantalla(self)
            Selenium.esperar_elemento(self, "Tabla etiquetas")
            textNomPerfil = Selenium.get_elements(self, "Tabla etiquetas").text
            self.assertIn(nomTag, textNomPerfil, "ERROR, no son similares")



    def test_tag_eliminar_correcto(self):
        Selenium.get_signin_juan_suaza(self)
        Selenium.get_json_file(self, "tags")
        Selenium.get_elements(self, "Boton Tags").click()

        for i in range(2):
            n= i+1
            borrar = self.driver.find_element_by_xpath(f"//tbody/tr[{n}]/td[1]/div[1]/div[2]/*[1]")
            Selenium.get_elements(self, borrar).click()
            Selenium.captura_pantalla(self)
            Selenium.esperar_elemento(self, "Tabla etiquetas")


    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
