'''This is the main file which has to be run for the execution of the project banking application'''
import banking_registration
import banking_login



def enter_menu():
        '''This method shows the options for logging in and registering'''
        global x
        x=int(input("\n {} Welcome to SBI Banking {} \n Select from below options: \n  \n1. Login  \n2. Registration \n \n Enter your choice: ".format('*'*30,'*'*30)))
        if x==1:
                banking_login.login()
                
        elif x==2:
                banking_registration.registration_details()
                
        else:
                print("Please select valid option!")
                enter_menu()


try:
        enter_menu()
except ValueError:
        print("Invalid input. Please try again.")
        enter_menu()