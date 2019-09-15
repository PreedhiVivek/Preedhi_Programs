"""
Test Automation 
Scope:
1. Navigate to https://weathershopper.pythonanywhere.com/moisturizer
2. Add the most expensive moisturizer to the cart
3. Click on cart and verify if the most expensive sunscreen is added to the cart
4. Exit the browser

Author: Preedhi Vivek
Date: 07/08/2019

"""
import time
from selenium import webdriver
import weather_shopper_module as m1 


#----START OF SCRIPT
if (__name__=='__main__') :
    
    url = "https://weathershopper.pythonanywhere.com/moisturizer"
    
    # create an instance of Chrome WebDriver
    driver = webdriver.Chrome()
    cart_items = {}

    # create an object of class Navigate  
    nav_obj1 = m1.Navigate(url,driver)
    # call the method to navigate to weather shopper webapplication
    nav_obj1.navigate_url()

    # maximize window
    driver.maximize_window()
    
    # call the method to verify navigation 
    nav_obj1.verify_navigation()

    # create an object of class Items
    items_obj1 = m1.Items(driver)

    #call the method to return the cost of sunscreens
    item_prices = items_obj1.get_item_prices(" ")

    #call the method to add the most expensive moisturizer to the cart 
    cart_item_name,cart_item_price = items_obj1.add_most_priced_item(' ',item_prices)
    cart_items.update({cart_item_name:cart_item_price})

    time.sleep(7)

    # create an object of class Cart
    cart_obj1 = m1.Cart(driver)

    #call the method to verify the cart label post addition of items
    cart_flag = cart_obj1.check_cart()
    try:
        if (cart_flag==1):
            #call the method to verify navigation to checkout page
            cart_flag = cart_obj1.verify_url()
        else:
             print("Incorrect navigation! Test Failed.")   
    except Exception as e:
            print("Exception:", e)         

    #Wait to display the items added to the cart  
    time.sleep(7)

    # Close the browser window
    driver.close() 
        
