# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import logging
from page.dashboardPage import *
from page.loginPage import *
from page.tagPage import *
from helpers.data import *
import requests
import HtmlTestRunner
import unittest
from page.loadDocPag import *
from seleniumwire import webdriver
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class testing_load_doc (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://10.200.33.17/auth/signin')
        self.page_login = PageLogin(self.driver)
        self.userAdm = data_login_by_userAdm()
        self.page_buscar = dashboardPage(self.driver)
        self.page_load = loadDocPag(self.driver)
        self.form = data_form_doc()
        self.docEquals = data_load_doc_equals()
        self.docNew1 = data_load_doc_new()

    def test_load_doc_prev_alma_id(self):
        self.page_login.login(self.userAdm.user, self.userAdm.password)
        self.page_load.select_tree_load_doc()
        self.page_load.select_dir()
        selectFolder = (By.XPATH, "//body/div[5]/div[3]/div[1]/div[2]")
        getTextFolders = self.driver.find_element(*selectFolder).text
        divFolders = getTextFolders.split("\n")
        folderOne = divFolders[1]
        logging.error(f'No se ah encontrado la carpeta {folderOne}')
        logging.info(f'Se ingresa a la carpeta {folderOne}')
        self.page_load.select_sub_dir(folderOne)
        self.page_load.select_icd_no_icd()
        metadataForm = (By.XPATH, "//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[6]/div[1]")
        getTextMeta= self.driver.find_element(*metadataForm).text
        self.assertIn("Metadata", getTextMeta, "ERROR ! .. El formulario no se visualiza")
        self.page_load.select_load_new_doc(self.docNew1.imageNew)
        spaceLoad = (By.XPATH,
                     "//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]")
        getTextSpace = self.driver.find_element(*spaceLoad).text
        print(f"Comprobando que el archivo {self.docNew1.validImageNew}.png se suba correctamente...")
        time.sleep(1)
        self.assertIn(self.docNew1.validImageNew, getTextSpace, "Error, no se encuentra la imagen subida")
        print(f"Archivo {self.docNew1.validImageNew}.png subido...")
        self.page_load.select_complete_form(self.form.almaDoc, self.form.date, self.form.modifiedBy,
                                            self.form.ownerName, self.form.subject, self.form.fielType,
                                            self.form.author, self.form.system, self.form.secMode, self.form.releaseBy,
                                            self.form.docId, self.form.forumId, self.form.approvedBy, self.form.revBy,
                                            self.form.group, self.form.docAbs)
        self.page_load.select_tag()
        self.page_load.select_button_load()
        self.page_load.select_button_load_confirm()
        try:
            mesajeAlmaElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[5]")))
        except:
            print("ERROR! La confirmacion del AlmaID de carga de documentos no se previsualiza.....",mesajeAlmaElement.is_displayed())
        assert mesajeAlmaElement.is_displayed()
        spaceConfirmLoad = (By.XPATH, "//body/div[5]")
        getTextAlmaID = self.driver.find_element(*spaceConfirmLoad).text
        print(f"Esperando AlmaID...")
        time.sleep(1)
        self.assertIn("AlmaID", getTextAlmaID, "¡ERROR!. El AlmaID no se encuentra")
        time.sleep(1)
        print(f"Finalizando y comprobando el titulo esperado...")
        time.sleep(1)
        self.assertEqual("Biblioteca-Apiux", self.driver.title,f"Error. Titulo esperado ='Biblioteca-Apiux' - Titulo devuelto ='{self.driver.title}'")

    def test_load_normal_new_doc(self):
        self.page_login.login(self.userAdm.user, self.userAdm.password)
        self.page_load.select_tree_load_doc()
        self.page_load.select_dir()
        self.page_load.select_icd_no_icd()
        self.page_load.select_load_new_doc(self.docNew1.imageNew)
        spaceLoad = (By.XPATH,"//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]")
        getTextSpace = self.driver.find_element(*spaceLoad).text
        print(f"Comprobando que el archivo {self.docNew1.validImageNew}.png se suba correctamente...")
        time.sleep(1)
        self.assertIn(self.docNew1.validImageNew, getTextSpace, "Error, no se encuentra la imagen subida")
        print(f"Archivo {self.docNew1.validImageNew}.png subido...")
        self.page_load.select_complete_form(self.form.almaDoc, self.form.date, self.form.modifiedBy, self.form.ownerName, self.form.subject, self.form.fielType, self.form.author, self.form.system, self.form.secMode, self.form.releaseBy, self.form.docId, self.form.forumId, self.form.approvedBy, self.form.revBy, self.form.group, self.form.docAbs)
        self.page_load.select_tag()
        self.page_load.select_button_load()
        self.page_load.select_button_load_confirm()
        time.sleep(2)
        spaceConfirmLoad = (By.XPATH,"//body/div[5]")
        getTextAlmaID = self.driver.find_element(*spaceConfirmLoad).text
        print(f"Esperando AlmaID...")
        time.sleep(1)
        self.assertIn("AlmaID", getTextAlmaID, "¡ERROR!. El AlmaID no se encuentra")
        time.sleep(1)
        print(f"Finalizando y comprobando el titulo esperado...")
        time.sleep(1)
        self.assertEqual("Biblioteca-Apiux", self.driver.title,f"Error. Titulo esperado ='Biblioteca-Apiux' - Titulo devuelto ='{self.driver.title}'")

    def test_allow_load_new_doc(self):
        self.page_login.login(self.userAdm.user, self.userAdm.password)
        self.page_load.select_tree_load_doc()
        for x in range(10):
            n = random.randint(1, 26)
            print(f"Cargando archivo ....qa{n}.PNG")
            imageNew = f"C:\\Users\\pipe_\\Desktop\\QA\\qa{n}.PNG"
            self.page_load.select_load_new_doc(imageNew)
            time.sleep(2)
            bucket = (By.XPATH,f"//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]")
            getText = self.driver.find_element(*bucket).text
            self.assertIn(f"qa{n}", getText, f"¡ERROR!. El archivo qa{n} no se ha cargado ")
            print(f"qa{n}.PNG...¡Se ha Cargado!")
            time.sleep(2)
        self.page_load.getStatus()
        self.assertEqual("Biblioteca-Apiux", self.driver.title, f"Error.'{self.driver.title}' no es el titulo esperado")


    def test_allow_and_preview_doc(self):
        self.page_login.login(self.userAdm.user, self.userAdm.password)
        self.page_load.select_tree_load_doc()
        for x in range(1):
            n = random.randint(1, 26)
            print(f"Cargando archivo ....qa{n}.PNG")
            imageNew = f"C:\\Users\\pipe_\\Desktop\\QA\\qa{n}.PNG"
            self.page_load.select_load_new_doc(imageNew)
            time.sleep(2)
            bucket = (By.XPATH,f"//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]")
            getText = self.driver.find_element(*bucket).text
            self.assertIn(f"qa{n}", getText, f"¡ERROR!. El archivo qa{n} no se ha cargado ")
            print(f"qa{n}.PNG...¡Se ha Cargado!")
            time.sleep(2)
            self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/*[local-name()='svg'][1]").click()
            prev = (By.XPATH, "//body/div[2]/div[3]")
            getTextPrev = self.driver.find_element(*prev).text
            self.assertIn("visualización", getTextPrev, "¡ERROR!, la previsualizacion no aparece !!!")
            time.sleep(2)
            self.driver.find_element_by_xpath("//button[@aria-label='close']//span[@class='MuiIconButton-label']").click()
        self.page_load.getStatus()
        self.assertEqual("Biblioteca-Apiux", self.driver.title, f"Error.'{self.driver.title}' no es el titulo esperado")

    def test_deny_load_doc_equal(self):
        self.page_login.login(self.userAdm.user, self.userAdm.password)
        self.page_load.select_tree_load_doc()
        for x in range(2):
            n = random.randint(1, 10)
            imageRepeat = f"C:\\Users\\pipe_\\Desktop\\QA\\DocRepetidos\\Firewall{n}.PNG"
            print(f"Cargando archivo ....Firewall{n}.PNG")
            self.page_load.select_load_equals_doc(imageRepeat)
            time.sleep(2)
            mensajeError = (By.XPATH, "//div[@role='dialog']")
            getTextError = self.driver.find_element(*mensajeError).text
            self.assertIn(getTextError, "Error")
            print(f"Documento Firewall{n}.PNG Ya existe\n")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()
            spaceLoad = (By.XPATH, "//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]")
            getTextSpace = self.driver.find_element(*spaceLoad).text
            self.assertNotIn(getTextSpace ,f"Firewall{n}")
        self.page_load.getStatus()
        self.assertEqual("Biblioteca-Apiux", self.driver.title, f"Error. Titulo esperado ='Biblioteca-Apiux' - Titulo devuelto ='{self.driver.title}'")

    def test_allow_and_deny_doc(self):
        self.page_login.login(self.userAdm.user, self.userAdm.password)
        self.page_load.select_tree_load_doc()
        for x in range(5):
            n = random.randint(1, 10) #26
            print(f"Cargando archivo ....qa{n}.PNG")
            imageNew = f"C:\\Users\\pipe_\\Desktop\\QA\\qa{n}.PNG"
            time.sleep(1)
            self.page_load.select_load_new_doc(imageNew)
            time.sleep(3)
            spaceLoad = (By.XPATH,"//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]")
            getTextSpace = self.driver.find_element(*spaceLoad).text
            time.sleep(2)
            print(f"Comprobando que el archivo qa{n} se cargue correctamente...")
            time.sleep(1)
            self.assertIn(f"qa{n}", getTextSpace, f"¡ERROR!. El archivo qa{n} no se ha cargado ")
            print(f"qa{n}.PNG...¡Se ha Cargado!\n")
            time.sleep(1)
            print(f"Cargando archivo ....Firewall{n}.PNG")
            time.sleep(1)
            imageRep = f"C:\\Users\\pipe_\\Desktop\\QA\\DocRepetidos\\Firewall{n}.PNG"
            self.page_load.select_load_new_doc(imageRep)
            time.sleep(1)
            print(f"Comprobando que el archivo Firewall{n}.png no esté espacio de carga...")
            time.sleep(1)
            self.assertNotIn(f"Firewall{n}", getTextSpace, f"¡ERROR!. ¡¡¡El archivo Firewall{n} se ha cargado como repetido!!!")
            mesajeDocExist = (By.XPATH,"//body/div[5]/div[1]")
            getText_mesajeExist = self.driver.find_element(*mesajeDocExist).text
            print(f"Comprobando que el mensaje 'The document is already exists' aparezca...")
            time.sleep(1)
            self.assertIn("The document is already exists", getText_mesajeExist, f"¡ERROR!. ¡¡¡El mensaje de que el documento Firewall{n} ya existe No aparece!!!")
            buttonOk = (By.XPATH, "//button[contains(text(),'OK')]")
            self.driver.find_element(*buttonOk).click()
            time.sleep(1)
            print(f"Comprobando que el archivo qa{n}.png siga en el espacio de carga...\n")
            time.sleep(1)
            self.assertIn(f"qa{n}", getTextSpace, f"¡ERROR!. El archivo qa{n} cargado anteriormente. ¡¡NO SE ENCUENTRA EN LA PAGINA!! ")
            time.sleep(1)
        self.page_load.getStatus()
        self.assertEqual("Biblioteca-Apiux", self.driver.title, f"Error.'{self.driver.title}' no es el titulo esperado")

    def test_allow_and_delete_doc(self):
        self.page_login.login(self.userAdm.user, self.userAdm.password)
        self.page_load.select_tree_load_doc()
        for x in range(1):
            n = random.randint(1, 26)
            print(f"Cargando archivo ....qa{n}.png")
            imageNew = f"C:\\Users\\pipe_\\Desktop\\QA\\qa{n}.PNG"
            print(imageNew)
            self.page_load.select_load_new_doc(imageNew)
            time.sleep(2)
            bucket = (By.XPATH,"//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]")
            getText = self.driver.find_element(*bucket).text
            print(f"Comprobando que el archivo qa{n}.png se cargue correctamente...")
            time.sleep(1)
            self.assertIn(f"qa{n}", getText, f"¡ERROR!. El archivo qa{n} no se ha cargado ")
            print(f"qa{n}.PNG...¡Se ha Cargado!\n")
            time.sleep(2)
            print(f"Borrando documento qa{n}.png. . .")
            buttonDelet = (By.XPATH, "//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]")
            self.driver.find_element(*buttonDelet).click()
            time.sleep(2)
            confirmNoElement =  WebDriverWait(self.driver,10).until(EC.invisibility_of_element((By.XPATH, "//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]")))
            print(f"Comprobando que el archivo qa{n}.png se haya eliminado...")
            time.sleep(1)
            self.assertTrue(confirmNoElement, "ERROR documento es visible")
            print(f"El documento qa{n}.PNG se ah borrado exitosamente\n")
            time.sleep(2)
        print("Esperando el status...")
        time.sleep(2)
        self.page_load.getStatus()
        print("Finalizando y validando el titulo esperado...")
        time.sleep(1)
        self.assertEqual("Biblioteca-Apiux", self.driver.title, f"Error.'{self.driver.title}' no es el titulo esperado")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))