from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import clients
from flask_app.models import sports
from flask_app.models import users
from flask_app.models import messages
from flask_app.models import sessions

class Coach:
    def __init__(self,data) :
        self.id=data["id"]
        self.certifcat=data["certifcat"]
        self.experience=data["experience"]
        self.sport_id=data["sport_id"]
        self.user_id=data["user_id"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.details=clients.Client.get_by_id({'id':self.user_id})



    @classmethod
    def show_all_clients_of_coach(cls):
        query = """
        SELECT * FROM clients
        left join coachs on clients.coach_id=coachs.id
        where coach_id=%(id)s;
        """
        result=connectToMySQL(DATABASE).query_db(query)
        all_clients=[]
        for each_coach in result:
            coach_dict={**each_coach,
                        "id":each_coach["coachs.id"],
                        "created_at":each_coach["coachs.created_at"],
                        "updated_at":each_coach["coachs.updated_at"]
                        }
            this_client=clients.Client(each_coach)
            this_client.infos=cls(coach_dict)
            all_clients.append(this_client)
        return all_clients
    
        
    @classmethod
    def newcoach(cls,data):
        query = """
                    insert into coachs (certifcat,experience,sport_id,user_id)
                    values(%(certifcat)s,%(experience)s,%(sport_id)s,%(user_id)s);
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
        
    @classmethod
    def show_all_Sessions(cls):
        query = """
            SELECT * FROM sessiions
            left join coachs on sessiions.coach_id=coachs.id;
        """
        result=connectToMySQL(DATABASE).query_db(query)
        all_sessions=[]
        for each_user in result:
            user_dict={**each_user,
                        "created_at":each_user["users.created_at"],
                        "updated_at":each_user["users.updated_at"]
                        }
            this_session=sessions.Session(each_user)
            this_session.infos=users.User(user_dict)
            all_sessions.append(this_session)
        return all_sessions
    
    
    
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
