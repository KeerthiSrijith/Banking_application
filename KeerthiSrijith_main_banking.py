import mysql.connector
import random



connection = mysql.connector.connect(host='localhost',
                                         database='banking_app',
                                         user='root',
                                         password='Krishna12*',auth_plugin='mysql_native_password')


cursor=connection.cursor()

    

def registration_details():
        global username
        username=input("Enter username:")
        address=input("Enter address:")
        aadhar=input("Enter aadhar number:")
        mob=int(input("Enter mobile no.:"))
        
        print("Account creation successful")
        insert_stmt = ("INSERT INTO Registration_details VALUES (%s, %s, %s, %s)")
        data=(username,address,aadhar,mob)
        cursor.execute(insert_stmt,data)
        allot_cards()
        print("Login here")
        login()

def allot_cards():
    
    
    
    print("Your creditcard number is:")
      
    y=random.randint(111,999)*99999999
    print(y)

    print("Your debitcard number is:")
    z=random.randint(111,999)*99999999
    print(z)
    a=random.randint(111,999)*99999999
    insert=("INSERT INTO Accountdetails VALUES (%s, %s, %s, %s, %s)")
    account_details=(username,a,0,y,z)
    cursor.execute(insert,account_details)

    
    
    c_mpin=random.randint(1111,9999)
    d_mpin=random.randint(1111,9999)
    c_cvv=random.randint(111,999)
    d_cvv=random.randint(111,999)
    insrt_card_details=("INSERT INTO card_details VALUES ( %s, %s,%s, %s, %s, %s, %s, %s)")
    card_details=(username,a,y,c_mpin,c_cvv,z,d_mpin,d_cvv)
    cursor.execute(insrt_card_details, card_details)
    


def change_mpin():
        print("To change mpin")
        acc=input("Enter Account number:")
        mpin=int(input("Enter old mpin"))
        sql='''select accountnum,cpin from card_details union select accountnum,dpin from card_details '''
        cursor.execute(sql)
        result=cursor.fetchall()
        d={}
        for a, b in result:
            d.setdefault(a, []).append(b)
        m=(d[acc])

        if mpin!=m[0] and mpin!=m[1]:
                print("wrong pin entered. Please try again!")
                change_mpin()
        
        else:
                newmpin=int(input("Enter new mpin:"))
                m=(newmpin,acc)
                cursor.execute(f"Update card_details set  cpin=(%s) where creditcardnum=(%s)",m)
                cursor.execute(f"Update card_details set  dpin=(%s) where debitcardnum=(%s)",m)
                print("Pin successfully updated")
                revert_to_login()
        
  

def login_menu():
    m=int(input("Select from below options: \n 1. Display account info \n 2. Add beneficiaries \n 3. Deposit money \n 4. Show list of beneficiaries \n 5. Update account info \n 6. Transfer fund \n 7. Change mpin \n 8. Register new card"))
    if m==1:
        display_account_details()
    elif m==2:
        add_beneficiary()
    elif m==3:
        deposit()
        
    elif m==4:
       list_beneficiary()
    elif m==5:
        update_account_info()
    elif m==6:
        transfer_fund()
    elif m==7:
        change_mpin()
    elif m==8:
        register_newcard()
    
    else:
            print("Please choose valid option!")
            login_menu()
    
    
    
    
def display_account_details():
    
    sql = '''SELECT * from Accountdetails'''

#Executing the query
    cursor.execute(sql)

#Fetching 1st row from the table
    result = cursor.fetchall();
    for i in result:
        if i[0]==username:
            
            print("Account balance is:",i[2] )

    revert_to_login()

            

def add_beneficiary():
    ben1=input("Enter name of  beneficiary 1:")
    ben2=input("Enter name of beneficiary 2:")
    ben3=input("Enter name of beneficiary 3:")
    ben4=input("Enter name of beneficiary 4:")
    insert_ben=("INSERT INTO beneficiary_details VALUES (%s, %s, %s, %s, %s)")
    ben_details=(username,ben1,ben2,ben3,ben4)
    cursor.execute(insert_ben,ben_details)
    revert_to_login()
    
            
    
def list_beneficiary():
    sql='''Select * from beneficiary_details'''
    cursor.execute(sql)
    result=cursor.fetchall();
    l=[]
    for i in result:

        l.append(i[0])
    
    if username not in l:
                print("No beneficiaries added to account. Press 2 to add beneficiary.")
                login_menu()
                
    for i in result:     
        if i[0]==username:
            print("Name of Beneficiary 1 :",i[1])
            print("Name of Beneficiary 2 :",i[2])
            print("Name of Beneficiary 3:",i[3])
            print("Name of Beneficiary 4:",i[4])
            revert_to_login()


                
    

def update_account_info():
    n=int(input("Choose to update: \n 1. Username \n 2. Address \n 3. Aadhar \n 4. Mobile no."))
    if n==1:
        new=input("Enter new username:")
        u=(new,username)
        cursor.execute(f"Update Registration_details set  username=(%s) where username=(%s)",u)
        cursor.execute(f"Update card_details set  username=(%s) where username=(%s)",u)
        cursor.execute(f"Update Accountdetails set  username=(%s) where username=(%s)",u)
    elif n==2:
        new_add=input("Enter new address:")
        a=(new_add,username)
        cursor.execute(f"Update Registration_details set  address=(%s) where username=(%s)",a)
    elif n==3:
        new_aadhar=input("Enter new aadhar number:")
        aa=(new_aadhar,username)
        cursor.execute(f"Update Registration_details set  Aadhar=(%s) where username=(%s)",aa)
    elif n==4:
        new_mobile=input("Enter new mobile number:")
        m=(new_mobile,username)
        cursor.execute(f"Update Registration_details set  Mobile_no=(%s) where username=(%s)",m)
    else:
        print("Wrong option selected!")
    print("Updation successful")
    revert_to_login()
        
def deposit():
    acc_no=input("Enter Account number:")
    amt=int(input("Enter amount to deposit:"))
    aaa=(amt,acc_no)
    cursor.execute(f"Update Accountdetails set  account_balance=account_balance+(%s) where accountnum=(%s)",aaa)
    
    print("Money deposited in account")
    print("Back to login menu!")
    login_menu()


def transfer_fund():

    
    acc_no=input("Enter Account number:")

    sql='''select username,accountnum from Accountdetails'''
    cursor.execute(sql)
    result=cursor.fetchall()
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
    if acc_no not in l1 and d[username]!=acc_no:
                     print("Sorry, entered account number is incorrect. Please try again!")
                     transfer_fund()
                     exit
    else:
            d1={}
            sql1='''select accountnum,account_balance from Accountdetails'''
            cursor.execute(sql1)
            result1=cursor.fetchall()
            for m,n in result1:
                    d1.setdefault(m,[]).append(n)

            amt=int(input("Enter amount to transfer:"))
            if int(d1[acc_no][0])<amt:
                    print("Insufficient balance. Fund transfer not possible!")
                    print("Back to login menu")
                    login_menu()
            
            else:
                    acc_to_transfer=input("Enter Account number to transfer fund to")
                    if acc_to_transfer not in l1:
                            print("Sorry, entered account number is incorrect. Please try again!")
                            transfer_fund()
                    else:
                            aaa1=(amt,acc_to_transfer)
                            aaa2=(amt,acc_no)
                            cursor.execute(f"Update Accountdetails set  account_balance=account_balance-(%s) where accountnum=(%s)",aaa2)
                            cursor.execute(f"Update Accountdetails set  account_balance=account_balance+(%s) where accountnum=(%s)",aaa1)
                            print("Amount successfully transfered")
                            print("Back to login menu")
                            login_menu()


def register_newcard():
        
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
                cursor.execute(insert,val)
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
                cursor.execute(insertd,vald)
        
        print("Back to login menu!")
        login_menu()

def revert_to_login():
            q=int(input("Press: \n 1 to go back to Login menu \n 2 to close application"))
            if q==1:
                    login_menu()
            else:
                    exit

        

def login():
    global username,m
    print("Welcome to login bar")
    username=input("Enter username:")
    sql='''select username from Registration_details'''
    cursor.execute(sql)
    result=cursor.fetchall()
    l=[]
    for i in result:
            l.append(i[0])
    if username not in l:
                     print("Sorry, incorrect username. If new user, please register!")
                     enter_menu()
                     exit
    else:
            login_menu()

    
    

def enter_menu():
        global x
        x=int(input("Select from below options: \n 1. Login  \n 2. Registration "))
        if x==1:
                login()
                
        elif x==2:
                registration_details()
                
        else:
                print("Please select valid option!")
                enter_menu()


try:
        enter_menu()
except ValueError:
        print("Invalid input. Please try again.")
        enter_menu()
        


    
      


connection.commit()
connection.close()



