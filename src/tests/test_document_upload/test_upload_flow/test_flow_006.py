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
Al rellenar la segunda pantalla y clickar sobre el boton 'SIGUIENTE', deberia de aparecer un cuadro de resumen,
el cual contenga toda la informacion anteriormente ingresada. Validar la informacion que aparece en el cuadro de resumen 
</br></br>""")

class test_flow_006(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.dataRoles = ['felipe.bravo', 'juan.suaza', 'dvalero84', 'nadia.gallardo'] #USUARIOS PARA EL FLUJO
            self.dataComentario = ['Hola necesitamos que en conjunto pongamos mas de nuestra parte', 'No tengo ningun comentario',
                                   'Por favor poner ojo con esto', 'Te asigne un par de días', 'Necesito aprobación de esto lo antes posible',
                                   'Estamos haciendo unas pruebas', 'Estos son test', 'Comentarios de pruebas', 'Es necesario aprobar esto ahora',
                                   'Genial aprobación']

    @allure.title(u'Cuadro de resumen')
    @allure.story(u'Validar nombres, roles, nombre del archivo, fecha, etc.')
    def test_resumen(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            usuario = ['juan.suaza', 'nadia.gallardo', 'felipe.bravo', 'dvalero84'] #USUARIOS PARA INICIAR SESIÓN
            nomUser = random.choice(usuario)
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
                if x > 1 and x < 6:
                    Selenium.check_visibility_element_located(self, f"button {x}")
                    Selenium.get_elements(self, f"button {x}").click()
                    if x == 6:
                        Selenium.foto(self, "Botones")

            for a in range(6):
                for b in range(3):
                    check = Selenium.check_element(self, campos[b] + " " + roles[a])
                    assert check == True, f"Error, no se encontro el {campos[b]}" f"{roles[a]}"
                    if a >= 0 and a <= 5 and not b == 2:
                        Selenium.get_elements(self, 'Button Siguiente').click()
                        check = Selenium.check_exists_by_xpath(self, "//p[contains(text(), 'Campo requerido')]")
                        if check == False:
                            Selenium.foto(self, "Campos requeridos")
                            assert check == True, f"Error el campo {campos[b]} {roles[a]}, no tiene la validacion 'Campos requeridos'"
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
            if enabled == False:
                Selenium.foto(self, "Boton siguiente bloqueado")
                assert enabled == True, "El boton siguiente al parecer esta bloqueado"
            Selenium.get_elements(self, 'Button Siguiente').click()

            data = []
            for a in range(6):
                for b in range(3):
                    Selenium.check_element(self, campos[b] + " " + roles[a])
                    if b == 0:
                        data.append(roles[a])
                        value = Selenium.get_elements(self, campos[b] + " " + roles[a]).get_attribute("value")
                        data.append(value)
                    if b == 1:
                        valu = Selenium.get_elements(self, campos[b] + " " + roles[a]).get_attribute("value")
                        data.append(valu + " días")
                    if b == 2:
                        value = Selenium.get_elements(self, campos[b] + " " + roles[a]).get_attribute("value")
                        data.append(value)

            xpath1 = "//*[@id='body']/div[2]/div[3]/div/div[2]/div[1]/div/div/table/tbody/tr/td"  #PRIMERA TABLA DEL CUADRO DE RESUMEN
            check1 = Selenium.check_exists_by_xpath(self, xpath1)
            if check1 == False:
                Selenium.foto(self, "tabla")
                assert check1 == True, "No se encuentra la tabla de informacion"
            elements1 = self.driver.find_elements_by_xpath(xpath1)
            for td in range(len(elements1)):
                td += 1
                element = self.driver.find_element_by_xpath(f"//*[@id='body']/div[2]/div[3]/div/div[2]/div[1]/div/div/table/tbody/tr/td[{str(td)}]").text
                if td == 1:
                    self.assertIn(element, names[0], f"Error los elementos no coinciden con el valor ingresado='{names[0]}'")
                if td == 2:
                    self.assertIn(element, ("/"+names[1]), f"Error los elementos no coinciden con el valor ingresado='{names[1]}'")
                if td == 3:
                    if not element == Selenium.textDateEnvironmentReplace(self, "hoy"):
                        Selenium.foto(self, "foto")
                        assert element == Selenium.textDateEnvironmentReplace(self, "hoy"), "La fecha no es igual a la ingresada"
                if td == 4:
                    if not element == usuario:
                        Selenium.foto(self, "foto")
                        assert element == nomUser, "El usuario no es el mismo con el cual se esta ingresando"
                if td == 5:
                    if not element == "1.0":
                        Selenium.foto(self, "foto")
                        assert element == "1.0", f"La version ya es la numero = {element}"

            xpath2 = "//*[@id='body']/div[2]/div[3]/div/div[2]/div[2]/div/div/table/tbody/tr"
            check2 = Selenium.check_exists_by_xpath(self, xpath2)
            if not check2:
                Selenium.foto(self, "tabla")
                assert check2, "No se encuentra la tabla de informacion"
            elements2 = len(self.driver.find_elements_by_xpath(xpath2))
            dataResumen = []
            for tr in range(elements2):
                tr += 1
                tds = len(self.driver.find_elements_by_xpath(f"//*[@id='body']/div[2]/div[3]/div/div[2]/div[2]/div/div/table/tbody/tr[{str(tr)}]/td"))  #SEGUNDA TABLA DEL CUADRO DE RESUMEN
                for td in range(tds):
                    td += 1
                    info = self.driver.find_element_by_xpath(f"//*[@id='body']/div[2]/div[3]/div/div[2]/div[2]/div/div/table/tbody/tr[{str(tr)}]/td[{str(td)}]").text

                    dataResumen.append(info)

            Selenium.foto(self, "Cuadro de resumen")
            for d in range(len(data)):
                if not dataResumen[d].lower() == data[d].lower():
                    Selenium.foto(self, "Los datos no son iguales")

                    self.assertIn(dataResumen[d].lower(), data[d].lower(), "Los datos visualizados en el cuadro de resumen no son correctos")

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))