from banking_connection import *
import banking_login


def add_beneficiary(username):
    
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


    

    if ben==1:

        insert_ben=("INSERT INTO beneficiary_details(username,beneficiary1) VALUES (%s, %s)")
        ben1=ben_list[0]
        ben_details=(username,ben1)
        cursor1.execute(insert_ben,ben_details)
        list_beneficiary(username)
    elif ben>1:
        sql=("SELECT  RIGHT(COLUMN_NAME,1) FROM information_schema.COLUMNS  WHERE TABLE_SCHEMA = 'banking_app' AND TABLE_NAME ='beneficiary_details' ORDER BY ORDINAL_POSITION DESC  LIMIT 1")
        cursor2.execute(sql)
        result2=cursor2.fetchall()
        last_column_no=int(result2[0][0])
        for j in range(last_column_no+1,ben+1):
            update_ben=(f"ALTER TABLE beneficiary_details ADD beneficiary{j} varchar(100)")
            cursor1.execute(update_ben)
        val=("%s,"*ben +"%s")

        insert_ben=(f"INSERT INTO beneficiary_details VALUES ({val})")
        
        values=(username,*ben_list)
        cursor1.execute(insert_ben,values)
    connection1.commit()
    n=int(input("\n Press 1 to list all beneficiaries \n       2 to go back to menu bar"))
    while n:
        if n==1:
            list_beneficiary(username)
            break

        elif n==2:
            banking_login.revert_to_login(username)
            break
        else:
            print("Invalid input! Try again..")
            n=int(input("\n Press 1 to list all beneficiaries \n       2 to go back to menu bar"))


            
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
                sql=('''SELECT  RIGHT(COLUMN_NAME,1) FROM information_schema.COLUMNS  WHERE TABLE_SCHEMA = 'banking_app' 
                AND 
                TABLE_NAME ='beneficiary_details' ORDER BY ORDINAL_POSITION DESC  LIMIT 1''')
                cursor2.execute(sql)
                result2=cursor2.fetchall()
                n=int(result2[0][0])
                for j in range(1,n+1):
                    if i[j]!=None:
                        print(f"Name of Beneficiary{j} : {i[j]}")
                banking_login.revert_to_login(username)
                              
                        
                    

    connection1.commit()
    
    