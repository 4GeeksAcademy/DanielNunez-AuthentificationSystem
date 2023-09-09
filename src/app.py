# from flask import Flask, request, jsonify
# from datetime import timedelta, datetime, timezone
# from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
# from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt

# from api.models import db, User

# app = Flask(__name__)

# migrate = Migrate(app, db)

# app.config['SECRET_KEY'] = 'super-secret'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'


# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
# jwt = JWTManager(app)

# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = True

# bcrypt = Bcrypt(app)
# db.init_app(app)

# with app.app_context():
#     db.create_all()

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/logintoken', methods=['POST'])
# def create_token():
#     email = request.json.get("email", None)
#     password = request.json.get("password", None)


#     user = User.query.filter_by(email=email).first()

#     if user is None:
#         return {"msg": "User not found"}, 401
    
#     if not Bcrypt().check_password_hash(user.password, password):
#         return jsonify({"error": "Unauthorized"}), 401
    
    
#     access_token = create_access_token(identity=email)
#     response = {"access_token": access_token}
    
#     return jsonify({
#         "email": email,
#         "access_token": access_token
#     }), 200

# @app.route('/signup', methods=['POST'])
# def signup():
#     name = request.json["name"]
#     email = request.json["email"]
#     password = request.json["password"]

#     user_exists = User.query.filter_by(email=email).first() is not None

#     if user_exists:
#         return jsonify({"error": "User already exists"}), 409
    
#     hashed_password = Bcrypt().generate_password_hash(password)
#     new_user = User(name=name, email=email, password=hashed_password)
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({
#         "id": new_user.id,
#         "email": new_user.email
#     }), 201

# @app.after_request
# def refresh_expiring_jwts(response):
#     try:
#         exp_timestamp = get_jwt()["exp"]
#         now = datetime.now(timezone.utc)
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
#         if target_timestamp > exp_timestamp:
#             access_token = create_access_token(identity=get_jwt_identity())
#             data = response.get_json()
#             if type(data) is not dict:
#                 data["access_token"] = access_token
#                 response.data = json.dumps(data)
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original respone
#         return response
    
# @app.route('/logout', methods=['POST'])
# def logout():
#     response = jsonify({"msg": "logout successful"})
#     unset_jwt_cookies(response)
#     return response, 200

# @app.route('/profile/<getemail>')
# @jwt_required()
# def my_profile(getemail):
#     print(getemail)
#     if not getemail:
#         return jsonify({"error": "Unauthorized"}), 401
#     user = User.query.filter_by(email=getemail).first()

#     response_body = {
#         "id": user.id,
#         "name": user.name,
#         "email": user.email
#     }
#     return response_body, 200