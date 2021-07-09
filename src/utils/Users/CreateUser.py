from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.functions.functions import Functions as Selenium

class CreateUser:

    def modal(self):  # RETORNA TRUE O FALSE, SI VISUALIZA TODOS LOS ELEMENTOS DEL MODAL. Se debe ingresar el nombre del grupo.
        Selenium.get_json_file(self, "users")
        Selenium.foto(self, "Modal")
        try:
            visual = Selenium.check_visibility_element_located(self, "Modal crear editar")
            assert visual, "ERROR, No se visualiza el modal de CREAR USUARIOS"

            check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),'Agregar nuevo usuario')]")
            if not check:
                Selenium.foto(self, "Error")
                assert check, "ERROR, El titulo del modal ya no es el mismo, este a cambiado"

            check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),' llegara al correo indicado.')]")
            if not check:
                Selenium.foto(self, "Error")
                assert check, "ERROR, El mensaje de que llegara una contraseña al correo no se visualiza en el modal"

            elements = ['nombres', 'apellidos', 'email', 'empresa', 'departamento', 'usuario', 'categories', 'cancelar', 'crear']

            for i in range(len(elements)):
                check = Selenium.check_element(self, elements[i])

                if i < 6:
                    value = Selenium.get_elements(self, elements[i]).get_attribute("value")
                    if not value == "":
                        Selenium.foto(self, "error")
                        assert value == "", f"Error, el campo '{elements[i]}', contiene el valor='{value}', y este deberia de estar vacio."

                if i < 3 or i == 5:
                    assert Selenium.get_elements(self, elements[i]).get_attribute("aria-invalid") == "false"

                if not check:
                    Selenium.foto(self, "No existe")
                    assert check, f"ERROR, No se encuentra el elemento '{elements[i]}'"

                if i == 3:
                    check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),'Agregar nuevo usuario')]")
                    assert check, "ERROR, El titulo del modal ya no es el mismo, este a cambiado"

                if i == 6:
                    visual = Selenium.check_visibility_element_located(self, elements[i])
                    if not visual:
                        Selenium.foto(self, "No existe")
                        assert visual, f"ERROR, el boton '{elements[i]}' no se visualiza"

                if i == 7:
                    enabled = Selenium.get_elements(self, elements[i]).is_enabled()
                    text = Selenium.get_elements(self, elements[i]).text
                    if not text == "CANCELAR":
                        Selenium.foto(self, "No es igual")
                        assert text == "CANCELAR", f"ERROR, el nombre del boton '{elements[i]}' no es igual a 'CANCELAR'"
                    if not enabled:
                        Selenium.foto(self, "Esta bloqueado")
                        assert enabled, "Error, al parecer el boton esta deshabilitado y este deberia de estar habilitado"
                if i == 8:
                    enabled = Selenium.get_elements(self, elements[i]).is_enabled()
                    text = Selenium.get_elements(self, elements[i]).text
                    if not text == "CREAR":
                        Selenium.foto(self, "No es igual")
                        assert text == "CREAR", f"ERROR, el nombre del boton '{elements[i]}' no es igual a 'CREAR'"
                    if enabled:
                        Selenium.foto(self, "Esta bloqueado")
                        assert not enabled, "Error, al parecer el boton esta habilitado, y este deberia de estar deshabilitado"

            emp = Selenium.check_invisibility_element_located(self, "empresaOther")
            if not emp:
                Selenium.foto(self, "empresa")
                assert emp, "ERROR, SE VISUALIZA EL CAMPO DE 'OTRA EMPRESA'"

            dep = Selenium.check_invisibility_element_located(self, "departamentoOther")
            if not dep:
                Selenium.foto(self, "empresa")
                assert dep, "ERROR, SE VISUALIZA EL CAMPO DE 'OTRA EMPRESA'"

            message = Selenium.check_exists_by_xpath(self, "//p[contains(text(),'Usuario ya existe')]")
            if message:
                Selenium.foto(self, "mensaje")
                assert not message, "Error, APARECE EL MENSAJE DE QUE EL USUARIO YA EXISTE DEBAJO DEL INPUT " \
                                "'NOMBRE DE USUARIO', y en este modal deberia de estar todo vacio, ya que se esta " \
                                "abriendo denuevo"
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False