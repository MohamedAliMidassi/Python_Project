from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Client:
    def __init__(self,data) :
        self.id=data["id"]
        self.weight=data["weight"]
        self.height=data["height"]
        self.allergies=data["allergies"]
        self.budget=data["budget"]
        self.injury=data["injury"]
        self.trained=data["trained"]
        self.user_id=data["user_id"]
        self.coach_id=data["coach_id"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]