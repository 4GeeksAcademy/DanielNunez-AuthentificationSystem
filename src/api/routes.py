"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

# Flask jwt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# Flask Bcrypt
from flask_bcrypt import Bcrypt

app = Flask(__name__)

api = Blueprint('api', __name__)

# Flask Bcrypt
bcrypt = Bcrypt(app)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/register', methods=['POST'])
def create_user():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # encrypt password:
    pw_hash = bcrypt.generate_password_hash(password)
    # create new user
    new_user = User(email=email, password=pw_hash)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 200


@api.route("/login", methods=["POST"])
def login():
    password_from_database = 'contraseña'
    # Hash pasword, only for test, in the data base the password is encrypt:
    db_pw_hash = bcrypt.generate_password_hash(password_from_database)

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if email != "test" and bcrypt.check_password_hash(db_pw_hash, password):
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

@api.route("/private", methods=["POST"])
@jwt_required()
def private():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200