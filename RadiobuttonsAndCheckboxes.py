from selenium import webdriver
import time

class RadiobtnAndCheckbox():
    def QA(self):
        baceUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baceUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        bmwradiobtn = driver.find_element_by_id('bmwradio')
        bmwradiobtn.click()

        time.sleep(3)
        benzradiobtn = driver.find_element_by_id('benzradio')
        benzradiobtn.click()

        time.sleep(3)
        hondaradiobtn = driver.find_element_by_id('hondaradio')
        hondaradiobtn.click()

        time.sleep(3)
        bmwcheckbox = driver.find_element_by_id('bmwcheck')
        bmwcheckbox.click()

        time.sleep(3)
        benzcheckbox = driver.find_element_by_id('benzcheck')
        benzcheckbox.click()

        time.sleep(3)
        hondacheckbox = driver.find_element_by_id("hondacheck")
        hondacheckbox.click()


        print("BMW radio button is selected?" + str(bmwradiobtn.is_selected()))
        print("BENZ radio button is selected?" + str(benzradiobtn.is_selected()))
        print("BMW checkbox is selected?" + str(bmwcheckbox.is_selected()))
        print("BENZ checkbox is selected?" + str(benzcheckbox.is_selected()))
        print("Honda checkbox is selected?" + str(hondacheckbox.is_selected()))

dd = RadiobtnAndCheckbox()
dd.QA()