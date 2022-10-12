from banking_connection import *
import banking_accountdetails
import banking_deposit_and_transfer
import banking_beneficiary
import banking_updation
global username
def login_menu(username):
    m=int(input(" \n Select from below options: \n 1. Display account info \n 2. Add beneficiaries \n 3. Deposit money \n 4. Show list of beneficiaries \n 5. Update account info \n 6. Transfer fund \n 7. Change mpin \n 8. Register new card \n \n Please enter your choice:"))
    if m==1:
        banking_accountdetails.display_account_details(username)
    elif m==2:
        banking_beneficiary.add_beneficiary(username)
    elif m==3:
        banking_deposit_and_transfer.deposit(username)
        
    elif m==4:
       banking_beneficiary.list_beneficiary(username)
    elif m==5:
        banking_updation.update_account_info(username)
    elif m==6:
        banking_deposit_and_transfer.transfer_fund(username)
    elif m==7:
        banking_updation.change_mpin(username)
    elif m==8:
        banking_updation.register_newcard(username)
    
    else:
            print("Please choose valid option!")
            login_menu(username)

    
def revert_to_login(username):
            q=int(input("Press: \n 1 to go back to Login menu \n 2 to go back to home page \n 3 to close application \n Enter your choice:"))
            if q==1:
                    login_menu(username)
            elif q==2:
                    import Banking_main
                    Banking_main.enter_menu()
            else:
                    exit

        

def login():
    global username,m
    
    username=input("\n Enter username:")
    sql='''select username from Registration_details'''
    cursor1.execute(sql)
    result=cursor1.fetchall()
    l=[]
    for i in result:
            l.append(i[0])
    count=0
    a=username not in l
    while count<2 and a:
                        print("Sorry, incorrect username. Please try again!")
                        username=input("\n Enter username:")
                        a=username not in l
                        count+=1
    if count==2:
            print("Sorry incorrect username. If new user, please register.")
            import Banking_main
            Banking_main.enter_menu()
            exit
    else:
            print(f"\n {'*'*30} You have successfully logged in ... {'*'*30} \n ")
            login_menu(username)
    connection1.commit()