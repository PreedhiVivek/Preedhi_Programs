"""
Selenium Test Automation:
Scope:
1.To Read the temperature and go to either mosturizer page or sunscreen page accordingly
2.Add the two least expensive moisturizers/sunscreens accordingly
3.Verify the cart screen 
4.Click on 'Pay with Card'. Enter the stripe test card details, email, other requried details and click on Pay now button
5.Verify if redirected to payment successful page 

Author: Preedhi Vivek
Date: 06/08/2019

"""
import time
from selenium import webdriver
import weather_shopper_module as m1 


# Start of program execution
if (__name__ == '__main__') :

    url = "https://weathershopper.pythonanywhere.com/"
    cart_items = {}
    # create an instance of Chrome WebDriver
    driver = webdriver.Chrome()

    # create an object of class Navigate  
    nav_obj1 = m1.Navigate(url,driver)
    # call the method to navigate to weather shopper webapplication
    nav_obj1.navigate_url()

    # maximize window
    driver.maximize_window()

    #Wait for page to load
    time.sleep(2)
    
    # call the method to verify navigation based on the page title
    nav_obj1.verify_navigation_on_page_title()
    
    # create an object of class Decision_Maker
    dec_maker1 = m1.Decision_Maker(driver)

    # call the method to decide the purchase (if moisturizer or sunscreen)
    flag = dec_maker1.decide_purchase()

    #Wait for page to load
    time.sleep(2)

    # call the method to verify the redirection of webpage based on the purchase decision
    nav_obj1.verify_url()

    # create an object of class Items
    items_obj1 = m1.Items(driver)

    if(flag==1):
        #call the method to return the cost of the Aloe Moiturizers 
        item_prices = items_obj1.get_item_prices('Aloe')
    
        time.sleep(2)

        #call the method to add the least priced Aloe Moisturizer to the cart 
        cart_item_name,cart_item_price = items_obj1.add_least_priced_item('Aloe',item_prices)
        cart_items.update({cart_item_name:cart_item_price})
        time.sleep(2)

        #call the method to return the cost of the Almond Moiturizers 
        item_prices = items_obj1.get_item_prices('Almond')

        #call the method to add the least priced Almond Moisturizer to the cart 
        cart_item_name,cart_item_price = items_obj1.add_least_priced_item('Almond',item_prices)
        cart_items.update({cart_item_name:cart_item_price})
        time.sleep(2)

    elif (flag ==2):
        #call the method to return the cost of the spf50 sunscreens
        item_prices = items_obj1.get_item_prices('SPF-50')

        #call the method to add the least priced spf50 sunscreen to the cart 
        cart_item_name,cart_item_price = items_obj1.add_least_priced_item('SPF-50',item_prices)
        cart_items.update({cart_item_name:cart_item_price})
        
        time.sleep(2)
        #call the method to return the cost of the spf30 sunscreens
        item_prices = items_obj1.get_item_prices('SPF-30')
        
        #call the method to add the least priced spf30 sunscreen to the cart 
        cart_item_name,cart_item_price = items_obj1.add_least_priced_item('SPF-30',item_prices)
        cart_items.update({cart_item_name:cart_item_price})
        time.sleep(2)

    # create an object of class Cart
    cart_obj1 = m1.Cart(driver)
    #create an object of class common_events
    com_events1= m1.common_events(driver)

    #call the method to verify the cart label post addition of items
    cart_flag = cart_obj1.check_cart()
    time.sleep(2)
    try:
        if (cart_flag==1):
            #call the method to verify navigation to checkout page
            cart_flag = nav_obj1.verify_url()

            if (cart_flag ==2):
            #call the method to verify the cart content    
                cart_flag = cart_obj1.verify_cart_content(cart_items)
                time.sleep(2)
                if (cart_flag == 3):        
                    #call the method to click on the Pay with Card button
                    com_events1.click_button()
                    time.sleep(2)
         
    except Exception as e:
            print("Exceptions:",e)
            cart_flag = -1

    try:
        #Proceed with payment only if the cart content is correct 
        if (cart_flag == 3):        
            # create an object of class PaymentDetails
            payment = m1.PaymentDetails(driver)

            # call the method to send the payment information
            time.sleep(5)
            payment.send_payment_info()

            #call the method to submit the payment details
            com_events1.click_button()

            #Wait for page to load
            time.sleep(5)

            # call the method to verify the redirection to the payment success confirmation page
            nav_obj1.verify_url()
            time.sleep(5)
    except Exception as e :
        #print("Exception:",e)
        print("Payment Failed!")
    
    # Close the browser window
    driver.close() 
        

