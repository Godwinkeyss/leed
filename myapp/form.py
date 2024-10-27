from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, NumberRange, Length, Optional, Email, EqualTo

class Addpatient(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    middle_name = StringField('Middle Name', validators=[Optional(), Length(max=50)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    address = StringField('Address', validators=[DataRequired(), Length(max=100)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=120)])
    hypertension = SelectField('Hypertension', choices=[(1, 'Yes'), (0, 'No')], validators=[DataRequired()])
    ever_married = SelectField('Ever Married', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    work_type = StringField('Work Type', validators=[DataRequired(), Length(max=50)])
    residence_type = SelectField('Residence Type', choices=[('Urban', 'Urban'), ('Rural', 'Rural')], validators=[DataRequired()])
    avg_glucose_level = FloatField('Average Glucose Level', validators=[DataRequired(), NumberRange(min=0)])
    bmi = FloatField('BMI', validators=[DataRequired(), NumberRange(min=0)])
    smoking_status = SelectField('Smoking Status', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    stroke = SelectField('Stroke', choices=[(1, 'Yes'), (0, 'No')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class Editpatient(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    middle_name = StringField('Middle Name', validators=[Optional(), Length(max=50)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    address = StringField('Address', validators=[DataRequired(), Length(max=100)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=120)])
    hypertension = SelectField('Hypertension', choices=[(1, 'Yes'), (0, 'No')], validators=[DataRequired()])
    ever_married = SelectField('Ever Married', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    work_type = StringField('Work Type', validators=[DataRequired(), Length(max=50)])
    residence_type = SelectField('Residence Type', choices=[('Urban', 'Urban'), ('Rural', 'Rural')], validators=[DataRequired()])
    avg_glucose_level = FloatField('Average Glucose Level', validators=[DataRequired(), NumberRange(min=0)])
    bmi = FloatField('BMI', validators=[DataRequired(), NumberRange(min=0)])
    smoking_status = SelectField('Smoking Status', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    stroke = SelectField('Stroke', choices=[(1, 'Yes'), (0, 'No')], validators=[DataRequired()])
    submit = SubmitField('Submit')
    



class Register(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(),Email(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')
    
    
class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')