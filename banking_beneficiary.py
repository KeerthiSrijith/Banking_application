from banking_connection import *
import banking_login
def add_beneficiary(username):
    #This function is to add beneficiaries 
    ben=int(input("Enter number of beneficiaries:"))
    ben_list=[input(f"Enter name of beneficiary {ben} :") for ben in range(1,ben+1)]

    if ben==1:

        insert_ben=("INSERT INTO beneficiary_details VALUES (%s, %s)")
        ben1=ben_list[0]
        ben_details=(username,ben1)
        cursor1.execute(insert_ben,ben_details)
        list_beneficiary(username)
    connection1.commit()
            
#This function shows the list of beneficiaries 
def list_beneficiary(username):
    sql='''Select * from beneficiary_details'''
    cursor1.execute(sql)
    result=cursor1.fetchall();
    l=[]
    for i in result:

        l.append(i[0])
    
    if username not in l:
                print("No beneficiaries added to account. Press 2 to add beneficiary.")
                banking_login.login_menu(username)
                
    for i in result:     
        if i[0]==username:
            print("Name of Beneficiary 1 :",i[1])

            banking_login.revert_to_login(username)
    connection1.commit()