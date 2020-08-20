import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.zhipin.com/user/login.html")

driver.find_element_by_name()
driver.find_element_by_name("account").send_keys("19806586880")

time.sleep(3)
