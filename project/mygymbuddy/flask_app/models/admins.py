from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import coachs
from flask_app.models import clients
from flask_app.models import sports
from flask_app.models import users
from flask_app.models import messages


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
    def show_all_clients(cls):
        query = """
        SELECT * FROM clients
        left join users on clients.user_id=users.id;
        """
        result=connectToMySQL(DATABASE).query_db(query)
        all_clients=[]
        for each_user in result:
            user_dict={**each_user,
                        "id":each_user["users.id"],
                        "created_at":each_user["users.created_at"],
                        "updated_at":each_user["users.updated_at"]
                        }
            this_client=clients.Client(each_user)
            this_client.infos=users.User(user_dict)
            all_clients.append(this_client)
        return all_clients
    
    
    
    @classmethod
    def show_all_messages(cls):
        query = """
            SELECT * FROM message_the_admin
            left join users on message_the_admin.sender_id=users.id;
        """
        result=connectToMySQL(DATABASE).query_db(query)
        all_messages=[]
        for each_user in result:
            user_dict={**each_user,
                        "created_at":each_user["users.created_at"],
                        "updated_at":each_user["users.updated_at"]
                        }
            this_message=messages.Message(each_user)
            this_message.infos=users.User(user_dict)
            all_messages.append(this_message)
        return all_messages
    
    
    @classmethod
    def show_all_sports(cls):
        query = "SELECT * FROM sports;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_sport = []
        if results :
            for row in results:
                show=sports.Sport(row)
                all_sport.append(show)
            return all_sport
        return []
    

    @classmethod
    def get_coach_infos(cls,data):
        query="""
                    SELECT * FROM coachs
                    left join users on coachs.user_id=users.id
                    where coachs.id=%(id)s; 
                """
        result=connectToMySQL(DATABASE).query_db(query,data)
        this_coach=coachs.Coach(result[0])

        for each_user in result:
            user_dict={**each_user,
                        "id":each_user["users.id"],
                        "created_at":each_user["users.created_at"],
                        "updated_at":each_user["users.updated_at"]
                        }
        this_coach.infos=users.User(user_dict)
        return this_coach
    



    @classmethod
    def get_client_infos(cls,data):
        query="""
                    SELECT * FROM clients
                    left join users on clients.user_id=users.id
                    where clients.id=%(id)s; 
                """
        result=connectToMySQL(DATABASE).query_db(query,data)
        this_client=clients.Client(result[0])

        for each_user in result:
            user_dict={**each_user,
                        "id":each_user["users.id"],
                        "created_at":each_user["users.created_at"],
                        "updated_at":each_user["users.updated_at"]
                        }
        this_client.infos=users.User(user_dict)
        return this_client
    


    @classmethod
    def get_sport_infos(cls,data):
        query="""
                    SELECT * FROM coachs
                    left join sports  on coachs.sport_id=sports.id
                    where sports.id=%(id)s; 
                """
        result=connectToMySQL(DATABASE).query_db(query,data)
        this_coach=coachs.Coach(result[0])

        for each_sport in result:
            sport_dict={**each_sport,
                        "id":each_sport["sports.id"],
                        "created_at":each_sport["sports.created_at"],
                        "updated_at":each_sport["sports.updated_at"]
                        }
        this_coach.infos=sports.Sport(sport_dict)
        return this_coach
    


    


    
    @classmethod
    def delete_coach(cls,data):
        query="""DELETE FROM coachs WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_client(cls,data):
        query="""DELETE FROM clients WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_sport(cls,data):
        query="""DELETE FROM sports WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_message(cls,data):
        query="""DELETE FROM messages WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    