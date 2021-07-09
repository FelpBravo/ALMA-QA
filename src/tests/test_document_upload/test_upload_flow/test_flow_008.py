# -*- coding: utf-8 -*-
import random
import time
import unittest
import allure
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Carga de documentos')
@allure.testcase(u'[Flujo carga Doc] Cuadro de resumen')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""validaciones: </br>
Validar boton 'Confirmar' en el cuadro de resumen</br></br>""")

class test_flow_008(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.dataRoles = ['felipe.bravo', 'juan.suaza', 'dvalero84', 'nadia.gallardo'] #USUARIOS PARA EL FLUJO
            self.dataComentario = ['Hola necesitamos que en conjunto pongamos mas de nuestra parte', 'No tengo ningun comentario',
                                   'Por favor poner ojo con esto', 'Te asigne un par de días', 'Necesito aprobación de esto lo antes posible',
                                   'Estamos haciendo unas pruebas', 'Estos son test', 'Comentarios de pruebas', 'Es necesario aprobar esto ahora',
                                   'Genial aprobación']

    @allure.title(u'Cuadro de resumen')
    @allure.story(u'Mostrar el boton cancelar, probar funcionalidad del boton cancelar.')
    def test_button(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            usuario = ['juan.suaza', 'nadia.gallardo', 'felipe.bravo', 'dvalero84'] #USUARIOS PARA INICIAR SESIÓN
            nomUser = random.choice(usuario) ###########################################################################
            Selenium.get_signin_administrator(self, nomUser) #Cambiar el usuario colocar alguno diferente del admin

        with allure.step(u'PASO 3 : Rellenar formulario'):
            names = Selenium.carga_doc_controlado(self)
            names

        with allure.step(u'PASO 4 : Realizar el llenado y validaciones.'):
            Selenium.get_json_file(self, "flujoCargaDocumento")
            campos = ['Input nombre', 'Input dias', 'Input comentario']
            roles = ['owner', 'coAutor', 'Stakeholder', 'Reviewed', 'Approved', 'released']
            for x in range(6):
                x += 1
                Selenium.check_element(self, f"button {x}")
                Selenium.check_visibility_element_located(self, f"button {x}")
                self.driver.execute_script('arguments[0].scrollIntoView(true);', Selenium.get_elements(self, f"button {x}"))
                if 1 < x < 6:
                    Selenium.check_visibility_element_located(self, f"button {x}")
                    Selenium.get_elements(self, f"button {x}").click()
                    if x == 6:
                        Selenium.foto(self, "Botones")

            for a in range(6):
                for b in range(3):
                    check = Selenium.check_element(self, campos[b] + " " + roles[a])
                    assert check, f"Error, no se encontro el {campos[b]}" f"{roles[a]}"
                    if 0 <= a <= 5 and not b == 2:
                        Selenium.get_elements(self, 'Button Siguiente').click()
                        check = Selenium.check_exists_by_xpath(self, "//p[contains(text(), 'Campo requerido')]")
                        if not check:
                            Selenium.foto(self, "Campos requeridos")
                            assert check, f"Error el campo {campos[b]} {roles[a]}, no tiene la validacion 'Campos requeridos'"
                    if b == 0:
                        rol = random.choice(self.dataRoles)
                        if b == 0 and a == 0:
                            while rol == nomUser:
                                rol = random.choice(self.dataRoles)
                        Selenium.get_elements(self, campos[b] + " " + roles[a]).send_keys(rol)
                        time.sleep(0.5)
                        Selenium.send_especific_keys(self, campos[b] + " " + roles[a], "Enter")
                    if b == 1:
                        Selenium.get_elements(self, campos[b] + " " + roles[a]).send_keys(random.randint(1,99))
                    if b == 2:
                        Selenium.get_elements(self, campos[b] + " " + roles[a]).send_keys(random.choice(self.dataComentario))
            Selenium.get_elements(self, "textbox").send_keys(random.choice(self.dataComentario))
            enabled = Selenium.get_elements(self, 'Button Siguiente').is_enabled()
            if not enabled:
                Selenium.foto(self, "Boton siguiente bloqueado")
                assert enabled, "El boton siguiente al parecer esta bloqueado"
            time.sleep(99*99)#####################################################################
            Selenium.get_elements(self, 'Button Siguiente').click()
            resumen = Selenium.check_visibility_element_located(self, "modal resumen")
            Selenium.foto(self, "Modal resumen")
            assert resumen, "Error, el modal de resumen no se encuentra visualizado"

            check = Selenium.check_element(self, "confirmar")
            visi = Selenium.check_visibility_element_located(self, "confirmar")
            enabled = Selenium.get_elements(self, "confirmar").is_enabled()

            if not check:
                Selenium.foto(self, "Boton")
                assert check, "Error, el boton confirmar no existe"
            if not visi:
                Selenium.foto(self, "Boton")
                assert visi, "Error, el boton confirmar no es visible"
            if not enabled:
                Selenium.foto(self, "Boton")
                assert enabled, "Error, el boton confirmar esta bloqueado"

            Selenium.get_elements(self, "confirmar").click()

            #############VALIDANDO MODAL CON EL ALMA ID###############
            h2 = "//h2[@id='swal2-title']"
            ul = "//div[@id='swal2-content']"
            element1 = Selenium.check_exists_by_xpath(self, h2)
            element2 = Selenium.check_exists_by_xpath(self, ul)
            button = Selenium.check_element(self, "button Ok")
            if not element1:
                Selenium.foto(self, "modal")
                assert element1 == True, "Error, el mensaje del modal 'Solicitud enviada' no existe"
            if not element2:
                Selenium.foto(self, "modal")
                assert element2 == True, "Error, el ID en el modal al parecer no es visible"
            if not button:
                Selenium.foto(self, "modal")
                assert button == True, "Error, el boton 'Ok' confirmar no esta en el modal"

            time.sleep(2)
            Selenium.foto(self, "Modal resumen")
            assert 'Solicitud enviada' == self.driver.find_element_by_xpath(h2).text, "ERROR, el mensaje de 'Solicitud enviada' ya no es igual"

            ul = self.driver.find_element_by_xpath(ul).text
            id = Selenium.split(self, ul, " ")

            if not len(id) == 3:
                Selenium.foto(self, "ID")
                assert len(id) == 3, "Error falta un parametro"
            if id[2].isdigit():
                True
            else:
                Selenium.foto(self, "id")
                assert id[2].isdigit() == True, "ERROR, EL ID NO SE HA MOSTRADO"
                False

            enalbed = Selenium.get_elements(self, "button Ok").is_enabled()
            if enalbed == False:
                Selenium.foto(self, "modal de solicitud enviada")
                assert enalbed == True, "Error, el boton esta bloqueado"

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))