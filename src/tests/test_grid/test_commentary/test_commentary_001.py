# -*- coding: utf-8 -*-
import os
import unittest
from datetime import time
import time
import allure
import pytest
from src.functions.functions import Functions as Selenium
import HtmlTestRunner
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

@allure.feature(u'Comentarios de los documentos')
@allure.testcase(u'Comentarios y Attachments', u'https://api-ux.atlassian.net/browse/ALMA-48')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere validar los comentarios en un documento: </br>
Validación:</br>
Comentar un comentario</br>
Estado del input y el button comentario</br>
Adjuntar archivos</br>
Estado de los elementos en general</br>
Caracteres especiales</br>
Visibilidad del div al ingresar un nuevo comentario</br>
Visualizar area de comentarios</br>
</br></br>""")

class test_commentary_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            date = Selenium.textDateEnvironmentReplace(self, "hoy")
            id = Selenium.generate_id(length=3)
            self.comentario = f"Comentario generado por Selenium {date + ' id' +id}"
            self.caracterEspecial = f"Prueba caracteres_especiales{id}! # $ % & ' ( ) * +, -. / 0 1 2 3 4 5 6 7 8 9 :;= ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z |  ~ ñ Ñ Á á ´ °. -_ , ;"

    @allure.title(u'Botón comentarios.')
    @allure.story(u'Comprobar que "Comentarios" tiene que sea visible.')
    def test_boton_comentarios_001(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.direccionar_a_comentarios(self)
            Selenium.get_json_file(self, "comentarios")

        with allure.step(u'PASO 3 : Visualizar botón "Comentarios"'):
            visibilidad = Selenium.check_visibility_element_located(self, "boton Comentarios")
            Selenium.foto(self, "Visibilidad del boton 'Comentarios'")
            self.assertTrue(visibilidad, "Error, no se visualiza ningun boton de 'Comentarios'")

    @allure.title(u'Botón comentarios.')
    @allure.story(u'Comprobar que "Comentarios" sea clickable.')
    def test_boton_comentarios_002(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.direccionar_a_comentarios(self)
            Selenium.get_json_file(self, "comentarios")
        with allure.step(u'PASO 3 : Clickear botón "Comentarios"'):
            click = Selenium.check_click_element(self, "boton Comentarios")
            Selenium.foto(self, "Click en comentarios")
            self.assertTrue(click, "Error, El boton de 'Comentarios' no es clickable")

    @allure.title(u'Área de comentarios.')
    @allure.story(u'Comprobar visualizacion y estado de los elementos en el area de comentarios.')
    def test_status_element(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nom_folder = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Area de comentarios'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                if x == 1:
                    Selenium.foto(self, "Comentarios")
                Selenium.get_json_file(self, "comentarios")
                Selenium.esperar_elemento(self, "boton Comentarios")
                Selenium.get_elements(self, "boton Comentarios").click()

                Selenium.check_element(self, "Boton ingresar comentario")
                Selenium.check_element(self, "Input")

                Selenium.foto(self, "Elementos de comentarios")
                self.assertTrue(Selenium.esperar_elemento(self, "Input"), "ERROR, El input no es clickable")
                self.assertFalse(Selenium.get_elements(self, "Boton ingresar comentario").is_enabled(), "ERROR, El boton de comentar esta habilitado")
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nom_folder}')]").click()

    @allure.title(u'Escribir un comentario.')
    @allure.story(u'Validar que se ingresa correctamente un comentario.')
    def test_escribir_comentario(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Escribir un comentario'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                Selenium.get_json_file(self, "comentarios")
                Selenium.get_elements(self, "boton Comentarios").click()
                while False:
                    Selenium.check_visibility_element_located(self, "Boton ingresar comentario")
                time.sleep(1) #Obligatorio
                Selenium.send_key_text(self, "Input", self.comentario)
                Selenium.get_elements(self, "Boton ingresar comentario").click()

                Selenium.foto(self, "Comentario de selenium")
                assert True == Selenium.check_exists_by_xpath(self,f"//span[contains(text(),'{self.comentario}')]") , "Error, no se encuentra ningun comentario agregado anteriormente"

                if x == 1:
                    Selenium.foto(self, "Selector de carpetas")
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.title(u'Adjuntar')
    @allure.story(u'Adjuntar un archivo al comentario.')
    def test_adjuntar_archivo(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nom_folder = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Escribir un comentario'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                Selenium.get_json_file(self, "comentarios")
                Selenium.get_elements(self, "boton Comentarios").click()
                while False:
                    Selenium.check_visibility_element_located(self, "Boton ingresar comentario")
                time.sleep(1)  # Obligatory
                Selenium.send_key_text(self, "Input", self.comentario)
                file = Selenium.random_file(self)
                type = Selenium.split(self, file, ".")
                Selenium.get_elements(self, "Adjuntar archivo").send_keys(Selenium.basedir + f"\\file\\.{type[1]}\\" + str(file))
                Selenium.foto(self, "Adjuntar documento")
                Selenium.get_elements(self, "Boton ingresar comentario").click()
                Selenium.foto(self, "Adjuntar documento")
                assert Selenium.check_exists_by_xpath(self, f"//*[text()[contains(.,'{file}')]]"), "Error, no se encuentra ningun archivo adjunto agregado anteriormente"
                if x == 1:
                    Selenium.foto(self, "Selector de carpetas")
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nom_folder}')]").click()

    @allure.title(u'Comentarios')
    @allure.story(u'Visualizar caracteres especiales.')
    def test_caracteres_especiales(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.get_signin_administrator(self)
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 3 : Escribir un comentario con caracteres especiales'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()
                Selenium.get_json_file(self, "comentarios")
                Selenium.get_elements(self, "boton Comentarios").click()
                while False:
                    Selenium.check_visibility_element_located(self, "Boton ingresar comentario")
                time.sleep(1)  # Obligatorio
                Selenium.send_key_text(self, "Input", self.caracterEspecial)
                Selenium.get_elements(self, "Boton ingresar comentario").click()

                Selenium.foto(self, "Comentario de selenium")
                comentario = Selenium.split(self, self.caracterEspecial, "!")
                valor = self.driver.find_element_by_xpath(f"//span[contains(text(),'{comentario[0]}')]").text
                self.assertNotIn("�" , valor,  "El comentario no muestra uno mas caracteres especiales")
                if x == 1:
                    Selenium.foto(self, "Selector de carpetas")
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))