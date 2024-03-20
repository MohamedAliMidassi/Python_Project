from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import coachs
from flask_app.models import users


class Admin:
    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.role=data["role"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.infos=[]


        #* =========== READ ONE ===========
    @classmethod
    def get_by_id(cls,data):
        query="""SELECT * FROM users WHERE id=%(id)s"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return None
    @classmethod
    def get_by_email(cls,data):
        query="""SELECT * FROM users WHERE email=%(email)s"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return False
    


        #* =========== READ ALL ===========
    @classmethod
    def show_all(cls):
        query = """
        SELECT * FROM coachs
        left join users on coachs.user_id=users.id;
        """
        result=connectToMySQL(DATABASE).query_db(query)
        all_coachs=[]
        for each_user in result:
            user_dict={**each_user,
                        "id":each_user["users.id"],
                        "created_at":each_user["users.created_at"],
                        "updated_at":each_user["users.updated_at"]
                        }
            this_coach=coachs.Coach(each_user)
            this_coach.infos=users.User(user_dict)
            all_coachs.append(this_coach)
        return all_coachs
    


    
    @classmethod
    def delete(cls,data):
        query="""DELETE FROM coachs WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    