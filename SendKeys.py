from selenium import webdriver
import time

class SendKey():
    def test(self):
        baseUrl = "https://www.youtube.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        searchbox = driver.find_element_by_xpath("//input[@id='search']")
        searchbox.send_keys("Peppa pig")
        time.sleep(3)


        searcbbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
        searcbbutton.click()
        time.sleep(3)
        driver.quit()

dd = SendKey()
dd.test()



