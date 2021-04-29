import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def administ(driver):
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, "Administración"))).click()
    url = driver.current_url
    print("URL Actual",url)
    time.sleep(2)
    nomWorkspace = "ejemplo9"
    nomForum = "Ejemplo Forum"
    nomFolder = "SubFolder1"

    driver.find_element_by_xpath("//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]").click()
    time.sleep(1)
    #Tipo de espacio (workspace)
    driver.find_element_by_xpath("//div[@id='mui-component-select-type']").click()
    driver.find_element_by_xpath("//body/div[@id='menu-type']/div[3]/ul[1]/li[1]").click()
    time.sleep(1)
    #Nombre
    formAd = driver.find_element_by_xpath("//body/div[4]/div[3]/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]")
    formAd.send_keys(nomWorkspace)
    time.sleep(1)
    driver.find_element_by_xpath("// span[contains(text(), 'Guardar')]").click()
    time.sleep(1)
    if (driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/table/tbody/tr[1]/th").is_displayed()):
        print("Se creó Workspace con el nombre: ", nomWorkspace)
    else:
        print("Falló al crear Workspace")
    time.sleep(1)
    driver.find_element_by_xpath("//tbody/tr[1]/th[1]").click()
    time.sleep(1)

    #Crear forum
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/button").click()
    formForum = driver.find_element_by_xpath("/ html / body / div[4] / div[3] / div / div[2] / div[3] / div[1] / div / input")
    formForum.send_keys(nomForum)
    time.sleep(1)
    driver.find_element_by_xpath("// div[ @ id = 'mui-component-select-type']").click()
    driver.find_element_by_xpath("//body/div[@id='menu-type']/div[3]/ul[1]/li[1]").click()
    time.sleep(1)
    #Guardar
    driver.find_element_by_xpath("// span[contains(text(), 'Guardar')]").click()
    time.sleep(2)
    #Verificar guardado
    if (driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/table/tbody/tr/th").is_displayed()):
        print("Se creó Forum con el nombre: ", nomForum)
    else:
        print("Falló al crear Forum")
    time.sleep(2)
    driver.find_element_by_xpath("// tbody / tr[1] / th[1]").click()
    time.sleep(1)
    #Crear folder
    driver.find_element_by_xpath("// body / div[ @ id = 'app-site'] / div[1] / div[1] / div[3] / main[1] / div[1] / div[1] / div[1] / div[1] / div[1] / div[2] / div[1] / div[1] / div[2] / button[1]").click()
    #Nombre
    formFolder = driver.find_element_by_xpath("// body / div[4] / div[3] / div[1] / div[2] / div[3] / div[1] / div[1] / input[1]")
    formFolder.send_keys(nomFolder)
    time.sleep(1)
    #Tipo
    driver.find_element_by_xpath("//div[@id='mui-component-select-type']").click()
    driver.find_element_by_xpath("//body/div[@id='menu-type']/div[3]/ul[1]/li[1]").click()
    time.sleep(1)
    #Guardar
    driver.find_element_by_xpath("// span[contains(text(), 'Guardar')]").click()
    #Verificar
    if (driver.find_element_by_xpath("//tbody/tr[1]/th[1]").is_displayed()):
        print("Se creó Folder con el nombre: ", nomFolder)
    else:
        print("Falló al crear Folder")
    time.sleep(2)
    driver.find_element_by_xpath("// a[contains(text(), 'General')]").click()

