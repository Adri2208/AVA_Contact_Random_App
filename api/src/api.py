from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import requests as rq

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/contact"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/contacts")
def users():
        result = Contact.query.all()
        contacts= []
        for row in result:
            conatct = {
                "id": row.id,
                "firstname": row.firstname,
                "lastname": row.lastname,
                "number": row.number,
                "email" : row.email,
                "picture": row.picture,
                }
            contacts.append(conatct)
        return (jsonify(contacts))
    
@app.route("/contacts/<id>")
def users_by_contact(id):
    result = Contact.query.filter_by(id=id).first_or_404()
    contacts= []
    conatct = {
        "id": result.id,
        "firstname": result.firstname,
        "lastname": result.lastname,
        "number": result.number,
        "email" : result.email,
        "picture": result.picture,
        }
    contacts.append(conatct)
    return (jsonify(contacts))
    # return(conatct)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    number = db.Column(db.String(200))
    email = db.Column(db.String(200))
    picture = db.Column(db.String(200))
    
    def __init__(self, firstname, lastname, number, email, picture):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.email = email
        self.picture = picture
        
def populate_tables():
    url = 'https://randomuser.me/api/'
    r = rq.get(url).json()
    for i in range(1,50):
        url = 'https://randomuser.me/api/'
        r = rq.get(url).json()
        firstname = r['results'][0]['name']['first']
        lastname = r['results'][0]['name']['last']
        number = r['results'][0]['phone']
        email = r['results'][0]['email']
        picture = r['results'][0]['picture']['medium']
        new_contact = Contact(firstname, lastname, number, email, picture)
        db.session.add(new_contact)
    db.session.commit()
        
if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()
    # populate_tables()
    app.run(host="0.0.0.0", port=8080, debug=True)