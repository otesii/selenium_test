from selenium import webdriver
 
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options) 

driver.get('https://www.google.com/')

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()

driver.quit()