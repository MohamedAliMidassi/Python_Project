from flask_app import app
from flask import redirect, render_template, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.sports import Sport
from flask_app.models.users import User
from flask_app.models.admins import Admin
from flask_app.models.messages import Message
from flask_app.models.coachs import Coach


bcrypt = Bcrypt(app)



@app.route('/report/new', methods=['POST'])
def create_report():
    if not Message.validate_message(request.form):
        return redirect('/report')
    User.sendreport(request.form )
    return redirect('/userdashboard')


@app.route("/report")
def reporte():
    if not 'user_id' in session:
        return redirect('/')
    return render_template ("report.html")


@app.route("/register")
def show():
    if not 'user_id' in session:
        return redirect('/')
    sports = Sport.get_all_sport()
    return render_template("all_sports.html" , all_sports = sports)


@app.route("/coaches/<int:id>")
def show_coach(id):
    if not 'user_id' in session:
        return redirect('/')
    sport = Admin.get_sport_infos({"id":id})
    return render_template("all_coaches.html" , sport = sport)

