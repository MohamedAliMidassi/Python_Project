from flask_app import app
from flask import redirect, render_template, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.sports import Sport
from flask_app.models.users import User
from flask_app.models.admins import Admin
from flask_app.models.messages import Message
from flask_app.models.coachs import Coach
from flask_app.models.clients import Client

bcrypt = Bcrypt(app)





@app.route('/report/new', methods=['POST'])
def create_report():
    # Extracting sender_id from the form data
    sender_id = request.form['sender_id']  # Assuming sender_id is present in the form data
    
    if not Message.validate_message(request.form):
        return redirect('/report')
    
    # Pass the form data directly to the sendreport method
    Client.sendreport(request.form)
    
    return redirect('/userdashboard')





@app.route("/report/<int:id>")
def reporte(id):
    if not 'user_id' in session:
        return redirect('/')
    sender_id = id
    return render_template("report.html", sender_id=sender_id)



@app.route("/register")
def show():
    if not 'user_id' in session:
        return redirect('/')
    sports = Sport.get_all_sport()
    user_id = session['user_id']
    return render_template("all_sports.html" , all_sports = sports,user_id=user_id)


