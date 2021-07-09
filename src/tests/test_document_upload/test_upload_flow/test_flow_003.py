# -*- coding: utf-8 -*-
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'[Flujo carga Doc] Elementos')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Cargar todos los elementos habituales'</br>
Nombres de los participantes</br>
Localizar y visualizar botones</br>
Localizar y visualizar inputs</br>
</br></br>""")

class test_flow_003(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Nombre de los roles')
    @allure.story(u'Localizar y visualizar los nombres correcto de los roles')
    def test_rol(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Localizando nombres de los miembros'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            data = {'Owner', 'Co-Author', 'Stakeholder', 'Reviewed', 'Approved', 'Released'}
            h5 = self.driver.find_elements_by_xpath("//h5")
            for roles in h5:
                self.assertIn(roles.text, str(data), f"ERROR, Algo cambio...se encuentra el rol {roles.text}, nunca "
                                                     f"antes visto en la biblioteca")

    @allure.title(u'Validar botones (Agregar)')
    @allure.story(u'Localizar, visualizar y obtener texto de los botones (Agregar)')
    def test_button(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Localizando botones'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            Selenium.foto(self, "Botones")
            for x in range(6):
                x += 1
                check = Selenium.check_element(self, f"button {x}")
                visual = Selenium.check_visibility_element_located(self, f"button {x}")
                assert check == True and visual == True, f"Error, no se encontro o no se visualizo el elemento (button {x})"
                text = Selenium.get_elements(self, f"button {x}")
                assert text.text == "Agregar", "El nombre esperado no coincide con el botón"

    @allure.title(u'Funcionalidad botones (Agregar)')
    @allure.story(u'Localizar, visualizar Div agregados a raiz del boton  (Agregar)')
    def test_agree_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)
        with allure.step(u'PASO 4 : Localizando botones'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            for x in range(6):
                x += 1
                self.driver.execute_script('arguments[0].scrollIntoView(true);', Selenium.get_elements(self, f"button {x}"))
                for click in range(10):
                    Selenium.get_elements(self, f"button {x}").click()
                    a = self.driver.find_element_by_xpath(f"/html/body/div/div/div/div[2]/main/div/div/div/div/div/form/div[1]/div[3]/div/div[2]/div[{x+1}]").is_enabled() #Este es el div que se habre hacia abajo
                    assert True == a , f"Error, no se encontro o no se visualizo el div"
                    basurero2 = Selenium.check_element(self, "basurero 2")
                    if not basurero2 == True:
                        Selenium.foto(self, "Basurero")
                        assert basurero2 == True, "No se visualiza el basurero"
                Selenium.foto(self, "Botones")

    @allure.title(u'Localizar y visualizar Inputs (Selecionar nombre)')
    @allure.story(u'Validar visualizacion y localizacion de inputs (Selecionar nombre)')
    def test_input_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Localizando inputs'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            roles = {'owner', 'released'}
            for rol in roles:
                self.driver.execute_script('arguments[0].scrollIntoView(true);',Selenium.get_elements(self, f"Input nombre {rol}"))
                Selenium.foto(self, "Inputs")
                check = Selenium.check_element(self, f"Input nombre {rol}")
                visual = Selenium.check_visibility_element_located(self, f"Input nombre {rol}")
                assert (check and visual) == True, "No se encontro o no se visualizan los inputs"

    @allure.title(u'Localizar y visualizar Inputs (Plazo en días)')
    @allure.story(u'Validar visualizacion y localizacion de inputs (Plazo en días)')
    def test_input_002(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Localizando inputs'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            roles = {'owner', 'released'}
            for rol in roles:
                self.driver.execute_script('arguments[0].scrollIntoView(true);',
                                           Selenium.get_elements(self, f"Input dias {rol}"))
                Selenium.foto(self, "Inputs")
                check = Selenium.check_element(self, f"Input dias {rol}")
                visual = Selenium.check_visibility_element_located(self, f"Input dias {rol}")
                assert (check and visual) == True, "No se encontro o no se visualizan los inputs"

    @allure.title(u'Localizar y visualizar Inputs (Comentario)')
    @allure.story(u'Validar visualizacion y localizacion de inputs (Comentario)')
    def test_input_003(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Localizando inputs'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            roles = {'owner', 'released'}
            for rol in roles:
                self.driver.execute_script('arguments[0].scrollIntoView(true);',
                                           Selenium.get_elements(self, f"Input comentario {rol}"))
                Selenium.foto(self, "Inputs")
                check = Selenium.check_element(self, f"Input comentario {rol}")
                visual = Selenium.check_visibility_element_located(self, f"Input comentario {rol}")
                assert (check and visual) == True, "No se encontro o no se visualizan los inputs"

    @allure.title(u'Localizar y visualizar area de comentarios')
    @allure.story(u'Validar visualizacion y localizacion del area de comentarios')
    def test_input_004(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Rellenar formulario'):
            Selenium.carga_doc_controlado(self)

        with allure.step(u'PASO 4 : Localizando area de comentarios'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            check = Selenium.check_element(self, "textbox")
            visual = Selenium.check_visibility_element_located(self, "textbox")

            self.driver.execute_script('arguments[0].scrollIntoView(true);',
                                       Selenium.get_elements(self, "textbox"))
            Selenium.foto(self, "Textarea")
            assert (check and visual) == True, "No se encontro el elemento"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))