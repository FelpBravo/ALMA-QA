
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class dashboardPage :

    def __init__(self, myDriver):
        self.driver = myDriver
        self.search = (By.XPATH,"*//div[1]/div[1]/div[1]/input[1]")
        self.bSearch= (By.XPATH, "//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]")
        self.buttonSavedSearch= (By.XPATH, "//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]")
        self.selectSaveSearch= (By.XPATH, "//body/div[4]/div[3]/nav[1]/div[3]")
        self.tabla = (By.CLASS_NAME, "MuiTable-root")
        self.editColor= (By.XPATH, "//body/div[4]/div[3]/div[1]/div[2]/div[2]/div[3]/span[2]/div[1]")
        self.delete = (By.XPATH,"//tbody/tr[18]/td[1]/div[1]/div[2]")
        self.confirmDelete = (By.XPATH, "/html/body/div[4]/div/div[3]/button[1]")

    def search_advan_doc(self):
        pass

    def select_click_search_saved(self):
        time.sleep(3)
        SearchSave = (By.XPATH, "//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]")
        self.driver.find_element(*SearchSave).click()

    def select_search_saved(self, favoriteSaved):
        mySearchSave = (By.XPATH, f"//div[contains(text(),'{favoriteSaved}')]")
        self.driver.find_element(*mySearchSave).click()

    def select_search_advanced(self):
        time.sleep(2)
        clickSearchAdv = (By.XPATH, "//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]")
        self.driver.find_element(*clickSearchAdv).click()

    def select_form(self):
        pass

    def search_name_doc(self):
        time.sleep(5)
        self.driver.find_element(*self.search).send_keys("example")
        self.driver.find_element(*self.bSearch).click()
        #table_xpath = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='app-site']/div[1]/div[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/table[1]")))
        #rows = table_xpath.find_elements(By.TAG_NAME,"tr").text
        declararT = self.driver.find_element(*self.tabla).text
        declararT_split= declararT.split("\n")
        print(declararT_split)
        for tr_split in declararT_split:
            print(tr_split)
            separarDenuevo = tr_split.split(" ")
            for tr_split2 in separarDenuevo:
                print(tr_split2[10])
                if tr_split2 == "Acciones":
                    print("Se encontro la palabra Acciones")



    def saved_search(self):
        self.driver.find_element(*self.buttonSavedSearch).click()
        time.sleep(1)
        self.driver.find_element(*self.selectSaveSearch).click()
        time.sleep(1)
        for request in self.driver.requests:
            a = request.response.status_code
            if request.response:
                print(
                    "STATUS CODE: ", request.response.status_code, "  -  ", "URL: ", request.url
                )
                try:
                    assert request.response.status_code < 399, f"ERROR, STATUS {a} CODE"
                except:
                    print(f"ERROR, STATUS {a} CODE")
                time.sleep(1)
