"""
Test Automation 
Purpose:
To add all sunscreens on the webpage to the cart.

Author: Preedhi Vivek
Date: 17/07/2019

"""
import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the sunscreen web page
driver.get("https://weathershopper.pythonanywhere.com/sunscreen")

# maximize window
driver.maximize_window()

# Check if the title of the page is proper
if(driver.title=="The best moisturizers in the world!"):
    print ("Success: Sunscreen Page launched successfully!")
else:
    print ("Failure: Sunscreen Page Title is incorrect")    

#Locate all the Add buttons under the sunscreens
Add_Sunscreens = driver.find_elements_by_xpath("//button[@class='btn btn-primary']")
#Locate the web elements that hold the names of the sunscreens 
Sunscreens_Name = driver.find_elements_by_xpath("//p[@class='font-weight-bold top-space-10']")
#Add the located sunscreen to the cart one by one on click
try :
    for i in range(len(Add_Sunscreens)) :
        Add_Sunscreens[i].click()
        #Locate the Cart button and extract the text to verify if the sunscreen is added
        Get_CartButton = driver.find_element_by_xpath("//button[@onclick='goToCart()']")
        if(Get_CartButton.text !=  "Cart - Empty") :
            #Display the name of the sunscreen that was successfully added.
            print("Added " + Sunscreens_Name[i].text + " Sunscreen.")
        else :
            print("Item not added to the cart!")

except :     
        print("Error in adding sunscreen to the cart!")

#Wait for page to load 
time.sleep(10)

# Close the browser window
driver.close() 
        

