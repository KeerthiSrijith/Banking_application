"""This file contains the method for displaying user information
;param- username is passed. The value is taken as input while logging in"""


from banking_connection import *
import banking_login

def display_account_details(username):
    """This function shows the account details of user"""
    
    sql = '''SELECT * from Accountdetails'''

#Executing the query
    cursor1.execute(sql)

#Fetching 1st row from the table
    result = cursor1.fetchall();
    
    print("\n")
    print("******Account Details******")
    for i in result:
        if i[0]==username:
            
                

            print('-'*60)
            print("| {:^30} | {:^30}|".format("Account number",i[1]))
            print('-'*60)
            print("| {:^30} | {:^30}|".format("Account balance",i[2]))
            print('-'*60)
            print("| {:^30} | {:^30}|".format("Creditcard number",i[3]))
            print('-'*60)
            print("| {:^30} | {:^30}|".format("Creditcard number",i[4]))
            print('-'*60)





    banking_login.revert_to_login(username)