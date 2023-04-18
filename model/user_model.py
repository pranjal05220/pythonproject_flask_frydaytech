import json

import mysql.connector


class user_model():
    def __init__(self):  # constructor
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="pass123",
                                               database="flask_tutorial")
            self.cur = self.con.cursor(dictionary=True)
            print("connection done")
        except:
            print("error")

    def user_getall_model(self):  #read operation
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0: #if dictionary contains more then 1 value function
         return json.dumps(result)
        else:
            return "NO DATA FOUND" #if we delete data from mysql database
        # query execution code

