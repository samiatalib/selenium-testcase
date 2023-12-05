from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import unittest

class WebAppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_driver_path = "D:\chromedriver\chrome-win64"  

        cls.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

        cls.base_url = "http://localhost/Online-BankingPHP/Online-BankingPHP/staff_login.php"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    @classmethod
    def test_login_successful(self):
        self.driver.get(self.base_url + "/staff_login.php")

        # Find the staff ID and password input fields and enter valid credentials
        staff_id_input = self.driver.find_element("name", "staff_id")
        password_input = self.driver.find_element("name", "password")

        staff_id_input.send_keys("120001")
        password_input.send_keys("password")

        # Find and click the login button
        submit_button = self.driver.find_element("name", "staff_login-btn")
        submit_button.click()

        # Check if the login was successful by verifying a page element that appears after login
        welcome_message = self.driver.find_element("xpath", '//label[@class="login-success"]')
        self.assertEqual(welcome_message.text, 'Welcome, Staff!')

    def test_login_failed(self):
        self.driver.get(self.base_url + "/staff_login.php")

        # Find the staff ID and password input fields and enter invalid credentials
        staff_id_input = self.driver.find_element("name", "staff_id")
        password_input = self.driver.find_element("name", "password")

        staff_id_input.send_keys("22334")
        password_input.send_keys("anything")

        # Find and click the login button
        submit_button = self.driver.find_element("name", "staff_login-btn")
        submit_button.click()

        # Check if an error message is displayed
        error_message = self.driver.find_element("xpath", '//label[@class="login-error"]')
        self.assertEqual(error_message.text, 'Invalid staff ID or password')

    def test_empty_login_fields(self):
        self.driver.get(self.base_url + "/staff_login.php")

        # Find the login button and click it without entering any credentials
        submit_button = self.driver.find_element("name", "staff_login-btn")
        submit_button.click()

        # Check if an error message is displayed for empty fields
        error_message = self.driver.find_element("xpath", '//label[@class="login-error"]')
        self.assertEqual(error_message.text, 'Staff ID and password are required')

    def test_account_deletion_successful(self):
        self.driver.get(self.base_url + "/delete_customer.php")

        # Find the customer details input fields and enter valid details for account deletion
        acc_no_input = self.driver.find_element("name", "Cust_ac_no")
        cust_id_input = self.driver.find_element("name", "Cust_ac_Id")
        reason_input = self.driver.find_element("name", "reason")

        acc_no_input.send_keys("1011801011950")
        cust_id_input.send_keys("1011950")
        reason_input.send_keys("account closed")

        # Find and click the delete button
        delete_button = self.driver.find_element("name", "delete")
        delete_button.click()

        # Check if the success message is displayed after deletion
        success_message = self.driver.find_element("xpath", '//script[contains(text(),"Customer Deleted Successfully")]')
        self.assertIsNotNone(success_message)

    def test_account_deletion_failure(self):
        self.driver.get(self.base_url + "/delete_customer.php")

        # Find the customer details input fields and enter invalid details for account deletion
        acc_no_input = self.driver.find_element("name", "Cust_ac_no")
        cust_id_input = self.driver.find_element("name", "Cust_ac_Id")
        reason_input = self.driver.find_element("name", "reason")

        acc_no_input.send_keys("456254")
        cust_id_input.send_keys("64666")
        reason_input.send_keys("cust")

        # Find and click the delete button
        delete_button = self.driver.find_element("name", "delete")
        delete_button.click()

        # Check if the error message is displayed after deletion failure
        error_message = self.driver.find_element("xpath", '//script[contains(text(),"Customer not deleted")]')
        self.assertIsNotNone(error_message)

if __name__ == '__main__':
    unittest.main()
