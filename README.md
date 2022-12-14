# Banking_application

**Project Description**

The project is based on developing a banking application which allows users to create account and perform several banking operations. It acts as a user interface wich enables users to register themselves and login to the application in order to perform the operations. The code is written in python and mysql database is connected via mysql connector.

**Tools used**
Python3 is used for programming. MySQL version 8.0.30 can be used for creating databases. Python mysql-connector is used for connecting python with mysql databse.


**Code description**

The execution of the program starts with a menu for user to select option to login or register.
If user selects register option, the function to register user, registration_details() is invoked. In this function the user can enter personal details and account details. Once registration is complete, the user will be redirected to login page.
When the login function is called, the function login_menu() is invoked which displays various functionalities of the banking application to the user.

The functions mapping the functionalities are:
1. display_account_details() - To display account details of user
2. add_beneficiary() - Allows users to add beneficiaries
3. deposit() - Allows users to deposit money
4. list_beneficiary() - To list out the beneficiaries
5. update_account_info() To update account information
6. transfer_fund() - To transfer funds across accounts
7. change_mpin() Allows users to change pin of existing cards
8. register_newcard() - Allows users to register new card

In all the above functions, username is taken as the parameter which is taken as input from user.

**Validation checks**
There are validation checks implemented on several variables. The validity of the following variables are checked in the manner described.
1. username - Must contain only alphabets and spaces
2. password - Should contain 1 capital letter, 1 small letter, 1 number and 1 special character
3. Aadhar - Should contain 12 digits (space may be included )
4. Mobile_no - Should contain 10 digits only


**Modules imported**

I have imported the modules mysql.connector and the libraries re and random to make use of the libary functions.

**Tables descrition**

I have created 5 tables- 


1. Registration details - Stores the username and all other information of the user
2. Accoutdetails - Includes the account information of the user such as name, account number and account balance
3. beneficiary_details -  Stores the beneficiary name for each username
4. card_details - Stores card detais such as cardnumber,mpin and cvv
5. login_details - This tables stores user credentials, i.e, username and password

**Database and tables initialisation**

All the commands to initialise the database and tables can be found in the file sqlfiles

**To execute the program:**

Run the single file **Banking_main.py** which is the main file onto which all other files are imported.
