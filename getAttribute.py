from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetAttribute():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("class")

        print("Value of attribute is " + result)
        time.sleep(1)
        driver.quit()

dd = GetAttribute()
dd.test()

