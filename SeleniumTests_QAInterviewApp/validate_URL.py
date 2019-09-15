"""
AUTHOR: Preedhi Vivek
Date: 02/08/2019

SCOPE:
1) Launch Chrome Webdriver
2) Navigate to QA Interview (Factorial Calculator) application webpage
3) Verify if navigated to the correct page
4) Close the browser
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

#Wait for the page to load and get displayed for verification
time.sleep(5)
# Quit the browser window
browser.quit() 
