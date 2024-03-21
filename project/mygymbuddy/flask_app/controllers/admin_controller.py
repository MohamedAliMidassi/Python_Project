from flask_app import app
from flask import render_template,session,redirect,request,flash
from flask_app.models.admins import Admin
from flask_app.models.users import User
from flask_app.models.sports import Sport




@app.route('/')
def home():
    return render_template('index.html')




@app.route('/showinfos')
def showallinfos1():
    if not 'user_id' in session:
        return redirect('/')
    all_coachs=Admin.show_all()
    all_clients=Admin.show_all_clients()
    all_sports=Admin.show_all_sports()
    all_messages=Admin.show_all_messages()
    return render_template('allinfos.html',all_coachs=all_coachs,all_clients=all_clients,all_sports=all_sports,all_messages=all_messages)




@app.route('/userdashboard')
def client():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('client.html')




@app.route('/coachdashboard')
def coach():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('coach.html')




@app.route('/coach/<int:id>')
def one_coach(id):
    if not 'user_id' in session:
        return redirect('/')
    this_coach=Admin.get_coach_infos({"id":id})
    return render_template('one_coach.html',this_coach=this_coach)



@app.route('/client/<int:id>')
def one_client(id):
    if not 'user_id' in session:
        return redirect('/')
    this_client=Admin.get_client_infos({"id":id})
    return render_template('one_client.html',this_client=this_client)



@app.route('/sport/<int:id>')
def one_sport(id):
    if not 'user_id' in session:
        return redirect('/')
    this_sport=Admin.get_sport_infos({"id":id})
    this_coach=Admin.get_coach_infos({"id":id})
    return render_template('one_sport.html',this_sport=this_sport,this_coach=this_coach)




@app.route('/coach/delete/<int:id>')
def delete_coach(id):
    if not 'user_id' in session:
        return redirect('/')
    Admin.delete_coach({'id':id})
    return redirect("/showinfos")




@app.route('/client/delete/<int:id>')
def delete_client(id):
    if not 'user_id' in session:
        return redirect('/')
    Admin.delete_client({'id':id})
    return redirect("/showinfos")



@app.route('/sport/delete/<int:id>')
def delete_sport(id):
    if not 'user_id' in session:
        return redirect('/')
    Admin.delete_sport({'id':id})
    return redirect("/showinfos")

@app.route('/message/delete/<int:id>')
def delete_message(id):
    if not 'user_id' in session:
        return redirect('/')
    Admin.delete_message({'id':id})
    return redirect("/showinfos")




@app.route('/sport/add')
def add_sport():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("newsport.html")


@app.route('/sports/new', methods=['POST'])
def create():
    if not Sport.validate(request.form):
        return redirect('/sport/add')
    Sport.newsport(request.form )
    return redirect('/showinfos')





@app.route('/coach/add')
def add_coach():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("newcoach.html")



@app.route('/login', methods=['post'])
def login():
    user_from_db=Admin.get_by_email({'email':request.form['email']})
    if not user_from_db:
        flash("Password or email is wrong please try again","login")
        return redirect('/')
    if user_from_db.role==1:
        session['user_id']=user_from_db.id
        session["first_name"]=user_from_db.first_name
        return redirect("/showinfos")
    if user_from_db.role==2:
        session['user_id']=user_from_db.id
        session["first_name"]=user_from_db.first_name
        return redirect("/coachdashboard")
    session['user_id']=user_from_db.id
    session["first_name"]=user_from_db.first_name
    return redirect("/userdashboard")


@app.route('/logout', methods=['post'])
def logout():
    session.clear()
    return redirect("/")