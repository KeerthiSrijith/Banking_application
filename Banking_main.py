import banking_registration
import banking_login




def enter_menu():
        global x
        x=int(input("{} Welcome to SBI Banking {} \n Select from below options: \n 1. Login  \n 2. Registration \n Enter your choice: ".format('*'*30,'*'*30)))
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