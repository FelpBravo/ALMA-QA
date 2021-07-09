# -*- coding: utf-8 -*-
import unittest
from datetime import time
import time
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Compartir documentos- Acceso público')
@allure.testcase(u'Se necesita compartir documentos con acceso público a externos.', u'https://api-ux.atlassian.net/jira/software/projects/ALMA/boards/224?selectedIssue=ALMA-26')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Dado que necesito compartir documentos a externos a ALMA: </br>
El sistema debe tener la capacidad de compartir documento vía acceso tipo GUEST o publico (sin credenciales).</br>
El sistema debe proporcionar la capacidad de otorgar a los documentos relevantes del grupo de trabajo un acceso público a las partes interesadas externas. El sistema deberá poder compartir una URL para compartir el puntero a un documento dentro del sistema con los permisos adecuados evidencia de capacidad de compartir documento via URL - generar link para compartir documento, con permiso de lectura con fecha de caducación, clave de acceso y permiso de impresión.</br>
Invisibilidad de todo mensaje de error</br>
Carpeta clickable</br>
</br></br>""")

class test_share_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.dateUntil = Selenium.textDateEnvironmentReplace(self, "hoy")
            self.password = "1234"

    @allure.title(u'Botón compartir.')
    @allure.story(u'Comprobar estado y funcionalidad del boton compartir.')
    def test_boton_compartir(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Clickear primera carpeta'):
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 4 : Clickear compartir documento'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/*[5]").click()

                Selenium.get_json_file(self, "compartir")
                self.assertTrue(Selenium.check_element(self, "Compartir"), "Compartir documento no es clickable")
                Selenium.esperar_elemento(self, "Compartir")
                self.driver.execute_script("arguments[0].click()", Selenium.get_elements(self, "Compartir"))

                Selenium.foto(self, "Visibilidad del área compartir documento")
                check = Selenium.check_element(self, "Nombre documento en compartir")
                self.assertTrue(check, "Compartir documento no es visible")

                if x == 1:
                    Selenium.foto(self, "Grilla, boton compartir")
                Selenium.get_json_file(self, "compartir")
                Selenium.get_elements(self, "Boton cancelar").click()

                Selenium.get_json_file(self, "tree")
                Selenium.esperar_elemento(self, "carpetas")
                self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]"))

    @allure.title(u'Botón compartir.')
    @allure.story(u'Comprobar estado y visibilidad de los elementos.')
    def test_visibilidad_elementos(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresar a una carpeta con archivos'):
            Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.get_json_file(self, "compartir")
            Selenium.check_element(self, "Ingresar a compartir")
            Selenium.get_elements(self, "Ingresar a compartir").click()
            Selenium.esperar_elemento(self, "Compartir")
            self.driver.execute_script("arguments[0].click()", Selenium.get_elements(self, "Compartir"))

        with allure.step(u'PASO 4 : Validando checkbox, fecha y campo password'):
            Selenium.foto(self, "Validando checkbox, campo fecha y password")
            fechaElem = Selenium.check_visibility_element_located(self, "Campo fecha")
            self.assertTrue(fechaElem, "Error, el campo de fecha no es visible")

            passElem = Selenium.check_click_element(self, "Campo password")
            checkboxElem = Selenium.get_elements(self, "checkbox").is_selected()
            if checkboxElem == True:
                self.assertTrue(passElem, "Error, el checkbox esta habilitado y el campo de password esta bloqueado")
            else:
                self.assertTrue(checkboxElem, "Error, el checkbox no es clickable")

        with allure.step(u'PASO 5 : Validando estado del boton Crear'):
            Selenium.foto(self, "Validar estado del boton")
            self.assertFalse(Selenium.get_elements(self, "Boton crear").is_enabled(), "Error, el boton está habilitado y los campos aun no han sido rellenados")

        with allure.step(u'PASO 6 : Validando congruencia entre checkbox y campo password'):
            Selenium.get_elements(self, "checkbox").click()
            Selenium.foto(self, "Validando checkbox y el campo password")
            passElem = Selenium.get_elements(self, "Campo password").is_enabled()
            self.assertFalse(passElem, "Error, el campo password está habilitado y el checkbox esta marcado para no ingresar password")

        with allure.step(u'PASO 7 : Finalizando'):
            Selenium.get_elements(self, "checkbox").click()
            Selenium.send_key_text(self, "Campo fecha", self.dateUntil)
            Selenium.send_key_text(self, "Campo password", self.password)
            Selenium.foto(self, "Validando boton 'Crear'")

    @allure.title(u'Visualizar enlace.')
    @allure.story(u'Visibilidad y generación del enlace.')
    def test_visibilidad_generar_enlace(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresar a una carpeta con archivos'):
            Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.get_json_file(self, "compartir")
            Selenium.get_elements(self, "Ingresar a compartir").click()
            Selenium.esperar_elemento(self, "Compartir")
            self.driver.execute_script("arguments[0].click()", Selenium.get_elements(self, "Compartir"))

        with allure.step(u'PASO 4 : Validando invisibilidad del enlace'):
            Selenium.foto(self, "Invisibilidad del enlace")
            enlaceFalse = Selenium.check_element(self, "Enlace")
            self.assertFalse(enlaceFalse, "ERROR, El enlace se ha mostrado y aun no se rellenan los campos")

        with allure.step(u'PASO 5 : Rellenar campos y comprobar visibilidad del enlace'):
            Selenium.send_key_text(self, "Campo fecha", self.dateUntil)
            Selenium.send_key_text(self, "Campo password", self.password)
            Selenium.get_elements(self, "Boton crear").click()
            Selenium.foto(self, "Visibilidad Enlace")
            check = Selenium.check_element(self, "Enlace")
            visual = Selenium.check_visibility_element_located(self, "Enlace")

            self.assertTrue(check, "ERROR, El enlace no se encuentra en el modal")
            self.assertTrue(visual, "ERROR, El enlace no se ha mostrado y se rellenaron todos los campos correctamente")

    @allure.title(u'Nombre de documento y enlace.')
    @allure.story(u'Congruencia del nombre de documento entre enlaces.')
    def test_congruencia_enlace(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma y generar un enlace con password'):
            Selenium.direccionar_crear_enlace_password(self)

        with allure.step(u'PASO 3 : Guardar nombre del archivo'):
            Selenium.foto(self, "Nombre del archivo")
            compartir = Selenium.get_text(self, "Nombre documento en compartir")
            comp = compartir.split("\n")

        with allure.step(u'PASO 4 : Ingresando al enlace'):
            Selenium.swith_to_windows_name(self, "Biblioteca")
            Selenium.new_window(self, Selenium.generar_enlace(self))
            Selenium.swith_to_windows_name(self, "Enlace")
            Selenium.foto(self, "Ingreso al enlace generado")
            enlace = Selenium.get_text(self, "Nombre documento en enlace")
            enl = enlace.split(" ")
        with allure.step(u'PASO 5 : Validando congruencia de nombre'):
            Selenium.foto(self, "Nombres entre enlace y grilla")
            self.assertIn(enl[0], comp[1], "Error, Los nombre de los documentos no son iguales")

    @allure.title(u'Generacion enlace.')
    @allure.story(u'Visibilidad y generación del enlace.')
    def test_password_en_enlace(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma y generar un enlace con password'):
            Selenium.direccionar_crear_enlace_password(self)
            Selenium.swith_to_windows_name(self, "Biblioteca")

        with allure.step(u'PASO 3 : Ingresando al enlace'):
            Selenium.new_window(self, Selenium.generar_enlace(self))
            Selenium.swith_to_windows_name(self, "Enlace")
            passwordClick = Selenium.check_click_element(self, "Campo password enlace")

        with allure.step(u'PASO 4 : Validando estado del campo password'):
            Selenium.foto(self, "Campo de password")
            self.assertTrue(passwordClick, "Error, el campo para ingresar la password esta bloqueado")
            Selenium.get_elements(self, "Campo password enlace").send_keys(self.password)

    @allure.title(u'Enlace.')
    @allure.story(u'Estado y funcionalidad del boton principal en el enlace.')
    def test_boton_enviar_en_enlace(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma y generar un enlace con password'):
            Selenium.direccionar_crear_enlace_password(self)
            Selenium.swith_to_windows_name(self, "Biblioteca")

        with allure.step(u'PASO 3 : Ingresando al enlace'):
            Selenium.new_window(self, Selenium.generar_enlace(self))
            Selenium.swith_to_windows_name(self, "Enlace")
            Selenium.get_elements(self, "Campo password enlace").send_keys(self.password)

        with allure.step(u'PASO 4 : Ingresando al enlace'):
            Selenium.foto(self, "Boton Enviar")
            botonEnviar = Selenium.check_click_element(self, "Boton enviar al ingresar password")
            self.assertTrue(botonEnviar, "Error, el boton Enviar está bloqueado")

    @allure.title(u'Nombre del documento en enlace.')
    @allure.story(u'Congruencia del documento en el enlace vs el documento en la grilla.')
    def test_documento_enlace(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma y generar un enlace con password'):
            Selenium.direccionar_crear_enlace_password(self)
            Selenium.swith_to_windows_name(self, "Biblioteca")

            compartir = Selenium.get_text(self, "Nombre documento en compartir")
            comp = compartir.split("\n")

        with allure.step(u'PASO 3 : Ingresar a la plataforma y generar un enlace con password'):
            Selenium.new_window(self, Selenium.generar_enlace(self))
            Selenium.swith_to_windows_name(self, "Enlace")
            Selenium.get_elements(self, "Campo password enlace").send_keys(self.password)
            Selenium.get_elements(self, "Boton enviar al ingresar password").click()

        with allure.step(u'PASO 4 : Validando nombre documento'):
            Selenium.foto(self, "Nombre documento")
            nombreDocu = Selenium.get_text(self, "nombre documento en enlace descarga")
            self.assertIn(nombreDocu ,comp , "Error, Los nombre de los documentos no coinciden")

    @allure.title(u'Botón descargar.')
    @allure.story(u'Comprobar funcionalidad y estado del boton Descargar.')
    def test_descargar_documento_enlace(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma y generar un enlace con password'):
            Selenium.direccionar_crear_enlace_password(self)
            Selenium.swith_to_windows_name(self, "Biblioteca")
            Selenium.new_window(self, Selenium.generar_enlace(self))
            Selenium.swith_to_windows_name(self, "Enlace")

        with allure.step(u'PASO 3 : Rellenando campos'):
            Selenium.get_elements(self, "Campo password enlace").send_keys(self.password)
            Selenium.get_elements(self, "Boton enviar al ingresar password").click()

        with allure.step(u'PASO 4 : Validando boton descargar'):
            Selenium.foto(self, "Boton descargar")
            descargar = Selenium.check_click_element(self, "Boton descargar documento")
            self.assertTrue(descargar, "ERROR. El boton descargar no es clickable")

    @allure.title(u'Descargar documento.')
    @allure.story(u'Validar descarga y nombre del documento descargado.')
    def test_validar_descargar_documento(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma y generar un enlace con password'):
            Selenium.direccionar_crear_enlace_password(self)
            Selenium.swith_to_windows_name(self, "Biblioteca")
            compartir = Selenium.get_text(self, "Nombre documento en compartir")
            comp = compartir.split("\n")

        with allure.step(u'PASO 3 : Redireccionando al enlace'):
            Selenium.new_window(self, Selenium.generar_enlace(self))
            Selenium.swith_to_windows_name(self, "Enlace")

        with allure.step(u'PASO 4 : Rellenando campos'):
            Selenium.get_elements(self, "Campo password enlace").send_keys(self.password)
            Selenium.get_elements(self, "Boton enviar al ingresar password").click()
            Selenium.get_elements(self, "Boton descargar documento").click()

        with allure.step(u'PASO 5 : Validando la descarga y el documento correcto'):
            Selenium.foto(self, "Descargar documento")
            self.assertTrue(Selenium.descargar_documento(self, comp[1]), "Error")
            Selenium.borrar_descarga(self, comp[1])

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))