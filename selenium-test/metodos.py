import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def assertIsInstance(elem, driver, param):
    pass


def iniciarsesion(driver):
    user = "admin"
    pwd = "Alma2021"
    time.sleep(1)

    # Declaracion de variables
    botonAcceder = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/button")
    usuario = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/div[1]/div/input")
    password = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/div[2]/div/input")

    # Validar estado del boton
    if (botonAcceder.is_enabled() == False):
        print("Boton 'ACCEDER' deshabilitado")
    else:
        print("Boton 'ACCEDER' habilitado sin campos rellenados")

    # Ingreso de user y password
    time.sleep(2)
    usuario.send_keys(user)
    time.sleep(1)
    password.send_keys(pwd)
    time.sleep(1)

    # Validar visibilidad de los elementos
    if usuario.is_displayed() and password.is_displayed():
        print("Los elementos se muestran correctamente")
    else:
        print("No se muestan los elementos", usuario, " ", password)

    # Validar estado del boton
    if (botonAcceder.is_enabled() == True):
        print("Boton 'ACCEDER' se habilita")
    else:
        print("Boton 'ACCEDER' NO se habilita")

    time.sleep(1)
    botonAcceder.click()
    time.sleep(3)
    if (
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div/ul/li[2]/div/div[2]").is_displayed()):
        print("Login sucess")
    else:
        print("Login failed")

def etiquetas(driver):
    nom_etiq = "Tag222"
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "Etiquetas"))).click()
    # Nombre
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/button").click()
    etiquet = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[1]/div/input").send_keys(nom_etiq)
    time.sleep(1)
    # Color
    etiquet = driver.find_element_by_xpath('//*[@title="#EB144C"]').click()
    # etiquet = browser.find_element_by_xpath('//*[@title="##9900EF"]').click()
    time.sleep(1)
    etiquet = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[3]/button[2]/span[1]").click()

def administracion(driver):
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, "Administración"))).click()
    # driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[1]/nav/div[1]/div[2]/div[2]/a").click()
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/button"))).click()
    driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]").click()
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "button.MuiTypography-root"))).click()
    # adminis.click()

    # .find_element_by_xpath('//div[@class="MuiTypography-root"]/*[name()="svg"][@aria-label="Search"]').click()

def cargadocumentos(driver):
    time.sleep(3)
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, "Carga documentos"))).click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[2]/div[1]/div[1]/div/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div[2]/div/ul/div[5]/li[1]/i").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div[2]/div/ul/div/li/div").click()
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[2]/div[2]/div/div/select").click()
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[2]/div[2]/div/div/select/option[3]").click()
    time.sleep(8)
    #                                           Formulario

    # ALMA Doc Number
    form1 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[2]/div[1]/div/div/input")
    form1.send_keys("Ejemplo")
    time.sleep(1)
    # Project Code
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[2]/div[2]/div/div/input").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div[1]/div/div/ul/div[5]").click()
    time.sleep(1)
    # Fecha
    date1 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[2]/div[3]/div/div/input")
    date1.send_keys("2021-03-31")
    # Modified by
    form2 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[3]/div[1]/div/div/input")
    form2.send_keys("Test")
    time.sleep(1)
    # Organization
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[3]/div[2]/div/div/input").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div[1]/div/div/ul/div[2]").click()
    # Owner Name
    form3 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[3]/div[3]/div/div/input")
    form3.send_keys("Ejemplo Nombre")
    time.sleep(1)
    # Subject
    form4 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[4]/div[1]/div/div/input")
    form4.send_keys("Ejemplo Tema")
    time.sleep(1)
    # File Type
    form4 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[4]/div[2]/div/div/input")
    form4.send_keys("PNG")
    time.sleep(1)
    # Author
    form5 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[4]/div[3]/div/div/input")
    form5.send_keys("Team QA")
    time.sleep(1)
    # Document Status
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[5]/div[1]/div/div/input").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div[1]/div/div/ul/div[5]").click()

    # System
    form6 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[5]/div[3]/div/div/input")
    form6.send_keys("Ejemplo System")
    time.sleep(1)
    # Security Mode
    form7 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[6]/div[1]/div/div/input")
    form7.send_keys("Ejemplo Security Mode")
    time.sleep(1)
    # Release By
    form8 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[6]/div[2]/div/div/input")
    form8.send_keys("Ejemplo Release")
    time.sleep(1)
    # DocID
    form9 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[6]/div[3]/div/div/input")
    form9.send_keys("1234")
    time.sleep(1)
    # ForumID
    form10 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[7]/div[1]/div/div/input")
    form10.send_keys("EjForumID")
    time.sleep(1)
    # Document Type
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[7]/div[2]/div/div/input").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div[1]/div/div/ul/div[8]").click()
    time.sleep(1)
    # Approved By
    form11 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[7]/div[3]/div/div/input")
    form11.send_keys("EJ Nombre")
    time.sleep(1)
    # Reviewed By
    form12 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[8]/div[1]/div/div/input")
    form12.send_keys("EJ Nombre2")
    time.sleep(1)
    # Gruop/Area
    form13 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[8]/div[2]/div/div/input")
    form13.send_keys("Recursos Humanos")
    time.sleep(1)
    # Document Abstract
    form13 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[8]/div[3]/div/div/input")
    form13.send_keys("Ej Document")
    time.sleep(1)

    # Etiquetas
    driver.find_element_by_css_selector("#demo-mutiple-checkbox").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/ul/li[3]/div/span").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[contains(text(),'Cargar')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
    time.sleep(2)
    # Cargar Documento
    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
    time.sleep(2)