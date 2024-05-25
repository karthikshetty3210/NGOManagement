from database import db


# User Table
class VolunteerTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phoneno = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Volunteer %r>' % self.name


# User Table
class DonarTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phoneno = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Donar %r>' % self.name



# Complaint Table
# class ComplaintTable(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     uid = db.Column(db.Integer)
#     pname = db.Column(db.String(50))
#     phoneno = db.Column(db.String(100), nullable=False)
#     address = db.Column(db.String(200), nullable=False)
#     branchID = db.Column(db.Integer)
#     branchName = db.Column(db.String(300))
#     techID = db.Column(db.Integer, default=None)
#     createdAt = db.Column(db.String(200))
#     isOpen = db.Column(db.Integer, default=0)


# Admin Table
class AdminTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Admin %r>' % self.name


# Branch Table
# class BranchTable(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     code = db.Column(db.String(50), unique=True, nullable=False)
#     address = db.Column(db.String(200), nullable=False)
#     phoneno = db.Column(db.String(50), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(50), nullable=False)
#
#     def __repr__(self):
#         return '<Branch %r>' % self.name
