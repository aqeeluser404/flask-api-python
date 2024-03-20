# API creation 
from flask import request, jsonify
from config import app, db
from models import Contact


# Get
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()      # GETS all the contacts

    # calling the method json to add the contacts to a new json list
    json_contacts = [contact.to_json() for contact in contacts]    
    return jsonify({"contacts": json_contacts})


# Create
@app.route("/create_contact", methhods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include first name, last name and email"}), 
            400,
        )
    # creating new entry to the data 
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201


# update
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated."}), 200


# delete
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200


# run backend
if __name__ == "__main__":
    with app.app_context():
        db.create_all()     # creates the database and modals if it doesnt exist
    
    app.run(debug=True)