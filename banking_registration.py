"""This file contains the methods invoked for registering users"""


from banking_connection import *
import random
import banking_login




def registration_details():
        """This method takes all the user information as input 
        and stores in the table Registration_details"""

        global username
        username=input("\n Enter username:")
        a=username != '' and all(chr.isalpha() or chr.isspace() for chr in username)     #Validation for username
        while not a:
            print("Invalid name entered. Please try again!")
            username=input("Enter username:")
            a=username != '' and all(chr.isalpha() or chr.isspace() for chr in username)
        
        address=input("Enter address:")
        aadhar=input("Enter aadhar number:")
        aadhar="".join(aadhar.split())
        b=aadhar.isnumeric() and len(aadhar)==12                                         #Validation for aadhar number
        while not b:
            print("Invalid aadhar number entered. Aadhar number should be of 12 digits.Please try again!")
            aadhar=input("Enter aadhar number:")
            aadhar="".join(aadhar.split())
            b=aadhar.isnumeric() and len(aadhar)==12


        mob=input("Enter mobile no.: {}".format('+91'))                                   #Validation for mobile number
        c=mob.isnumeric() and len(mob)==10
        while not c:
            print("Invalid mobile number entered. Mobile number should be of 10 digits. Please try again!")
            mob=input("Enter mobile no.: {}".format('+91'))
            mob="".join(mob.split())
            c=mob.isnumeric() and len(mob)==10


        
        print("Account creation successful")
        insert_stmt = ("INSERT INTO Registration_details VALUES (%s, %s, %s, %s)")
        data=(username,address,aadhar,mob)                                
        cursor1.execute(insert_stmt,data)
        allot_cards()                                                 #Calling function to allot cards during registration
        print("Login here")
        banking_login.login()
        connection1.commit()

def allot_cards():
    """This function is called to allot 1 creditcard and 1 debitcard to user at the time of registration"""
    
    
    
    print("Your creditcard number is:")                                # Creditcard and debitcard numbers are randomly alloted
      
    y=random.randint(111,999)*99999999
    print(y)

    print("Your debitcard number is:")
    z=random.randint(111,999)*99999999
    print(z)
    a=random.randint(111,999)*99999999
    insert=("INSERT INTO Accountdetails VALUES (%s, %s, %s, %s, %s)")
    account_details=(username,a,0,y,z)
    cursor1.execute(insert,account_details)

    
                                                                    # Pin and cvv are randomly alloted for each card
    c_mpin=random.randint(1111,9999)
    d_mpin=random.randint(1111,9999)
    c_cvv=random.randint(111,999)
    d_cvv=random.randint(111,999)
    insrt_card_details=("INSERT INTO card_details VALUES ( %s, %s,%s, %s, %s, %s, %s, %s)")
    card_details=(username,a,y,c_mpin,c_cvv,z,d_mpin,d_cvv)
    cursor1.execute(insrt_card_details, card_details)
    connection1.commit()

