"""
AUTHOR: Preedhi Vivek
Date: 16/08/2019

PURPOSE:
To run the Selenium automated test on iPhone7 - iOS combination using
Browser Stack 

SCOPE:
1) Launch Chrome Webdriver
2) Navigate to QA Interview (Factorial Calculator) application webpage
3) Verify if navigated to the correct page
4) Close the browser
"""


import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
class SeleniumOnBrowserStack(unittest.TestCase):
    "Example class written to run Selenium tests on BrowserStack"
    def setUp(self):
        #self.driver = webdriver.Firefox()
        desired_cap = { 'device': 'iPhone 7','realMobile': 'true', 'platform': 'iOS','browserName': 'safari', 'browserstack.debug': 'true' }
        self.driver = webdriver.Remote(command_executor='http://preedhivivek1:ASBEzbfpjskzSppnrHxJ@hub.browserstack.com:80/wd/hub',desired_capabilities=desired_cap)
        # Create an instance of Chrome WebDriver
        self.browser = webdriver.Chrome()


 
    def QA_Interview_App_Test(self):
        self.browser.maximize_window()
        # Navigate to QA Interview (Factorial Calculator) application webpage
        self.browser.get('https://qainterview.pythonanywhere.com/')

        # Check if the title of the page is proper
        if(browser.title=="Factoriall"):
            print ("Success: Factorial Calculator page launched successfully!")
        else:
            print ("Failed: Factorial Calculator page title is incorrect!") 

        #Find the Calculate! button and click on it
        browser.find_element_by_xpath("//button[contains(text(),'Calculate!')]").click()

        #Verify if the validation message gets displayed owing to click of Calculate! button with no input
        try:
            browser.find_element_by_xpath("//p[contains(text(),'Please enter an integer')]")
            flag = 1
        except Exception:
            flag = 0
    
        if (flag==1) :
            print("Validation message displayed! Test Passed")    
        elif (flag==0) :
            print("Validation message NOT displayed! Test Failed")    

    def tearDown(self):
        #Wait for the page to load and get displayed for verification
        time.sleep(5)
        # Quit the browser window
        self.browser.quit() 
 
if __name__ == '__main__':
    unittest.main()







   