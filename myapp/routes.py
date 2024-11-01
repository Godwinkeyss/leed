from flask import render_template,request,jsonify,flash,url_for, redirect, request
from myapp import app,db,bcrypt
from .models import Patient,User
from .form import Addpatient, Register, Login,Editpatient 
from flask_login import login_user, logout_user, current_user, login_required

#TODO: ADD PATIENTS TO DATABASE

@app.route('/addpatient', methods=['GET', 'POST'])
@login_required
def add_patient():
    form = Addpatient()
    if form.validate_on_submit():
        first_name = form.data.get('first_name')
        last_name = form.data.get('last_name')
        middle_name = form.data.get('middle_name')
        phone_number = form.data.get('phone_number')
        address = form.data.get('address')
        gender = form.data.get('gender')
        age = form.data.get('age')
        hypertension = form.data.get('hypertension')
        ever_married = form.data.get('ever_married')
        work_type = form.data.get('work_type')
        residence_type = form.data.get('residence_type')
        avg_glucose_level = form.data.get('avg_glucose_level')
        bmi = form.data.get('bmi')
        smoking_status = form.data.get('smoking_status')
        stroke = form.data.get('stroke')
        patients = Patient(first_name=first_name, last_name=last_name, middle_name=middle_name, phone_number=phone_number, address=address, gender=gender, age=age, hypertension=hypertension, ever_married=ever_married, work_type=work_type, residence_type=residence_type, avg_glucose_level=avg_glucose_level,bmi=bmi,smoking_status=smoking_status,stroke=stroke )
        db.session.add(patients)
        db.session.commit()
        flash(f'Patients added successfully','success')
        return redirect(url_for('patient',))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in creating a user: {err_msg}', 'danger')
            print(f'There was an error in creating a user: {err_msg}')
            return redirect(url_for('add_patient'))
    return render_template('add_patient.html', form=form)
    
        
 #TODO: SERVE THE PATIENT TO FRONTEND   
@app.route("/patient", methods=["GET"])
@login_required
def patient():
        patients = Patient.query.all()
        return render_template('patient.html', patients=patients)
    
    
 #TODO: EDIT PATIENT DATA 
   
@app.route('/patient/<int:id>', methods=["POST", "GET"])
def patient_edit(id):
    # Retrieve patient from the database
    patient = Patient.query.get_or_404(id)
    form = Editpatient (obj=patient)  # Pre-fills form fields with patient data

    if form.validate_on_submit():  # Only triggers on POST with valid data
        # Update patient fields with form data
        form.populate_obj(patient)  # Assigns form data to patient fields directly
        db.session.commit()
        
        flash('Patient updated successfully', 'success')
        return redirect(url_for('patient', id=patient.id))
    elif form.errors:  # This triggers if POST fails validation
        flash('There was an error in updating the patient', 'danger')
        for err_msgs in form.errors.values():
            for err in err_msgs:
                flash(err, 'danger')

    # Render template with form, which includes any errors on failed POST
    return render_template('edit_patient.html', form=form)

 #TODO: DELETE PATIENT DATA   
@app.route('/patient/delete/<int:id>', methods=["POST"])
def delete(id):
    patient = Patient.query.get_or_404(id)
    try:
        db.session.delete(patient)
        db.session.commit()
        flash("Patient's details have been deleted successfully.", "success")
        return redirect(url_for('patient'))  # Redirect to a list of patients or homepage
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        flash("Something went wrong, please try again.", "error")
        return redirect(url_for('index'))  # Redirect to a safe page

 
 
 
 
@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Register()
    if form.validate_on_submit():
        first_name = form.data.get('first_name')
        last_name = form.data.get('last_name')
        email = form.data.get('email')
        password = form.data.get('password')
        confirm_password = form.data.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
            return redirect(url_for('register'))
        if User.query.filter_by(email = email).first():
            flash('Email already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(first_name=first_name, last_name=last_name, email=email,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. You can now login.','success')
        return redirect(url_for('login'))
        
    return render_template('register.html', form=form)
    
@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Login()
    if form.validate_on_submit():
        email = form.data.get('email')
        password = form.data.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember = form.remember.data)  
            flash('Login successful. You can now access your account.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)
    
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
    
 
 
 
    
@app.route("/")
def index():
    return render_template('index.html')   