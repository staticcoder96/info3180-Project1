


from app import app
from app import db
import time,os
from random import randint
from flask import render_template, request, redirect, url_for, flash,jsonify,make_response
from forms import Form
from models import Profiles
from werkzeug.utils import secure_filename

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('welcome.html')

@app.route('/profile',methods=["GET", "POST"])
def addProfile():
    """Render website's add profile page."""
    form = Form()
    
    if form.validate_on_submit() and request.method == "POST":
         file_folder =  app.config['UPLOAD_FOLDER']
         
         uname = form.user.data
         gender = form.gender.data
         fname = form.fname.data
         lname = form.lname.data
         age = form.age.data
         bio = form.bio.data
         date = form.date.data
         
         
         #get picture
         pic = request.files['image']
         image = secure_filename(pic.filename)
         pic.save(os.path.join(file_folder, image))
         
         #get id and date.
         userid = id()
         date= timeinfo()
         
         user = Profiles(userid=userid,fname=fname,lname=lname,uname=uname,gender=gender, age=age, bio=bio,date=date)
         db.session.add(user)
         db.session.commit()
         
         
         flash("Profile successfully Added")
         
         return redirect(url_for('showProfiles')) #they should be redirected to showProfiles route 
    return render_template('form.html',form=form)
    
    
    
@app.route('/profiles',methods=["GET","POST"])
def showProfiles():
    """Render website's show all profile page."""
    users = Profiles.query.all()
    
    ulist = [{"people": people.uname, "userid": people.userid} for people in users]
    
    if request.method == "GET":
        file_folder = app.comfig['UPLOAD_FOLDER']
        return render_template('all.html',users=users)
    
    elif request.method == "POST":
        res = make_response(jsonify({"users": ulist}))
        res.headers['Content-Type'] = 'application/json'
        return res


@app.route('/profile/<userid>', methods=["GET", "POST"])
def oneProfile(userid):
    userid = id()
    user = Profiles.query.filter_by(userid=userid).first()
    
    if request.method == "GET":
        file_folder = app.comfig['UPLOAD_FOLDER']
        return render_template('one.html',user=user)
        
    elif request.method == "POST":
        if user is not None:
            res = make_response(jsonify(userid=user.userid,uname=user.name,gender=user.gender,age=user.age,date=user.date))
            res.headers['Content-Type'] = 'application/json'
            return res


def timeinfo():
    #generate time
    return (time.strftime("%a, %d  %b ,%Y"))
    
def id():
    """generate id"""
    num = randint(100000000, 999999999)
    return num
    
    
    
    

# The functions below should be applicable to all Flask apps.


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    #Send your static text file.
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    
    """Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes."""
    
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
