class PageItems:

    def __init__(self, my_driver):
        self.no_results_banner = '//*[@id="center_column"]/p'
        self.title_banner = '//*[@id="center_column"]/h1/span[1]'
        self.orange_button = '//*[@id="color_1"]'
        self.driver = my_driver

    def return_no_element_text(self):
        return self.driver.find_element_by_xpath(self.no_results_banner).text

    def return_section_title(self):
        return self.driver.find_element_by_xpath(self.title_banner).text

    def click_on_orange_button(self):
        self.driver.find_element_by_xpath(self.orange_button).click()
        self.driver.find_element_by_xpath(self.orange_button).click()