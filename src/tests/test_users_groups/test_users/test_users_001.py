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

class test_users_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")

    @allure.title(u'Menú.')
    @allure.story(u'Comprobar visualización del menu de directorios.')
    def test_menu(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Validando:'):
            Selenium.get_json_file(self, "panel")

            Selenium.foto(self, "Administración")
            check = Selenium.check_element(self, "Administracion")
            assert check == True, "No se visualiza el menu de administración"
            Selenium.get_elements(self, "Administracion").click()

            Selenium.foto(self, "Usuarios y grupos")
            check = Selenium.check_element(self, "Usuarios y grupos")
            assert check == True, "No se visualiza el menu de administración"

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

            Selenium.get_json_file(self, "users")
            check = Selenium.check_element(self, "titulo")
            Selenium.foto(self, "titulo")
            assert check == True, "Error no se encuentra el elemento del titulo 'Usuarios y grupos'"

    @allure.title(u'Botón ADMINISTRACIÓN DE USUARIOS.')
    @allure.story(u'Comprobar el estado y visualizacion del boton.')
    def test_button_001(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "users")

            check = Selenium.check_element(self, "Adminsitracion de usuarios")
            Selenium.foto(self, "Adminsitracion de usuarios")
            assert check == True, "Error, el botón no se encuentra en la pantalla"

            selected = Selenium.get_elements(self, "Adminsitracion de usuarios").get_attribute("aria-selected")
            assert selected == "true", "El botón no se encuentra seleccionado como se esperaba"

            enabled = Selenium.get_elements(self, "Adminsitracion de usuarios").is_enabled()
            assert enabled == True, "El botón no se encuentra habilitado"

            name = Selenium.get_elements(self, "Adminsitracion de usuarios").text
            assert name == "Administración de usuarios", "El nombre del botón ha cambiado, ahora es diferente al esperado"

    @allure.title(u'Input BUSCAR USUARIO.')
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
            Selenium.get_json_file(self, "users")

            check = Selenium.check_element(self, "input buscar")
            Selenium.foto(self, "Adminsitracion de usuarios")
            assert check == True, "Error no se encuentra el input en la pantalla"

            placeholder = Selenium.get_elements(self, "input buscar").get_attribute("placeholder")
            assert placeholder == "Buscar usuario", "El placeholder del input ha cambiado, ya no es igual"

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
            Selenium.get_json_file(self, "users")

            check = Selenium.check_element(self, "button buscar")
            Selenium.foto(self, "Adminsitracion de usuarios")
            assert check == True, "Error, el botón no se encuentra en la pantalla"

            enabled = Selenium.get_elements(self, "button buscar").is_enabled()
            assert enabled == False, "El botón se encuentra habilitado, este no es un comportamiento esperado"

            name = Selenium.get_elements(self, "button buscar").text
            assert name == "BUSCAR", "El nombre del botón ha cambiado, ahora es diferente al esperado"

    @allure.title(u'Botón CREAR NUEVO USUARIO.')
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
            Selenium.get_json_file(self, "users")

            check = Selenium.check_element(self, "crear usuario")
            Selenium.foto(self, "Adminsitracion de usuarios")
            assert check == True, "Error, el botón no se encuentra en la pantalla"

            enabled = Selenium.get_elements(self, "crear usuario").is_enabled()
            assert enabled == True, "El botón se encuentra deshabilitado, este no es un comportamiento esperado"

            name = Selenium.get_elements(self, "crear usuario").text
            assert name == "Crear nuevo usuario", "El nombre del botón ha cambiado, ahora es diferente al esperado"

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
            Selenium.get_json_file(self, "users")

            check = Selenium.check_element(self, "Adminsitracion de grupos")
            Selenium.foto(self, "Adminsitracion de grupos")
            assert check == True, "Error, el botón no se encuentra en la pantalla"

            selected = Selenium.get_elements(self, "Adminsitracion de grupos").get_attribute("aria-selected")
            assert selected == "false", "El botón se encuentra seleccionado 'Adminsitracion de grupos'"

            enabled = Selenium.get_elements(self, "Adminsitracion de grupos").is_enabled()
            assert enabled == True, "El botón no se encuentra habilitado"

            name = Selenium.get_elements(self, "Adminsitracion de grupos").text
            assert name == "Administración de grupos", "El nombre del botón ha cambiado, ahora es diferente al esperado"

    @allure.title(u'Titulo h3.')
    @allure.story(u'Comprobar el titulo RESULTADO USUARIOS sea siempre el mismo.')
    def test_title_h3(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "users")

            check = Selenium.check_element(self, "h3 Resultado usuarios")
            Selenium.foto(self, "Adminsitracion de usuarios")
            assert check, "Error el titulo 'Resultado usuarios' no se encuentra en la pantalla"

    @allure.title(u'SubTitulo span.')
    @allure.story(u'Comprobar el sub-titulo MOSTRANDO TODOS LOS RESULTADO sea siempre el mismo.')
    def test_subtitle_span(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "users")

            check = Selenium.check_element(self, "span Mostrando todos los resultado")
            Selenium.foto(self, "Adminsitracion de usuarios")
            assert check == True, "Error el Sub-titulo 'Mostrando todos los resultado' no se encuentra en la pantalla"

    @allure.title(u'Nombre Columnas Grilla.')
    @allure.story(u'Comprobar que el nombre de las columnas de la grilla sea siempre el mismo.')
    def test_table(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "users")

            check = Selenium.check_element(self, "tabla 1")
            Selenium.foto(self, "Tabla")
            assert check == True, "ERROR, No existe la parte de arriba de la tabla (Parte en azul con titulos)"

            columnas = self.driver.find_element_by_xpath("//thead/tr").text
            columna = Selenium.split(self, columnas, " ")
            data = ['Usuario', 'Nombre', 'Email', 'Empresa', 'Departamento', 'Estado', 'Acciones']
            for c in range(7):
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
            Selenium.get_json_file(self, "users")

            check = Selenium.check_element(self, "tabla 1")
            Selenium.foto(self, "Tabla")
            assert check == True, "ERROR, No existe la parte de arriba de la tabla (Parte en azul con titulos)"

            consulta = Selenium.pyodbc_query(self, "SELECT COUNT(*) FROM public.company_user")
            for valor in consulta:
                if valor == 0:
                    pytest.skip(f"Cantidad de usuarios minimos para ejecutar la prueba es de '1', en la base de datos no existen usuarios")

            check = Selenium.check_exists_by_xpath(self, "//tbody/tr")
            assert check == True, f"En la base de datos existen {valor} usuarios. En la grilla al parecer no hay usuarios"

            columnas = len(self.driver.find_elements_by_xpath("//tbody/tr"))

            if valor >= 11:
                assert columnas == 10, f"Error, se visualizan {columnas} usuarios en la grilla, cuando en la bd existen {valor}"

                check = Selenium.check_element(self, "nextPage")
                assert check == True, "Error, no existe el elemento para redireccionar a la siguiente pagina"
            next = False
            while next == False:
                time.sleep(0.5)
                Selenium.check_exists_by_xpath(self,f"//tbody/tr[1]/td[6]/span[1]/span[1]/span[1]/input")
                columnas = len(self.driver.find_elements_by_xpath("//tbody/tr"))
                for tr in range(columnas):
                    tr += 1
                    checkB = Selenium.check_exists_by_xpath(self,
                                                            f"//tbody/tr[{str(tr)}]/td[6]/span[1]/span[1]/span[1]/input")
                    if checkB == False:
                        Selenium.foto(self, "No existe")
                        assert checkB == True, "No existe el input tipo checkbox para habilitar/deshabilitar cuentas de usuario"

                    checkE = Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(tr)}]/td[7]/div[1]/div[1]/*[1]")
                    if checkE == False:
                        Selenium.foto(self, "No existe")
                        assert checkE == True, "No existe el boton 'editar' para habilitar/deshabilitar cuentas de usuario"

                if Selenium.get_elements(self, "nextPage").is_enabled() == True:
                    Selenium.get_elements(self, "nextPage").click()
                    next = False
                else:
                    next = True

    @allure.title(u'Modal CREAR NUEVO USUARIO.')
    @allure.story(u'Comprobar botones y elementos del modal CREAR NUEVO USUARIO.')
    def test_modal_create(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            Selenium.get_json_file(self, "users")

            Selenium.check_element(self, "crear usuario")
            Selenium.get_elements(self, "crear usuario").click()

            Selenium.foto(self, "Modal")
            visual = Selenium.check_visibility_element_located(self, "Modal crear editar")
            assert visual == True, "ERROR, No se visualiza el modal de CREAR USUARIOS"

            check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),'Agregar nuevo usuario')]")
            assert check == True, "ERROR, El titulo del modal ya no es el mismo, este a cambiado"

            elements = ['nombres', 'apellidos', 'email', 'empresa', 'departamento', 'usuario', 'categories', 'cancelar' , 'crear']

            for i in range(len(elements)):
                check = Selenium.check_element(self, elements[i])

                if check == False:
                    Selenium.foto(self, "No existe")
                    assert check == True, f"ERROR, No se encuentra el elemento '{elements[i]}'"

                if i == 5:
                    Selenium.foto(self, "No existe")
                    check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),'La contraseña de generará automatícamente y llegar')]")
                    assert check == True, "ERROR, no se visualiza el mensaje habitual, '''La contraseña de generará automatícamente y llegar'''"

                if i == 7 or i == 8:
                    visual = Selenium.check_visibility_element_located(self, elements[i])
                    enabled = Selenium.get_elements(self, elements[i]).is_enabled()
                    text = Selenium.get_elements(self, elements[i]).text
                    if visual == False:
                        Selenium.foto(self, "No existe")
                        assert visual == True, f"ERROR, el boton '{elements[i]}' no se visualiza"
                    if i == 7:
                        if not text == "CANCELAR":
                            Selenium.foto(self, "No es igual")
                            assert text == "CANCELAR", f"ERROR, el nombre del boton '{elements[i]}' no es igual a 'CANCELAR'"
                        if enabled == False:
                            Selenium.foto(self, "Esta bloqueado")
                            assert enabled == True, "Error, al parecer el boton esta deshabilitado y este deberia de estar habilitado"
                    if i == 8:
                        if not text == "CREAR":
                            Selenium.foto(self, "No es igual")
                            assert text == "CREAR", f"ERROR, el nombre del boton '{elements[i]}' no es igual a 'CREAR'"
                        if enabled == True:
                            Selenium.foto(self, "Esta bloqueado")
                            assert enabled == False, "Error, al parecer el boton esta habilitado, y este deberia de estar deshabilitado"

    @allure.title(u'Modal EDITAR USUARIO.')
    @allure.story(u'Comprobar botones y elementos del modal EDITAR USUARIO.')
    def test_modal_edit(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            consulta = Selenium.pyodbc_query(self, "SELECT COUNT(*) FROM public.company_user")
            for valor in consulta:
                if valor == 0:
                    pytest.skip(f"Cantidad de usuarios minimos para ejecutar la prueba es de '1', en la base de datos no existen usuarios")
            check = Selenium.check_exists_by_xpath(self, "//tbody/tr")
            assert check, f"En la base de datos existen {valor} usuarios. En la grilla al parecer no hay usuarios"

            if valor >= 11:
                Selenium.get_json_file(self, "users")
                check = Selenium.check_element(self, "nextPage")
                assert check == True, "Error, no existe el elemento para redireccionar a la siguiente pagina"
            next = False
            while not next:
                time.sleep(0.5)
                Selenium.check_exists_by_xpath(self, f"//tbody/tr[1]/td[6]/span[1]/span[1]/span[1]/input")
                columnas = len(self.driver.find_elements_by_xpath("//tbody/tr"))

                for tr in range(columnas):
                    tr += 1

                    if tr == 1:
                        Selenium.foto(self, "Modal")

                    Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(tr)}]/td[7]/div[1]/div[1]/*[1]")
                    self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[7]/div[1]/div[1]/*[1]").click()

                    Selenium.get_json_file(self, "users")

                    visual = Selenium.check_visibility_element_located(self, "Modal crear editar")
                    assert visual == True, "ERROR, No se visualiza el modal de CREAR EDITAR"

                    check = Selenium.check_exists_by_xpath(self, "//h2[contains(text(),'Editar usuario')]")
                    assert check == True, "ERROR, El titulo del modal ya no es el mismo, este a cambiado"

                    elements = ['usuario editar', 'nombres', 'apellidos', 'email', 'empresa', 'departamento', 'cancelar', 'crear']
                    x = 0
                    for i in range(len(elements)):
                        check = Selenium.check_element(self, elements[i])
                        value = Selenium.get_elements(self, elements[i]).get_attribute("value")

                        if check == False:
                            Selenium.foto(self, "No existe")
                            assert check == True, f"ERROR, No se encuentra el elemento '{elements[i]}'"

                        if i < 6:
                            if value == "":
                                assert not value == "", f"ERROR, No tiene ningun valor asignado el elemento '{elements[i]}'"

                        if i > 5:
                            visual = Selenium.check_visibility_element_located(self, elements[i])
                            enabled = Selenium.get_elements(self, elements[i]).is_enabled()
                            text = Selenium.get_elements(self, elements[i]).text
                            if not visual:
                                Selenium.foto(self, "No existe")
                                assert visual, f"ERROR, el boton '{elements[i]}' no se visualiza"
                            if i == 6:
                                if not text == "CANCELAR":
                                    Selenium.foto(self, "No es igual")
                                    assert text == "CANCELAR", f"ERROR, el nombre del boton '{elements[i]}' no es igual a 'CANCELAR'"
                                if not enabled:
                                    Selenium.foto(self, "Esta bloqueado")
                                    assert enabled == True, "Error, al parecer el boton esta deshabilitado y este deberia de estar habilitado"
                            if i == 7:
                                if not text == "EDITAR":
                                    Selenium.foto(self, "No es igual")
                                    assert text == "EDITAR", f"ERROR, el nombre del boton '{elements[i]}' no es igual a 'EDITAR'"
                                if not enabled:
                                    Selenium.foto(self, "Esta bloqueado")
                                    assert enabled, "Error, al parecer el boton esta deshabilitado, y este deberia de estar habilitado"

                        if i == 4 or i == 5:
                            value = Selenium.get_elements(self, elements[i]).get_attribute("value")
                            elements_other = ['empresaOther', 'departamentoOther']
                            if value == "Other":
                                check_other = Selenium.check_element(self, elements_other[x])
                                if check_other == False:
                                    Selenium.foto(self, "No existe")
                                    assert check_other, f"ERROR, No se encuentra el elemento '{elements_other[x]}'"
                                x += 1
                    Selenium.get_elements(self, "cancelar").click()
                if Selenium.get_elements(self, "nextPage").is_enabled():
                    Selenium.get_elements(self, "nextPage").click()
                    next = False
                else:
                    next = True

    @allure.title(u'Boton SIGUIENTE PAGINA.')
    @allure.story(u'Validar que cada pagina es diferente a la anterior.')
    def test_next_page(self):
        with allure.step(u'PASO 2 : Ingresar a la biblioteca'):
            Selenium.get_signin_administrator(self)

        with allure.step(u'PASO 3 : Ingresando a usuarios y grupos:'):
            Selenium.get_json_file(self, "panel")
            Selenium.check_element(self, "Administracion")
            Selenium.get_elements(self, "Administracion").click()
            Selenium.get_elements(self, "Usuarios y grupos").click()

        with allure.step(u'PASO 4 : Validando:'):
            consulta = Selenium.pyodbc_query(self, "SELECT COUNT(*) FROM public.company_user")
            for valor in consulta:
                if valor == 0:
                    pytest.skip(
                        f"Cantidad de usuarios minimos para ejecutar la prueba es de '1', en la base de datos no existen usuarios")
            check = Selenium.check_exists_by_xpath(self, "//tbody/tr")
            assert check == True, f"En la base de datos existen {valor} usuarios. En la grilla al parecer no hay usuarios"

            if valor >= 11:
                Selenium.get_json_file(self, "users")
                check = Selenium.check_element(self, "nextPage")
                assert check == True, "Error, no existe el elemento para redireccionar a la siguiente pagina"
            users = []
            next = False
            while next == False:
                time.sleep(0.5)
                Selenium.check_exists_by_xpath(self, f"//tbody/tr[1]")
                columnas = len(self.driver.find_elements_by_xpath("//tbody/tr"))

                for tr in range(columnas):
                    tr += 1
                    if tr == 1:
                        Selenium.foto(self, "Modal")
                    tabla = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]").text
                    user = Selenium.split(self, tabla, " ")
                    if tr > 1:
                        self.assertNotIn(user[0], users, "Error, se encontro un nombre de usuario repetido")
                    assert not user[0] == "admin", "ERROR!!! , SE VISUALIZA EL USUARIO ADMIN EN LA TABLA"
                    users.append(user[0])

                if Selenium.get_elements(self, "nextPage").is_enabled() == True:
                    Selenium.get_elements(self, "nextPage").click()
                    next = False
                else:
                    next = True

    @allure.title(u'Input BUSCAR USUARIO.')
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
            Selenium.get_json_file(self, "users")
            Selenium.check_element(self, "input buscar")

            filas = len(self.driver.find_elements_by_xpath("//tbody/tr"))
            consulta = Selenium.pyodbc_query(self, "SELECT COUNT(*) FROM public.company_user")
            for valor in consulta:
                if valor == 0:
                    pytest.skip(
                        f"Cantidad de usuarios minimos para ejecutar la prueba es de '1', en la base de datos no existen usuarios")
            check = Selenium.check_exists_by_xpath(self, "//tbody/tr")
            assert check == True, f"En la base de datos existen {valor} usuarios. En la grilla al parecer no hay usuarios"

            if valor >= 11:
                Selenium.get_json_file(self, "users")
                check = Selenium.check_element(self, "nextPage")
                assert check == True, "Error, no existe el elemento para redireccionar a la siguiente pagina"
            users = []
            next = False
            while next == False:
                time.sleep(0.5)
                Selenium.check_exists_by_xpath(self, f"//tbody/tr[1]")
                columnas = len(self.driver.find_elements_by_xpath("//tbody/tr"))

                for tr in range(columnas):
                    tr += 1
                    if tr == 1:
                        Selenium.foto(self, "Modal")
                    tabla = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]").text
                    user = Selenium.split(self, tabla, " ")

                    users.append(user[0])

                if Selenium.get_elements(self, "nextPage").is_enabled() == True:
                    Selenium.get_elements(self, "nextPage").click()
                    next = False
                else:
                    next = True

            for tr in range(filas):
                tr += 1

                if tr == 1:
                    Selenium.foto(self, "Modal")

                user = self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[1]").text
                users.append(user)

            for user in users:
                if len(users) > 0:
                    Selenium.get_elements(self, "Adminsitracion de usuarios").click()
                    Selenium.check_element(self, "input buscar")
                Selenium.get_elements(self, "input buscar").send_keys(user)
                Selenium.get_elements(self, "button buscar").click()

                time.sleep(1)
                results = []
                for f in range(len(self.driver.find_elements_by_xpath("//tbody/tr"))):
                    f += 1
                    result = self.driver.find_element_by_xpath(f"//tbody/tr[{str(f)}]/td[1]").text
                    results.append(result)
                    #if not result == user:
                        #Selenium.foto(self, "resultado")
                        #assert result == user, f"ERROR, EL RESULTADO '{result}' NO ES IGUAL AL INGRESADO '{user}'."
                if user not in results:
                    Selenium.foto(self, "NO ESTA")
                    self.assertIn(user, results, f"ERROR, EL USUARIO '{user}' BUSCADO, NO ES IGUAL AL RESULTADO(S) EN LA GRILLA")

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
