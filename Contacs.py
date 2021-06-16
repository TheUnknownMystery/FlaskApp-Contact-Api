from itertools import combinations_with_replacement
from flask import Flask, jsonify, request

print("...starting")

# creating a flask class with my module name....
app = Flask(__name__)

# Contact lit....

contact_list = [
    {
        'id': 1,
        'contact_num': '9477784145',
        'contact_users_name': 'Sanjay Sengupta',
        'contact-descrption': 'This is sanjay senguptas contact'
    },
    {
        'id': 2,
        'contact_num': '8902703162',
        'contact_users_name': 'Sharmishta',
        'contact-descrption': 'This is sharmishta sharmishtas contact'
    }
]


@app.route("/AddContacts", methods=["POST"])
def AddContact():
    if not request.json:
        return jsonify({
            'Welcome': "Welcome to this api!"
        }, 400)

    contact_item = {
        "id": contact_list[-1]['id']+1,
        "contact_num": request.json['contact_num'],
        "contact_users_name": request.json['contact_users_name'],
        "contact-descrption": request.json["contact-descrption"]
    }

    contact_list.append(contact_item)
    return jsonify({
        "status": "success",
        "message": "Task added successfully"
    })


@app.route("/getData")
def GetData():
    return jsonify({
        "data": contact_list
    })


if(__name__ == "__main__"):
    app.run(debug=True)
