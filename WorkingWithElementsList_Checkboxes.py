from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ListofElements():
    def testlistofelements(self):
        baseUrl = "http://test.rubywatir.com/checkboxes.php"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)

        checkboxeslist = driver.find_elements(
            By.XPATH,"//input[contains(@type,'checkbox') and contains(@name,'sports')]")
        size = len(checkboxeslist)
        print(f"Size of checkboxes list is: {size}")

        for checkboxes in checkboxeslist:
            isSelected = checkboxes.is_selected()
            if not isSelected:
                checkboxes.click()
                time.sleep(3)

dd = ListofElements()
dd.testlistofelements()