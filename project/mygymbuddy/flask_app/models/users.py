from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self,data) :
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.role=data["role"]
        self.age=data["age"]
        self.phone=data["phone"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]



    @classmethod
    def get_by_email(cls,data):
        query="""SELECT * FROM users WHERE email=%(email)s"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def get_by_id(cls,data):
        query="""SELECT * FROM users WHERE id=%(id)s"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return None
    
    @classmethod
    def newuser(cls,data):
        query = """
                    insert into users (first_name,last_name,email,role,age,phone,password)
                    values(%(first_name)s,%(last_name)s,%(email)s,%(role)s,%(age)s,%(phone)s,%(password)s);
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    

    @classmethod
    def sendreport(cls,data):
        query = """
                    insert into message_the_admin (sender_id,reciver_id,title,comment)
                    values(%(sender_id)s,%(reciver_id)s,%(title)s,%(comment)s);
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    
    

    @staticmethod
    def validate_user(data):
        is_valid=True
        # first & lastname validation
        if len(data["first_name"])==0:
            is_valid=False
            flash("First Name field must be fild ","create")
        
        if len(data["last_name"])==0:
            is_valid=False
            flash("Last Name field must be fild ","create")


        # email validation
        # email pattern:regex
        if len(data["email"])==0:
            is_valid=False
            flash("email field must be fild ","create")

        if not EMAIL_REGEX.match(data['email']):
            flash("invalid email address","create")
            is_valid=False
        #email must be unique
        if User.get_by_email({'email':data['email']}):
            flash("Email already in use, hope by you","create")
            is_valid=False
        if len(data["phone"])!=8:
            flash("phone number too short","create")
            is_valid=False
        #password
        # password length
        if len(data["password"])<6:
            flash("Password too short","create")
            is_valid=False
        # compare password and confirm password
        elif data["password"]!=data["confirm_password"]:
            flash("Password must match","create")
            is_valid=False
        return is_valid


