from flask import Blueprint, render_template, request, session, redirect, url_for
from database import db
from tables import VolunteerTable, ActivityTable, FeedbackTable

volunteer_module = Blueprint("volunteer_module", __name__)


# Home Page
@volunteer_module.route('/', methods=['GET', 'POST'])
def home():
    if not auth():
        return redirect(url_for('volunteer_module.login'))
    activities = ActivityTable.query.filter_by(isapproved=True).all()
    return render_template('volunteer/home.html', activities=activities)


# Add Activity
@volunteer_module.route('/add-activity', methods=['GET', 'POST'])
def activity():
    if not auth():
        return redirect(url_for('volunteer_module.login'))
    if request.method == "POST":

        # Get Form Data
        name = request.form.get('name')
        description = request.form.get('description')
        date = request.form.get('date')

        # Insert to Database
        event = ActivityTable(name=name, description=description, date=date)
        db.session.add(event)
        db.session.commit()
        msg = "Activity/Event Successfully Added !"
        return render_template('volunteer/add-activity.html', msg=msg)
    return render_template('volunteer/add-activity.html')


# Registration
@volunteer_module.route('/register', methods=['GET', 'POST'])
def register():
    if auth():
        return redirect(url_for('volunteer_module.home'))
    if request.method == "POST":
        # Get Form Data
        name = request.form.get('name')
        phoneno = request.form.get('phoneno')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if User Already Exist
        vol = VolunteerTable.query.filter_by(email=email, phoneno=phoneno).first()
        db.session.commit()

        if vol is None:
            # Insert to Database
            volunteer = VolunteerTable(name=name, phoneno=phoneno, email=email, password=password)
            db.session.add(volunteer)
            db.session.commit()
            return redirect(url_for('volunteer_module.login'))
        else:
            msg = 'Phone Number/Email already exist !'
            return render_template('volunteer/register.html', msg=msg)
    return render_template('volunteer/register.html')


# Login
@volunteer_module.route('/login', methods=['GET', 'POST'])
def login():
    if auth():
        return redirect(url_for('volunteer_module.home'))
    if request.method == "POST":

        # Get Form Data
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if User Already Exist
        volunteer = VolunteerTable.query.filter_by(email=email, password=password).first()
        db.session.commit()

        if volunteer is None:
            msg = 'Invalid Email/Password'
            return render_template('volunteer/login.html', msg=msg)
        else:
            session['volunteerID'] = volunteer.id
            return redirect(url_for('volunteer_module.home'))
    return render_template('volunteer/login.html')


# Profile
@volunteer_module.route('/profile', methods=['GET', 'POST'])
def profile():
    if not auth():
        return redirect(url_for('volunteer_module.login'))
    volunteerID = session['volunteerID']
    profileData = VolunteerTable.query.filter_by(id=volunteerID).first()
    db.session.commit()
    return render_template('volunteer/profile.html', profileData=profileData)


# Profile
@volunteer_module.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if not auth():
        return redirect(url_for('volunteer_module.login'))

    if request.method == "POST":
        # Get Form Data
        name = request.form.get('name')
        description = request.form.get('description')
        star = request.form.get('star')

        # Insert to Database
        feedback = FeedbackTable(name=name, description=description, star=star)
        db.session.add(feedback)
        db.session.commit()
        msg = "Feedback Sent !"
        return render_template('volunteer/feedback.html', msg=msg)
    return render_template('volunteer/feedback.html')


# Logout
@volunteer_module.route('/logout', methods=['GET', 'POST'])
def logout():
    if not auth():
        return redirect(url_for('volunteer_module.login'))
    session['volunteerID'] = None
    return redirect(url_for('volunteer_module.login'))


# Check If User Not Logged In
def auth():
    if 'volunteerID' not in session:
        session['volunteerID'] = None
    if session['volunteerID'] is None:
        return False
    else:
        return True
