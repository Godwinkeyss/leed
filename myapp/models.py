from myapp import db,app, login_manager
from flask_login import UserMixin


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(6), nullable=False)  # "Male", "Female", or "Other"
    age = db.Column(db.Integer, nullable=False)
    hypertension = db.Column(db.Integer, nullable=False)  # 0 or 1
    ever_married = db.Column(db.String(3), nullable=False)  # "No" or "Yes"
    work_type = db.Column(db.String(20), nullable=False)  # Various work types
    residence_type = db.Column(db.String(5), nullable=False)  # "Rural" or "Urban"
    avg_glucose_level = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    smoking_status = db.Column(db.String(20), nullable=False)  # Smoking status
    stroke = db.Column(db.Integer, nullable=False)  # 0 or 1
    
    
    
    def to_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name': self.middle_name,
            'phone_number': self.phone_number,
            'address': self.address,
            'gender': self.gender,
            'age': self.age,
            'hypertension': self.hypertension,
            'ever_married': self.ever_married,
            'work_type': self.work_type,
            'residence_type': self.residence_type,
            'avg_glucose_level': self.avg_glucose_level,
            'bmi': self.bmi,
            'smoking_status': self.smoking_status,
            'stroke': self.stroke
        }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    
    def __repr__(self):
        return f'<Register {self.first_name} {self.last_name} {self.email}>'









with app.app_context():
    db.create_all()