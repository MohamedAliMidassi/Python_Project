from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import coachs
from flask_app.models import sports
from flask_app.models import users
from flask_app.models import messages
from flask_app.models import sessions

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

    @classmethod
    def newclient(cls, data):
        query = """
            INSERT INTO message_the_admin (weight, height, allergies, budget,injury,trained,user_id,coach_id)
            VALUES (%(weight)s, %(height)s, %(allergies)s, %(budget)s,%(injury)s,%(trained)s,%(user_id)s,%(coach_id)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result



    @classmethod
    def get_by_email(cls,data):
        query="""SELECT * FROM users WHERE email=%(email)s"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return users.User(result[0])
        return False
    
    @classmethod
    def get_by_id(cls,data):
        query="""SELECT * FROM users WHERE id=%(id)s"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return users.User(result[0])
        return None

    

    @classmethod
    def sendreport(cls, data):
        query = """
            INSERT INTO message_the_admin (sender_id, reciver_id, title, comment)
            VALUES (%(sender_id)s, %(reciver_id)s, %(title)s, %(comment)s);
        """
        sender_id = data["sender_id"]
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result


    @classmethod
    def show_message(cls, user_id):
        query = """
            SELECT * FROM message_the_admin
            WHERE sender_id = %(id)s;
        """
        # Extract the sender_id from the user_id dictionary directly
        sender_id = user_id['id']
        # Provide the correct sender_id to the query
        result = connectToMySQL(DATABASE).query_db(query, {"id": sender_id})
        all_messages = []

        for row in result:
            this_message = messages.Message(row)
            all_messages.append(this_message)

        return all_messages


