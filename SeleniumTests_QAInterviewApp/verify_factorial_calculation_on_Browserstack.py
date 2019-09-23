"""
AUTHOR: Preedhi Vivek
Date: 23/09/2019

PURPOSE:
To run the Selenium automated test on iPhone7 - iOS - safari combination using
Browser Stack 

SCOPE:
1) Connect to browerstack 
2) Navigate to QA Interview (Factorial Calculator) application webpage
3) Verify if navigated to the correct page
4) Enter a valid postive integer in the console and it will be sent to the input box
5) Click on Calculate! button
6) Compare the factorial calculation in the webpage with the system calculated factorial value
6) Close the browser
"""

import time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SeleniumOnBrowserStack():
    "Example class written to run Selenium tests on BrowserStack"
    def setUp(self):
        desired_cap = { 'device': 'iPhone 7','realMobile': 'true', 'platform': 'iOS','browserName': 'safari', 'browserstack.debug': 'true' }
        self.driver = webdriver.Remote(command_executor='http://preedhivivek1:ASBEzbfpjskzSppnrHxJ@hub.browserstack.com:80/wd/hub',desired_capabilities=desired_cap)

    #verify page title
    def verify_title(self):
        #Go to the URL 
        self.driver.get('https://qainterview.pythonanywhere.com/')
        if(self.driver.title=="Factoriall"):
            print (self.driver.title)
            print ("Success: Factorial Calculator page launched successfully!")
        else:
            print ("Failed: Factorial Calculator page title is incorrect!") 
        time.sleep(2)


    #Get user input for factorial calculation
    def get_user_input(self):
        print("Enter a valid positive integer,less than 171 to perform factorial calculation:")
        input_number= input()
        return input_number


    #Find the input box and send the the number for which factorial has to be calculated. 
    def send_number_inputbox(self,input_number):
        locate_input_box=self.driver.find_element_by_xpath("//input[@placeholder='Enter an integer' and @id='number']")
        locate_input_box.send_keys(input_number)
        time.sleep(2)

    #Find the Calculate! button and click on it.
    def click_calculate(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'Calculate!')]").click()

    #Verify if the factorial calculation is correct
    def verify_factorial_calculation(self,input_number):
        factorial_text = ""
        factorial_calc = ""
        str_system_calc_factorial = ""
        
        locate_factorial_calc= self.driver.find_element_by_xpath("//*[contains(@id,'resultDiv')]")

        #extract only the factorial from the output text in the webpage          
        factorial_text = locate_factorial_calc.text
        factorial_calc = factorial_text.split(': ')[1]
        factorial_calc = factorial_calc.strip()
        print("Factorial of %s from the webpage: "%input_number,factorial_calc)
        
        #get the system's factorial calculation 
        system_calc_factorial = math.factorial(int(input_number))
        if (int(input_number)<=21):
            str_system_calc_factorial = str(system_calc_factorial).strip()
        elif (int(input_number)>21 and int(input_number)<171):
            system_calc_factorial = format(system_calc_factorial,'.17g')
            str_system_calc_factorial = str(system_calc_factorial).strip()
        elif (int(input_number)>=171):
            str_system_calc_factorial = "Infinity"    
        print("System calculated Factorial of %s: "%input_number,str_system_calc_factorial)


        #compare the factorial calculation between the webpage display and system calculated value
        if (factorial_calc == str_system_calc_factorial):
            print("Factorial calculation is correct! Test Passed")    
        else:
            print("Factorial calculation is incorrect! Test Failed")
    
    def tearDown(self):
        # Quit the browser window
        self.driver.quit()
 
#----START OF SCRIPT
if __name__=='__main__':

    # Create an object for class SeleniumOnBrowserStack 
    obj1 = SeleniumOnBrowserStack()

    obj1.setUp()
    #verify page title
    obj1.verify_title()

    #Call the function to receive user input
    input_no = obj1.get_user_input() 

    #Call the function to send the user input to be displayed in the input box and then click on the Calculate! button
    obj1.send_number_inputbox(input_no)

    #Call the function to click on the Calculate! button
    obj1.click_calculate()

    #Wait has to be introduced before verifying factorial calculation. Else the factorial calculation retrived from the webpage might return empty.  
    time.sleep(5)

    #Call the function to verify the factorial calculation
    obj1.verify_factorial_calculation(input_no)

    #Wait for the page to load and get displayed for verification
    time.sleep(5)
    
    obj1.tearDown()
