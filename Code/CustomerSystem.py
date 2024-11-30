# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import csv
import os
import time

def printMenu():
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')
    #time.sleep(3)
    return enterCustomerInfo()

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def enterCustomerInfo():
    while True:
        os.system('cls')
        first_name = input('First Name: ')
        if first_name == '':
            print('Please enter a first name')
            time.sleep(2)
        last_name = input('Last Name: ')
        if last_name == '':
            print('Please enter a last name')
            time.sleep(2)
        city = input('City: ')
        if city == '':
            print('Please enter a City')
            time.sleep(2)
        while True:
            postal_code = input('Postal Code: ')
            if len(postal_code) == 3 and validatePostalCode(postal_code) == True:
                break
            else:
                print('Invalid postal code. Please enter 3 character postal code.')
                time.sleep(1)
                os.system('cls')
        os.system('cls')
        print(f'Name: {first_name} {last_name}')
        print(f'City: {city}')
        print(f'Postal Code: {postal_code}')
        check = input('Confirmation (yes/no) ')
        if check == 'yes':
            break
        elif check == 'no':
            time.sleep(0.0001)
    while True:
        card_number = input('Card Number: ')
        valid = validateCreditCard(card_number)
        if valid == True:
            credentials = generateCustomerDataFile(first_name, last_name, city, postal_code, card_number)
            if credentials == True:
                print('Customer data file exists already')
                break
            else:
                print('Information has been updated')
                break
        else:
            print('Input a valid card number')
            time.sleep(1)
            
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed         
    This function may also be broken down further depending on your algorithm/approach
'''
#other encoding: 'ISO-8859-1'
def validatePostalCode(postal_code):
    code = postal_code
    with open('postal_codes.csv', 'r', newline = '', encoding = 'ISO-8859-1') as file:
        read = csv.reader(file, delimiter = '|')
        for row in read:
            if row[0] == code:
                print('Valid Postal Code')
                time.sleep(0.5)
                return True
        else:
            return False
        
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validateCreditCard(card_number):
    card = card_number
    reversed_digits = card[::-1]
    total_sum = 0
    for i, digit in enumerate(reversed_digits):
        digit = int(digit)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:  
                digit -= 9     
        total_sum += digit 
    if  total_sum % 10 == 0:
        return True
    else:
        return False
       
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def generateCustomerDataFile(first_name, last_name, city, postal_code, card_number):
    with open('solutions.csv', 'r', newline = '', encoding = 'UTF-8') as file:
        read = csv.reader(file, delimiter = '|')
        for row in read:
            if first_name == row[0]:
                return True
        else:
            with open('solutions.csv', 'r', newline = '', encoding = 'UTF-8') as file:
                read = csv.reader(file, delimiter = '|')
            with open('solutions.csv', 'a', newline = '', encoding = 'UTF-8') as file:
                write = csv.writer(file, delimiter = '|')
                write.writerow([ first_name, last_name, city, postal_code, card_number]) 
            return False

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        enterCustomerInfo()

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")