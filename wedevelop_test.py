import unittest
from selenium import webdriver



class Test_Wedevelop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://wedevelop.me/')
    
    def test_blog(self):
        
        #Get de Contact Us button
        #self.driver.find_element_by_xpath('//*[@id="root"]/header/nav/ul/li[1]/a').click()
        #Wait for the website response
        #self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('cookieconsent:desc').click()
        text_we_love = self.driver.find_element_by_partial_link_text("We love to meet new people ")
        self.assertEqual('We love to meet new people and have their ideas come alive in the projects we work.', text_we_love.text)
        
        #Verify correct Text about COVID Project
        #self.assertEqual('COVID-19 and Businesses Research Project', self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section[1]/div[2]/div[1]/div/section/div[2]/div/div/div[1]/div/h2/a').text)
        #self.driver.find_element_by_xpath('//*[@id="page-region"]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/table/tbody/tr[4]/td[3]/button').click()
        #assert main_page.is_title_matches(), "python.org title doesn't match."
        #Sets the text of search textbox to "pycon"
        #main_page.search_text_element = "pycon"
        #main_page.click_go_button()
        #search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        #assert search_results_page.is_results_found(), "No results found."
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


