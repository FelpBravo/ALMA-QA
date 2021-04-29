import time
from selenium.webdriver.common.by import By

class PageTag :

    def __init__(self, myDriver):
        self.driver = myDriver
        self.tree = (By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[1]/nav/div[1]/div[2]/div[3]/a/span")
        self.edit= (By.XPATH, "/html/body/div[1]/div/div/div[3]/main/div/div/div/div[1]/div/div/div/div[3]/div/div/table/tbody/tr[1]/td/div/div[1]")
        self.editName= (By.XPATH, "//body/div[4]/div[3]/div[1]/div[2]/div[1]/div[1]/input[1]")
        self.buttonEdit= (By.XPATH, "//body/div[4]/div[3]/div[1]/div[3]/button[2]")
        self.editColor= (By.XPATH, "//body/div[4]/div[3]/div[1]/div[2]/div[2]/div[3]/span[2]/div[1]")

        self.confirmDelete = (By.XPATH, "/html/body/div[4]/div/div[3]/button[1]")
        self.create = (By.XPATH,"/html/body/div[1]/div/div/div[3]/main/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/button")
        self.name = (By.XPATH, "/html/body/div[4]/div[3]/div/div[2]/div[1]/div/input")
        self.color = (By.XPATH, "/html/body/div[4]/div[3]/div/div[2]/div[2]/div[3]/span[10]/div")
        self.cancel = (By.XPATH, "/html/body/div[4]/div[3]/div/div[3]/button[1]")
        self.save = (By.XPATH,"/html/body/div[4]/div[3]/div/div[3]/button[2]")

    def create_new_tag(self, nameT):
        time.sleep(2)
        self.driver.find_element(*self.tree).click()
        for i in range(10):
            self.driver.find_element(*self.create).click()
            time.sleep(1)
            self.driver.find_element(*self.name).clear()
            time.sleep(2)
            self.driver.find_element(*self.name).send_keys(nameT,i)
            self.selectColor= (By.XPATH ,f"//body/div[4]/div[3]/div[1]/div[2]/div[2]/div[3]/span[{i+1}]/div[1]")
            self.driver.find_element(*self.selectColor).click()
            time.sleep(1)
            self.driver.find_element(*self.save).click()
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

    def edit_tag(self, newNameT):
        time.sleep(1)
        self.driver.find_element(*self.tree).click()
        time.sleep(1)
        self.driver.find_element(*self.edit).click()
        time.sleep(1)
        self.driver.find_element(*self.editName).clear()
        time.sleep(1)
        self.driver.find_element(*self.editName).send_keys(newNameT)
        time.sleep(1)
        self.driver.find_element(*self.editColor).click()
        time.sleep(1)
        self.driver.find_element(*self.buttonEdit).click()
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

    def delete_tag(self):
        time.sleep(1)
        self.driver.find_element(*self.tree).click()
        time.sleep(1)
        for i in range(33):
            n= i+1
            self.delete = (By.XPATH, f"//tbody/tr[{n}]/td[1]/div[1]/div[2]/*[1]")
            self.driver.find_element(*self.delete).click()
            time.sleep(1)
            self.driver.find_element(*self.confirmDelete).click()
            for request in self.driver.requests:
                a=request.response.status_code
                if request.response:
                    print(
                    "STATUS CODE: ", request.response.status_code, "  -  ", "URL: ", request.url
                    )
                    try:
                        assert request.response.status_code < 399, f"ERROR, STATUS {a} CODE"
                    except:
                        print(f"ERROR, STATUS {a} CODE")




