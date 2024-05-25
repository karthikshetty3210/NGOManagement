from flask import Flask, render_template

from database import db

from admin import admin_module
from donar import donar_module
from volunteer import volunteer_module

app = Flask(__name__)
app.secret_key = 'SecreatKey'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/NGOManagement"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "NGOManagement"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.register_blueprint(admin_module, url_prefix='/admin')
app.register_blueprint(volunteer_module, url_prefix='/volunteer')
app.register_blueprint(donar_module, url_prefix='/donar')

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True,port=4000)
