# -*- coding: utf-8 -*-
import os
import unittest
from datetime import time
import time
import allure
import pytest
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Comentarios en los documentos')
@allure.testcase(u'Boton de comentarios', u'https://api-ux.atlassian.net/browse/ALMA-283')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones sobre el boton: </br>
Estado</br>
Visibilidad</br>
Bloqueo</br>
</br></br>""")

class test_commentary_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.caracterEspecial = "! # $ % & ' ( ) * +, -. / 0 1 2 3 4 5 6 7 8 9 :;= ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~ "

    @allure.title(u'Test boton con el input vacio.')
    @allure.story(u'Estado del boton al no ingresar ningun comentario.')
    def test_button_001(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.direccionar_a_comentarios(self)
            Selenium.get_json_file(self, "comentarios")

        with allure.step(u'PASO 3 : Ingresar al area de comentarios'):
            Selenium.esperar_elemento(self, "boton Comentarios")
            Selenium.foto(self, "proceso")
            Selenium.get_elements(self, "boton Comentarios").click()

        with allure.step(u'PASO 4 : Obtener elementos del area de comentarios'):
            Selenium.check_element(self, "Boton ingresar comentario")
            estado = Selenium.get_elements(self, "Boton ingresar comentario").is_enabled()
            Selenium.foto(self, "Area de comentarios")
            assert estado == False, "El boton de comentarios esta habilitado, y el input esta vacio"

    @allure.title(u'Test visibilidad del boton.')
    @allure.story(u'visibilidad del boton al ingresar en el area de comentarios.')
    def test_button_002(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.direccionar_a_comentarios(self)
            Selenium.get_json_file(self, "comentarios")

        with allure.step(u'PASO 3 : Ingresar al area de comentarios'):
            Selenium.esperar_elemento(self, "boton Comentarios")
            Selenium.foto(self, "proceso")
            Selenium.get_elements(self, "boton Comentarios").click()

        with allure.step(u'PASO 4 : Obtener elementos del area de comentarios'):
            while True:
                e = Selenium.check_element(self, "Espera")
                if e == False:
                    break
            Selenium.send_key_text(self, "Input", "Selenium test_commentary_002")
            visible = Selenium.check_visibility_element_located(self, "Boton ingresar comentario")
            Selenium.foto(self, "Area de comentarios")
            assert visible == True, "El boton de comentarios no es visible"

    @allure.title(u'Test boton con el input llenado.')
    @allure.story(u'Estado del boton al ingresar un comentario.')
    def test_button_003(self):
        with allure.step(u'PASO 2 : Entrar en la previsualización de un documento'):
            Selenium.direccionar_a_comentarios(self)
            Selenium.get_json_file(self, "comentarios")

        with allure.step(u'PASO 3 : Ingresar al area de comentarios'):
            Selenium.esperar_elemento(self, "boton Comentarios")
            Selenium.foto(self, "proceso")
            Selenium.get_elements(self, "boton Comentarios").click()

        with allure.step(u'PASO 4 : Obtener elementos del area de comentarios'):
            while True:
                e = Selenium.check_element(self, "Espera")
                if e == False:
                    break
            Selenium.send_key_text(self, "Input", "Selenium test_commentary_002")
            estado = Selenium.get_elements(self, "Boton ingresar comentario").is_enabled()
            Selenium.foto(self, "Area de comentarios")
            assert estado == True, "El boton de comentarios esta deshabilitado, y el input esta llenado"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))