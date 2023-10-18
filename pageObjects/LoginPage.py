from selenium.webdriver.common.by import By

class LoginPage_Objects_Actions:
    # Login Page
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = "//button[contains(@class, 'oxd-button--main orangehrm-login-button')]"
    profile_link = "//span[@class='oxd-userdropdown-tab']"
    logout = "//a[normalize-space()='Logout']"
    invalid_cre = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text' and text()='Invalid credentials']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.profile_link).click()
        self.driver.find_element(By.XPATH, self.logout).click()

    def Login(self , username , password):
        self.setUserName(username)
        self.setPassword(password)
        self.clickLogin()

    def checkInvalidCredentialsExists(self):
        invalid_credentials = self.driver.find_element(By.XPATH, self.invalid_cre).is_displayed()
        return invalid_credentials


