# -*- coding: utf-8 -*-
import random
import unittest
from datetime import time
import time
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Pruebas de navegar entre carpetas')
@allure.testcase(u'Historia de usuario moverse entre carpetas', u'jira')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere validar el ingresar en una carpeta: </br>
Validación:</br>
Ingresar a a una carpeta</br>
Invisibilidad de todo mensaje de error</br>
Carpeta clickable</br>
</br></br>""")

class test_tree_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.story(u'Test. Entrar en las carpetas.')
    def test_001(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "tree")
        with allure.step(u'PASO 3 : Clickear primera carpeta'):
            carpetas = self.driver.find_elements_by_xpath("//p[@style='font-family: Poppins; font-size: 14px; font-weight: 400; padding: 4px 30px 8px 0px;']")
            for carpeta in range(len(carpetas)):
                carpeta+=1
            condition = False
            while condition == False:
                n = random.randint(1, carpeta)
                xpath = f"//body/div[@id='app-site']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/div[{n}]/li[1]/div[1]/div[2]/div[1]/p[1]"
                self.driver.find_element_by_xpath(xpath).click()
                Selenium.get_json_file(self, "tree")
                if Selenium.check_element(self, "comprobar tbody") == True:
                    print("'" + self.driver.find_element_by_xpath(xpath).text + "'" + " si tiene directorios")
                    return self.driver.find_element_by_xpath(xpath).text
                    condition == True
                    break

                print("'" + self.driver.find_element_by_xpath(xpath).text + "'" + " no tiene directorios")
                condition == False

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
