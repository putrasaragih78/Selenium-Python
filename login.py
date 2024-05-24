import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.loginPage import loginPage

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_a_login_success(self):
        browser = self.browser 
        browser.get(loginPage.url_login)
        browser.find_element(By.ID, loginPage.email).send_keys('saragihputra78@gmail.com')
        browser.find_element(By.ID, loginPage.password).send_keys('putra123')
        browser.find_element(By.CSS_SELECTOR, loginPage.button_login).click()
        url = browser.current_url
        self.assertEqual(url, loginPage.url_dashboard)
        
    def test_b_login_failed_emptypass(self):
        browser = self.browser 
        browser.get(loginPage.url_login)
        browser.find_element(By.ID, loginPage.email).send_keys('saragihputra78@gmail.com')
        browser.find_element(By.ID, loginPage.password).send_keys('')
        browser.find_element(By.CSS_SELECTOR, loginPage.button_login).click()
        url = browser.current_url
        self.assertEqual(url, loginPage.url_login)
       
        
        # Ambil pesan kesalahan
        error_message_element = browser.find_element(By.CSS_SELECTOR, loginPage.validasi_summary)
        error_message = error_message_element.text
        
        # Cetak pesan kesalahan untuk verifikasi
        print("Pesan Kesalahan: ", error_message)
        
        # Verifikasi pesan kesalahan (ganti dengan pesan kesalahan yang sesuai)
        expected_error_message = loginPage.msg_error
        self.assertIn(expected_error_message, error_message)
    
    def tearDown(self):
        self.browser.quit()

    def test_c_login_failed_invalidpass(self):
        browser = self.browser 
        browser.get(loginPage.url_login)
        browser.find_element(By.ID, loginPage.email).send_keys('saragihputra78@gmail.com')
        browser.find_element(By.ID, loginPage.password).send_keys('123')
        browser.find_element(By.CSS_SELECTOR, loginPage.button_login).click()
        url = browser.current_url
        self.assertEqual(url, loginPage.url_login)

if __name__ == '__main__':
    unittest.main()