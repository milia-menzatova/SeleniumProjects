from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class DropdownSelect():
    def test(self):
        baseUrl = "https://www.globalsqa.com/demo-site/select-dropdown-menu/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]/p/select')
        dsel = Select(element)

        dsel.select_by_value("ALA")
        dsel.select_by_value("CRI")

        print("Selected Alan Island by value")
        time.sleep(3)
        print("Selected Costa Rica by value")
        time.sleep(3)

        dsel.select_by_index('5')
        print("Selected Andorra Island by index")
        time.sleep(3)
        dsel.select_by_index('50')
        print("Selected by index")
        time.sleep(3)

        dsel.select_by_visible_text("Cuba")
        print("Selected Cuba by visible text")
        time.sleep(3)
        dsel.select_by_visible_text("Indonesia")
        print("Selected Indonesia by visible text")
        



dd = DropdownSelect()
dd.test()