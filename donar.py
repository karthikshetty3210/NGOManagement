from random import randint

from flask import Blueprint, render_template, request, session, redirect, url_for, json
from database import db
from tables import DonarTable, ActivityTable, FeedbackTable, DonationTable
import razorpay

# client = razorpay.Client(auth=("rzp_test_gZxcQbxIJBtsb1", "BSWzEo8vEYRkaOrWDgUGyRgh"))
donar_module = Blueprint("donar_module", __name__)


KEY_ID = "rzp_test_gZxcQbxIJBtsb1"
KEY_SECRET = "BSWzEo8vEYRkaOrWDgUGyRgh"
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))


def generateInvoice(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# Home Page
@donar_module.route('/', methods=['GET', 'POST'])
def home():
    if not auth():
        return redirect(url_for('donar_module.login'))
    activities = ActivityTable.query.filter_by(isapproved=True).all()
    return render_template('donar/home.html', activities=activities)


# Donate
@donar_module.route('/donate', methods=['GET', 'POST'])
def donate():
    if not auth():
        return redirect(url_for('donar_module.login'))
    if request.method == "POST":

        # Get Form Data
        amount = request.form.get('amount')
        note = request.form.get('note')

        # donarID = session['donarID']
        # profileData = DonarTable.query.filter_by(id=donarID).first()
        # print(profileData)
        # db.session.commit()


        # dname = profileData['name']
        data = {
            "amount": int(amount)*100,
            "currency": "INR",
            "receipt": str(generateInvoice(10)),
            "notes": {
                "note":note
            }
        }

        # payment = {"Ok":""}
        payment = client.order.create(data=data)

        print(payment)

        # Insert to Database
        # donation = DonationTable(amount=amount,note=note)
        # db.session.add(donation)
        # db.session.commit()
        # msg = "Thanks for donation !"
        donarID = session['donarID']
        profileData = DonarTable.query.filter_by(id=donarID).first()
        db.session.commit()
        return render_template('donar/make-payment.html', res=payment, profile=profileData)
    return render_template('donar/donate.html')



@donar_module.route('/success', methods=['POST'])
def success():
    # Insert to Database
    amount = request.form.get('amount')
    tamount = int(amount)/100
    note = request.form.get('note')
    donation = DonationTable(amount=int(tamount),note=note)
    db.session.add(donation)
    db.session.commit()
    msg = "Thanks for donation !"
    return render_template('donar/success.html',msg=msg)


# Add Activity
@donar_module.route('/add-activity', methods=['GET', 'POST'])
def activity():
    if not auth():
        return redirect(url_for('donar_module.login'))
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
        return render_template('donar/add-activity.html', msg=msg)
    return render_template('donar/add-activity.html')



# Registration
@donar_module.route('/register', methods=['GET', 'POST'])
def register():
    if auth():
        return redirect(url_for('donar_module.home'))
    if request.method == "POST":
        # Get Form Data
        name = request.form.get('name')
        phoneno = request.form.get('phoneno')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if User Already Exist
        don = DonarTable.query.filter_by(email=email, phoneno=phoneno).first()
        db.session.commit()

        if don is None:
            # Insert to Database
            donar = DonarTable(name=name, phoneno=phoneno, email=email, password=password)
            db.session.add(donar)
            db.session.commit()
            return redirect(url_for('donar_module.login'))
        else:
            msg = 'Phone Number/Email already exist !'
            return render_template('donar/register.html', msg=msg)
    return render_template('donar/register.html')


# Login
@donar_module.route('/login', methods=['GET', 'POST'])
def login():
    if auth():
        return redirect(url_for('donar_module.home'))
    if request.method == "POST":

        # Get Form Data
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if User Already Exist
        donar = DonarTable.query.filter_by(email=email, password=password).first()
        db.session.commit()

        if donar is None:
            msg = 'Invalid Email/Password'
            return render_template('donar/login.html', msg=msg)
        else:
            session['donarID'] = donar.id
            return redirect(url_for('donar_module.home'))
    return render_template('donar/login.html')


# Profile
@donar_module.route('/profile', methods=['GET', 'POST'])
def profile():
    if not auth():
        return redirect(url_for('donar_module.login'))
    donarID = session['donarID']
    profileData = DonarTable.query.filter_by(id=donarID).first()
    db.session.commit()
    return render_template('donar/profile.html', profileData=profileData)


# Profile
@donar_module.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if not auth():
        return redirect(url_for('donar_module.login'))

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
        return render_template('donar/feedback.html', msg=msg)
    return render_template('donar/feedback.html')


# Logout
@donar_module.route('/logout', methods=['GET', 'POST'])
def logout():
    if not auth():
        return redirect(url_for('donar_module.login'))
    session['donarID'] = None
    return redirect(url_for('donar_module.login'))


# Check If User Not Logged In
def auth():
    if 'donarID' not in session:
        session['donarID'] = None
    if session['donarID'] is None:
        return False
    else:
        return True
