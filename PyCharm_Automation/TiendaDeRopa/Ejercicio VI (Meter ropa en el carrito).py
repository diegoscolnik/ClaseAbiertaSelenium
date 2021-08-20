import unittest
from selenium import webdriver
import time

class PreOrderTShirts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_search_tshirts(self):
        self.driver.find_element_by_id('search_query_top').send_keys('T-shirts')
        self.driver.find_element_by_name('submit_search').click()
        self.driver.find_elements_by_xpath('//*[@id="color_1"]').click()
        #self.driver.find_element_by_id('color_1').click()
        self.driver.find_element_by_xpath('//*[@id="quantity_wanted"]').clear()
        self.driver.find_element_by_xpath('//*[@id="quantity_wanted"]').send_keys(25)
        self.driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').click()
        self.driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').click()
        self.driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').click()
        #self.assertEqual('28', self.driver.find_element_by_xpath('//*[@id="quantity_wanted"]').get_attribute('value'))
        #self.assertTrue('28' in self.driver.find_element_by_xpath('//*[@id="quantity_wanted"]').get_attribute('value'))
        self.assertGreaterEqual('28', self.driver.find_element_by_xpath('//*[@id="quantity_wanted"]').get_attribute('value'))
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
