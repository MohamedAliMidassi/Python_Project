from flask_app import app
from flask import redirect, render_template, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.sports import Sport
from flask_app.models.users import User
from flask_app.models.admins import Admin
from flask_app.models.messages import Message
from flask_app.models.coachs import Coach
from flask_app.models.clients import Client



@app.route("/request")
def requestes():
    if not 'user_id' in session:
        return redirect('/')
    return render_template ("request.html")


@app.route("/addoffer")
def offers():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("offer.html")

@app.route("/members")
def members():
    if not 'user_id' in session:
        return redirect('/')
    all_clients=Admin.show_all_clients()
    return render_template("members.html",all_clients=all_clients)


@app.route('/feddback/new', methods=['POST'])
def create_fedback():
    sender_id = request.form['sender_id']  
    if not Message.validate_message(request.form):
        return redirect('/feedback')
    Client.sendreport(request.form)
    return redirect('/dashboard')





@app.route("/feedback/<int:id>")
def feedback(id):
    if not 'user_id' in session:
        return redirect('/')
    sender_id = id
    return render_template("feedback.html", sender_id=sender_id)
