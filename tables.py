from database import db


# Volunteer Table
class VolunteerTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phoneno = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Volunteer %r>' % self.name


# Donar Table
class DonarTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phoneno = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Donar %r>' % self.name


# Admin Table
class AdminTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phoneno = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Admin %r>' % self.name


# Children Table
class ChildrenTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    adoptedby = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Children %r>' % self.name


# Activity Table
class ActivityTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    date = db.Column(db.String(150), nullable=True)
    isapproved = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return '<Activity %r>' % self.name


# Feedback Table
class FeedbackTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    star = db.Column(db.String(10), nullable=True)

    def __repr__(self):
        return '<Feedback %r>' % self.name


# Donation Table
class DonationTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(50), nullable=False)
    note = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return '<Donation %r>' % self.name
