import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.registPage import registerPage, loginData

class RegistTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_a_regist_success(self):
        browser = self.browser 
        browser.get(registerPage.url_regist)
        browser.find_element(By.ID, registerPage.jenis_kelamin).click()
        browser.find_element(By.ID, registerPage.nama_depan).send_keys('Putra')
        browser.find_element(By.ID, registerPage.nama_belakang).send_keys('Saragih')
        browser.find_element(By.ID, registerPage.email).send_keys('saragihputra78@gmail.com')
        browser.find_element(By.ID, registerPage.password).send_keys('putra123')
        browser.find_element(By.ID, registerPage.confirmpass).send_keys('putra123')
        browser.find_element(By.ID, registerPage.clik_regist).click()
        url = browser.current_url
        self.assertEqual(url, registerPage.url_dashboard)

    def test_b_regist_failed_emailsudahterdaftar(self):
        browser = self.browser 
        browser.get(registerPage.url_regist)
        browser.find_element(By.ID, registerPage.jenis_kelamin).click()
        browser.find_element(By.ID, registerPage.nama_depan).send_keys('topan')
        browser.find_element(By.ID, registerPage.nama_belakang).send_keys('Saragih')
        browser.find_element(By.ID, registerPage.email).send_keys('saragihputra78@gmail.com')
        browser.find_element(By.ID, registerPage.password).send_keys('putra123')
        browser.find_element(By.ID, registerPage.confirmpass).send_keys('putra123')
        browser.find_element(By.ID, registerPage.clik_regist).click()

    def test_c_regist_failed_emptypass(self):
        browser = self.browser 
        browser.get(registerPage.url_regist)
        browser.find_element(By.ID, registerPage.jenis_kelamin).click()
        browser.find_element(By.ID, registerPage.nama_depan).send_keys('topan')
        browser.find_element(By.ID, registerPage.nama_belakang).send_keys('Saragih')
        browser.find_element(By.ID, registerPage.email).send_keys('saragihputra78@gmail.com')
        browser.find_element(By.ID, registerPage.password).send_keys('')
        browser.find_element(By.ID, registerPage.confirmpass).send_keys('putra123')
        browser.find_element(By.ID, registerPage.clik_regist).click()
   

if __name__ == '__main__':
    unittest.main()