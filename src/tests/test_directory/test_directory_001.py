# -*- coding: utf-8 -*-
import unittest
from datetime import time
import time
import allure
import pytest
from src.functions.functions import Functions as Selenium
import HtmlTestRunner

@allure.feature(u'Pruebas Directorios')
@allure.testcase(u'Pruebas unitarias')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Validaciones: </br>
Estado de botones</br>
Campos requeridos, como nombre y tipo de directorio</br>
Relacion correcta de la BD con lo mostrado en la grilla</br>
visibilidad de los elementos</br>
</br></br>""")

class test_directory_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1 : Ingresar al navegador'):
            Selenium.open_browser(self, navegador="CHROME")
            self.editDir = "test_edit" + Selenium.generate_id(length=2)
            self.creaDir = "test_create" + Selenium.generate_id(length=2)

    @allure.title(u'Menú DIRECTORIOS')
    @allure.story(u'Estado y visualizacion del menu de directorios.')
    def test_menu(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Visualizar y pulsar el menú de directorios'):
            Selenium.get_elements(self, "Menu administracion").click()

            check = Selenium.check_element(self, "Menu directorios")
            visual = Selenium.check_visibility_element_located(self, "Menu directorios")

            Selenium.foto(self, "Menu de directorios")
            self.assertTrue(visual and check, "Error, el menu de directorios no se puede encontrar porque no esta visible")

    @allure.title(u'Titulo')
    @allure.story(u'Validar que se muestra el titulo Administración directorios.')
    def test_title(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Visualizar y pulsar el menú de directorios'):
            Selenium.get_elements(self, "Menu administracion").click()

            Selenium.get_elements(self, "Menu directorios").click()

            Selenium.foto(self, "Menu de directorios")
            check = Selenium.check_exists_by_xpath(self, "//h3[contains(text(),'directorios')]")
            self.assertTrue(check, "Error, el titulo 'Administración directorios' no se puede encontrar o no está.")

    @allure.title(u'Miga de pan')
    @allure.story(u'Validar que se muestra la miga de pan por defecto GENERAL.')
    def test_miga(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Visualizar y pulsar el menú de directorios'):
            Selenium.get_elements(self, "Menu administracion").click()

            Selenium.get_elements(self, "Menu directorios").click()

            Selenium.foto(self, "Menu de directorios")
            check = Selenium.check_exists_by_xpath(self, "//p[contains(text(),'General')]")
            self.assertTrue(check, "Error, la miga de pan por defecto 'General' no se puede encontrar o no está.")

    @allure.title(u'Nombre de campos de la tabla')
    @allure.story(u'Validar que el nombre de los campos de la tabla siempre sea el mismo.')
    def test_table(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Visualizar y pulsar el menú de directorios'):
            Selenium.get_elements(self, "Menu administracion").click()

            Selenium.get_elements(self, "Menu directorios").click()

            Selenium.foto(self, "Menu de directorios")
            element = len(self.driver.find_elements_by_xpath("//thead/tr[1]/th"))
            data = ['Nombre', 'Tipo', 'Acciones']
            x = 0
            for th in range(element):
                th += 1
                xpath = self.driver.find_element_by_xpath(f"//thead/tr[1]/th[{str(th)}]").text
                print(data[x], xpath)
                self.assertIn(data[x], xpath, f"ERROR, NO COINCIDEN LOS ELEMENTOS. Esperado:'{data[x]}'  Obtenido: '{xpath}'")
                x += 1

    @allure.title(u'Botón CREAR NUEVO DIRECTORIO')
    @allure.story(u'Validar el boton crear nuevo directorio.')
    def test_create(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Valindado..'):
            Selenium.get_elements(self, "Menu administracion").click()

            Selenium.get_elements(self, "Menu directorios").click()

            Selenium.foto(self, "Directorios")

            check = Selenium.check_element(self, "Crear nuevo directorio")
            assert check, "ERROR, NO SE ENCUENTRA EL ELEMENTO BOTÓN PARA CREAR UN NUEVO DIRECTORIO"

            check = Selenium.get_elements(self, "Crear nuevo directorio").is_enabled()
            assert check, "ERROR, EL BOTON CREAR NUEVO DIRECTORIO SE ENCUENTRA BLOQUEADO"

    @allure.title(u'Botón EDITAR y BORRAR')
    @allure.story(u'Validar el boton para EDITAR y BORRAR un directorio.')
    def test_element(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Valindado..'):
            Selenium.get_elements(self, "Menu administracion").click()

            Selenium.get_elements(self, "Menu directorios").click()

            Selenium.foto(self, "Directorios")

            long = len(self.driver.find_elements_by_xpath("//tbody/tr"))
            if long < 1:
                pytest.skip("PRUEBA SALTADA, SE NECESITA ALMENOS UNA CARPETA PARA EJECUTAR ESTE TEST.")
            for tr in range(long):
                tr += 1
                edit = Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[1]")
                delete = Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[2]")

                if not edit:
                    Selenium.foto(self, "editar")
                    assert edit, "ERROR, NO SE ENCUENTRA EL BOTON PARA EDITAR UN DIRECTORIO"

                if not delete:
                    Selenium.foto(self, "borrar")
                    assert delete, "ERROR, NO SE ENCUENTRA EL BOTON PARA BORRAR UN DIRECTORIO"

    @allure.title(u'Modal CREAR')
    @allure.story(u'Validar los elementos del modal CREAR NUEVO DIRECTORIO.')
    def test_modal_create(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Valindado..'):
            Selenium.get_elements(self, "Menu administracion").click()

            Selenium.get_elements(self, "Menu directorios").click()

            Selenium.foto(self, "Directorios")

            Selenium.check_element(self, "Crear nuevo directorio")
            Selenium.get_elements(self, "Crear nuevo directorio").click()

            check = Selenium.check_element(self, "dialogo")
            if not check:
                Selenium.foto(self, "Crear dir")
                assert check, "ERROR, NO SE ENCUENTRA EL ELEMENTO DEL MODAL CREAR DIRECTORIO"

            check = Selenium.check_exists_by_xpath(self, "//h2[contains(text(),'Crear nuevo espacio de trabajo')]")
            if not check:
                Selenium.foto(self, "titulo")
                assert check, "ERROR, NO SE ENCUENTRA EL TITULO DEL MODAL ''Crear nuevo espacio de trabajo''"

            check = Selenium.check_exists_by_xpath(self, "//h4[contains(text(),'Permisos de grupo')]")
            if not check:
                Selenium.foto(self, "titulo")
                assert check, "ERROR, NO SE ENCUENTRA EL TITULO DEL MODAL ''Permisos de grupo''"

            elements = ['tipo espacio trabajo', 'nombre', 'heredar permisos', 'seleccionar grupo', 'cancelar', 'guardar']
            for e in range(len(elements)):
                check = Selenium.check_element(self, elements[e])
                if not check:
                    Selenium.foto(self, "elementos")
                    assert check, f"ERROR, NO SE ENCUENTRA EL ELEMENTO '{elements[e]}' DEL MODAL ''Crear nuevo espacio de trabajo''"

                if e == 2:
                    select = Selenium.get_elements(self, elements[e]).is_selected()
                    if select:
                        Selenium.foto(self, "elementos")
                        assert not select, "ERROR, EL CHECKBOX HEREDAR PERMISOS ESTÁ SELECCIONADO"

                if e == 4:
                    text = Selenium.get_elements(self, elements[e]).text
                    enabled = Selenium.get_elements(self, elements[e]).is_enabled()
                    if not text == 'Cancelar':
                        Selenium.foto(self, "elementos")
                        assert text == 'Cancelar', "ERROR, EL BOTÓN CANCELAR YA NO TIENE EL MISMO NOMBRE"
                    if not enabled:
                        Selenium.foto(self, "elementos")
                        assert enabled, "ERROR, EL BOTÓN CANCELAR NO ESTÁ HABILITADO"

                if e == 5:
                    text = Selenium.get_elements(self, elements[e]).text
                    enabled = Selenium.get_elements(self, elements[e]).is_enabled()
                    if not text == 'Guardar':
                        Selenium.foto(self, "elementos")
                        assert text == 'Guardar', "ERROR, EL BOTÓN GUARDAR YA NO TIENE EL MISMO NOMBRE"
                    if not enabled:
                        Selenium.foto(self, "elementos")
                        assert enabled, "ERROR, EL BOTÓN GUARDAR NO ESTÁ HABILITADO"

    @allure.title(u'Modal EDITAR')
    @allure.story(u'Validar los elementos del modal EDITAR DIRECTORIO.')
    def test_modal_edit(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Valindado..'):
            Selenium.get_elements(self, "Menu administracion").click()

            Selenium.get_elements(self, "Menu directorios").click()

            Selenium.foto(self, "Directorios")

            long = len(self.driver.find_elements_by_xpath("//tbody/tr"))
            if long < 1:
                pytest.skip("PRUEBA SALTADA, SE NECESITA ALMENOS UNA CARPETA PARA EJECUTAR ESTE TEST.")
            for tr in range(long):
                tr += 1
                Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[1]")
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[1]").click()

                check = Selenium.check_element(self, "dialogo")
                if not check:
                    Selenium.foto(self, "Editar dir")
                    assert check, "ERROR, NO SE ENCUENTRA EL MODAL EDITAR"

                check = Selenium.check_exists_by_xpath(self, "//h2[contains(text(),'Editar espacio de trabajo')]")
                if not check:
                    Selenium.foto(self, "titulo")
                    assert check, "ERROR, NO SE ENCUENTRA EL TITULO DEL MODAL ''Editar espacio de trabajo''"

                check = Selenium.check_exists_by_xpath(self, "//h4[contains(text(),'Permisos de grupo')]")
                if not check:
                    Selenium.foto(self, "titulo")
                    assert check, "ERROR, NO SE ENCUENTRA EL TITULO DEL MODAL ''Permisos de grupo''"

                elements = ['nombre', 'heredar permisos', 'seleccionar grupo', 'cancelar',
                            'guardar']
                for e in range(len(elements)):
                    check = Selenium.check_element(self, elements[e])
                    if not check:
                        Selenium.foto(self, "elementos")
                        assert check, f"ERROR, NO SE ENCUENTRA EL ELEMENTO '{elements[e]}' DEL MODAL ''Crear nuevo espacio de trabajo''"

                    if e == 3:
                        text = Selenium.get_elements(self, elements[e]).text
                        enabled = Selenium.get_elements(self, elements[e]).is_enabled()
                        if not text == 'Cancelar':
                            Selenium.foto(self, "elementos")
                            assert text == 'Cancelar', "ERROR, EL BOTÓN CANCELAR YA NO TIENE EL MISMO NOMBRE"
                        if not enabled:
                            Selenium.foto(self, "elementos")
                            assert enabled, "ERROR, EL BOTÓN CANCELAR NO ESTÁ HABILITADO"

                    if e == 4:
                        text = Selenium.get_elements(self, elements[e]).text
                        enabled = Selenium.get_elements(self, elements[e]).is_enabled()
                        if not text == 'Guardar':
                            Selenium.foto(self, "elementos")
                            assert text == 'Guardar', "ERROR, EL BOTÓN GUARDAR YA NO TIENE EL MISMO NOMBRE"
                        if not enabled:
                            Selenium.foto(self, "elementos")
                            assert enabled, "ERROR, EL BOTÓN GUARDAR NO ESTÁ HABILITADO"

                Selenium.get_elements(self, "cancelar").click()

    @allure.title(u'Modal BORRAR')
    @allure.story(u'Validar los elementos del modal BORRAR DIRECTORIO.')
    def test_modal_delete(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Valindado..'):
            Selenium.get_elements(self, "Menu administracion").click()

            Selenium.get_elements(self, "Menu directorios").click()

            Selenium.foto(self, "Directorios")

            long = len(self.driver.find_elements_by_xpath("//tbody/tr"))
            if long < 1:
                pytest.skip("PRUEBA SALTADA, SE NECESITA ALMENOS UNA CARPETA PARA EJECUTAR ESTE TEST.")
            for tr in range(long):
                tr += 1
                Selenium.check_exists_by_xpath(self, f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[2]")
                self.driver.find_element_by_xpath(f"//tbody/tr[{str(tr)}]/td[2]/div[1]/div[2]").click()

                check = Selenium.check_element(self, "modal eliminar")
                if not check:
                    Selenium.foto(self, "Editar dir")
                    assert check, "ERROR, NO SE ENCUENTRA EL MODAL EDITAR"

                check = Selenium.check_exists_by_xpath(self, "//h2[contains(text(),'Eliminar')]")
                if not check:
                    Selenium.foto(self, "titulo")
                    assert check, "ERROR, NO SE ENCUENTRA EL TITULO DEL MODAL ''Eliminar''"

                check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),'¿Está seguro que quiere eliminar la carpeta?')]")
                if not check:
                    Selenium.foto(self, "titulo")
                    assert check, "ERROR, NO SE ENCUENTRA EL MENSAJE DE CONFIRMACION DEL MODAL ''¿Está seguro que quiere eliminar la carpeta?''"

                elements = ['cancel', 'Boton OK']
                for e in range(len(elements)):
                    check = Selenium.check_element(self, elements[e])
                    if not check:
                        Selenium.foto(self, "elementos")
                        assert check, f"ERROR, NO SE ENCUENTRA EL ELEMENTO '{elements[e]}' DEL MODAL ''Eliminar''"

                    if e == 0:
                        text = Selenium.get_elements(self, elements[e]).text
                        enabled = Selenium.get_elements(self, elements[e]).is_enabled()
                        if not text == 'Cancel':
                            Selenium.foto(self, "elementos")
                            assert text == 'Cancel', "ERROR, EL BOTÓN CANCELAR YA NO TIENE EL MISMO NOMBRE"
                        if not enabled:
                            Selenium.foto(self, "elementos")
                            assert enabled, "ERROR, EL BOTÓN CANCELAR NO ESTÁ HABILITADO"

                    if e == 1:
                        text = Selenium.get_elements(self, elements[e]).text
                        enabled = Selenium.get_elements(self, elements[e]).is_enabled()
                        if not text == 'OK':
                            Selenium.foto(self, "elementos")
                            assert text == 'OK', "ERROR, EL BOTÓN OK YA NO TIENE EL MISMO NOMBRE"
                        if not enabled:
                            Selenium.foto(self, "elementos")
                            assert enabled, "ERROR, EL BOTÓN OK NO ESTÁ HABILITADO"

                Selenium.get_elements(self, "cancel").click()

    @allure.title(u'Crear un directorio')
    @allure.story(u'Crear un directorio y validaciones : Base de datos, Grilla y Arbol de directorios.')
    def test_create_001(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Ingresar en directorios'):
            Selenium.get_elements(self, "Menu administracion").click()
            Selenium.get_elements(self, "Menu directorios").click()

        with allure.step(u'PASO 4: Creando un directorio'):
            Selenium.check_element(self, "Crear nuevo directorio")
            Selenium.foto(self, "Crear nuevo directorio")
            Selenium.get_elements(self, "Crear nuevo directorio").click()
            Selenium.get_elements(self, "nombre").send_keys(self.creaDir)
            Selenium.get_elements(self, "tipo espacio trabajo").click()
            Selenium.get_elements(self, "workspace").click()
            Selenium.get_elements(self, "guardar").click()

        with allure.step(u'PASO 5: Obteniendo nombres y validando directorio creado'):
            Selenium.check_element(self, "Crear nuevo directorio")
            time.sleep(3)
            directorios = self.driver.find_elements_by_xpath("//tbody/tr/th[1]")
            for nombre in directorios:
                if nombre.text == self.creaDir:
                    break
            Selenium.foto(self, f"Creacion del directorio {self.creaDir}")
            time.sleep(1)
            self.assertIn(self.creaDir, nombre.text, f"No se encontro el directorio {self.creaDir} creado")
            consulta = Selenium.pyodbc_query(self, f"SELECT name FROM company_folder WHERE name='{nombre.text}'")
            self.assertIn(nombre.text, consulta,f"Error, el directorio {nombre.text} no se encuentra en la base de datos")

            self.driver.execute_script('arguments[0].scrollIntoView(true);',
                                       self.driver.find_element_by_xpath(f"//p[contains(text(),'{self.creaDir}')]"))
            assert Selenium.check_exists_by_xpath(self, f"//p[contains(text(),'{self.creaDir}')]"), \
                f"ERROR, NO SE VISUALIZA EL DIRECTORIO '{self.creaDir}' EN EL ARBOL DE DIRECTORIOS"
            print("DIRECTORIO CREADO: " + self.driver.find_element_by_xpath(f"//p[contains(text(),'{self.creaDir}')]").text)

    @allure.title(u'Grilla VS Base de datos')
    @allure.story(u'Comprobando que los nombre de los directorios de la grilla y base de datos concuerden.')
    def test_grid(self):
        with allure.step(u'PASO 2 : Ingresar con el usuario Admin'):
            Selenium.get_signin_administrator(self)
            Selenium.get_json_file(self, "directorios")

        with allure.step(u'PASO 3 : Ingresar en directorios'):
            Selenium.get_elements(self, "Menu administracion").click()
            Selenium.get_elements(self, "Menu directorios").click()

        with allure.step(f'PASO 4: Buscando el directorios en base de datos'):
            Selenium.check_visibility_element_located(self, "Crear nuevo directorio")
            time.sleep(2)
            names = self.driver.find_elements_by_xpath("//tbody/tr/th[1]")
            Selenium.foto(self, "Grilla")
            directorys = []
            for name in names:
                directorys.append(name.text)
        with allure.step(f'PASO 5: Validando directorios en la grilla con la base de datos'):
            i = 0
            for x in range(len(directorys)):
                grillaBD = Selenium.pyodbc_query_list(self, f"SELECT name FROM company_folder WHERE name = '{directorys[i]}'")
                self.assertNotEqual(grillaBD, None, "ERROR, La grilla no coincide con la Base de Datos")
                i += 1

    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))