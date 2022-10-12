"""This file contains methods 
to update user information, to change mpin of cards, and to register for a newcard
;param - usename is passed as parameter across all functions"""


from banking_connection import *
import banking_login
def update_account_info(username):
    """This method allows user to update information such as username, address, aadhar and mobile number"""
    n=int(input("Choose to update: \n 1. Username \n 2. Address \n 3. Aadhar \n 4. Mobile no. \n Enter your choice for updation:"))
    if n==1:
        new=input("Enter new username:")
        u=(new,username)
        cursor1.execute(f"Update Registration_details set  username=(%s) where username=(%s)",u)
        cursor1.execute(f"Update card_details set  username=(%s) where username=(%s)",u)
        cursor1.execute(f"Update Accountdetails set  username=(%s) where username=(%s)",u)
    elif n==2:
        new_add=input("Enter new address:")
        a=(new_add,username)
        cursor1.execute(f"Update Registration_details set  address=(%s) where username=(%s)",a)
    elif n==3:
        new_aadhar=input("Enter new aadhar number:")
        aa=(new_aadhar,username)
        cursor1.execute(f"Update Registration_details set  Aadhar=(%s) where username=(%s)",aa)
    elif n==4:
        new_mobile=input("Enter new mobile number:")
        m=(new_mobile,username)
        cursor1.execute(f"Update Registration_details set  Mobile_no=(%s) where username=(%s)",m)
    else:
        print("Wrong option selected!")
    print("Updation successful")
    connection1.commit()
    banking_login.revert_to_login(username)

def change_mpin(username):
        """This method is called when the user intends to change the mpin of his/her card"""
        print("To change mpin")
        acc=input("Enter Account number :")
        mpin=int(input("Enter old mpin : "))
        sql="select cpin,dpin from card_details where accountnum={} ".format(acc) 
        
        cursor1.execute(sql)
        result=cursor1.fetchall()
        l=[]
        for i in result:
            l.append(i[0])
               
        if (mpin in l):
            newmpin=int(input("Enter new mpin:"))
        else:
            print("Please enter correct pin ")
            change_mpin(username)

        # for a, b in result:
        #     d.setdefault(a, []).append(b)
        # l=[]
        # for i in result:
        #     l.append(i[1])
        
        # if str(d[acc][0])!=mpin:
        #         print("wrong pin entered. Please try again!")
        #         change_mpin(username)
        
        # else:
                # newmpin=int(input("Enter new mpin:"))
        m=(newmpin,acc)
        cursor1.execute(f"Update card_details set  cpin=(%s) where creditcardnum=(%s)",m)
        cursor1.execute(f"Update card_details set  dpin=(%s) where debitcardnum=(%s)",m)
        print("Pin successfully updated")
        connection1.commit()
        banking_login.revert_to_login(username)


def register_newcard(username):
        """This method is invoked for registering for a new card"""
        
        t=input("Enter type of card(credit/debit)")
        if t =='credit' or t=='CREDIT' or t=='Credit':
                print("Credit card allotted successfully!")
                print("Your new credit card details are:")
                y=random.randint(111,999)*99999999
                print(y)
                pin=random.randint(1111,9999)
                cvv=random.randint(111,999)
                print("cvv number=",cvv)
                print("mpin=",pin)
                u=(y,pin,cvv,username)

                insert="INSERT INTO card_details(username,creditcardnum,cpin,ccvv) VALUES ( %s, %s, %s, %s)  "
                
                val=(username,y,pin,cvv)
                cursor1.execute(insert,val)
        elif t=='debit' or t=='Debit' or t=='DEBIT':
                print("Debit card allotted successfully!")
                print("Your new debit card details are:")
                z=random.randint(111,999)*99999999
                print(z)
                pin=random.randint(1111,9999)
                cvv=random.randint(111,999)
                print("cvv number=",cvv)
                print("mpin=",pin)
                insertd="INSERT INTO card_details(username,debitcardnum,dpin,dcvv) VALUES ( %s, %s, %s, %s)"
                vald=(username,z,pin,cvv)
                cursor1.execute(insertd,vald)
        
        print("Back to login menu!")
        banking_login.login_menu(username)