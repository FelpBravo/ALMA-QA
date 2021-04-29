import time
from selenium.webdriver.common.by import By

class PageLogin :

    def __init__(self, myDriver):
        self.driver = myDriver
        self.email = (By.XPATH,"//body/div[@id='app-site']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]")
        self.pw = (By.XPATH,"//body/div[@id='app-site']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/input[1]")
        self.recordarPw = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/form/div[3]/label/svg")
        self.olvidePw = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/form/div[3]/span")
        self.btn = (By.XPATH,"//body/div[@id='app-site']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/button[1]")

    def login(self, user, password):
        self.driver.find_element(*self.email).send_keys(user)
        self.driver.find_element(*self.pw).send_keys(password)
        self.driver.find_element(*self.btn).click()
        for request in self.driver.requests:
            if request.response:
                try:
                    assert request.response.status_code < 399, f"ERROR, STATUS {request.response.status_code} CODE"
                except:
                    print(f"ERROR, STATUS CODE {request.response.status_code}  -  WITH URL {request.url}")