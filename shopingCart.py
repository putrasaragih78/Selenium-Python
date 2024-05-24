import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class ShopingCartTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()



    def test_a_checkout_success(self):
        browser = self.browser 
        browser.get('https://demowebshop.tricentis.com/login')
        browser.find_element(By.ID, 'Email').send_keys('saragihputra78@gmail.com')
        browser.find_element(By.ID, 'Password').send_keys('putra123')
        browser.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()
        browser.get('https://demowebshop.tricentis.com/books')
        browser.find_element(By.CSS_SELECTOR, '.button-2.product-box-add-to-cart-button').click()

        # Tunggu sampai notifikasi muncul
        notification = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.bar-notification.success'))
        )      
        # Ambil teks dari notifikasi
        notification_text = notification.text
        print("Notification Text: ", notification_text)
        
        # Verifikasi teks notifikasi (sesuaikan dengan teks notifikasi yang diharapkan)
        expected_text = 'The product has been added to your shopping cart'
        self.assertIn(expected_text, notification_text)
        
        browser.get('https://demowebshop.tricentis.com/cart')
        browser.find_element(By.ID, 'CountryId').send_keys('Indonesia')
        browser.find_element(By.ID, 'ZipPostalCode').send_keys('12790')
        #browser.find_element(By.CSS_SELECTOR, '.button-2.estimate-shipping-button').click()
        browser.find_element(By.ID, 'termsofservice').click()
        browser.find_element(By.CSS_SELECTOR, '.button-1.checkout-button').click()

        WebDriverWait(browser, 10).until
        country_select = Select(browser.find_element(By.ID, 'BillingNewAddress_CountryId'))
        country_select.select_by_visible_text('Indonesia')
        

        
        
if __name__ == '__main__':
    unittest.main()