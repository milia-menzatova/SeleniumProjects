from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXPathFormat():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        # Login --> Lecture "How to click and type on a web element"
        driver.find_element(By.XPATH,'//*[@id="navbar-inverse-collapse"]/div/div/a').click()
        time.sleep(2)
        email = driver.find_element(By.ID, "email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "password")
        password.send_keys("abcabc")
        driver.find_element(By.CLASS_NAME, "btn-default").click()

        #Search for course
        searchBox = driver.find_element(By.NAME, "course")
        searchBox.send_keys("JavaScript")
        time.sleep(3)
        #Select course
        _course = "//div//h4[contains(@class,'dynamic-heading') and contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")


        courseElement = driver.find_element(By.XPATH,_courseLocator)
        courseElement.click()
        driver.quit()


dd = DynamicXPathFormat()
dd.test()

