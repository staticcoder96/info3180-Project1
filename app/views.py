from app import app
from flask import render_template, request, redirect, url_for, flash
#from flask_login import login_user, logout_user, current_user, login_required
#from forms import Form
#from models import UserProfile

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('welcome.html')

@app.route('/profile')
def addProfile():
    """Render website's add profile page."""
    return render_template('form.html')
    
    
@app.route('/profiles')
def showProfiles():
    """Render website's show all profile page."""
    return render_template('all.html')


@app.route('/profile/<userid>')
def oneProfile(userid):
    """Render website's show individual profile page."""
    return render_template('one.html',id="userid")
    
    
    
    

# The functions below should be applicable to all Flask apps.

"""
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    #Send your static text file.
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    Custom 404 page.
    return render_template('404.html'), 404

"""
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
