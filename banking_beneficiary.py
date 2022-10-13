'''This file contains functions to add beneficiaries and to list beneficiaries'''


from banking_connection import *
import banking_login
import random

def executesql(sql):
    '''This function is for executing select statements in sql 
    and storing the result in variable resultset'''
    cursor1.execute(sql)
    resultset=cursor1.fetchall()
    return resultset

def add_beneficiary(username):
    '''This function is to add benficiaries for current user by taking number of beneficiaries as input from user'''

    
    ben=int(input("Enter number of beneficiaries:"))
    ben_list=[input(f"Enter name of beneficiary {ben} :") for ben in range(1,ben+1)]
    for i in range(ben):
        insert_ben=("INSERT INTO beneficiary_details VALUES (%s, %s,%s)")
        ben1=ben_list[i]
        ben_details=(username,ben1,i+1)
        cursor1.execute(insert_ben,ben_details)
        list_beneficiary(username)
    connection1.commit()
            
#This function shows the list of beneficiaries 
def list_beneficiary(username):
    '''This function shows the user the list of beneficiaries added to account'''

    result=executesql('''Select username,beneficiary_name from beneficiary_details''')
    l=[]
    for i in result:

        l.append(i[0])
    
    if username not in l:
                print("No beneficiaries added to account. Press 2 to add beneficiary.")
                banking_login.login_menu(username)
    d={}
    for a,b in result:
        d.setdefault(a,[]).append(b) 
    

     
    resultset=executesql('''select username,accountnum from Accountdetails''')
    acc={}
    for a,b in resultset:
        acc.setdefault(a,[]).append(b)

    sql='''select username,count(beneficiary_id) from beneficiary_details group by username'''
    cursor1.execute(sql)
    count=cursor1.fetchall()
    for n in count:
        if n[0]==username:
            num_ben=n[1]
            if d.get(username)!=None:
                for j in d.get(username):
                    print(f"Name of beneficiary : {j}\t Account number : {acc[j][0]}")
    connection1.commit()
    
    

 
                              
                        
                    

    
    
    