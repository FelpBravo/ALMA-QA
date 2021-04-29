from page.dashboardPage import dashboardPage
from page.loginPage import PageLogin
from helpers.data import *
import HtmlTestRunner
import unittest
from page.loadDocPag import *
from seleniumwire import webdriver


class test_tag_001(unittest.TestCase):

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

    def test_tag_create(self):
        self.page_login.login(self.user1.user,self.user1.password)
        self.pag_tag.create_new_tag(self.nTag.nTag)
        for request in self.driver.requests:
            self.page_login.login(self.user1.user, self.user1.password)
            self.pag_tag.create_new_tag(self.nTag.nTag)
            if request.response:
                print("STATUS CODE: ",request.response.status_code,"  -  ","URL: ",request.url)

    def test_tag_delete(self):
        self.page_login.login(self.user1.user,self.user1.password)
        self.pag_tag.delete_tag()
        for request in self.driver.requests:
            self.page_login.login(self.userAdm.user, self.userAdm.password)
            self.pag_tag.delete_tag
            if request.response:
                print("STATUS CODE: ",request.response.status_code,"  -  ","URL: ",request.url)

    @unittest.skip("Sin ejecución")
    def test_tag_edit(self):
        pass

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
