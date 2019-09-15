"""
AUTHOR: Preedhi Vivek
Date: 02/08/2019

SCOPE:
1) Launch Chrome Webdriver
2) Navigate to QA Interview (Factorial Calculator) application webpage
3) Verify if navigated to the correct page
4) Click on the "Calculate!" button without entering any input in the input box
5) Verify if the validation message gets displayed
6) Close the browser
"""

import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
browser = webdriver.Chrome()
browser.maximize_window()

# Navigate to QA Interview (Factorial Calculator) application webpage
browser.get('https://qainterview.pythonanywhere.com/')

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
    
#Wait for the page to load and get displayed for verification
time.sleep(5)
# Quit the browser window
browser.quit() 
