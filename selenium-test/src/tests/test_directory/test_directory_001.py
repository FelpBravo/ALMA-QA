# -*- coding: utf-8 -*-
import unittest
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

class test_directory_001(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.open_browser(self, navegador="CHROME")

    def test_workspace_correcto(self):
        Selenium.get_signin_juan_suaza(self)
        nomWork = Selenium.directorio_random(self)
        nomForum = f"{nomWork} Forum"
        nomFolder = f"{nomWork} Folder"

        Selenium.get_json_file(self, "directoriosj")
        Selenium.get_elements(self, "Boton Adminis").click()
        Selenium.esperar_elemento(self, "Crear Workspace")
        Selenium.get_elements(self, "Crear Workspace").click()
        Selenium.send_key_text(self, "Nombre Work", nomWork)
        Selenium.get_elements(self, "Tipo espacio").click()
        Selenium.get_elements(self, "Tipo Workspace").click()
        Selenium.get_elements(self, "Boton guardar").click()
        Selenium.captura(self, "Pagina Workspace")
        Selenium.captura_pantalla(self)
        Selenium.esperar_elemento(self, "Tabla Workspace")
        textNomPerfil = Selenium.get_elements(self, "Tabla Workspace").text
        self.assertIn(nomWork, textNomPerfil, "ERROR, no son similares")

        self.driver.find_element_by_xpath(f"//th[normalize-space()='{nomWork}']").click()  # Seleccionar Work
        Selenium.esperar_elemento(self, "Crear Forum")
        Selenium.get_elements(self, "Crear Forum").click()
        Selenium.send_key_text(self, "Nombre forum", nomForum)
        Selenium.get_elements(self, "Tipo espacio2").click()
        Selenium.get_elements(self, "Tipo forum").click()
        Selenium.get_elements(self, "Guardar forum").click()
        Selenium.captura(self, "Pagina Forum")
        Selenium.captura_pantalla(self)
        Selenium.esperar_elemento(self, "Tabla Forum")
        textNomPerfil2 = Selenium.get_elements(self, "Tabla Forum").text
        self.assertIn(nomForum, textNomPerfil2, "ERROR, no son similares")

        self.driver.find_element_by_xpath(f"//th[normalize-space()='{nomForum}']").click()  # Seleccionar Work
        Selenium.get_elements(self, "Crear Folder").click()
        Selenium.send_key_text(self, "Nombre folder", nomFolder)
        Selenium.get_elements(self, "Tipo espacio3").click()
        Selenium.get_elements(self, "Tipo folder").click()
        Selenium.get_elements(self, "Guardar folder").click()
        Selenium.captura(self, "Pagina Folder")
        Selenium.captura_pantalla(self)
        Selenium.esperar_elemento(self, "Tabla Folder")
        textNomPerfil3 = Selenium.get_elements(self, "Tabla Folder").text
        self.assertIn(nomFolder, textNomPerfil3, "ERROR, no son similares")

    def test_borrar_correcto(self):
        Selenium.get_signin_juan_suaza(self)
        Selenium.get_json_file(self, "directoriosj")
        Selenium.get_elements(self, "Boton Adminis").click()
        Selenium.get_elements(self, "BtnEliminar Workspace").click()
        Selenium.get_elements(self, "BtnConfirmar Workspace").click()
        #text1 = self.driver.find_element_by_xpath(f"//th[normalize-space()='{nomWork1}']").location
        #print("Posicion:", text1)

    def test_edit_correcto(self):
        Selenium.get_signin_juan_suaza(self)
        nomWork2 = f"Nuevo {Selenium.directorio_random(self)}"
        Selenium.get_json_file(self, "directoriosj")
        Selenium.get_elements(self, "Boton Adminis").click()
        Selenium.get_elements(self, "Edit Workspace").click()
        Selenium.get_elements(self, "CampoEdit Workspace").clear()
        Selenium.send_key_text(self, "CampoEdit Workspace", nomWork2)
        Selenium.get_elements(self, "CampoGuardar Workspace").click()
        #text1 = self.driver.find_element_by_xpath(f"//th[normalize-space()='{nomWork1}']").location
        #print("Posicion:", text1)

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
