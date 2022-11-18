from flask_app import app, bcrypt, render_template, request, redirect, session, flash
from flask_app.models.vet import Vet

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/register/vet", methods=['POST'])
def register():
    print(request.form)
    if not Vet.validate_vet(request.form):
        return redirect('/')
    data ={'email': request.form['email']}
    check_for_vet = Vet.get_by_email(data)
    if check_for_vet:
        flash('email already registered')
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "branch": request.form['branch'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    vet_id = Vet.save(data)
    session['vet_id'] = vet_id
    session['vet_name'] = f"{request.form['first_name']} {request.form['last_name']}"
    return redirect('/chat/home')

@app.route('/login', methods=['post'])
def login():
    data = {'email': request.form['email']}
    vet_in_db = Vet.get_by_email(data)
    if not vet_in_db:
        flash('invalid credentials')
        return redirect('/')
    if not bcrypt.check_password_hash(vet_in_db.password, request.form['password']):
        flash('invalid credentials')
        return redirect('/')
    session['vet_id'] = vet_in_db.id
    session['vet_name'] =f"{vet_in_db.first_name} {vet_in_db.last_name}" 
    return redirect('/chat/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')