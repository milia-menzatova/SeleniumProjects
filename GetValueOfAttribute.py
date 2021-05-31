from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetValue():
    def test(self):
        baseUrl = "https://ceotech.ca/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        element = driver.find_element(By.XPATH, "//div[@id='mainMenu']/ul/li[3]/div[@class='dropdown']/div[@id='dropdownMenuLink']")
        result = element.get_attribute("role")
        print("Value of element is " + result)

dd = GetValue()
dd.test()