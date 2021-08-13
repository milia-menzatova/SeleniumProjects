from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ExplicitWait():
    def test(self):
        baseUrl = "https://www.expedia.ca/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(.5)
        driver.get(baseUrl)
        driver.find_element(By.XPATH,"//span[contains(text(),'Flights')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="location-field-leg1-origin-menu"]/div[1]/button"]').send_keys("Toronto")
        #driver.find_element(By.XPATH, "//div[@id='app-layer-base']").send_keys("Crimea")

dd = ExplicitWait()
dd.test()