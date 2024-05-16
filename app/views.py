"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
from mailbox import Message
import os
from app import app, db, login_manager
from flask import flash, render_template, request, redirect, url_for,flash, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from flask import jsonify
from app.forms import AddFishForm, LoginForm, ContactForm
from app.models import Fish, UserProfile
from app import mail
##
# Routing for your application.
###

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/admin/upload', methods=['POST', 'GET'])
@login_required
def addFish():
    form = AddFishForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            breed = form.breed.data
            description = form.description.data
            availability = form.availability.data
            print(availability)
            photo = form.photo.data

            filename = secure_filename(photo.filename)

            newFish = Fish(name,breed, description,availability, filename)
            print(newFish)
            
            db.session.add(newFish)
            db.session.commit()
            photo.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename ))

            flash('Added Fish', 'success')
            return redirect(url_for('fishes'))
        else:
            print(form.errors)

    return render_template('add_fish.html', form=form)


@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html')


@app.route('/fishes')
def fishes():
    fishes = Fish.query.all()
    return render_template('fishes.html', fishes=fishes)

@app.route('/fishes/<fishid>')
def view_fish(fishid):
    fish = Fish.query.filter_by(id=fishid).first()
    return render_template('view_fish.html', fish=fish)

@app.route('/get_fishes')
def get_fishes():
    fishes = Fish.query.all()
    fish_data = []
    for fish in fishes:
        fish_info = {
            'id': fish.id,
            'name': fish.name,
            'breed': fish.breed,
            'description': fish.description,
            'availability': fish.availability,
            'photo_filename': fish.photo_filename
        }
        fish_data.append(fish_info)
    return jsonify(fish_data)

@app.route("/uploads/<filename>")
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)



@app.route('/contact', methods=['GET', 'POST'])  # Ensure methods are defined for GET and POST requests
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        fish = form.fish.data
        message = form.message.data
        subscribe = form.subscribe.data

    
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage: {message}\n\n"
        if fish:  
            full_message += f"Fish Interested In: {fish}\n"
        if subscribe:  
            full_message += "The user has subscribed to new stock notifications."

        msg = Message(
            subject,
            sender=(name, email),
            recipients=["aaliyahreid12345@gmail.com"]
        )
        msg.body = full_message
        mail.send(msg)
        flash('You have successfully filled out the form', 'success')
        return redirect(url_for('home'))  
    
    flash_errors(form) 

    return render_template('contact.html', form=form)  


# @app.route('/fishes/<fishid>')

@app.route('/admin/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Query for the user based on username
        user = db.session.execute(db.select(UserProfile).filter_by(username=username)).scalar()

        # and check_password_hash(user.password, password):
        # Verify user and password
        if user:
            if user.is_admin:  # Check if user has admin privileges
                login_user(user)
                flash('Logged in successfully as admin!', 'success')
                return redirect(url_for("admin_dashboard"))  # Make sure this is the correct endpoint
            else:
                flash('Access denied. Admin privileges required.', 'danger')
        else:
            flash('Username or Password is incorrect.', 'danger')

    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(UserProfile).filter_by(id=id)).scalar()


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


# if __name__ == "__main__":
#     app.run(debug=True)