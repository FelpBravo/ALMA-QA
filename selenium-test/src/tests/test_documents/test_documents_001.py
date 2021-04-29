# -*- coding: utf-8 -*-
import unittest
from datetime import time
import time
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Pruebas Carga de documentos 001')
@allure.testcase(u'Historia de usuario Carga de documentos', u'https://api-ux.atlassian.net/jira/software/projects/ALMA/boards/224?selectedIssue=ALMA-224')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere validar la carga de documentos: </br>
Validación:</br>
Estado de botones</br>
Refrescar la pagina al cargar un documento</br>
Seguir el flujo habitual al cargar un documento</br>
Obtener AlamaID y el nombre del documento cargado</br>
Campos requeridos</br>
Previsualizacion documentos</br>
Borrar documento precargado</br>
Validacion de funcionalidades de cada elemento de esta página</br>
</br></br>""")

class test_documents_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.story(u'Test buscar la carga de documentos en el árbol.')
    def test_mostrar_arbol_cargar_documento(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Juan Suaza'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "documents")
        with allure.step(u'PASO 3 : Buscar la carga de documentos en el arbol'):
            Selenium.check_visibility_element_located(self, "Arbol carga documentos")
            text = Selenium.get_text(self, "Arbol carga documentos")
            Selenium.captura(self, "Arbol 'Carga documentos'")
            Selenium.captura_pantalla(self)
            self.assertEqual(text, "Carga documentos", "Error, Los textos comparados no coindicen")

    @allure.story(u'Test Cargar documento siguiendo el flujo habitual.')
    def test_carga_exitosa_documento(self):

        with allure.step(u'PASO 2 : Ingresar con el usuario Juan Suaza'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "documents")
            Selenium.esperar_elemento(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()

        with allure.step(u'PASO 3 : Seleccionar carpeta'):
            Selenium.esperar_elemento(self, "Seleccionar carpeta")
            Selenium.get_elements(self, "Seleccionar carpeta").click()
            Selenium.selecionar_primera_carpeta(self)

        with allure.step(u'PASO 4 : Seleccionar ICD/NoICD'):
            Selenium.get_elements(self, "Seleccionar ICD/NO").click()
            Selenium.get_elements(self, "Opcion NoICD").click()


        with allure.step(u'PASO 5 : Subir un documento y comprobar previsualización'):
            Selenium.subir_documento(self)
            Selenium.rellenar_formulario(self)

        with allure.step(u'PASO 6 : Relllenar formulario'):
            Selenium.seleccionar_etiqueta(self)
            Selenium.esperar_elemento(self, "Boton cargar documento")
            time.sleep(3)

        with allure.step(u'PASO 7 : Confirmar la carga de documentos'):
            Selenium.get_elements(self, "Boton cargar documento").click()
            Selenium.get_elements(self, "Boton confirmar cargar documento").click()

        with allure.step(u'PASO 8 : Validar el mensaje de éxito'):
            Selenium.captura(self, "Resultado al presionar boton 'Cargar'")
            Selenium.captura_pantalla(self)
            Selenium.assert_msj_carga_exitosa(self)
            Selenium.get_elements(self, "Error boton OK").click()

        with allure.step(u'PASO 9 : Refrescar la pagina una vez se carga un documento'):
            Selenium.captura(self, "Validación de actualizar 'Carga de documentos'..")
            Selenium.captura_pantalla(self)
            self.assertTrue(Selenium.check_visibility_element_located(self, "Seleccionar carpeta"), "Error, La seleccion de 'carpetas' no se visualiza")
            self.assertTrue(Selenium.check_visibility_element_located(self, "Seleccionar ICD/NO"), "Error, La seleccion de 'ICD/NoICD' no se visualiza")
            self.assertTrue(Selenium.check_visibility_element_located(self, "Boton Limpiar cargar documento"), "Error, El boton 'limpiar' no se visualiza")
            self.assertTrue(Selenium.check_visibility_element_located(self, "Checkbox etiquetas"), "Error, El boton 'cargar' no se visualiza")
            self.assertFalse(Selenium.check_visibility_element_located(self, "Esperar nombre documento en previsualizacion"), "Error, No se limpia la previsualización del documento")

    @allure.story(u'Test previsualizar un documento.')
    def test_prev_documento(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Juan Suaza'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "documents")
        with allure.step(u'PASO 3 : Ingresar a la carga de documentos'):
            Selenium.esperar_elemento(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()
        with allure.step(u'PASO 4 : Validar documento precargado'):
            Selenium.subir_documento(self)
        with allure.step(u'PASO 5 : Ingresar y validar la previsualización del documento'):
            Selenium.get_elements(self, "Seleccionar previsualizacion").click()
            visible = Selenium.check_visibility_element_located(self, "Espacio de previsualizacion")
            Selenium.captura(self, "Previsualicación del documento'")
            Selenium.captura_pantalla(self)
            self.assertTrue(visible, "Error, no se persive la previsualizacion del documento")
            Selenium.assert_prev_documento(self)

    @allure.story(u'Test boton limpiar.')
    def test_boton_limpiar(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Juan Suaza'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "documents")
        with allure.step(u'PASO 3 : Ingresar a la carga de documentos'):
            Selenium.esperar_elemento(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()
        with allure.step(u'PASO 3 : Rellenado solo las etiquetas, hacer click en el boton limpiar'):
            Selenium.esperar_elemento(self, "Boton Limpiar cargar documento")
            Selenium.seleccionar_etiqueta(self)
            Selenium.get_elements(self, "Boton Limpiar cargar documento").click()
        with allure.step(u'PASO 4 : Validar el resultado del boton limpiar'):
            Selenium.captura(self, "Accion del boton LIMPIAR campos")
            Selenium.captura_pantalla(self)
            Selenium.seleccionar_etiqueta(self)
            self.assertTrue(Selenium.check_visibility_element_located(self, "Seleccionar carpeta"), "Error, La seleccion de carpetas no se visualiza")
            self.assertTrue(Selenium.check_visibility_element_located(self, "Seleccionar ICD/NO"), "Error, La seleccion de ICD/NoICD no se visualiza")

    @allure.story(u'Test Boton cargar, sobre campos requeridos.')
    def test_boton_cargar_campos_requeridos(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Juan Suaza'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "documents")
        with allure.step(u'PASO 3 : Ingresar a la carga de documentos'):
            Selenium.esperar_elemento(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()
            Selenium.captura(self, "Carga de documentos")
            Selenium.captura_pantalla(self)
        with allure.step(u'PASO 4 : Validar estado del boton cargar, con campos vacios y rellenados'):
            self.assertFalse(Selenium.check_click_element(self, "Boton cargar documento"), "Error, campos requerido estan vacios, mientras que el boton 'CARGAR' permanece como habilitado")
            while Selenium.check_click_element(self,"Boton cargar documento") == False:
                Selenium.esperar_elemento(self, "Seleccionar carpeta")
                Selenium.get_elements(self, "Seleccionar carpeta").click()
                Selenium.selecionar_primera_carpeta(self)
                Selenium.get_elements(self, "Seleccionar ICD/NO").click()
                Selenium.get_elements(self, "Opcion NoICD").click()
                Selenium.subir_documento(self)
                Selenium.rellenar_formulario_campos_requeridos(self)
        with allure.step(u'PASO 5 : Validar estado del boton cargar solo con campos requeridos'):
            Selenium.scroll_final_pagina(self, "Boton cargar documento")
            Selenium.captura(self, "Carga de documentos")
            Selenium.captura_pantalla(self)
            self.assertTrue(Selenium.check_click_element(self,"Boton cargar documento"), "Error, se rellenaron campos requerido y el boton 'CARGAR' permanece bloqueado")
            Selenium.esperar_elemento(self, "Boton cargar documento")
            Selenium.get_elements(self, "Boton cargar documento").click()

    @allure.story(u'Test Borrar documento previsualizado.')
    def test_borrar_documento_previsualizado(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Juan Suaza'):
            Selenium.get_signin_juan_suaza(self)
            Selenium.get_json_file(self, "documents")
        with allure.step(u'PASO 3 : Ingresar a la carga de documentos'):
            Selenium.esperar_elemento(self, "Arbol carga documentos")
            Selenium.get_elements(self, "Arbol carga documentos").click()
        with allure.step(u'PASO 3 : Precargar un documento y borrarlo'):
            Selenium.subir_documento(self)
            Selenium.captura(self, "Documento precargado")
            Selenium.captura_pantalla(self)
        with allure.step(u'PASO 4 : Validar que el documento no permanesca en la carga de documentos'):
            Selenium.get_elements(self, "Borrar documento precargado").click()
            Selenium.assert_eliminar_documento_previsualizado(self)
            Selenium.captura(self, "Documento precargado eliminado")
            Selenium.captura_pantalla(self)

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
