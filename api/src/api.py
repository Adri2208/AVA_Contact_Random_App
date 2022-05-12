from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests as rq

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/contact"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    number = db.Column(db.String(200))
    email = db.Column(db.String(200))
    
    def __init__(self, firstname, lastname, number, email):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.email = email
        
def populate_tables():
    url = 'https://randomuser.me/api/'
    r = rq.get(url).json()
    print(r)
    # for i in range(1,1000):
    #     firstname = fake.first_name()
    #     lastname = fake.last_name()
    #     number = fake.phone_number()
    #     email = fake.email()
    #     new_contact = Contact(firstname, lastname, number, email)
    #     db.session.add(new_contact)
    # db.session.commit()
        
if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    populate_tables()
    app.run(host="0.0.0.0", port=8080, debug=True)