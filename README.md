# Banking_application

Project Description

The project is based on developing a banking application which allows users to create account and perform several banking operations. It acts as a user interface wich enables users to register themselves and login to the application in order to perform the operations. The code is written in python and mysql database is connected via mysql connector.

Code description

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
