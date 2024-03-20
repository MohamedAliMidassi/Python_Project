from flask_app import app
from flask import render_template,session,redirect,request,flash
from flask_app.models.admins import Admin
from flask_app.models.users import User


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/showinfos')
def showallinfos1():
    if not 'user_id' in session:
        return redirect('/')
    all_coachs=Admin.show_all()
    return render_template('allinfos.html',all_coachs=all_coachs)


@app.route('/showclientinfos')
def showallinfos2():
    if not 'user_id' in session:
        return redirect('/')
    all_clients=Admin.show_all_clients()
    return render_template('allinfos.html',all_clients=all_clients)


@app.route('/delete/<int:id>')
def delete_show(id):
    if not 'user_id' in session:
        return redirect('/')
    Admin.delete({**request.form,'id':id})
    return redirect("/showinfos")


@app.route('/logout', methods=['post'])
def logout():
    session.clear()
    return redirect("/")


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