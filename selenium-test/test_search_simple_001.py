# -*- coding: utf-8 -*-
import time
import HtmlTestRunner
import unittest
import pytest
import random
from src.functions.functions import Functions as Selenium
from src.pages.login import Login
from src.pages.dashboard import Dashboard

class test_search_simple_001(Selenium, unittest.TestCase):

    def setUp(self):
        cursor = Selenium.pyodbc_query(self, "SELECT * FROM public.company_tag ORDER BY id ASC")
        Selenium.open_browser(self, navegador="CHROME")
        Selenium.get_json_file(self, "login")
        self.dateCreation = Selenium.textDateEnvironmentReplace(self, "semana pasada")
        self.dateUntil = Selenium.textDateEnvironmentReplace(self, "hoy")

    def test_search_by_date(self):
        Selenium.send_key_text(self, "Usuario", "admin")
        Selenium.send_key_text(self, "Password", "Alma2021")
        Selenium.captura_pantalla(self)
        #Selenium.get_elements(self, "Password").send_keys("Alma2021")
        ######CREAR DICCIONARIOS CON CLAVE Y UNA PALABRA EN REPRESENTACION DEL VALOR###
        #Selenium.save_variable_scenary(self, "UsuarioEmail", "Usuario")
        #Selenium.save_variable_scenary(self, "UsuarioPass", "Password")
        ######IMPRIMIR EL VALOR DE UNA CLAVE DEL DICCIONARIO#####
        #textoDicc = Selenium.get_variable_scenary(self, "Usuario")
        #print(textoDicc)
        #Selenium.send_key_text(self, "Usuario", textoDicc)
        Selenium.get_elements(self, "Boton acceder").click()
        i = 0
        while i < 3:
            i = i + 1
            Selenium._xpath_element(self, Dashboard.but_search_advanzed_xpath).click()
            time.sleep(1)
            getTextForm = Selenium.xpath_element(self, Dashboard.search_form_xpath).text
            self.assertIn("fecha", getTextForm, "ERROR, no se encuentra el campo de fechas")
            Selenium.xpath_element(self, Dashboard.date_create_in_xpath).send_keys(self.dateCreation)
            while i == 1:
                Selenium.xpath_element(self, Dashboard.but_search_xpath).click()
                getTextError = Selenium.xpath_element(self, Dashboard.mesaje_error_xpath).text
                path = Selenium.captura_pantalla(self)
                print(path)
                self.assertIn("Debe seleccionar un filtro", getTextError, "ERROR, no aparece mensaje para rellenar todos los campos")
                Selenium.xpath_element(self, Dashboard.ok_mesaje_error_xpath).click()
                break
            Selenium.xpath_element(self, Dashboard.date_until_in_xpath).send_keys(self.dateUntil)
            time.sleep(3)
            Selenium._xpath_element(self, Dashboard.but_search_xpath).click()
            Selenium._xpath_element(self, Dashboard.but_save_search_xpath).click()
            getTextnameSearch = Selenium.xpath_element(self, Dashboard.mesaje_name_search_xpath).text
            self.assertIn("Asigna un nombre a tu búsqueda avanzada", getTextnameSearch)
            n = random.randint(1, 100)
            Selenium.xpath_element(self, Dashboard.name_search_date_xpath).send_keys(f"Test Date QA{n}")
            if i == 1:
                validSave1 = f"Test Date QA{n}"
            if i == 2:
                validSave2 = f"Test Date QA{n}"
            if i == 3:
                validSave3 = f"Test Date QA{n}"
            Selenium.xpath_element(self, Dashboard.but_save_name_xpath).click()
        Selenium._xpath_element(self, Dashboard.my_search_saved_xpath).click()
        listado = Selenium.xpath_element(self, Dashboard.my_search_saved_list_xpath).text
        getList1 = listado.split("\n")
        assert getList1[2] == validSave1, "El nombre de busqueda guardada no es igual al que se muestra"
        assert getList1[1] == validSave2, "El nombre de busqueda guardada no es igual al que se muestra"
        assert getList1[0] == validSave3, "El nombre de busqueda guardada no es igual al que se muestra"
        assert "Biblioteca-Apiux" == self.driver.title, "Error el titulo no es igual"

    def test_search_save_recent(self):
        Selenium.xpath_element(self, Login.username_xpath).send_keys("admin")
        Selenium.xpath_element(self, Login.password_xpath).send_keys("Alma2021")
        Selenium.xpath_element(self, Login.but_ok_xpath).click()
        time.sleep(1)
        Selenium.xpath_element(self, Dashboard.my_search_saved_xpath).click() #PROBLEMA  SI NO LIMPIO CACHE AQUÍ NO FUNCIONA
        listado = Selenium.xpath_element(self, Dashboard.my_search_saved_list_xpath).text
        getList1 = listado.split("\n")
        count = 0
        for list1 in getList1:
            assert getList1[count] == list1, "Error, Las listas no coinciden"
            count = count + 1
            Selenium._xpath_element(self, f"//div[contains(text(),'{list1}')]").click()
            Selenium._xpath_element(self, Dashboard.but_search_xpath).click()
            table = Selenium._xpath_element(self, Dashboard.table_list_xpath).text
            tableSplit = table.split(" ")
            self.assertIn(self.dateCreation , tableSplit , "Error de validacion, la fecha no se encuentre en la pagina")
            Selenium._xpath_element(self, Dashboard.my_search_saved_xpath).click()
            assert count < 4 , "ERROR"
        assert "Biblioteca-Apiux" == self.driver.title, "Error el titulo no es igual"

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
