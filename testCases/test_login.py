import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage_Objects_Actions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

logger = LogGen.loggen()    
@pytest.mark.regression
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()    
    password = ReadConfig.getPassword()   
    
    def test_homePageTitle(self,setup):
        logger.info("*************** Test_001_Login Page Title *****************")
        logger.info("****Started Login page title test ****")
        driver = setup
        logger.info("****Opening URL****")
        driver.get(self.baseURL)
        driver.maximize_window()
        time.sleep(10)       
        act_title = driver.title      
        if act_title == 'OrangeHRM':
            logger.info("**** Login page title test passed ****")
            logger.handlers[0].flush() 
            logger.handlers[0].close()
            assert True
            driver.close()       
        else: 
            logger.error("**** Login page title test failed****")
            driver.save_screenshot('.\\Screenshots\\'+'test_homePageTitle.png')
            driver.close()
            assert False            
      

    def test_login(self,setup):
        logger.info("*************** Test_002_Home Page Login *****************")
        logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(10)       
        self.LP = LoginPage_Objects_Actions(self.driver)       
        self.LP.setUserName(self.username)
        self.LP.setPassword(self.password)
        self.LP.clickLogin()
        act_title = self.driver.title       
        if act_title == 'OrangeHRM':
            logger.info("****Login test passed ****")
            logger.handlers[0].flush() 
            logger.handlers[0].close()
            assert True
            self.driver.close()           
        else:
            logger.error("****Login test failed ****")
            self.driver.save_screenshot('.\\Screenshots\\'+'test_login.png')
            self.driver.close()
            assert False
  