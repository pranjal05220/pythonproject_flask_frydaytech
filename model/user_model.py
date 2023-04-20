import json

import mysql.connector


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
         return json.dumps(result)
        else:
            return "NO DATA FOUND" #if we delete data from mysql database
        # query execution code

    def user_addone_model(self, data):  # read operation
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}' )")
        # print(data['email'])
        return "user addded successully"

    def user_update_model(self, data):  # read operation
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password'{data['password']}'WHERE id='{data['id']}' )")
        return "user updated successully"

    def user_delete_model(self, id):  # read operation
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return "user deleted successully"
        else:
            return "nothing to delete"

