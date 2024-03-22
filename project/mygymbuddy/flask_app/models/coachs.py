from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import users

class Coach:
    def __init__(self,data) :
        self.id=data["id"]
        self.certifcat=data["certifcat"]
        self.experience=data["experience"]
        self.sport_id=data["sport_id"]
        self.user_id=data["user_id"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.details=users.User.get_by_id({'id':self.user_id})



    
    @classmethod
    def newcoach(cls,data):
        query = """
                    insert into coachs (certifcat,experience,sport_id,user_id)
                    values(%(certifcat)s,%(experience)s,%(sport_id)s,%(user_id)s);
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    

    @staticmethod
    def validate_coach(data):
        is_valid=True
        if len(data["certifcat"])==0:
            is_valid=False
            flash("certifcat field must be fild ","create")
        
        if len(data["experience"])==0:
            is_valid=False
            flash("experience field must be fild ","create")
        return is_valid
