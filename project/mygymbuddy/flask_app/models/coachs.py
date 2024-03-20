from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Coach:
    def __init__(self,data) :
        self.id=data["id"]
        self.certifcat=data["certifcat"]
        self.experience=data["experience"]
        self.sport_id=data["sport_id"]
        self.user_id=data["user_id"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]