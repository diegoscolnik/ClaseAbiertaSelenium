from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www1.masterconsultas.com.ar/socios/context/init_input.action')

driver.find_element_by_id('usernameId').send_keys('dscolnik')
driver.find_element_by_id('password').send_keys('')
driver.find_element_by_id('submitLogin').click()
