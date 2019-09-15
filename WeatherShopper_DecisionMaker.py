"""
Test Automation:
To Read the temperature and 
go to either mosturizer page 
or sunscreen page accordingly

Author: Preedhi Vivek
Date: 16/07/2019

"""
import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to weathershopper website
driver.get("https://weathershopper.pythonanywhere.com")

# maximize window
driver.maximize_window()

# Check if the title of the page is proper
if(driver.title=="The best moisturizers in the world!"):
    print ("Success: Weathershopper Page launched successfully")
else:
    print ("Failure: Weathershopper Page Title is incorrect")    

# Locate the temperate element and read its value
Temperature_Value = driver.find_element_by_xpath("//div[@id='weather']")
#Slicing the first two characters to extract only the temperature part and removing the oC suffix
Temperature_Sliced = Temperature_Value.text[0:2]

print("Current temperature sliced:" + Temperature_Sliced)

#hold the page display for a few seconds before the next event
time.sleep(3)

#if the temperature is below 19 degrees, click on Buy mosturizers button

if int(Temperature_Sliced) < 19 :
    print("Buy mosturizers")
    driver.find_element_by_xpath("//a[@href='/moisturizer']").click()
    #Verify if redirected to the buy mosturizers page
    try:
        if (driver.current_url=="https://weathershopper.pythonanywhere.com/moisturizer") :
                print ("Redirected to the buy mosturizers page!")
    except:
                print("Redirected to an incorrect page!")

#else if the temperature is above 34 degrees, click on Buy sunscreens button    
elif int(Temperature_Sliced) > 34 :
    print("Buy Sunscreens")
    driver.find_element_by_xpath("//a[@href='/sunscreen']").click()
    #Verify if redirected to the buy sunscreens page
    try:
        if (driver.current_url=="https://weathershopper.pythonanywhere.com/sunscreen") :
                print ("Redirected to the buy sunscreens page!")
    except:
                print("Redirected to an incorrect page!")


#Wait for page to load
time.sleep(3)

# Close the browser window
driver.close() 
        

