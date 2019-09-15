"""
AUTHOR: Preedhi Vivek
Date: 02/08/2019

SCOPE:
1) Launch Chrome Webdriver
2) Navigate to QA Interview (Factorial Calculator) application webpage
3) Verify if navigated to the correct page
4) Enter a valid postive integer in the console and it will be sent to the input box
5) Click on Calculate! button
6) Compare the factorial calculation in the webpage with the system calculated factorial value
6) Close the browser
"""

import time
import math
from selenium import webdriver

#Get user input for factorial calculation
def get_user_input():
    print("Enter a valid positive integer,less than 171 to perform factorial calculation:")
    input_number= input()
    return input_number

#Find the input box and send the the number for which factorial has to be calculated. 
def send_number_inputbox(input_number):
    locate_input_box=browser.find_element_by_xpath("//input[@placeholder='Enter an integer' and @id='number']")
    locate_input_box.send_keys(input_number)
    time.sleep(2)

#Find the Calculate! button and click on it.
def click_calculate()    :
    browser.find_element_by_xpath("//button[contains(text(),'Calculate!')]").click()

#Verify if the factorial calculation is correct
def verify_factorial_calculation(input_number):
    factorial_text = ""
    factorial_calc = ""
    str_system_calc_factorial = ""
    
    locate_factorial_calc= browser.find_element_by_xpath("//*[contains(@id,'resultDiv')]")

    #extract only the factorial from the output text in the webpage          
    factorial_text = locate_factorial_calc.text
    factorial_calc = factorial_text.split(': ')[1]
    factorial_calc = factorial_calc.strip()
    print("Factorial of %s from the webpage: "%input_number,factorial_calc)
    
    #get the system's factorial calculation 
    system_calc_factorial = math.factorial(int(input_number))
    if (int(input_number)<=21):
        str_system_calc_factorial = str(system_calc_factorial).strip()
    elif (int(input_number)>21 and int(input_number)<171):
        system_calc_factorial = format(system_calc_factorial,'.17g')
        str_system_calc_factorial = str(system_calc_factorial).strip()
    elif (int(input_number)>=171):
        str_system_calc_factorial = "Infinity"    
    print("System calculated Factorial of %s: "%input_number,str_system_calc_factorial)


    #compare the factorial calculation between the webpage display and system calculated value
    if (factorial_calc == str_system_calc_factorial):
        print("Factorial calculation is correct! Test Passed")    
    else:
        print("Factorial calculation is incorrect! Test Failed")
   

#----START OF SCRIPT
if __name__=='__main__':
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

    #Call the function to receive user input
    input_no = get_user_input() 

    #Call the function to send the user input to be displayed in the input box and then click on the Calcule! button
    send_number_inputbox(input_no)

    #Call the function to click on the Calculate! button
    click_calculate()
    #Wait has to be introduced before verifying factorial calculation. Else the factorial calculation retrived from the webpage might return empty.  
    time.sleep(5)

    #Call the function to verify the factorial calculation
    verify_factorial_calculation(input_no)

    #Wait for the page to load and get displayed for verification
    time.sleep(5)
    # Quit the browser window
    browser.quit() 
