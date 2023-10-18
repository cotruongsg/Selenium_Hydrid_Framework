import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage_Objects_Actions
from pageObjects.HomePage import HomePage_Objects_Actions
from pageObjects.AdminPage import AdminPage_Objects_Actions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.CommonActions import CommonActions
from utilities import XLUtils

logger = LogGen.loggen()    

class Test_Admin_Page:
    baseURL = ReadConfig.getApplicationURL()  
    username = ReadConfig.getUseremail()    
    password = ReadConfig.getPassword() 


    @pytest.mark.sanity    
    def test_add_admin_user(self,setup):
        logger.info("*************** Test Add Admin User*****************")
        logger.info("****Started Adding User****")
        self.driver = setup
        self.driver.get(self.baseURL)
        # Get objects and methods from PageObjects Model
        LoginPage = LoginPage_Objects_Actions(self.driver)  
        HomePage = HomePage_Objects_Actions(self.driver)
        AdminPage = AdminPage_Objects_Actions(self.driver)
        ACTION = CommonActions(self.driver)

        # Login
        ACTION.waitForElementExists(LoginPage.button_login_xpath,5)
        LoginPage.setUserName(self.username)
        LoginPage.setPassword(self.password)
        ACTION.click(LoginPage.button_login_xpath)
        ACTION.waitForElementExists(HomePage.admin_link,3)

        # Click Admin link
        ACTION.click(HomePage.admin_link)
        ACTION.waitForElementExists(AdminPage.admin_header_label,5)

        # Click Add button
        ACTION.click(AdminPage.add_button)
        ACTION.waitForElementExists(AdminPage.user_role_label,3) 

        # Fill Out Information
        ACTION.click(AdminPage.user_role_arrow_selector)
        ACTION.click(AdminPage.admin_role_link)
        ACTION.click(AdminPage.status_role_arrow)
        ACTION.click(AdminPage.status_role_link)
        ACTION.inputValue(AdminPage.employee_name_input,'Charlie')
        time.sleep(5)
        ACTION.click(AdminPage.employee_name_Charlie)
        ACTION.inputValue(AdminPage.username_input,'mantisSG1')
        ACTION.inputValue(AdminPage.password_input,'Tr123456789!')
        ACTION.inputValue(AdminPage.confirm_password_input,'Tr123456789!')
        ACTION.click(AdminPage.save_button)
        ACTION.waitForElementExists(AdminPage.add_button,6)

        # Check table displays
        result = ACTION.checkElementExists(AdminPage.data_table)
        if result == True:
            assert True
            logger.info("*************** Ending Add Admin User*****************")
            logger.info("****Add User Passed****")
        else:
            assert False






        

        
    
        