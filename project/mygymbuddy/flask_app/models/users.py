from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

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


