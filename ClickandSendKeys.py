from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickandSendKey():
    def qa(self):
       driver = webdriver.Firefox()
       baceUrl = "https://www.google.com/search?client=firefox-b-d&q=facebook&sa=X&ved=2ahUKEwjS8KP3i7jwAhXEG80KHZj9DxEQ7xYoAHoECAEQMA&biw=1280&bih=607&dpr=1.5"
       driver.maximize_window()
       driver.get(baceUrl)
       driver.implicitly_wait(10)

       loginlink = driver.find_element(By.XPATH, "//div[@class='yuRUbf']//h3[contains(text(),'Facebook - Log In or Sign Up')]")
       time.sleep(3)
       loginlink.click()

       emailfield = driver.find_element(By.ID, 'email')
       emailfield.send_keys("Milia is")

       passwordfield = driver.find_element(By.ID,'pass')
       passwordfield.send_keys("78888777")

       time.sleep(3)
       emailfield.clear()
       passwordfield.clear()
       time.sleep(3)

       emailfield.send_keys("the Super star))")
       passwordfield.send_keys("677888")




dd = ClickandSendKey()
dd.qa()
