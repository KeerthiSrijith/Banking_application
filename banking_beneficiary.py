from pprint import pprint
from banking_connection import *
import banking_login
import random

def executesql(sql):
    cursor1.execute(sql)
    resultset=cursor1.fetchall()
    return resultset

def add_beneficiary(username):
    global ben,ben_list,ben_name
    
    #This function is to add beneficiaries 
    ben=int(input("Enter number of beneficiaries:"))
    sql='''select username,accountnum from Accountdetails'''
    cursor1.execute(sql)
    result=cursor1.fetchall()
    l1=[]
    
    for i in result:
            l1.append(i[0])
    ben_list=[]
    for k in range(1,ben+1):
        ben_name=input(f"Enter name of beneficiary {k} :")
        b=ben_name in l1
        while not b:
            print("Beneficiary not registered with SBI. Enter valid name of beneficiary")
            ben_name=input(f"Enter name of beneficiary {k} :")
            b=ben_name in l1
        if b:
            ben_list.append(ben_name)
    
    for j in range(ben):
        insert_ben=("INSERT INTO ben_details VALUES (%s, %s, %s)")
        insert_values=(username,ben_list[j],j+1)
        cursor1.execute(insert_ben,insert_values)
        connection1.commit()

      
    n=int(input("\n Press 1 to list all beneficiaries \n       2 to go back to menu bar"))
    if n==1:
            list_beneficiary(username)
            

    elif n==2:
            banking_login.revert_to_login(username)
            
    else:
            print("Invalid input! Try again..")
            n=int(input("\n Press 1 to list all beneficiaries \n       2 to go back to menu bar"))


    
#This function shows the list of beneficiaries 
def list_beneficiary(username):
    
    sql='''Select username,beneficiary_name from ben_details'''
    cursor1.execute(sql)
    result=cursor1.fetchall();
    l=[]
    for i in result:

        l.append(i[0])
    
    if username not in l:
                print("No beneficiaries added to account. Press 2 to add beneficiary.")
                banking_login.login_menu(username)
    d={}
    for a,b in result:
        d.setdefault(a,[]).append(b) 
    

    sql='''select username,count(beneficiary_id) from ben_details group by username''' 
    resultset=executesql('''select username,accountnum from Accountdetails''')
    acc={}
    for a,b in resultset:
        acc.setdefault(a,[]).append(b)


    cursor1.execute(sql)
    count=cursor1.fetchall()
    for n in count:
        if n[0]==username:
            num_ben=n[1]
            for j in d.get(username):
                    print(f"Name of beneficiary : {j}\t Account number : {acc[j][0]}")
    connection1.commit()
    
    

    # for i in result:     
    #         if i[0]==username:
    #             sql=('''SELECT  RIGHT(COLUMN_NAME,1) FROM information_schema.COLUMNS  WHERE TABLE_SCHEMA = 'banking_app' 
    #             AND 
    #             TABLE_NAME ='beneficiary_details' ORDER BY ORDINAL_POSITION DESC  LIMIT 1''')
    #             cursor2.execute(sql)
    #             result2=cursor2.fetchall()
    #             n=int(result2[0][0])
    #             for j in range(1,n+1):
    #                 if i[j]!=None:
    #                     print(f"Name of Beneficiary{j} : {i[j]}")
    #             banking_login.revert_to_login(username)
                              
                        
                    

    
    
    