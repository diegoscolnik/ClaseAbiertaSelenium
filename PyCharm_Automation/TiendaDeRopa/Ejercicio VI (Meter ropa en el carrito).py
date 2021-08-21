import unittest
from selenium import webdriver
from pageIndex import PageIndex
from pageItems import PageItems
from pagePreOrder import PreOrder


class PreOrderTShirts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.preOrder = PreOrder(self.driver)

    def test_search_tshirts(self):
        self.indexPage.search('t-shirt')
        self.itemsPage.click_on_orange_button()
        self.preOrder.add_quantity(25)
        self.preOrder.add_button_quantity_3()
        self.assertTrue('28' in self.preOrder.get_quantity())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
