from selenium.webdriver.common.by import By

class AdminPage_Objects_Actions:
    admin_header_label = "//h6[normalize-space()='User Management']"
    add_button = "//button[normalize-space()='Add']"
    user_role_label = "//label[normalize-space()='User Role']"
    user_role_arrow_selector = "//label[contains(text(), 'User Role')]/following::div[1]//i[contains(@class, 'arrow')]"
    admin_role_link = "//span[contains(text(),'Admin')]"
    status_role_arrow = "//label[contains(text(), 'Status')]/following::div[1]//i[contains(@class, 'arrow')]"
    status_role_link = "//span[contains(text(), 'Enabled')]"
    employee_name_input = "//input[@placeholder='Type for hints...']"
    employee_name_Charlie = "//span[contains(text(),'Charlie')]"
    username_input = "//label[contains(text(), 'Username')]/following::div[1]/input"
    password_input = "//label[contains(text(), 'Password')]/following::div[1]/input"
    confirm_password_input = "//label[contains(text(), 'Confirm Password')]/following::div[1]/input"
    save_button = "//button[normalize-space()='Save']"
    data_table = "//div[@class='oxd-table']"

    def __init__(self,driver):
        self.driver=driver