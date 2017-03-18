from app import db

class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Firstname = db.Column(db.String(80))
    Lastname = db.Column(db.String(80))
    Username = db.Column(db.String(80), unique=True)
    Gender = db.Column(db.String(60))
    Age = db.Column(db.Integer)
    Biography = db.Column(db.String(250))
    Userid = db.Column(db.Integer)
    Date = db.Column(db.String(255))
    

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)