from selenium import webdriver
import unittest
import time


tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_id('search_query_top').send_keys('Hola Mundo')
driver.find_element_by_name('submit_search').click()
time.sleep(5)
tc.assertEqual('No results were found for your search "Hola Mundo"', driver.find_element_by_xpath('//*[@id="center_column"]/p').text)
driver.find_element_by_link_text('Women').click()
#time.sleep(2)
driver.find_element_by_partial_link_text('Dres').click()
#time.sleep(2)
#Link Text
#driver.find_element_by_link_text('Casual Dresses').click()
#Partial Link Text
#driver.find_element_by_partial_link_text('Casual').click()
#Por classname
#driver.find_element_by_class_name('subcategory-name').click()
#Por CSSS_Selector
#driver.find_element_by_css_selector('a.subcategory-name').click()
#Por X-Path
#driver.find_element_by_xpath('//*[@id="subcategories"]/ul/li[1]/h5/a').click()
#Por Tag
#driver.find_elements_by_tag_name('a').click()

#driver.close()
#driver.quit()



