from selenium import webdriver
from selenium.webdriver.common.by import By

class GetText():
    def test(self):
        baseUrl = "https://www.cartersoshkosh.ca/en_CA/home?cm_mmc=SEM_Canada-_-Brand_Google_CA-_-PPC_Carters_CA_B_Brand_X_ALL_EN_Exact_Desktop_-_58700005548125353-_-carters.-e-_-71700000061422352&src=&gclid=CjwKCAjw47eFBhA9EiwAy8kzNPE1WNne2B3-29Byird4K64x3BiROwjILwQ0erKtZ7T00V4rOZz4DxoCl6MQAvD_BwE&gclsrc=aw.ds"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        babyGirlTab = driver.find_element_by_class_name('btn-secondary')
        elementText = babyGirlTab.text
        print("Text on the element is " + elementText)


dd = GetText()
dd.test()
