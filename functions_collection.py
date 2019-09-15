"""
Purpose:
Test Script to have a collection of common functions.

Author: Preedhi Vivek
Date: 23/07/2019

"""

"""
Function Name : get_item_prices
Purpose : To get the prices of the items and extract only the numeric part
Returns : List containing the prices of the items 

"""
def get_item_prices(items_price) :
    #variables initialization
    split_items_price = []
    all_items_price = []
    new_price = 0
        
    for i in range(0,len(items_price)) :
        
        split_items_price = items_price[i].text.split("Price: ", 1)

        if (split_items_price[1].find('Rs. ')!=-1):
            new_price = split_items_price[1].split('Rs. ')
            new_price = int(new_price[1])
        else:
            new_price = split_items_price[1]
            new_price = int(new_price)
            
        all_items_price.append(new_price)
        
        
    return all_items_price



