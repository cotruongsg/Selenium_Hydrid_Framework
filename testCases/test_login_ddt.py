import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage_Objects_Actions
from pageObjects.HomePage import HomePage_Objects_Actions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

logger = LogGen.loggen()    
class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "D:\\Selenium_Hydrid_Framework\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()         
    
    @pytest.mark.regression
    def test_login(self,setup):
        logger.info("*************** Test_DDT_Home Page Login *****************")
        logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(10)       
        self.lp = LoginPage_Objects_Actions(self.driver)   
        
        # Get data from excel
        workbook = XLUtils.open_workbook(self.path)
        self.rows = XLUtils.getRowCount(workbook,'Sheet1')
        print('Number of rows...',self.rows)       

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(workbook,'Sheet1',r,1)
            self.password = XLUtils.readData(workbook, 'Sheet1', r, 2)
            self.lp.Login(self.user,self.password)                   
            time.sleep(8)  

            if  r == 2 :              
                try:
                    self.hp = HomePage_Objects_Actions(self.driver) 
                    profile = self.hp.checkProfileLinkExists()
                    if  profile == True:                                       
                        assert True
                        self.lp.clickLogout()
                        time.sleep(5)
                        self.status = XLUtils.writeData(workbook, 'Sheet1', r, 3, 'Pass', self.path)
                except Exception as e:                   
                    self.driver.save_screenshot('.\\Screenshots\\' + 'test_login.png')
                    self.status = XLUtils.writeData(workbook, 'Sheet1', r, 3, 'Fail' , self.path)
                    assert False                                          
            else:
                if  self.lp.checkInvalidCredentialsExists() == True:                    
                    self.status = XLUtils.writeData(workbook,'Sheet1', r, 3 , 'Pass' , self.path)
                    assert True
                else:                    
                    self.driver.save_screenshot('.\\Screenshots\\' + 'test_login.png')
                    self.status = XLUtils.writeData(workbook, 'Sheet1', r, 3, 'Fail' , self.path)
                    assert False   
            workbook.close()      
                

               