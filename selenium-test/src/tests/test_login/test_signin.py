# -*- coding: utf-8 -*-
import unittest
import allure
import pytest
from src.functions.functions import Functions as Selenium
import HtmlTestRunner
import random

@allure.feature(u'Test signin')
@allure.story(u'Se realizan validaciones en el signin al entrar en la biblioteca')
@allure.testcase(u'Historia de usuario ALMA 001', u'aqui pegar la direccion de jira')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere validar el signin: </br>
Validación de campos vacios</br>
Validación del estado de los botones</br>
Validación del titulo de la página de signin</br>
Se trata de ingresar con credenciales similares y erroneas</br>
Se validan los mensajes de error</br>
Validacion de funcionalidades de cada elemento de esta página</br>
</br></br>""")

class test_signin(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    def test_credenciales_correctas(self):
        assert "Biblioteca-Apiux" == self.driver.title, "Error el titulo no es igual"
        Selenium.get_json_file(self, "signin")
        with allure.step(u'PASO 2 : Validar autentificación correcta'):
            Selenium.send_key_text(self, "Usuario", "juan.suaza")
            Selenium.send_key_text(self, "Password", "1234")
            Selenium.captura(self, "Pagina signin")
            Selenium.captura_pantalla(self)
            Selenium.get_elements(self, "Boton acceder").click()
            Selenium.get_json_file(self, "bienvenidaSesion")
            Selenium.captura_pantalla(self)
            Selenium.esperar_elemento(self, "Nombre perfil")
            textNomPerfil = Selenium.get_elements(self, "Nombre perfil").text
            self.assertIn("Juan", textNomPerfil, "ERROR, no son similares")

    def test_credenciales_incorrectas(self):
        r = random.randint(1, 100)
        Selenium.get_json_file(self, "signin")
        with allure.step(u'PASO 3 : Validar autentificación incorrecta'):
            Selenium.send_key_text(self, "Usuario", f"juanito.perez{r}")
            Selenium.send_key_text(self, "Password", f"12{r}43{r}4")
            Selenium.captura_pantalla(self)
            Selenium.get_elements(self, "Boton acceder").click()
            Selenium.esperar_elemento(self, "Msj error credenciales incorrectas")
            Selenium.captura(self, "Mensaje de error de credenciales incorrectas")
            Selenium.captura_pantalla(self)
            msjError = Selenium.check_element(self, "Msj error credenciales incorrectas")
            self.assertTrue(msjError, "ERROR, No se muestra el mensaje 'Usuario y/o contraseña incorrecto'")
            if msjError == True:
                msjErrorText = Selenium.get_text(self, "Msj error credenciales incorrectas")
                self.assertIn("incorrecto", msjErrorText, "No coinciden")
                Selenium.get_elements(self,"Msk error boton OK").click()
            else:
                Selenium.captura(self, "Bienvenida de sesión")
                Selenium.captura_pantalla(self)
                Selenium.get_json_file(self, "bienvenidaSesion")
                inicioSesion = Selenium.check_element(self, "Pagina de inicio")
                self.assertFalse(inicioSesion, "ERROR, se logró iniciar sesion con credenciales erroneas")

    def test_elementos_campo_vacio(self):
        Selenium.get_json_file(self, "signin")
        Selenium.get_select_elements(self, "Usuario")
        Selenium.get_select_elements(self, "Password")
        Selenium.captura_pantalla(self)
        Selenium.captura(self, "Capos vacios (User y password)")
        self.assertFalse(Selenium.get_elements(self, "Boton acceder").is_enabled(), "'BOTON ACCEDER' se encuentra habilitado con campos vacios")
        Selenium.get_select_elements(self, "Usuario").send_keys("admin")
        Selenium.captura_pantalla(self)
        Selenium.captura(self, "Campo contraseña, vacio")
        self.assertFalse(Selenium.get_elements(self, "Boton acceder").is_enabled(), "'BOTON ACCEDER' se encuentra habilitado con campos vacios")
        Selenium.get_select_elements(self, "Usuario").clear()
        Selenium.get_select_elements(self, "Password").send_keys("1234")
        Selenium.captura_pantalla(self)
        Selenium.captura(self, "Boton 'acceder'")
        estadoAcceder = Selenium.get_elements(self, "Boton acceder").is_enabled()
        if estadoAcceder == True:
            Selenium.captura_pantalla(self)
            Selenium.get_elements(self, "Boton acceder").click()


    def test_checkbox(self):
        Selenium.get_json_file(self, "signin")
        Selenium.get_select_elements(self, "Usuario")
        Selenium.get_select_elements(self, "Password")
        textPag = Selenium.get_select_elements(self, "Area Completa").text
        Selenium.captura_pantalla(self)
        Selenium.captura(self, "Checkbox'")
        self.assertIn("Recordar contraseña", textPag, "ERROR, no se visualiza 'Recordar contraseña'")
        if textPag:
            pytest.skip("No se ejecuto la prueba, el elemento 'OLVIDE CONTRASEÑA' no es clickable ni seleccionable")

    def test_pass_olvidada(self):
        Selenium.get_json_file(self, "signin")
        Selenium.get_select_elements(self, "Usuario")
        Selenium.get_select_elements(self, "Password")
        textPag = Selenium.get_select_elements(self, "Area Completa").text
        Selenium.captura_pantalla(self)
        Selenium.captura(self, "Olvide mi contraseña")
        self.assertIn("Olvidé mi contraseña", textPag, "ERROR, no se visualiza 'Olvidé mi contraseña'")
        if textPag:
            pytest.skip("No se ejecuto la prueba, el elemento 'OLVIDE CONTRASEÑA' no es clickable ni seleccionable")

    def test_cerrar_sesion(self):
        Selenium.get_signin_admin(self)
        Selenium.get_json_file(self, "bienvenidaSesion")
        Selenium.esperar_elemento(self, "Boton opciones Perfil")
        Selenium.get_elements(self, "Boton opciones Perfil").click()
        Selenium.esperar_elemento(self, "Boton cerrar sesion")
        Selenium.captura_pantalla(self)
        Selenium.captura(self, "Cerrar sesión")
        self.assertIn("Cerrar", Selenium.get_text(self, "Boton cerrar sesion"), "ERROR, los texto 'Cerrar sesion' no coinciden")
        Selenium.get_elements(self, "Boton cerrar sesion").click()

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))

