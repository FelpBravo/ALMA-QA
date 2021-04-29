from page.dashboardPage import *
from page.loginPage import *
from helpers.data import *
import HtmlTestRunner
import unittest
from page.loadDocPag import *
from seleniumwire import webdriver

class test_login_001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://10.200.33.17/auth/signin')
        self.page_login = PageLogin(self.driver)
        self.userAdm = data_login_by_userAdm()
        self.page_buscar = dashboardPage(self.driver)
        self.page_load = loadDocPag(self.driver)
        self.f = data_form_doc()
        self.docEquals = data_load_doc_equals()
        self.docNew1 = data_load_doc_new()

    def test_login_success(self):
        self.page_login.login(self.userAdm.user, self.userAdm.password)
        self.assertEqual("Biblioteca-Apiux", self.driver.title,f"Error. Titulo esperado ='Biblioteca-Apiux' - Titulo devuelto ='{self.driver.title}'")

    def test_login_failed(self):
        self.page_login.login(self.user2.user, self.user2.password)
        self.assertEqual("Biblioteca-Apiux", self.driver.title,f"Error. Titulo esperado ='Biblioteca-Apiux' - Titulo devuelto ='{self.driver.title}'")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
