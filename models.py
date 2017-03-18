from app import db

class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    uname = db.Column(db.String(80), unique=True)
    gender = db.Column(db.String(60))
    age = db.Column(db.Integer)
    bio = db.Column(db.String(250))
    userid = db.Column(db.Integer)
    date = db.Column(db.String(255))
    

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)