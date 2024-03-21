from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Message:
    def __init__(self,data) :
        self.sender_id=data["sender_id"]
        self.reciver_id=data["reciver_id"]
        self.comment=data["comment"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]