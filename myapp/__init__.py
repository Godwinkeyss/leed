from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = "FHHGJGDKFNFNFNnsnbjdvjdjd74757"


db = SQLAlchemy(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)


from myapp import routes


