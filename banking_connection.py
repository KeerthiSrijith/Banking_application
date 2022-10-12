"""This file connections to the databases used. 
Two connections are made"""


import mysql.connector
import random



connection1 = mysql.connector.connect(host='localhost',     # This connection is made 
                                    database='banking_app', #to my mysql database banking_app
                                     user='usernew',password='yourpassword'
                                        )    
                                         


cursor1=connection1.cursor()                        

connection2=mysql.connector.connect(host='localhost',        # This connection is made to the database information_schema
                                  user='usernew',            #for the purpose of adding new columns to beneficiary table based on existing columns
                                  database='information_schema',
                                 password='yourpassword')
cursor2=connection2.cursor()