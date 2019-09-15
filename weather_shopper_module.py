"""
Weather Shopper Module
Scope:
1. To contain all the classes required for weather shopper automation

Author: Preedhi Vivek
Date: 06/08/2019
---------------------------
Updated 
date: 14/08/2019
scope: added few methods to Cart class
---------------------------

"""
import time

class Navigate() :
    def __init__(self,url,driver) :
        self.url = url
        self.driver = driver

    """
    Method name : navigate_url
    Purpose     : To navigate to the url 
    Returns     : None
    """
    def navigate_url(self) :
        # Create an instance of Chrome WebDriver
         self.driver.get(self.url)
    
    
    """
    Method name : verify_navigation_on_page_title
    Purpose     : To verify if the navigation is to the expected webpage based on the webpage title
    Returns     : None
    """    
    def verify_navigation_on_page_title(self) :
        if(self.driver.title=="The best moisturizers in the world!"):
            print ("Success: Weathershopper Page launched successfully")
        else:
            print ("Failure: Weathershopper Page Title is incorrect")    

    """
    Method name : verify_url
    Purpose     : To verify if navigation is to the correct webpage based on the current url
    Returns     : None
    """    
    def verify_url(self):        
        flag = 0
        try:
            if (self.driver.current_url=="https://weathershopper.pythonanywhere.com/moisturizer") :
                print ("Redirected to the buy mosturizers page!")
            elif (self.driver.current_url=="https://weathershopper.pythonanywhere.com/sunscreen") :
                print ("Redirected to the buy sunscreens page!")  
            elif (self.driver.current_url=="https://weathershopper.pythonanywhere.com/cart") :
                print ("Redirected to the Checkout page!")
                flag = 2
            elif (self.driver.current_url=="https://weathershopper.pythonanywhere.com/confirmation") :
                print ("Redirected to the Payment Success confirmation page!")            
        except:
            print("Redirected to an incorrect page!")
                
        return flag            


class common_events():
    def __init__(self,driver) :
        self.driver = driver
    
    """
    Method Name : click_button
    Purpose     : To click on the submit button in the webpage page
    Returns     : none   
    """
    def click_button(self) :
        pay_button = self.driver.find_element_by_xpath("//button[contains(@type,'submit')]")
        pay_button.click()


class Decision_Maker() :
    def __init__(self,driver) :
        self.driver = driver

    """
    Method name : decide_purchase
    Purpose     : To make a decision on purchase of either moisturizers or sunscreens based on temperature 
    Returns     : Flag
    """        
    def decide_purchase(self) :
        # Locate the temperate element and read its value
        Temperature_Value = self.driver.find_element_by_xpath("//div[contains(@id,'weather')]")
        #Slicing the first two characters to extract only the temperature part and removing the oC suffix
        Temperature_Sliced = Temperature_Value.text[0:2]

        #hold the page display for a few seconds before the next event
        time.sleep(3)

        #if the temperature is below 19 degrees, click on Buy mosturizers button
        if int(Temperature_Sliced) < 19 :
            print("Buy mosturizers")
            self.driver.find_element_by_xpath("//a[contains(@href,'/moisturizer')]").click()
            self.flag = 1
            

        #else if the temperature is above 34 degrees, click on Buy sunscreens button    
        elif int(Temperature_Sliced) > 34 :
            print("Buy Sunscreens")
            self.driver.find_element_by_xpath("//a[contains(@href,'/sunscreen')]").click()
            self.flag = 2
        return self.flag    

    
class Items():
    def __init__(self,driver) :
        self.driver = driver
    
    """
    Method name : get_item_prices
    Purpose     : To get the prices of the items and extract only the numeric part  
    Returns     : List containing the prices of the items
    """
    def get_item_prices(self,item_name) :
        #variables initialization
        price_of_items = []
        split_price_of_items = []
        item_prices = []
        new_price = 0
        price_of_items = self.driver.find_elements_by_xpath("//*[contains(text(),'"+item_name+"')]/following-sibling::p") 
    
        for i in range(0,len(price_of_items)) :
        
            split_price_of_items = price_of_items[i].text.split("Price: ", 1)

            if (split_price_of_items[1].find('Rs. ')!=-1):
                new_price = split_price_of_items[1].split('Rs. ')
                new_price = int(new_price[1])
            else:
                new_price = split_price_of_items[1]
                new_price = int(new_price)
                    
            item_prices.append(new_price)
        
        return item_prices

    """
    Method name : add_least_priced_item
    Purpose     : To find the least expensive item and add it to the cart
    Returns     : The least priced item name and price   

    """
    def add_least_priced_item(self,item_name,item_prices):
        least_item_price = min(item_prices)
        str_least_item_price = str(least_item_price)
        add_button = self.driver.find_element_by_xpath("//p[contains(text(),'"+item_name+"')]/following-sibling::p[contains(text(),'"+str_least_item_price+"')]/following-sibling::button[contains(@class,'btn btn-primary')]")
        add_button.click() 
        least_item_name = self.driver.find_element_by_xpath("//p[contains(text(),'"+str_least_item_price+"')]/preceding-sibling::p[contains(text(),'"+item_name+"')]")
        print("Least priced Item name: ",least_item_name.text)
        print("Least priced Item cost: Rs.",str_least_item_price)
        return least_item_name.text, str_least_item_price

    """
    Method name : add_most_priced_item
    Purpose     : To find the most expensive item and add it to the cart
    Returns     : The most expensive item name and price   

    """
    def add_most_priced_item(self,item_name,item_prices):
        most_expensive_item_price = max(item_prices)
        str_most_expensive_item_price = str(most_expensive_item_price)
        add_button = self.driver.find_element_by_xpath("//p[contains(text(),'"+item_name+"')]/following-sibling::p[contains(text(),'"+str_most_expensive_item_price+"')]/following-sibling::button[contains(@class,'btn btn-primary')]")
        add_button.click() 
        most_expensive_item_name = self.driver.find_element_by_xpath("//p[contains(text(),'"+str_most_expensive_item_price+"')]/preceding-sibling::p[contains(text(),'"+item_name+"')]")
        print("Most priced Item name: ",most_expensive_item_name.text)
        print("Most priced Item cost: Rs.",str_most_expensive_item_price)
        return most_expensive_item_name.text, str_most_expensive_item_price


class Cart():
    def __init__(self,driver) :
        self.driver = driver
        
    """
    Method Name : check_cart_label
    Purpose     : To verify the cart label post addition of items
    Returns     : flag   
    """
    def check_cart(self) :
        cart_button = self.driver.find_element_by_xpath("//button[contains(@onclick,'goToCart()')]")
        try :
            if(cart_button.text !=  "Cart - Empty") :
                print("Item(s) added to the cart successfully! Test Passed!")
                cart_flag = 1
                cart_button.click()
            else :
                print("Cart is Empty! Test Failed!")
            
        except :     
            print("Error in adding items to the cart!")
        return cart_flag
          
    """
    Method Name : verify_cart_content
    Purpose     : To verify items present in the cart
    Returns     : None   
    """
    def verify_cart_content(self,cart_items) :
        
        table = self.driver.find_element_by_xpath("//table[contains(@class,'table table-striped')]")
        # get the rows in the table
        rows = table.find_elements_by_xpath("//tbody/descendant::tr")
        # Create a dictionary to store the table content as item_name:item_price pairs 
        cart_content = {}
        # Go to each row and get the no of columns and the navigate to column 
        # Then get the text from each column
        
        for i in range(0,len(rows)):
            # Find no of columns by getting the td elements in each row
            cols = rows[i].find_elements_by_tag_name('td')
            cols_data = []
            
            for j in range(0,len(cols)):
                # Get the text of each field 
                cols_data.append(cols[j].text)
            
            cart_content.update({cols_data[0]:cols_data[1]})                
                
        #compare and verify the cart content         
        for x1 in cart_content.keys():
                if (cart_content.get(x1) == cart_items.get(x1)):
                    cart_flag = 3   
                else:
                    cart_flag = -1    
               
        if (cart_flag == 3):
            print("Cart content verified. Test Passed!")
        elif (cart_flag == -1):
            print("Cart content mismatch. Test Failed!")
        return cart_flag    

    """
    Method Name : get_cart_item_count
    Purpose     : To count the number of items present in the cart
    Returns     : count   
    """
    def get_cart_item_count(self,cart_items) :
        count = 0
        for key in cart_items.keys():
            count = count + 1
        return count 

        
    """
    Method Name : get_cart_total_cost
    Purpose     : To calculate the total cost of items listed in the cart
    Returns     : total cost
    """
    
    def get_cart_total_cost(self,cart_items) :
        total_cost = 0
        
        for key,value in cart_items.items():
            total_cost = total_cost + int(value)
        return total_cost 
    

class PaymentDetails():
    def __init__(self,driver):
        self.driver = driver
        self.email = 'pree1985@gmail.com'
        self.card_number = '4242 4242 4242 4242'
        self.month_year = '08/21'
        self.cvc = '981'
        self.zip_code = '10001'
        self.mobile_number = '9958796475'
    
    """
    Method Name : send_payment_info
    Purpose     : To send the payment details to the Stripe.com modal dialog
    Returns     : none   
    """    
    def send_payment_info(self):
        
        #switch control to iframe (ie) Stripe.com here
        self.driver.switch_to_frame(self.driver.find_element_by_xpath("//iframe[contains(@name,'stripe_checkout_app')]"))
        #send email info
        email = self.driver.find_element_by_xpath("//input[contains(@type,'email')]")
        email.send_keys(self.email)
        time.sleep(2)
        #send card number
        card_number = self.driver.find_element_by_xpath("//input[contains(@placeholder,'Card number')]")
        card_number.send_keys(self.card_number)
        time.sleep(2)
        #send MM/YY
        month_year = self.driver.find_element_by_xpath("//input[contains(@placeholder,'MM / YY')]")
        month_year.send_keys(self.month_year)
        time.sleep(2)
        #send cvc
        cvc = self.driver.find_element_by_xpath("//input[contains(@placeholder,'CVC')]")
        cvc.send_keys(self.cvc)
        time.sleep(2)
        #send Zip Code
        zip_code = self.driver.find_element_by_xpath("//input[contains(@placeholder,'ZIP Code')]")
        zip_code.send_keys(self.zip_code)
        time.sleep(2)
        #enable the Remember me checkbox
        remember_me = self.driver.find_element_by_xpath("//div[contains(@class,'Checkbox-tick')]")
        remember_me.click()
        time.sleep(2)
        #send the mobile number
        mobile_number = self.driver.find_element_by_xpath("//input[contains(@inputmode,'tel')]")
        mobile_number.send_keys(self.mobile_number)
        time.sleep(2)

