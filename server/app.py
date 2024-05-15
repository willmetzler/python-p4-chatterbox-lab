from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    
    if request.method == 'GET':
        messages = [message.to_dict() for message in Message.query.all()]
        response = make_response(
            messages,
            200
        )

        return response

    elif request.method == 'POST':
        new_message = Message(
            body=request.json.get("body"),
            username=request.json.get("username"),
            created_at=request.json.get("created_at"),
            updated_at=request.json.get("updated_at")
        )

        db.session.add(new_message)
        db.session.commit()

        message_dict = new_message.to_dict()

        response = make_response(
            message_dict,
            201
        )

        return response


@app.route('/messages/<int:id>', methods=['PATCH', 'DELETE'])
def messages_by_id(id):
    message= Message.query.filter(Message.id == id).first()
    if message is None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }
        response = make_response(response_body, 404)
        return response

    if request.method == 'PATCH':
        message.body = request.json.get('body')
        db.session.commit()
        response = make_response(message.to_dict(), 200)
        return response

    elif request.method == 'DELETE':
        db.session.delete(message)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "message deleted."
        }
        response = make_response(response_body, 200)
        return response

if __name__ == '__main__':
    app.run(port=5555)
