import mysql.connector
import random



connection1 = mysql.connector.connect(host='localhost',
                                         database='banking_app',
                                         user='usernew',password='yourpassword'
                                        )


cursor1=connection1.cursor()
