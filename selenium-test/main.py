from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from loginQA import testIniciarSesion
from etiquetasQA import crearEtiqueta, eliminarEtiqueta
from cargadoc import test_UrlValidacionCar

def test_UrlValidacion(driver):
    url = driver.current_url
    print("URL Actual",url)
    for request in driver.requests:
        print(request.url)
    time.sleep(1)


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://10.200.33.17/")

assert "Biblioteca-Apiux" in driver.title
testIniciarSesion(driver)
# crearEtiqueta(driver)

test_UrlValidacionCar(driver)



