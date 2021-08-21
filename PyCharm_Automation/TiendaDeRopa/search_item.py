import unittest
from selenium import webdriver
import time
from pageIndex import PageIndex
from pageItems import PageItems


class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)

    def test_search_no_elements(self):
        self.indexPage.search('hola')
        time.sleep(2)
        self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "hola"')

    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        time.sleep(2)
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    def test_search_find_tshirt(self):
        self.indexPage.search('t-shirt')
        time.sleep(2)
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()