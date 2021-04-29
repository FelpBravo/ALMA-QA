import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
import subprocess


def test_UrlValidacionCar(driver):
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, "Carga documentos"))).click()
    url = driver.current_url
    print("URL Actual",url)
    time.sleep(1)




    #Validación boton cargar
    btncargar = driver.find_element_by_xpath("//span[contains(text(),'Cargar')]")
    if (btncargar.is_enabled() == True):
        print("Boton 'CARGAR' se habilita")
    else:
        print("Boton 'CARGAR' NO se habilita")


    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[2]/div[1]/div[1]/div/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div[2]/div/ul/div[1]/li[1]/i").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div[2]/div/ul/div/li/div").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[2]/div[2]/div/div/select").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[2]/div[2]/div/div/select/option[3]").click()
   # adj = driver.find_element_by_xpath("//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]")
    #adj.send_keys('eejemplo3.pdf')
    #i1 = 'C:\\Users\\Ignacio\\Desktop\\ejemplos\\eejemplo4.PDF'
    driver.find_element_by_xpath("//input[@type='file']").send_keys('C:\\Users\\Ignacio\\Desktop\\ejemplos\\eejemplo3.PDF')
    #mensajeError = driver.find_element_by_xpath("/html[1]/body[1]/div[5]/div[1]/div[1]/h2[1]").isDisplayed()
    msjError = driver.findElement(By.XPATH("//button[contains(text(),'OK')]"))
    print(msjError)
    driver.find_element_by_xpath("//input[@type='file']")
    #driver.assertTrue(mensajeError)
    time.sleep(2)

    #                                           Formulario

    # ALMA Doc Number
    form1 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[2]/div[1]/div/div/input")
    form1.send_keys("Ejemplo4")
    time.sleep(1)
    # Project Code
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[2]/div[2]/div/div/input").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div[1]/div/div/ul/div[5]").click()
    time.sleep(1)
    # Fecha
    date1 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[2]/div[3]/div/div/input")
    date1.send_keys("2021-03-01")
    # Modified by
    form2 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[3]/div[1]/div/div/input")
    form2.send_keys("Test3")
    time.sleep(1)
    # Organization
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[3]/div[2]/div/div/input").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div[1]/div/div/ul/div[2]").click()
    # Owner Name
    form3 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[3]/div[3]/div/div/input")
    form3.send_keys("Ejemplo Nombre2")
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

    # Etiqueta
    driver.find_element_by_css_selector("#demo-mutiple-checkbox").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[3]/ul/li[3]/div/span").click()
    driver.find_element_by_xpath("/html/body/div[5]/div[1]").click()
    time.sleep(3)
    btncargar.click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
    time.sleep(2)
    if (driver.find_element_by_xpath("/html/body/div[5]/div/div[1]").is_displayed()):
        print("Éxito al subir documento")
    else:
        print("Carga fallida")
    # Cargar Documento
    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
    time.sleep(2)
