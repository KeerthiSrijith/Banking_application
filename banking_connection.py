import mysql.connector
import random



connection1 = mysql.connector.connect(host='localhost',
                                         database='banking_app',
                                         user='usernew',password='yourpassword'
                                        )


cursor1=connection1.cursor()

connection2=mysql.connector.connect(host='localhost',user='usernew',database='information_schema',password='yourpassword')
cursor2=connection2.cursor()