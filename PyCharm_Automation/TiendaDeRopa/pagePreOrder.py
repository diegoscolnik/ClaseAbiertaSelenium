class PreOrder:

    def __init__(self, my_driver):
        self.quantity = '//*[@id="quantity_wanted"]'
        self.plus_button = '//*[@id="quantity_wanted_p"]/a[2]/span/i'
        self.driver = my_driver

    def add_quantity(self, item):
        self.driver.find_element_by_xpath(self.quantity).clear()
        self.driver.find_element_by_xpath(self.quantity).send_keys(item)

    def add_button_quantity_3(self):
        self.driver.find_element_by_xpath(self.plus_button).click()
        self.driver.find_element_by_xpath(self.plus_button).click()
        self.driver.find_element_by_xpath(self.plus_button).click()

    def get_quantity(self):
        return self.driver.find_element_by_xpath(self.quantity).get_attribute('value')
