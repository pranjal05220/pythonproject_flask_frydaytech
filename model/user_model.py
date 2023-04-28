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

    def user_getall_model(self):  # read operation
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result) > 0:  # if dictionary contains more then 1 value function
            # return json.dumps(result)
            res = make_response({"payload": result}, 200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res
        else:
            # return "NO DATA FOUND" #if we delete data from mysql database
            # query execution code
            return make_response({"message": "NO DATA FOUND"}, 204)

    def user_addone_model(self, data):  # read operation
        self.cur.execute(
            f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}' )")
        # print(data['email'])
        return make_response({"message": "USER ADDED SUCCESSFULLY"}, 200)

    def user_update_model(self, data):  # read operation
        self.cur.execute(
            f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password'{data['password']}'WHERE id='{data['id']}' )")
        return make_response({"message": "USER UPDATED SUCCESSFULLY"}, 202)

    def user_delete_model(self, id):  # read operation
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount > 0:
            return make_response({"message": "USER DELETED SUCCESSFULLY"}, 200)
        else:
            return make_response({"message": "NOTHING TO DELETE"}, 204)

    def user_pagination_model(self, limit, page):

        pass

    def user_patch_model(self, form, id):

        pass


    def patch_user_model(self, data):
        qry = "UPDATE users SET "
        for key in data:
            if key != 'id':
                qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id = {data['id']}"
        self.cur.execute(qry)
        if self.cur.rowcount > 0:
            return make_response({"message": "UPDATED_SUCCESSFULLY"}, 201)
        else:
            return make_response({"message": "NOTHING_TO_UPDATE"}, 204)

    def user_pagination_model(self, limit, page):
        page = int(page)
        limit = int(limit)
        start = (page * limit) - limit
        qry = f"SELECT * FROM users LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        if len(result) > 0:
            res = make_response({"payload": result, "page_no": page, "per_page": limit, "this_page": len(result), },200)
            return res
        else:
            return make_response({"message": "No Data Found"}, 204)
