from flask import Blueprint, render_template, request, session, redirect, url_for
from database import db
from tables import AdminTable, ActivityTable, FeedbackTable, DonationTable, ChildrenTable, VolunteerTable, DonarTable


admin_module = Blueprint("admin_module", __name__)


# Admin Dashboard
@admin_module.route('/', methods=['GET', 'POST'])
def home():
    if not auth():
        return redirect(url_for('admin_module.login'))
    childrens = ChildrenTable.query.all()
    volunteer = VolunteerTable.query.all()
    donars = DonarTable.query.all()
    activities = ActivityTable.query.all()
    donation = DonationTable.query.all()
    feedbacks = FeedbackTable.query.all()
    totalDonation = 0
    for d in donation:
        totalDonation += int(d.amount)
        print("Donation:" + str(d.amount))
    return render_template('admin/home.html', feedbacks=feedbacks,totalDonation=totalDonation, donation=donation, donars=donars,
                           activities=activities, childrens=childrens, volunteers=volunteer)


# All Volunteers
@admin_module.route('/volunteers', methods=['GET', 'POST'])
def volunteers():
    if not auth():
        return redirect(url_for('admin_module.login'))
    childrens = ChildrenTable.query.all()
    volunteer = VolunteerTable.query.all()
    donars = DonarTable.query.all()
    activities = ActivityTable.query.all()
    donation = DonationTable.query.all()
    totalDonation = 0
    for d in donation:
        totalDonation += int(d.amount)
    return render_template('admin/volunteers.html', totalDonation=totalDonation, donation=donation, donars=donars,
                           activities=activities, childrens=childrens, volunteers=volunteer)


# Delete Volunteer
@admin_module.route('/delete-volunteer/<int:id>', methods=['GET', 'POST'])
def deletevolunteer(id):
    VolunteerTable.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('admin_module.volunteers'))



# Add Children
@admin_module.route('/add-children', methods=['GET', 'POST'])
def addchild():
    if not auth():
        return redirect(url_for('admin_module.login'))
    if request.method == "POST":
        # Get Form Data
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        address = request.form.get('address')

        # Insert to Database
        children = ChildrenTable(name=name, age=age, gender=gender,address=address,adoptedby="None")
        db.session.add(children)
        db.session.commit()
        msg = "Successfully Added !"
        return render_template('admin/add-children.html', msg=msg)
    return render_template('admin/add-children.html')



# View All Childrtens
@admin_module.route('/childrens', methods=['GET', 'POST'])
def childrens():
    if not auth():
        return redirect(url_for('admin_module.login'))
    childrens = ChildrenTable.query.all()
    # volunteer = VolunteerTable.query.all()
    # donars = DonarTable.query.all()
    # activities = ActivityTable.query.all()
    # donation = DonationTable.query.all()
    # totalDonation = 0
    # for d in donation:
    #     totalDonation += int(d.amount)
    return render_template('admin/childrens.html', childrens=childrens)


# Delete Children
@admin_module.route('/delete-children/<int:id>', methods=['GET', 'POST'])
def deletechildren(id):
    ChildrenTable.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('admin_module.childrens'))


# Delete Children
@admin_module.route('/update-children/<int:id>', methods=['GET', 'POST'])
def updatechild(id):
    if not auth():
        return redirect(url_for('admin_module.login'))
    child = ChildrenTable.query.filter_by(id=id).first()
    if request.method == "POST":
        # Get Form Data
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        address = request.form.get('address')
        adoptedby = request.form.get('adoptedby')

        # Insert to Database
        child.name = name
        child.age = age
        child.gender = gender
        child.address = address
        child.adoptedby = adoptedby

        db.session.commit()
        msg = "Successfully Updated !"
        return render_template('admin/update-childrens.html', msg=msg, child=child)
    return render_template('admin/update-childrens.html', child=child)


# View All Activity
@admin_module.route('/activities', methods=['GET', 'POST'])
def activities():
    if not auth():
        return redirect(url_for('admin_module.login'))
    childrens = ChildrenTable.query.all()
    volunteer = VolunteerTable.query.all()
    donars = DonarTable.query.all()
    activities = ActivityTable.query.all()
    donation = DonationTable.query.all()
    totalDonation = 0
    for d in donation:
        totalDonation += int(d.amount)
    return render_template('admin/activities.html', totalDonation=totalDonation, donation=donation, donars=donars,
                           activities=activities, childrens=childrens, volunteers=volunteer)


# Delete Activity
@admin_module.route('/update-activity/<int:id>', methods=['GET', 'POST'])
def updateactivity(id):
    a = ActivityTable.query.filter_by(id=id).first()
    a.isapproved = True
    db.session.commit()
    return redirect(url_for('admin_module.activities'))



# Delete Activity
@admin_module.route('/delete-activity/<int:id>', methods=['GET', 'POST'])
def deleteactivity(id):
    ActivityTable.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('admin_module.activities'))


# View All Donations
@admin_module.route('/donations', methods=['GET', 'POST'])
def donations():
    if not auth():
        return redirect(url_for('admin_module.login'))
    childrens = ChildrenTable.query.all()
    volunteer = VolunteerTable.query.all()
    donars = DonarTable.query.all()
    activities = ActivityTable.query.all()
    donation = DonationTable.query.all()
    totalDonation = 0
    for d in donation:
        totalDonation += int(d.amount)
    return render_template('admin/donations.html', totalDonation=totalDonation, donations=donation, donars=donars,
                           activities=activities, childrens=childrens, volunteers=volunteer)


# Delete Donation
@admin_module.route('/delete-donation/<int:id>', methods=['GET', 'POST'])
def deletedonation(id):
    DonationTable.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('admin_module.donations'))



# View All Donars
@admin_module.route('/donars', methods=['GET', 'POST'])
def donars():
    if not auth():
        return redirect(url_for('admin_module.login'))
    childrens = ChildrenTable.query.all()
    volunteer = VolunteerTable.query.all()
    donars = DonarTable.query.all()
    activities = ActivityTable.query.all()
    donation = DonationTable.query.all()
    totalDonation = 0
    for d in donation:
        totalDonation += int(d.amount)
    return render_template('admin/donars.html', totalDonation=totalDonation, donation=donation, donars=donars,
                           activities=activities, childrens=childrens, volunteers=volunteer)


# Delete Donar
@admin_module.route('/delete-donar/<int:id>', methods=['GET', 'POST'])
def deletedonar(id):
    DonarTable.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('admin_module.donar'))


# Donate
@admin_module.route('/donate', methods=['GET', 'POST'])
def donate():
    if not auth():
        return redirect(url_for('admin_module.login'))
    if request.method == "POST":
        # Get Form Data
        amount = request.form.get('amount')
        note = request.form.get('note')

        # order_amount = int(amount)
        # order_currency = 'INR'
        # order_receipt = 'order_rcptid_11'
        # notes = note  # OPTIONAL
        #
        # res = client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)

        # Insert to Database
        donation = DonationTable(amount=amount, note=note)
        db.session.add(donation)
        db.session.commit()
        msg = "Thanks for donation !"
        return render_template('admin/donate.html', msg=msg)
    return render_template('admin/donate.html')


# Add Activity
@admin_module.route('/add-activity', methods=['GET', 'POST'])
def activity():
    if not auth():
        return redirect(url_for('admin_module.login'))
    if request.method == "POST":
        # Get Form Data
        name = request.form.get('name')
        description = request.form.get('description')
        date = request.form.get('date')

        # Insert to Database
        event = ActivityTable(name=name, description=description, date=date,isapproved=True)
        db.session.add(event)
        db.session.commit()
        msg = "Activity/Event Successfully Added !"
        return render_template('admin/add-activity.html', msg=msg)
    return render_template('admin/add-activity.html')


# Admin Registration
@admin_module.route('/register', methods=['GET', 'POST'])
def register():
    if auth():
        if request.method == "POST":
            # Get Form Data
            name = request.form.get('name')
            phoneno = request.form.get('phoneno')
            email = request.form.get('email')
            password = request.form.get('password')

            # Check if User Already Exist
            admn = AdminTable.query.filter_by(email=email, phoneno=phoneno).first()
            db.session.commit()

            if admn is None:
                # Insert to Database
                admin = AdminTable(name=name, phoneno=phoneno, email=email, password=password)
                db.session.add(admin)
                db.session.commit()
                msg = 'Successfully registerd'
                return render_template('admin/register.html', msg=msg)
            else:
                msg = 'Phone Number/Email already exist !'
                return render_template('admin/register.html', msg=msg)
        return render_template('admin/register.html')
    return redirect(url_for('admin_module.home'))


# Admin Login
@admin_module.route('/login', methods=['GET', 'POST'])
def login():
    if auth():
        return redirect(url_for('admin_module.home'))
    if request.method == "POST":

        # Get Form Data
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if User Already Exist
        admin = AdminTable.query.filter_by(email=email, password=password).first()
        db.session.commit()

        if admin is None:
            msg = 'Invalid Email/Password'
            return render_template('admin/login.html', msg=msg)
        else:
            session['adminID'] = admin.id
            return redirect(url_for('admin_module.home'))
    return render_template('admin/login.html')


# Adminh Profile
@admin_module.route('/profile', methods=['GET', 'POST'])
def profile():
    if not auth():
        return redirect(url_for('admin_module.login'))
    adminID = session['adminID']
    profileData = AdminTable.query.filter_by(id=adminID).first()
    db.session.commit()
    return render_template('admin/profile.html', profileData=profileData)


# Admin Feeddback
@admin_module.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if not auth():
        return redirect(url_for('admin_module.login'))

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
        return render_template('admin/feedback.html', msg=msg)
    return render_template('admin/feedback.html')


# Admin Logout
@admin_module.route('/logout', methods=['GET', 'POST'])
def logout():
    if not auth():
        return redirect(url_for('admin_module.login'))
    session['adminID'] = None
    return redirect(url_for('admin_module.login'))

# view feedback
@admin_module.route('/view-feedback', methods=['GET', 'POST'])
def viewfeedback():
    if not auth():
        return redirect(url_for('admin_module.login'))
    childrens = ChildrenTable.query.all()
    volunteer = VolunteerTable.query.all()
    donars = DonarTable.query.all()
    activities = ActivityTable.query.all()
    donation = DonationTable.query.all()
    feedbacks = FeedbackTable.query.all()
    totalDonation = 0
    for d in donation:
        totalDonation += int(d.amount)
    return render_template('admin/feedback.html',feedbacks=feedbacks, totalDonation=totalDonation, donation=donation, donars=donars,
                           activities=activities, childrens=childrens, volunteers=volunteer)








# Check If Admin Not Logged In
def auth():
    if 'adminID' not in session:
        session['adminID'] = None
    if session['adminID'] is None:
        return False
    else:
        return True
