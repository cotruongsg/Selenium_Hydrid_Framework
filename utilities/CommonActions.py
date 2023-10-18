from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CommonActions:

    def __init__(self,driver):
        self.driver=driver

    def click(self,element):
        self.driver.find_element(By.XPATH,element).click()
        
    def waitForElementExists(self,element,timeout):
        wait = WebDriverWait(self.driver,timeout)
        wait.until(EC.presence_of_element_located((By.XPATH, element)))

    def inputValue(self,element,value):
        input = self.driver.find_element(By.XPATH,element)
        input.clear()
        input.send_keys(value)

    def checkElementExists(self,element):
        element = self.driver.find_element(By.XPATH,element).is_displayed()
        return element