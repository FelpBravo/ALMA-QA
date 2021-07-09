# -*- coding: utf-8 -*-
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Informacion general del documento')
@allure.testcase(u'Validando elementos en la visualizacion del documento', u'Jira')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones de la información general del documento: </br>
Ingresar a la vizualización del documento</br>
Miga de pan, congruencia</br>
Visualizacion de la imagen del documento</br>
Visualizacion de todos los campos de la metadata</br>
Elementos del menu (Comentarios y Documentos adjuntos)</br>
</br></br>""")

class test_visualize_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.story(u'Miga de pan .')
    @allure.story(u'Validar ruta correcta, comprobando nombre del documento y carpeta.')
    def test_visualize_001(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Validando miga de pan'):
            element = self.driver.find_elements_by_xpath("//tbody/tr") #Esta es la grilla
            for x in range(len(element)):
                x+=1
                nombreDoc = self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[1]").text #Nombre doc en grilla
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click() #Boton VISUALIZAR
                Selenium.get_json_file(self, "breadCrumbs")
                Selenium.check_element(self, "Miga")
                migaPan = Selenium.split(self, Selenium.get_elements(self, "Miga").text, "\n") # 0=dashboar - 2=carpeta - 4=doc

                Selenium.foto(self, "Miga de pan")
                assert migaPan[0] == "Dashboard", "EL noombre(Dashboard) esperado no coincide en la miga de pan"
                assert migaPan[2] == nomCapeta, "EL nombre de la carpeta en el arbol con coincide con el de la miga de pan"
                assert migaPan[4] == nombreDoc, "EL nombre del documento de la miga de pan, no con coincide con el de la grilla"
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.story(u'Visualizar elemento (Información general).')
    @allure.story(u'Validar visualizacion, estado y nombre esperado del elemento (Información general).')
    def test_visualize_002(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Validando todos los campos de metadata de cada uno de los documentos'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()  # Boton VISUALIZAR
                Selenium.get_json_file(self, "breadCrumbs")
                estado = Selenium.esperar_elemento(self, "Informacion general")
                habilitado = Selenium.get_elements(self, "Informacion general").is_enabled()

                Selenium.foto(self, "Informacion general")
                assert estado == True, "Error, el elemento no es visible o no es clickable"
                assert habilitado == True, "Error, el elemento está bloqueado"
                assert "Información General" == Selenium.get_elements(self, "Informacion general").text, "Error, el nombre no coincide con el esperado"
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.story(u'Visualizar metadata.')
    @allure.story(u'Validar visualizacion de todos los campos de la metadata.')
    def test_visualize_003(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Validando todos los campos de metadata de cada uno de los documentos'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                    x += 1
                    Selenium.get_json_file(self, "breadCrumbs")
                    self.driver.find_element_by_xpath(f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()  # Boton VISUALIZAR

                    data = Selenium.split(self, Selenium.get_elements(self, "metadata").text, "\n")
                    self.assertIn("Metadata", data , "Error no se encuentra el campo 'Metadata' en la metadata")
                    self.assertIn("ALMA Doc Number:", data, "Error no se encuentra el campo 'ALMA Doc Number' en la metadata")
                    self.assertIn("Project Code:", data, "Error no se encuentra el campo 'Project Code' en la metadata")
                    self.assertIn("Release Date:", data, "Error no se encuentra el campo 'Release Date' en la metadata")
                    self.assertIn("Modified by:", data, "Error no se encuentra el campo 'Modified by' en la metadata")
                    self.assertIn("Organization:", data, "Error no se encuentra el campo 'Organization' en la metadata")
                    self.assertIn("Owner Name:", data, "Error no se encuentra el campo 'Owner Name' en la metadata")
                    self.assertIn("Subject:", data, "Error no se encuentra el campo 'Subject' en la metadata")
                    self.assertIn("File Type:", data, "Error no se encuentra el campo 'File Type' en la metadata")
                    self.assertIn("Author:", data, "Error no se encuentra el campo 'Author' en la metadata")
                    self.assertIn("Documentation Status:", data, "Error no se encuentra el campo 'Documentation Status' en la metadata")
                    self.assertIn("Configuration Control Board (CCB) flag:", data, "Error no se encuentra el campo 'Configuration Control Board (CCB) flag' en la metadata")
                    self.assertIn("System/Subsystem:", data, "Error no se encuentra el campo 'System/Subsystem' en la metadata")
                    self.assertIn("Security Mode:", data, "Error no se encuentra el campo 'Security Mode' en la metadata")
                    self.assertIn("Released By:", data, "Error no se encuentra el campo 'Released By' en la metadata")
                    self.assertIn("DocID:", data, "Error no se encuentra el campo 'DocID' en la metadata")
                    self.assertIn("Forum ID:", data, "Error no se encuentra el campo 'Forum ID' en la metadata")
                    self.assertIn("Document Type:", data, "Error no se encuentra el campo 'Document Type' en la metadata")
                    self.assertIn("Approved By:", data, "Error no se encuentra el campo 'Approved By' en la metadata")
                    self.assertIn("Reviewed By:", data, "Error no se encuentra el campo 'Reviewed By' en la metadata")
                    self.assertIn("Group/Area:", data, "Error no se encuentra el campo 'Group/Area' en la metadata")
                    self.assertIn("Document Abstract:", data, "Error no se encuentra el campo 'Document Abstract' en la metadata")

                    Selenium.foto(self, "Informacion general")
                    self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.story(u'Visualizar imagen metadata.')
    @allure.story(u'Validar visualizacion y localizacion de la imagen en la metadata.')
    def test_visualize_004(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)
            Selenium.foto(self, "Documentos en la grilla")

        with allure.step(u'PASO 4 : Validando visualizacion de todas las imagenes en la metadata de cada uno de los documentos'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            for x in range(len(element)):
                x += 1
                Selenium.get_json_file(self, "breadCrumbs")
                self.driver.find_element_by_xpath(
                    f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]").click()  # Boton VISUALIZAR

                visualizar = Selenium.check_visibility_element_located(self, "Imagen en metadata")
                Selenium.foto(self, "Imagen en metadata")
                assert visualizar == True, "No se encuentra o no se visualiza la imagen en la metadata del documento"
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.story(u'Visualizar elementos del menu.')
    @allure.story(u'Validar visualizacion y localizacion de los elementos del menu en la metadata (Comentarios y Documentos adjuntos).')
    def test_visualize_005(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)
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
                assert (comentario and docAdjuntos) == True, "No se encuentra o no se visualizan los elementos del menu (Comentarios o Documentos adjuntos)"
                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    @allure.story(u'Boton de visualización .')
    @allure.story(u'Validar existencia y visualizacion del boton de visualización.')
    def test_visualize_006(self):
        with allure.step(u'PASO 2 : Ingresar a la plataforma'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Seleccionar una carpeta'):
            Selenium.foto(self, "Documentos en la grilla")
            nomCapeta = Selenium.comprobar_carpeta_con_archivos(self)

        with allure.step(u'PASO 4 : Validando visualización y existencia'):
            element = self.driver.find_elements_by_xpath("//tbody/tr")  # Esta es la grilla
            Selenium.foto(self, "Documentos en la grilla")
            for x in range(len(element)):
                x += 1

                exist = Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]")
                assert exist == True, "No existe el boton de visualización"

                visual = Selenium.check_visibility_by_xpath(self, f"//tbody/tr[{str(x)}]/td[8]/div[1]/div[1]")
                assert visual == True, "No se visualiza el boton de visualización"

                self.driver.find_element_by_xpath(f"//p[contains(text(),'{nomCapeta}')]").click()

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
