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

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/loginform")
def loginform():
    return render_template("login.html")


@app.route("/user/add/<int:id>")
def clientsinfos(id):
    return render_template("newclient.html")

#! ACTION ROUTE
# === Register ===
@app.route("/register", methods=["POST"])
def process_register():

    # validate the form here ...
    if not User.validate_user(request.form):
        return redirect("/sign_up")
    # create the hash
    print("-------->", request.form["password"])
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print("=======>", pw_hash)
    # User.create(request.form)
    data = {**request.form, "password": pw_hash}
    # store the user id inside the session
    user_id = User.newuser(data)
    session["user_id"] = user_id
    return redirect(f'/user/add/{user_id}')





# * View Route
@app.route("/dashboard")
def dash():
    #! ROUTE GUARD
    if "user_id" not in session:
        return redirect("/")
    # grab the user id from session and put in a dictionary
    data = {"id": session["user_id"]}
    # grab the user by id from DB
    current_user = Client.get_by_id(data)
    print("===> current_user:", current_user)
    return render_template("dashboard.html", username=current_user.first_name)


