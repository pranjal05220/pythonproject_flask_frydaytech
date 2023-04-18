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

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        print(result)
        # query execution code
        return "this is user_signup_model"
