"""This file connections to the databases used."""


import mysql.connector
import random



connection1 = mysql.connector.connect(host='localhost',     # This connection is made 
                                    database='banking_app', #to my mysql database banking_app
                                     user='yourusername',password='yourpassword'
                                        )    
                                         


cursor1=connection1.cursor()                        



def executesql(sql):
    cursor1.execute(sql)
    resultset=cursor1.fetchall()
    return resultset
