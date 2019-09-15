"""
AUTHOR: Preedhi Vivek
Date: 16/08/2019

PURPOSE:
To run the Selenium automated test on iPhone7 - iOS - safari combination using
Browser Stack 

SCOPE:
1) Navigate to QA Interview (Factorial Calculator) application webpage
2) Verify title
3) Quit
"""

import unittest, time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
class SeleniumOnBrowserStack(unittest.TestCase):
    "Example class written to run Selenium tests on BrowserStack"
    def setUp(self):
        desired_cap = { 'device': 'iPhone 7','realMobile': 'true', 'platform': 'iOS','browserName': 'safari', 'browserstack.debug': 'true' }
        self.driver = webdriver.Remote(command_executor='http://preedhivivek1:ASBEzbfpjskzSppnrHxJ@hub.browserstack.com:80/wd/hub',desired_capabilities=desired_cap)
 
    def test_QA_Interview_App_Test(self):
        # Navigate to QA Interview (Factorial Calculator) application webpage
        self.driver.get('https://qainterview.pythonanywhere.com/')

        #Wait for the page to load and get displayed for verification
        time.sleep(5)
        #await asyncio.sleep(5)
        # Check if the title of the page is proper
        if(self.driver.title=="Factoriall"):
            print(self.driver.title)
            print ("Success: Factorial Calculator page launched successfully!")
        else:
            print ("Failed: Factorial Calculator page title is incorrect!") 
        time.sleep(2)
        #await asyncio.sleep(2)
 
    def tearDown(self):
        # Quit the browser window
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main()
    





   