"""
Test Automation 
Purpose:
To add two moisturizers to the cart based on conditions mentioned below:

(*) Add the least expensive moisturizer that contains Aloe
(*) Add the least expensive moisturizer that contains Almond

Click on cart and verify if the two least expensive moisturizers are added to the cart. Exit the browser. 

Author: Preedhi Vivek
Date: 22/07/2019

"""
import time
from selenium import webdriver

#variables initialization
aloe_prices = []
almond_prices = []

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the moisturizers web page
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")

# maximize window
driver.maximize_window()

# Check if the title of the page is proper
if(driver.title=="The best moisturizers in the world!"):
    print ("Success: Moisturizers Page launched successfully!")
else:
    print ("Failure: Moisturizers Page Title is incorrect")    

"""
Function Name : get_aloe_prices
Purpose : To get the prices of aloe moisturizers and extract only the numeric part
Returns : List containing the prices of the aloe moisturizers 

"""
def get_aloe_prices() :
    #variables initialization
    price_aloe_moisturizers = []
    split_price_aloe_moisturizers = []
    new_price = 0
       
    price_aloe_moisturizers = driver.find_elements_by_xpath("//*[contains(text(),'Aloe') or contains(text(),'aloe')]/following-sibling::p") 
    
    for i in range(0,len(price_aloe_moisturizers)) :
        
        split_price_aloe_moisturizers = price_aloe_moisturizers[i].text.split("Price: ", 1)

        if (split_price_aloe_moisturizers[1].find('Rs. ')!=-1):
            new_price = split_price_aloe_moisturizers[1].split('Rs. ')
            new_price = int(new_price[1])
        else:
            new_price = split_price_aloe_moisturizers[1]
            new_price = int(new_price)
                    
        aloe_prices.append(new_price)
        
    return aloe_prices
    
"""
Function Name : get_almond_prices
Purpose : To get the prices of alomond moisturizers and extract only the numeric part
Returns : List containing the prices of the almond moisturizers 

"""
def get_almond_prices() :
    #variables initialization
    price_almond_moisturizers = []
    split_price_almond_moisturizers = []
    new_price = 0

    price_almond_moisturizers = driver.find_elements_by_xpath("//*[contains(text(),'Almond') or contains(text(),'almond')]/following-sibling::p") 
    
    for i in range(0,len(price_almond_moisturizers)) :
        
        split_price_almond_moisturizers = price_almond_moisturizers[i].text.split("Price: ", 1)

        if (split_price_almond_moisturizers[1].find('Rs. ')!=-1):
            new_price = split_price_almond_moisturizers[1].split('Rs. ')
            new_price = int(new_price[1])
        else:
            new_price = split_price_almond_moisturizers[1]
            new_price = int(new_price)
                    
        almond_prices.append(new_price)
        
    return almond_prices

"""
Function Name : add_least_priced_aloe
Purpose : To find the least expensive aloe moisturizer and add it to the cart
Returns : None   

"""
def add_least_priced_aloe(aloe_prices):
        least_price_aloe = min(aloe_prices)
        str_least_price_aloe = str(least_price_aloe)
        print("least priced aloe: ",str_least_price_aloe)
        add_button = driver.find_element_by_xpath("//p[contains(text(),'Aloe') or contains(text(),'aloe')]/following-sibling::p[contains(text(),'"+str_least_price_aloe+"')]/following-sibling::button[contains(@class,'btn btn-primary')]")
        add_button.click()    

"""
Function Name : add_least_priced_almond
Purpose : To find the least expensive almond moisturizer and add it to the cart
Returns : None   

"""
def add_least_priced_almond(almond_prices):
        least_price_almond = min(almond_prices)
        str_least_price_almond = str(least_price_almond)
        print("least priced almond: ",str_least_price_almond)
        add_button = driver.find_element_by_xpath("//p[contains(text(),'Almond') or contains(text(),'almond')]/following-sibling::p[contains(text(),'"+str_least_price_almond+"')]/following-sibling::button[contains(@class,'btn btn-primary')]")
        add_button.click()    

"""
Function Name : check_cart
Purpose : To verify if the items are added to the cart
Returns : None   

"""

def check_cart() :
    cart_button = driver.find_element_by_xpath("//button[contains(@onclick,'goToCart()')]")
    try :
        if(cart_button.text !=  "Cart - Empty") :
            print("Added least expensive aloe and almond moisturizers!")
        else :
            print("Item not added to the cart!")
        cart_button.click()
        
    except :     
        print("Error in adding items to the cart!")


#----START OF SCRIPT
if __name__=='__main__':
    
    #call the function to return the cost of the aloe moisturizers 
    get_aloe_prices()

    
    #call the function to add the least priced aloe moisturizer to the cart 
    add_least_priced_aloe(aloe_prices)

    #call the function to return the cost of the almond moisturizers 
    get_almond_prices()
    
    #call the function to add the least priced almond moisturizer to the cart
    add_least_priced_almond(almond_prices)

    #Wait for the page to load  
    time.sleep(7)

    #call the function to verify the text on the cart button and redirection to the cart page 
    check_cart()


#Wait to display the items added to the cart  
time.sleep(7)

# Close the browser window
driver.close() 
        
