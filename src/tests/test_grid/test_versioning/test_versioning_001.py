# -*- coding: utf-8 -*-
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner


@allure.feature(u'Versionamiento')
@allure.testcase(u'Validando elementos en el versionamiento del documento', u'Jira')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones sobre el versionamiento: </br>
Elementos del menu (Comentarios y Documentos adjuntos)</br>
</br></br>""")
class test_versioning_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.story(u'Boton de versionamiento .')
    @allure.story(u'Validar existencia y visualizacion del boton de versionamiento.')
    def test_versioning_001(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.foto(self, "Documentos en la grilla")
            Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 4 : Validando visualización y existencia'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1

                exist = Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[4]")
                assert exist == True, "No existe el boton de versionamiento"

                visual = Selenium.check_visibility_by_xpath(self, f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[4]")
                assert visual == True, "No se visualiza el boton de versionamiento"

                Selenium.comprobar_carpeta_con_archivos(self)

    @allure.story(u'Miga de pan.')
    @allure.story(u'Validar ruta correcta, comprobando nombre del documento y carpeta.')
    def test_versioning_002(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Validando miga de pan'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                nombreDoc = self.driver.find_element_by_xpath(
                    f"//tbody/tr[{str(x)}]/td[1]").text  # Nombre doc en grilla
                self.driver.find_element_by_xpath(
                    f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[4]").click()  # Boton VISUALIZAR
                Selenium.get_json_file(self, "versioning")
                Selenium.check_element(self, "Miga")
                migaPan = Selenium.split(self, Selenium.get_elements(self, "Miga").text,
                                         "\n")  # 0=dashboar - 2=carpeta - 4=doc

                Selenium.foto(self, "Miga de pan")
                assert migaPan[0] == "Dashboard", "EL noombre(Dashboard) esperado no coincide en la miga de pan"
                assert migaPan[
                           2] == nomCapeta, "EL nombre de la carpeta en el arbol con coincide con el de la miga de pan"
                assert migaPan[
                           4] == nombreDoc, "EL nombre del documento de la miga de pan, no con coincide con el de la grilla"
                Selenium.comprobar_carpeta_con_archivos(self)

    @allure.story(u'Titulo versionamiento.')
    @allure.story(u'Validar visualizacion y nombre esperado del titulo en el versionamiento.')
    def test_versioning_003(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Validando titulos del versionamiento'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(
                    f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[4]").click()  # Boton VISUALIZAR
                Selenium.get_json_file(self, "versioning")
                if x < 3 :
                    Selenium.foto(self, "Titulo esperado")
                assert Selenium.esperar_elemento(self, "titulo") == True, "No se localiza o no se encuentra el elemento del titulo"

                titulo = Selenium.get_elements(self, "titulo")
                assert "Historial de versionamiento" == titulo.text, "Error, el titulo no coincide con el esperado"

                Selenium.comprobar_carpeta_con_archivos(self)

    @allure.story(u'Visualizar grilla con documentos.')
    @allure.story(u'Validaciones versiones mostradas, versus el numero de versiones.')
    def test_versioning_004(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Validando todos los campos de metadata de cada uno de los documentos'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                Selenium.get_json_file(self, "breadCrumbs")
                version = self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[6]").text
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[4]").click()  # Boton VISUALIZAR

                versiones = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla del versionamiento
                for ver in range(len(versiones)):
                    ver += 1
                if version.is_integer():
                    print(ver, version)
                #Selenium.foto(self, "Informacion general")
                Selenium.comprobar_carpeta_con_archivos(self)
    #####################################################################################################

    @allure.story(u'Visualizar imagen metadata.')
    @allure.story(u'Validar visualizacion y localizacion de la imagen en la metadata.')
    def test_visualize_004(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(
                u'PASO 4 : Validando visualizacion de todas las imagenes en la metadata de cada uno de los documentos'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                Selenium.get_json_file(self, "breadCrumbs")
                self.driver.find_element_by_xpath(
                    f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()  # Boton VISUALIZAR

                visualizar = Selenium.check_visibility_element_located(self, "Imagen en metadata")
                Selenium.foto(self, "Imagen en metadata")
                assert visualizar == True, "No se encuentra o no se visualiza la imagen en la metadata del documento"
                Selenium.comprobar_carpeta_con_archivos(self)

    @allure.story(u'Visualizar elementos del menu.')
    @allure.story(
        u'Validar visualizacion y localizacion de los elementos del menu en la metadata (Comentarios y Documentos adjuntos).')
    def test_visualize_005(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(
                u'PASO 4 : Validando visualizacion de los elementos del menu'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                Selenium.get_json_file(self, "breadCrumbs")
                self.driver.find_element_by_xpath(
                    f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()  # Boton VISUALIZAR

                comentario = Selenium.check_visibility_element_located(self, "Comentarios")
                docAdjuntos = Selenium.check_visibility_element_located(self, "Documentos adjuntos")
                Selenium.foto(self, "visualizar menu")
                assert (
                               comentario and docAdjuntos) == True, "No se encuentra o no se visualizan los elementos del menu (Comentarios o Documentos adjuntos)"
                Selenium.comprobar_carpeta_con_archivos(self)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
