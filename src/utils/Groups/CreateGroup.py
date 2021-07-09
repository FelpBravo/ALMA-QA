from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.functions.functions import Functions as Selenium

class CreateGroup:

    def modal(self):  #RETORNA TRUE O FALSE, SI VISUALIZA TODOS LOS ELEMENTOS DEL MODAL.
        Selenium.get_json_file(self, "groups")
        try:
            visual = Selenium.check_visibility_element_located(self, "Modal crear agregar")
            assert visual, "ERROR, No se visualiza el modal de CREAR GRUPOS"

            check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),'Crear nuevo grupo')]")
            assert check, "ERROR, El titulo del modal ya no es el mismo, este a cambiado"

            elements = ['dependencia', 'perfiles', 'nombre de grupo', 'categories', 'cancelar', 'crear']

            for i in range(len(elements)):
                check = Selenium.check_element(self, elements[i])

                if i < 3:
                    value = Selenium.get_elements(self, elements[i]).get_attribute("value")
                    if not value == "":
                        Selenium.foto(self, "error")
                        assert value == "", f"Error, el campo '{elements[i]}', contiene el valor='{value}', y este deberia de estar vacio."

                if not check:
                    Selenium.foto(self, "No existe")
                    assert check, f"ERROR, No se encuentra el elemento '{elements[i]}'"

                if i == 3:
                    check = Selenium.check_exists_by_xpath(self, "//div[contains(text(),'Crear nuevo grupo')]")
                    assert check, "ERROR, El titulo del modal ya no es el mismo, este a cambiado"

                    message = Selenium.check_exists_by_xpath(self, "//p[contains(text(),'Grupo ya existe')]")
                    if message:
                        Selenium.foto(self, "mensaje")
                        assert not message, "Error, AL ABRIR NUEVAMENTE EL MODAL, APARECE EL MENSAJE DE QUE EL GRUPO YA " \
                                            "EXISTE DEBAJO DEL INPUT 'NOMBRE DE GRUPO'"

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
                            assert not enabled, "Error, al parecer el boton esta habilitado, y este deberia de estar deshabilitado"
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False