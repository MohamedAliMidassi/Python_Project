from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import coachs
from flask_app.models import clients
from flask_app.models import sports
from flask_app.models import users
from flask_app.models import messages

class Session:
    def __init__(self,data) :
        self.id=data["id"]
        self.location=data["location"]
        self.coach_id=data["coach_id"]
        self.client_id=data["client_id"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
