import mysql.connector
from mysql.connector import Error
import random

connection = mysql.connector.connect(host='localhost',
                                         database='banking_app',
                                         user='root',
                                         password='Krishna12*',auth_plugin='mysql_native_password')


cursor=connection.cursor()

    

def registration_details():
        global username
        username=input("Enter username:")
        #password=input("Create password:")
        #re_pass=input("Re-enter password:")
        #if password!=re_pass:
            #raise Exception("Passwords do not match")
        address=input("Enter address:")
        aadhar=input("Enter aadhar number:")
        mob=input("Enter mobile no.:")
        #bankname=input("Enter bank name:")
        #credit_card=input("Enter credit card number:")
        #debit_card=input("Enter debit card number:")
        print("Account creation successful")
        insert_stmt = (
   "INSERT INTO Registration_details VALUES (%s, %s, %s, %s)"
)
        data=(username,address,aadhar,mob)
        cursor.execute(insert_stmt,data)
        allot_cards()
        print("Login here")
        login()
def allot_cards():
    import random
    y=random.randint(0,9)
    
    print("Your creditcard number is:")
    #print=(random.randint(111,999)*99999999)
    
    y=random.randint(111,999)*99999999
    print(y)

    print("Your debitcard umber is:")
    z=random.randint(111,999)*99999999
    print(z)
    
    insert=("INSERT INTO Accountdetails VALUES (%s, %s, %s, %s, %s)")
    account_details=(username,y,0,z,0)
    cursor.execute(insert,account_details)

    
    
    c_mpin=random.randint(1111,9999)
    print(c_mpin)
    d_mpin=random.randint(1111,9999)
    c_cvv=random.randint(111,999)
    d_cvv=random.randint(111,999)
    insrt_card_details=("INSERT INTO card_details VALUES ( %s, %s, %s, %s, %s, %s, %s)")
    card_details=(username,y,c_mpin,c_cvv,z,d_mpin,d_cvv)
    cursor.execute(insrt_card_details, card_details)                  


def change_mpin():
        print("To change mpin")
        acc=input("Enter Account number:")
        mpin=int(input("Enter old mpin"))
        newmpin=int(input("Enter new mpin:"))
        m=(newmpin,acc)
        cursor.execute(f"Update card_details set  cpin=(%s) where creditcardnum=(%s)",m)
        cursor.execute(f"Update card_details set  dpin=(%s) where debitcardnum=(%s)",m)
        print("Pin successfully updated") 
        
  


    
    
    
    
def display_account_details():
    
    sql = '''SELECT * from Accountdetails'''

#Executing the query
    cursor.execute(sql)

#Fetching 1st row from the table
    result = cursor.fetchall();
    for i in result:
        if i[0]==username:
            print("Credit card number is:",i[1] )
            print("Credit card balance is:",i[2] )
            print("Debit card number is:",i[3] )
            print("Debit card balance is:",i[4] )
            

def add_beneficiary():
    ben1=input("Enter name of first beneficiary for credit card:")
    ben2=input("Enter name of second beneficiary for credit card:")
    ben3=input("Enter name of first beneficiary for debit card:")
    ben4=input("Enter name of second beneficiary for debit card:")
    insert_ben=("INSERT INTO beneficiary_details VALUES (%s, %s, %s, %s, %s)")
    ben_details=(username,ben1,ben2,ben3,ben4)
    cursor.execute(insert_ben,ben_details)
    
def list_beneficiary():
    sql='''Select * from beneficiary_details'''
    cursor.execute(sql)
    result=cursor.fetchall();
    for i in result:
        if i[0]==username:
            print("Beneficiary 1 for credit card:",i[1])
            print("Beneficiary 2 for credit card:",i[2])
            print("Beneficiary 1 for debit card:",i[3])
            print("Beneficiary 2 for credit card:",i[4])

def update_account_info():
    n=int(input("Choose to update: \n 1. Username \n 2. Address \n 3. Aadhar \n 4. Mobile no."))
    if n==1:
        new=input("Enter new username:")
        u=(new,username)
        cursor.execute(f"Update Registration_details set  username=(%s) where username=(%s)",u)
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
        
def deposit():
    acc_no=input("Enter Account number:")
    amt=int(input("Enter amount to deposit:"))
    aaa=(amt,acc_no)
    cursor.execute(f"Update Accountdetails set  credit_card_balance=credit_card_balance+(%s) where creditcardnum=(%s)",aaa)
    cursor.execute(f"Update Accountdetails set  debit_card_balance=debit_card_balance+(%s) where debitcardnum=(%s)",aaa)
    
    print("Money deposited in account")
def transfer_fund():
    acc_no=input("Enter Account number:")
    amt=int(input("Enter amount to transfer:"))
    acc_to_transfer=input("Enter Account number to transfer fund to")
    aaa1=(amt,acc_to_transfer)
    aaa2=(amt,acc_no)
    cursor.execute(f"Update Accountdetails set  credit_card_balance=credit_card_balance-(%s) where creditcardnum=(%s)",aaa2)
    cursor.execute(f"Update Accountdetails set  credit_card_balance=credit_card_balance+(%s) where creditcardnum=(%s)",aaa1)
    cursor.execute(f"Update Accountdetails set  debit_card_balance=debit_card_balance+(%s) where debitcardnum=(%s)",aaa1)
    cursor.execute(f"Update Accountdetails set  debit_card_balance=debit_card_balance-(%s) where debitcardnum=(%s)",aaa2)

def register_newcard():
        
        t=input("Enter type of card(credit/debit)")
        if t =='credit':
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
        if t=='debit':
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

def login():
    global username,m
    print("Welcome to login bar")
    username=input("Enter username:")
    #password=input("Create password:")
    
    login_menu()



        
    
        
        
        
        
        
        
def re_enter_menu():
        enter_menu()

    
    

def enter_menu():
        global x
        x=int(input("Select from below options: \n 1. Login  \n 2. Registration "))
        if x==1:
                login()
                exit
        elif x==2:
                registration_details()
                exit
        else:
                print("Please select valid option!")
                re_enter_menu()


enter_menu()



    
      


connection.commit()
connection.close()




