from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Message:
    def __init__(self,data) :
        self.sender_id=data["sender_id"]
        self.reciver_id=data["reciver_id"]
        self.comment=data["comment"]
        self.title=data["title"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]


    
    @staticmethod
    def validate_message(data):
        is_valid=True
        if len(data["comment"])==0:
            is_valid=False
            flash("comment field must be fild ","create")
        
        if len(data["title"])==0:
            is_valid=False
            flash("title field must be fild ","create")
        return is_valid 