import json

import mysql.connector
from flask import make_response

class user_model():
    def __init__(self):  # constructor
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="pass123",
                                               database="flask_tutorial")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("connection done")
        except:
            print("error")

    def user_getall_model(self):  #read operation
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0: #if dictionary contains more then 1 value function
         #return json.dumps(result)
         res = make_response({"payload": result}, 200)
         res.headers['Access-Control-Allow-Origin'] = "*"
         return res
        else:
            #return "NO DATA FOUND" #if we delete data from mysql database
        # query execution code
            return make_response({"message": "NO DATA FOUND"},204)
    def user_addone_model(self, data):  # read operation
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}' )")
        # print(data['email'])
        return make_response({"message": "USER ADDED SUCCESSFULLY"},200)

    def user_update_model(self, data):  # read operation
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password'{data['password']}'WHERE id='{data['id']}' )")
        return make_response({"message": "USER UPDATED SUCCESSFULLY"}, 202)

    def user_delete_model(self, id):  # read operation
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message": "USER DELETED SUCCESSFULLY"}, 200)
        else:
            return make_response({"message": "NOTHING TO DELETE"}, 204)

