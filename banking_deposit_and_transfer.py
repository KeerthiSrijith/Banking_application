
from banking_connection import *
import banking_beneficiary
import banking_login
"""This file contains the functions written for depositing money to user account 
and for transferring funds 
;param 1- username All the methods take the parameter username, which is the name of the account holder"""

def deposit(username):
    """This method takes the parameter as username and allows user to deposit money into his account"""
    
    
    acc_no=int(input("Enter your account number:"))           # Account number of user is taken as input for confirmation

    result=executesql('''select username,accountnum from Accountdetails''')
 
    l1=[]
    
    for i in result:
            l1.append(i[1])

            
    
    l2=[]
    for j in result:
            l2.append(i[0])
            l2.append(i[1])
    d={}
    for a,b in result:
            d.setdefault(a,[]).append(b)
  
    if (acc_no not in l1) or (d[username][0]!=acc_no):        # Account number validation
                     print("Sorry, entered account number is incorrect. Please try again!")
                     deposit(username)
                     exit
    else:

        amt=int(input("Enter amount to deposit:"))
        aaa=(amt,acc_no)
        cursor1.execute(f"Update Accountdetails set account_balance=account_balance+(%s) where accountnum=(%s)",aaa)
        connection1.commit()
        print("Money deposited in account")
        print("Back to login menu!")
        banking_login.login_menu(username)
        


def transfer_fund(username):
    """This method allows the user  to transfer fund to beneficiaries."""

    
    acc_no=int(input("Enter Account number:"))
      
    result=executesql('''select username,accountnum from Accountdetails''')
    l1=[]
    
    for i in result:
            l1.append(i[1])
 
            
    
    l2=[]
    for j in result:
            l2.append(i[0])
            l2.append(i[1])
    d={}
    for a,b in result:
            d.setdefault(a,[]).append(b)

    if (acc_no not in l1) and (d[username][0]!=acc_no):
                     print("Sorry, entered account number is incorrect. Please try again!")
                     transfer_fund(username)
                     exit
    else:
            d1={}
            sql1='''select accountnum,account_balance from Accountdetails'''
            cursor1.execute(sql1)
            result1=cursor1.fetchall()
            for m,n in result1:
                    d1.setdefault(m,[]).append(n)

            amt=int(input("Enter amount to transfer:"))
            if int(d1[acc_no][0])<amt:
                    print("Insufficient balance. Fund transfer not possible!")
                    print("Back to login menu")
                    banking_login.login_menu(username)
            
            else:
                    print("Beneficiary details are: \n")
                    banking_beneficiary.list_beneficiary(username)
                    acc_to_transfer=int(input("Enter Account number to transfer fund to"))
                    if acc_to_transfer not in l1:
                            print("Sorry, entered account number is incorrect. Please try again!")
                            transfer_fund(username)
                    else:
                            aaa1=(amt,acc_to_transfer)
                            aaa2=(amt,acc_no)
                            cursor1.execute(f"Update Accountdetails set  account_balance=account_balance-(%s) where accountnum=(%s)",aaa2)
                            cursor1.execute(f"Update Accountdetails set  account_balance=account_balance+(%s) where accountnum=(%s)",aaa1)
                            print("Amount successfully transfered")
                            print("Back to login menu")
                            banking_login.login_menu(username)
    connection1.commit()