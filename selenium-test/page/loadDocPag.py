import time
from selenium.webdriver.common.by import By
import os

import subprocess


class loadDocPag :

    def __init__(self, myDriver):
        self.driver = myDriver
        self.tree = (By.LINK_TEXT, "Carga documentos")
        self.btncargar = (By.XPATH,"//span[contains(text(),'Cargar')]")
        self.folder = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[2]/div[1]/div[1]/div/input")
        self.selectFol = (By.XPATH,"//span[contains(text(),'prueba')]")
        self.selectSubFolder = (By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div[2]/div/ul/div/li/div")
        self.optionFolder = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[2]/div[2]/div/div/select")
        self.nIcd = (By.XPATH, "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[2]/div[2]/div/div/select/option[3]")
        self.selectDoc = (By.XPATH, "//input[@type='file']")
        #FORMULARIO
        self.almaDoc = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[2]/div[1]/div/div/input")
        self.projectCode = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[2]/div[2]/div/div/input")
        self.selectProjectCode = (By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div[1]/div/div/ul/div[5]")
        self.date = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[2]/div[3]/div/div/input")
        self.modifiedBy = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[3]/div[1]/div/div/input")
        self.org = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[3]/div[2]/div/div/input")
        self.selectOrg = (By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div[1]/div/div/ul/div[2]")
        self.ownerName = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[3]/div[3]/div/div/input")
        self.subject = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[4]/div[1]/div/div/input")
        self.fielType = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[4]/div[2]/div/div/input")
        self.author = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[4]/div[3]/div/div/input")
        self.docStatus = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[5]/div[1]/div/div/input")
        self.selectDocStatus = (By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div[1]/div/div/ul/div[5]")
        self.system = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[5]/div[3]/div/div/input")
        self.secMode = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[6]/div[1]/div/div/input")
        self.releaseBy = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[6]/div[2]/div/div/input")
        self.docId = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[6]/div[3]/div/div/input")
        self.forumId = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[7]/div[1]/div/div/input")
        self.docType = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[7]/div[2]/div/div/input")
        self.selectDocType = (By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div[1]/div/div/ul/div[8]")
        self.approvedBy = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[7]/div[3]/div/div/input")
        self.revBy = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[8]/div[1]/div/div/input")
        self.group = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[8]/div[2]/div/div/input")
        self.docAbs = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[8]/div[3]/div/div/input")
        #ETIQUETAS
        self.checkbox1 = (By.CSS_SELECTOR, "#demo-mutiple-checkbox")
        self.selectcheck = (By.XPATH, "/html/body/div[5]/div[3]/ul/li[3]/div/span")
        self.campblanco = (By.XPATH, "/html/body/div[5]/div[1]")
        self.docAbs = (By.XPATH,
                       "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[8]/div[3]/div/div/input")
        self.docAbs = (By.XPATH,
                       "/html/body/div[1]/div/div/div[3]/main/div/div/div/div/div/form/div[6]/div/div[8]/div[3]/div/div/input")
        self.btncarga1 = (By.XPATH, "//span[contains(text(),'Cargar')]")
        self.btncarga2 = (By.XPATH, "//button[contains(text(),'OK')]")
        self.btncarga3 = (By.XPATH, "//button[contains(text(),'OK')]")
        self.msjeok = (By.XPATH, "/ html / body / div[5] / div / div[1]")

    def select_tree_load_doc (self):
        time.sleep(2)
        self.driver.find_element(*self.tree).click()
        time.sleep(2)

    def select_dir(self):
        self.driver.find_element(*self.folder).click()
        time.sleep(1)

    def select_sub_dir(self, folderOne):
        selectFol = (By.XPATH,f"//span[contains(text(),'{folderOne}')]")
        self.driver.find_element(*selectFol).click()

    def select_icd_no_icd (self):
        self.driver.find_element(*self.optionFolder).click()
        time.sleep(1)
        self.driver.find_element(*self.nIcd).click()

    def select_load_new_doc(self, imgNew):
        self.driver.find_element(*self.selectDoc).send_keys(imgNew)
        time.sleep(2)

    def select_load_equals_doc(self, imgRep):
        self.driver.find_element(*self.selectDoc).send_keys(imgRep)

    def select_complete_form(self, almadoc, date, modifiedby, ownername, subject, fieltype, author, system, secmode, releaseby, docid, forumid, approvedby, revby, group, docabs):
        self.driver.find_element(*self.almaDoc).send_keys(almadoc)
        self.driver.find_element(*self.projectCode).click()
        self.driver.find_element(*self.selectProjectCode).click()
        self.driver.find_element(*self.date).send_keys(date)
        self.driver.find_element(*self.modifiedBy).send_keys(modifiedby)
        self.driver.find_element(*self.org).click()
        self.driver.find_element(*self.selectOrg).click()
        self.driver.find_element(*self.ownerName).send_keys(ownername)
        self.driver.find_element(*self.subject).send_keys(subject)
        self.driver.find_element(*self.fielType).send_keys(fieltype)
        self.driver.find_element(*self.author).send_keys(author)
        self.driver.find_element(*self.docStatus).click()
        self.driver.find_element(*self.selectDocStatus).click()
        self.driver.find_element(*self.system).send_keys(system)
        self.driver.find_element(*self.secMode).send_keys(secmode)
        self.driver.find_element(*self.releaseBy).send_keys(releaseby)
        self.driver.find_element(*self.docId).send_keys(docid)
        self.driver.find_element(*self.forumId).send_keys(forumid)
        self.driver.find_element(*self.docType).click()
        self.driver.find_element(*self.selectDocType).click()
        self.driver.find_element(*self.approvedBy).send_keys(approvedby)
        self.driver.find_element(*self.revBy).send_keys(revby)
        self.driver.find_element(*self.group).send_keys(group)
        self.driver.find_element(*self.docAbs).send_keys(docabs)

    def select_tag (self):
        self.driver.find_element(*self.checkbox1).click()
        self.driver.find_element(*self.selectcheck).click()
        self.driver.find_element(*self.campblanco).click()
        time.sleep(1)

    def select_button_load(self):
        time.sleep(3)
        self.driver.find_element(*self.btncarga1).click()
        time.sleep(3)

    def select_button_load_confirm(self):
        self.driver.find_element(*self.btncarga2).click()


    def getStatus(self):
        for request in self.driver.requests:
            if request.response:
                try:
                    assert request.response.status_code < 399, f"ERROR, STATUS {request.response.status_code} CODE"
                except:
                    print(f"ERROR, STATUS CODE {request.response.status_code}  -  WITH URL {request.url}")