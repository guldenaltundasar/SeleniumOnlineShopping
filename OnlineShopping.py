from selenium import webdriver
from selenium.webdriver.support.select import Select

import time


driver = webdriver.Chrome(executable_path="/Users/galtu/Downloads/selenium/chromedriver")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

tomato = driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[2]/form/input").send_keys("tomato")
time.sleep(4)
tomato_click = driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div/div[3]/button").click()

clean = driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[2]/form/input").clear()

bers = driver.find_element_by_class_name("search-keyword").send_keys("ber")
time.sleep(4)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[3]/a[4]/img").click()
driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[3]/div[2]/div[2]/button").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/button").click()

driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/button").click()
dropdown=Select(driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/select"))
dropdown.select_by_visible_text("Turkey")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/input").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/button").click()
time.sleep(2)
driver.close()


