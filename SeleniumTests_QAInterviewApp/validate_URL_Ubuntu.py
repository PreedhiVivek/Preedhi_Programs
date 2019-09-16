"""
AUTHOR: Preedhi Vivek
Date: 13/09/2019

SCOPE:
1)ssh to Ubuntu
2) Launch the headless Chrome Webdriver
3) Navigate to QA Interview (Factorial Calculator) application webpage
4) Verify if navigated to the correct page
5) Close the browser
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)

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
