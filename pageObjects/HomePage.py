from selenium.webdriver.common.by import By

class HomePage_Objects_Actions:
    profile_link = "//span[@class='oxd-userdropdown-tab']"
    admin_link = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Admin']"

    def __init__(self,driver):
        self.driver=driver

    def checkProfileLinkExists(self):
        profile = self.driver.find_element(By.XPATH, self.profile_link).is_displayed()
        return profile
    
    
    

    