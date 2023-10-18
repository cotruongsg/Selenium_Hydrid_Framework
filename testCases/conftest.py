import pytest
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from pytest_metadata.plugin import metadata_key

### @pytest.fixture is a decorator that is used to define setup code that can be shared across multiple test functions.
@pytest.fixture()
def setup(browser):    
    if browser=='chrome':
        serv_obj = Service('D://Drivers//chromedriver.exe')
        driver=webdriver.Chrome(service=serv_obj)
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# # It is hook for Adding Environment info to HTML Report
@pytest.hookimpl(tryfirst=True) 
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]['Project Name'] = 'OrangeHRM'
    session.config.stash[metadata_key]['Module Name'] = 'Customers'
    session.config.stash[metadata_key]['Tester'] = 'Truong Duong' 

# # It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

