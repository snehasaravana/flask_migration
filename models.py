from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
#  User model 
class User(db.Model):
    __tablename__ = 'userList'
 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.Text(30))
    phone=db.Column(db.String(10))
    city=db.Column(db.String(20))
    country=db.Column(db.String(20))
    dob=db.Column(db.Date)
 

    def __init__(self, name,email,phone,city,country,dob):
        self.name = name
        self.age = email
        self.phone=phone
        self.city=city
        self.country=country
        self.dob=dob
 
    def __repr__(self):
        return f"{self.name}:{self.email}:{self.phone}:{self.city}:{self.country}:{self.dob}"

