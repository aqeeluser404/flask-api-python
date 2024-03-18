# CRUD endpoints

# API creation 
# Domain is the localhost:5000 or google.com
# The endpoint is whats after the domain

# send a request to the backend
# Request
# type: DELETE/POST/PUT
# can send json json: {}

# backend returns a response 
# Response 
# Properties:
# status: 200 success, 404 not found
# can also return json 

from flask import request, jsonify
from config import app, db
from models import Contact

# Get
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()      # GETS all the contacts
    json_contacts = list(lambda x: x.to_json(), contacts)        # calling the method json to add the contacts to a new json list
    return jsonify({"contacts": json_contacts})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()     # creates the database and modals if it doesnt exist
    
    app.run(debug=True)