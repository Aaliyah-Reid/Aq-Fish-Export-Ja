"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import flash, render_template, request, redirect, url_for
from app.forms import addFishForm
from app.models import Fish
from werkzeug.utils import secure_filename

##
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/admin/fishes/update', methods=['POST', 'GET'])
def addFish():
    form = addFishForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            breed = form.breed.data
            description = form.description.data
            photo = form.breed.data

            filename = secure_filename(photo.filename)

            newFish = Fish(name,breed, description, filename)
            
            db.session.add(newFish)
            db.session.commit()
            photo.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename ))

            flash('Added Fish', 'success')
            return redirect(url_for('fishes'))
        else:
            print(form.errors)

    return render_template('add_fish.html', form=form)

            


@app.route('/fishes')
def viewFishes():
    pass

# @app.route('/properties/<fishid>')

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


if __name__ == "__main__":
    app.run(debug=True)