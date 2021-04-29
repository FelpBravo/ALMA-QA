from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains

def crearEtiqueta(driver):
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[1]/nav/div[1]/div[2]/div[3]/a/span").click()
    url = driver.current_url
    print("URL Actual", url)
    time.sleep(1)
    time.sleep(1)
    for i in range(1):
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/main/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/button").click()

        elem = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div[2]/div[1]/div/input")
        elem.clear()
        elem.send_keys("EtiquetaQA00",i)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div[2]/div[2]/div[3]/span[10]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div[3]/button[2]/span[1]").click()
        time.sleep(1)


def eliminarEtiqueta(driver):
    driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/header/div/button").click()
    driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]/nav/div[1]/div[2]/div[3]").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/main/div/div/div/div[1]/div/div/div/div[3]/div/div/table/tbody/tr[19]/td/div/div[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()