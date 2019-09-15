"""
Test Automation 
Purpose:
To add two sunscreens to the cart based on conditions mentioned below:

(*) Add the least expensive sunscreen that contains SPF-50
(*) Add the least expensive sunscreen that contains SPF-30

Click on cart and verify if the two least expensive sunscreens are added to the cart. Exit the browser. 

Author: Preedhi Vivek
Date: 23/07/2019

"""
import time
from selenium import webdriver
import functions_collection as f1

#variables initialization
items_price = []
all_items_price = []

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the sunscreens web page
driver.get("https://weathershopper.pythonanywhere.com/sunscreen")

# maximize window
driver.maximize_window()

# Check if the title of the page is proper
if(driver.title=="The best moisturizers in the world!"):
    print ("Success: Suncreens Page launched successfully!")
else:
    print ("Failure: Sunscreens Page Title is incorrect")    


"""
Function Name : add_least_priced_item
Purpose : To find the least expensive item and add it to the cart
Returns : None   

"""
def add_least_priced_item(item_name,all_items_price):
        least_price_item = min(all_items_price)
        str_least_price_item = str(least_price_item)
        print("least priced ", item_name, " item: ",str_least_price_item)
        add_button = driver.find_element_by_xpath("//p[contains(text(),'"+item_name+"')]/following-sibling::p[contains(text(),'"+str_least_price_item+"')]/following-sibling::button[contains(@class,'btn btn-primary')]")
        add_button.click()    



"""
Function Name : check_cart
Purpose : To verify if the items are added to the cart
Returns : None   

"""
def check_cart(cart_button) :
    try :
        if(cart_button.text !=  "Cart - Empty") :
            print("Item(s) added to the cart successfully!")
            cart_button.click()
        else :
            print("Item(s) not added to the cart!")
      
    except :     
        print("Error in adding items to the cart!")

#----START OF SCRIPT
if __name__=='__main__':
    
    #call the function to return the cost of the SPF-50 sunscreens 
    items_price = driver.find_elements_by_xpath("//*[contains(text(),'SPF-50')]/following-sibling::p") 
    all_items_price = f1.get_item_prices(items_price)
       
    #call the function to add the least priced SPF-50 sunscreen to the cart 
    add_least_priced_item('SPF-50',all_items_price)
  
    #call the function to return the cost of the SPF-30 sunscreens 
    items_price = driver.find_elements_by_xpath("//*[contains(text(),'SPF-30')]/following-sibling::p") 
    all_items_price = f1.get_item_prices(items_price)
       
    #call the function to add the least priced SPF-30 sunscreen to the cart 
    add_least_priced_item('SPF-30',all_items_price)
  
    #Wait for the page to load  
    time.sleep(7)

    #call the function to verify the text on the cart button and redirection to the cart page 
    cart_button = driver.find_element_by_xpath("//button[contains(@onclick,'goToCart()')]")
    check_cart(cart_button)


#Wait to display the items added to the cart  
time.sleep(7)

# Close the browser window
driver.close() 
        
