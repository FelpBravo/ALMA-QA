# -*- coding: utf-8 -*-
import time
import unittest
import allure
import pytest
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Usuarios y grupos')
@allure.testcase(u'Pantalla de usuarios')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validar estado y visualizacion de los diferentes elementos de esta pantalla. </br></br>""")

class test_groups_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Titulo.')
    @allure.story(u'Validar el titulo USUARIOS Y GRUPOS.')
    def test_title(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

            Selenium.get_json_file(self, "groups")
            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()
            check = Selenium.check_element(self, "titulo")
            Selenium.foto(self, "titulo")
            assert check == True, "Error no se encuentra el elemento del titulo 'Usuarios y grupos'"

    @allure.title(u'Botón ADMINISTRACIÓN DE USUARIOS.')
    @allure.story(u'Comprobar el estado y visualizacion del boton al hacer click en ADMINISTRACIÓN DE GRUPOS.')
    def test_button_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")
            check = Selenium.check_element(self, "Adminsitracion de usuarios")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()
            Selenium.foto(self, "Adminsitracion de usuarios")
            assert check == True, "Error, el botón no se encuentra en la pantalla"

            selected = Selenium.get_elements(self, "Adminsitracion de usuarios").get_attribute("aria-selected")
            assert selected == "false", "El botón no se encuentra seleccionado como se esperaba"

            enabled = Selenium.get_elements(self, "Adminsitracion de usuarios").is_enabled()
            assert enabled == True, "El botón no se encuentra habilitado"

            name = Selenium.get_elements(self, "Adminsitracion de usuarios").text
            assert name == "Administración de usuarios", "El nombre del botón ha cambiado, ahora es diferente al esperado"

    @allure.title(u'Input BUSCAR GRUPO.')
    @allure.story(u'Comprobar el estado y visualizacion del input.')
    def test_input_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")

            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            check = Selenium.check_element(self, "input buscar")
            Selenium.foto(self, "Adminsitracion de usuarios")
            assert check == True, "Error no se encuentra el input en la pantalla"

            placeholder = Selenium.get_elements(self, "input buscar").get_attribute("placeholder")
            assert placeholder == "Buscar grupo", "El placeholder del input ha cambiado, ya no es igual"

            enabled = Selenium.get_elements(self, "input buscar").is_enabled()
            assert enabled == True, "El input no se encuentra habilitado"

    @allure.title(u'Botón BUSCAR.')
    @allure.story(u'Comprobar el estado y visualizacion del boton.')
    def test_button_002(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")

            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            check = Selenium.check_element(self, "button buscar")
            Selenium.foto(self, "Adminsitracion de grupos")
            assert check == True, "Error, el botón no se encuentra en la pantalla"

            enabled = Selenium.get_elements(self, "button buscar").is_enabled()
            assert enabled == False, "El botón se encuentra habilitado, este no es un comportamiento esperado"

            name = Selenium.get_elements(self, "button buscar").text
            assert name == "BUSCAR", "El nombre del botón ha cambiado, ahora es diferente al esperado"

    @allure.title(u'Botón CREAR NUEVO GRUPO.')
    @allure.story(u'Comprobar el estado y visualizacion del boton.')
    def test_button_003(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")

            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            check = Selenium.check_element(self, "crear grupo")
            Selenium.foto(self, "Adminsitracion de grupos")
            assert check == True, "Error, el botón no se encuentra en la pantalla"

            enabled = Selenium.get_elements(self, "crear grupo").is_enabled()
            assert enabled == True, "El botón se encuentra deshabilitado, este no es un comportamiento esperado"

            name = Selenium.get_elements(self, "crear grupo").text
            assert name == "Crear nuevo grupo", "El nombre del botón ha cambiado, ahora es diferente al esperado"

    @allure.title(u'Botón ADMINISTRACIÓN DE GRUPOS.')
    @allure.story(u'Comprobar el estado y visualizacion del boton.')
    def test_button_004(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")

            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            check = Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.foto(self, "Adminsitracion de grupos")
            assert check == True, "Error, el botón no se encuentra en la pantalla"

            selected = Selenium.get_elements(self, "Adminsitracion de grupos").get_attribute("aria-selected")
            assert selected == "true", "El botón se encuentra seleccionado 'Adminsitracion de grupos'"

            enabled = Selenium.get_elements(self, "Adminsitracion de grupos").is_enabled()
            assert enabled == True, "El botón no se encuentra habilitado"

            name = Selenium.get_elements(self, "Adminsitracion de grupos").text
            assert name == "Administración de grupos", "El nombre del botón ha cambiado, ahora es diferente al esperado"

    @allure.title(u'Titulo h3.')
    @allure.story(u'Comprobar el titulo GRUPOS sea siempre el mismo.')
    def test_title_h3(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")

            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            check = Selenium.check_element(self, "h3 Grupos")
            Selenium.foto(self, "Adminsitracion de usuarios")
            assert check == True, "Error el titulo 'Resultado usuarios' no se encuentra en la pantalla"

    @allure.title(u'Nombre Columnas Grilla.')
    @allure.story(u'Comprobar que el nombre de la columna de la grilla sea siempre el mismo.')
    def test_table(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")

            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            check = Selenium.check_element(self, "tabla 1")
            Selenium.foto(self, "Tabla")
            assert check == True, "ERROR, No existe la parte de arriba de la tabla (Parte en azul con titulos)"

            columnas = self.driver.find_element_by_xpath("//thead/tr").text
            columna = Selenium.split(self, columnas, " ")
            data = ['Grupos']
            for c in range(len(data)):
                assert columna[c] == data[c], f"Error, El nombre de la columna '{columna[c]}' con la esperada '{data[c]}', ya no son iguales"

    @allure.title(u'Elementos Grilla.')
    @allure.story(u'Comprobar que el nombre de las columnas de la grilla sea siempre el mismo.')
    def test_element_table(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")

            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            consulta = Selenium.pyodbc_query_list(self, "SELECT COUNT(*) FROM public.company_group")
            for valor in consulta:
                if valor == 0:
                    pytest.skip(f"Cantidad de grupos minimos para ejecutar la prueba es de '1', en la base de datos no existen grupos")

            consulta = Selenium.pyodbc_query_list(self, "SELECT name FROM public.company_group")

            data = []
            for con in consulta:
                data.append(con.name)

            check = Selenium.check_exists_by_xpath(self, "//tbody/tr")
            assert check == True, f"En la base de datos existen '{valor}' grupos. Y en la grilla al parecer no hay grupos"


            filas = len(self.driver.find_elements_by_xpath("//tbody/tr"))
            groups = []
            for tr in range(filas):
                tr += 1
                checkButton = Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[1]/*[1]")
                if checkButton == False:
                    Selenium.foto(self, "No existe")
                    assert checkButton == True, "No existe el boton de 'BASURERO' para borrar grupos."

                group = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[1]").text
                groups.append(group)

            for group in groups:
                consulta = Selenium.pyodbc_query_list(self, f"SELECT name FROM public.company_group WHERE name='{group}'")
                if consulta == None:
                    Selenium.foto(self, "No found")
                    assert not consulta == None, f"No se encontro el grupo '{group}' en la base de datos."

    @allure.title(u'Modal CREAR NUEVO GRUPO.')
    @allure.story(u'Comprobar botones y elementos del modal CREAR NUEVO GRUPO.')
    def test_modal_create(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")

            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            Selenium.check_element(self, "crear grupo")
            Selenium.get_elements(self, "crear grupo").click()

            Selenium.foto(self, "Modal")
            visual = Selenium.check_visibility_element_located(self, "Modal crear agregar")
            assert visual == True, "ERROR, No se visualiza el modal de CREAR GRUPOS"

            check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),'Crear nuevo grupo')]")
            assert check == True, "ERROR, El titulo del modal ya no es el mismo, este a cambiado"

            elements = ['dependencia', 'perfiles', 'nombre de grupo', 'categories', 'cancelar', 'crear']

            for i in range(len(elements)):
                if i < 3:
                    value = Selenium.get_elements(self, elements[i]).get_attribute("value")
                    if not value == "":
                        Selenium.foto(self, "error")
                        assert value == "", f"Error, el campo '{elements[i]}', contiene el valor='{value}', y este deberia de estar vacio."

            for i in range(len(elements)):
                check = Selenium.check_element(self, elements[i])

                if check == False:
                    Selenium.foto(self, "No existe")
                    assert check == True, f"ERROR, No se encuentra el elemento '{elements[i]}'"

                if i == 0:
                    xpath = "//body/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[@id='demo-simple-select-outlined']"
                    Selenium.check_exists_by_xpath(self, xpath)
                    self.driver.find_element_by_xpath(xpath).click()
                    dependencias = self.driver.find_elements_by_xpath("//ul[@role='listbox']/li")
                    data = ['APP', 'FINANZAS']
                    s = 0
                    for dependencia in dependencias:
                        dep = dependencia.get_attribute("data-value")
                        if not dep == data[s]:
                            Selenium.foto(self, "dependencia no es igual")
                            assert dep == data[s], f"ERROR, LA DEPENDENCIA '{dep}', YA NO ES IGUAL A LA DEPENDENCIA '{data[s]}'"
                        s += 1
                    self.driver.find_element_by_xpath(f"//ul[@role='listbox']/li[contains(text(),'{dep}')]").click()

                if i == 1:
                    xpath = "//body/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[@id='demo-simple-select-outlined']"
                    Selenium.check_exists_by_xpath(self, xpath)
                    self.driver.find_element_by_xpath(xpath).click()
                    perfiles = self.driver.find_elements_by_xpath("//ul[@role='listbox']/li")
                    consulta = Selenium.pyodbc_query_list(self, 'SELECT name FROM public.profile ')
                    data = []
                    for con in consulta:
                        data.append(con.name)

                    for perfil in perfiles:
                        per = perfil.get_attribute("data-value")
                        self.assertIn(per, data, f"ERROR, El PERFIL DEL MODAL CREAR GRUPO: '{per}' , NO ES IGUAL AL PERFIL DE BASE DE DATOS: '{data}'")
                        s += 1
                    self.driver.find_element_by_xpath(f"//ul[@role='listbox']/li[contains(text(),'{per}')]").click()

                if i == 3:
                    check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),'Crear nuevo grupo')]")
                    assert check == True, "ERROR, El titulo del modal ya no es el mismo, este a cambiado"

                if i == 4 or i == 5:
                    visual = Selenium.check_visibility_element_located(self, elements[i])
                    enabled = Selenium.get_elements(self, elements[i]).is_enabled()
                    text = Selenium.get_elements(self, elements[i]).text
                    if not visual:
                        Selenium.foto(self, "No existe")
                        assert visual, f"ERROR, el boton '{elements[i]}' no se visualiza"
                    if i == 7:
                        if not text == "CANCELAR":
                            Selenium.foto(self, "No es igual")
                            assert text == "CANCELAR", f"ERROR, el nombre del boton '{elements[i]}' no es igual a 'CANCELAR'"
                        if not enabled:
                            Selenium.foto(self, "Esta bloqueado")
                            assert enabled, "Error, al parecer el boton esta deshabilitado y este deberia de estar habilitado"
                    if i == 8:
                        if not text == "CREAR":
                            Selenium.foto(self, "No es igual")
                            assert text == "CREAR", f"ERROR, el nombre del boton '{elements[i]}' no es igual a 'CREAR'"
                        if enabled:
                            Selenium.foto(self, "Esta bloqueado")
                            assert enabled == False, "Error, al parecer el boton esta habilitado, y este deberia de estar deshabilitado"

    @allure.title(u'Modal AGREGAR USUARIO.')
    @allure.story(u'Comprobar botones y elementos del modal AGREGAR USUARIO.')
    def test_modal_agree(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")
            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            consulta = Selenium.pyodbc_query_list(self, "SELECT COUNT(*) FROM public.company_group")
            for valor in consulta:
                if valor == 0:
                    pytest.skip(f"Cantidad de grupos minimos para ejecutar la prueba es de '1', en la base de datos no existen grupos")

            filas = len(self.driver.find_elements_by_xpath("//tbody/tr"))
            for tr in range(filas):
                tr += 1

                if tr == 1:
                    Selenium.foto(self, "Modal")

                group = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[1]").text
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[1]").click()

                check = Selenium.check_exists_by_xpath(self, "//th[contains(text(),'Usuarios del grupo :')]")
                if check == False:
                    assert check == True, f"Error, no se visualiza el titulo de la tabla 'Usuarios del grupo : {group}'"

                check = Selenium.check_visibility_element_located(self, "Agregar Usuario")
                if check == False:
                    Selenium.foto(self, "boton agregar usuario")
                    assert check == True, "ERROR, No se visualiza el boton de AGREGAR USUARIO"

                Selenium.get_elements(self, "Agregar Usuario").click()

                visual = Selenium.check_visibility_element_located(self, "Modal crear agregar")
                assert visual == True, "ERROR, No se visualiza el modal de AGREGAR USUARIOS a un grupo"

                check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),'Agregar usuarios')]")
                if check == False:
                    Selenium.foto(self, "Error")
                    assert check == True, "ERROR, El titulo del modal ya no es el mismo, este a cambiado"

                check = Selenium.check_exists_by_xpath(self, "//h4[contains(text(),'Asignación de usuarios')]")
                if check == False:
                    Selenium.foto(self, "Error")
                    assert check == True, "ERROR, El titulo del modal ya no es el mismo, este a cambiado"

                elements = ['nombre de grupo', 'categories', 'cancelar', 'crear']

                for i in range(len(elements)):
                    check = Selenium.check_element(self, elements[i])
                    value = Selenium.get_elements(self, elements[i]).get_attribute("value")

                    if check == False:
                        Selenium.foto(self, "No existe")
                        assert check == True, f"ERROR, No se encuentra el elemento '{elements[i]}'"

                    if i == 0:
                        if not value == group:
                            assert  value == group, f"ERROR, El nombre del grupo '{group}' no coincide en el modal."

                    if i > 1:
                        visual = Selenium.check_visibility_element_located(self, elements[i])
                        enabled = Selenium.get_elements(self, elements[i]).is_enabled()
                        text = Selenium.get_elements(self, elements[i]).text
                        if visual == False:
                            Selenium.foto(self, "No existe")
                            assert visual == True, f"ERROR, el boton '{elements[i]}' no se visualiza"
                        if i == 6:
                            if not text == "CANCELAR":
                                Selenium.foto(self, "No es igual")
                                assert text == "CANCELAR", f"ERROR, el nombre del boton '{elements[i]}' no es igual a 'CANCELAR'"
                            if enabled == False:
                                Selenium.foto(self, "Esta bloqueado")
                                assert enabled == True, "Error, al parecer el boton esta deshabilitado y este deberia de estar habilitado"
                        if i == 7:
                            if not text == "EDITAR":
                                Selenium.foto(self, "No es igual")
                                assert text == "EDITAR", f"ERROR, el nombre del boton '{elements[i]}' no es igual a 'EDITAR'"
                            if enabled == False:
                                Selenium.foto(self, "Esta bloqueado")
                                assert enabled == True, "Error, al parecer el boton esta deshabilitado, y este deberia de estar habilitado"
                Selenium.get_elements(self, "cancelar").click()

    @allure.title(u'Input BUSCAR GRUPO.')
    @allure.story(u'Hacer una busqueda de un grupo y validar el resultado.')
    def test_search(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "groups")

            Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.get_elements(self, "Adminsitracion de grupos").click()

            Selenium.check_element(self, "input buscar")

            filas = len(self.driver.find_elements_by_xpath("//tbody/tr"))
            groups = []
            for tr in range(filas):
                tr += 1

                if tr == 1:
                    Selenium.foto(self, "Modal")

                group = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[1]").text
                groups.append(group)

            for group in groups:
                if len(groups) > 0:
                    Selenium.get_elements(self, "Adminsitracion de grupos").click()
                    Selenium.check_element(self, "input buscar")
                Selenium.get_elements(self, "input buscar").send_keys(group)
                Selenium.get_elements(self, "button buscar").click()

                time.sleep(1)
                filas = len(self.driver.find_elements_by_xpath("//tbody/tr"))
                if not filas == 1:
                    Selenium.foto(self, "busqueda")
                    assert filas == 1, f"ERROR, al parecer hay mas de un grupo con el nombre '{group}' o mas de un resultado incorrecto."

                for f in range(filas):
                    f += 1
                    result = self.driver.find_element_by_xpath(f"//tbody/tr[{str(f)}]/td[1]").text
                    if not result == group:
                        Selenium.foto(self, "resultado")
                        assert result == group, f"ERROR, EL RESULTADO '{result}' NO ES IGUAL AL INGRESADO '{group}'."

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
