from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from urllib3.util import wait


def testIniciarSesion(driver):
    user = "felipe.bravo"
    pwd = "1234"
    time.sleep(1)

    #Declaracion de variables
    botonAcceder = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/button")
    usuario = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/div[1]/div/input")
    password = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/div[2]/div/input")
    olvidePass = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/div[3]/span")



    print("Titulo actual: ",driver.title)
    # Validar estado del boton
    if (botonAcceder.is_enabled() == False):
        print("Boton 'ACCEDER' deshabilitado")
    else:
        print("Boton 'ACCEDER' habilitado sin campos rellenados")
    time.sleep(2)

    #Ingreso de user y password
    usuario.send_keys(user)
    time.sleep(1)
    password.send_keys(pwd)
    time.sleep(1)

    #Validar visibilidad de los elementos
    if usuario.is_displayed() and password.is_displayed():
        print("Los elemento se muestran correctamente")
    else:
        print("No se muestan los elementos", usuario," ",password)

    print("Estado de 'RECORDAR CONTRASEÑA'",olvidePass.is_selected())
    time.sleep(1)


    # Validar estado del boton
    if (botonAcceder.is_enabled() == True):
        print("Boton 'ACCEDER' se habilita")
    else:
        print("Boton 'ACCEDER' NO se habilita")

    time.sleep(1)
    botonAcceder.click()
    time.sleep(3)
    if(driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div/ul/li[2]/div/div[2]").is_displayed()):
        print("Se inicia sesion")
    else:
        print("Login failed")
    print("Titulo actual: ",driver.title)
    time.sleep(1)


