from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from User import *  # Assuming this imports functions related to user management
from transactions import *  # Assuming this imports functions related to transactions
import pymongo as pym



app = Flask(__name__)
client = pym.MongoClient("mongodb://localhost:27017")

# MongoDB database and collection setup here:
dp = client["flashcard_AI"]
flashcards = ["Flashcards"]
users = ["Users"]

# Route for registering a new account
@app.route("/register", methods=["POST"])
@cross_origin()
def register_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    # Register user (assuming register_user handles hashing/salting)
    success = register_User(username, password, email)

    if success:
        return jsonify({"message": "User registered successfully"})
    else:
        return jsonify({"error": "MemberID must be unique from other users"}), 400

# Route for user login
@app.route("/login", methods=["POST"])
@cross_origin()
def login_user():
    data = request.json
    password = data.get("password")
    username = data.get("username")
    
    # Authenticate user
    authorize = login(password, username)

    if authorize:
        user = users.find_one({ "username": username})
        return jsonify(
            {
                "message": "Login successful.",
                "username": user["username"],
            }
        )
    return jsonify({"message": "Incorrect username, member ID, or password."}), 401

# # Route for searching flashcards
# @app.route("/search_flashcard", methods=["GET"])
# @cross_origin()
# def search_flashcard():
#     #search user info

# # Route for fetching flashcard info
# @app.route('/flashcard', methods=['GET'])
# @cross_origin()
# def flashcard():
#     #fetch flashcard data



# Main entry point of the application
if __name__ == "__main__":
    # Enable CORS for all routes
    cors = CORS(app)
    # Run the Flask app on host 0.0.0.0 (accessible from any network interface)
    app.run(host='0.0.0.0')
