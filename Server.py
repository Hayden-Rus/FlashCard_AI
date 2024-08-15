from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from User import *  # Assuming this imports functions related to user management
from Flashcard import *  # Assuming this imports functions related to transactions
from Flashcard_Sets import *
import pymongo as pym

app = Flask(__name__)
client = pym.MongoClient("mongodb://localhost:27017")

# MongoDB database and collection setup here:
db = client["FlashCard_Ai"]
flashcards = db["Flashcards"]
users = db["Users"]

# Route for registering a new account
@app.route("/register", methods=["POST"])
@cross_origin()
def register_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    success = register_User(username, password, email)

    if success:
        return jsonify({"message": "User registered successfully"})
    else:
        return jsonify({"error": "Username must be unique from other users"}), 400


# Route for user login
@app.route("/login", methods=["POST"])
@cross_origin()
def login_user():
    data = request.json
    password = data.get("password")
    username = data.get("username")
    
    authorize = login(password, username)

    if authorize:
        user = users.find_one({"username": username})
        return jsonify(
            {
                "message": "Login successful.",
                "username": user["username"],
            }
        )
    return jsonify({"message": "Incorrect username or password."}), 401



# Route for adding a new flashcard
@app.route("/add_flashcard", methods=["POST"])
@cross_origin()
def add_flashcard():
    data = request.json
    question = data.get("question")
    answer = data.get("answer")
    category = data.get("category")

    flashcard_id = add_Flashcard(question, answer, category)
    return jsonify({"message": "Flashcard added successfully", "flashcard_id": str(flashcard_id)})

# Route for updating a flashcard
@app.route("/update_flashcard/<id_>", methods=["PUT"])
@cross_origin()
def update_flashcard(id_):
    data = request.json
    question = data.get("question")
    answer = data.get("answer")
    category = data.get("category")

    success = update_Flashcard(id_, question, answer, category)
    if success:
        return jsonify({"message": "Flashcard updated successfully"})
    else:
        return jsonify({"error": "Flashcard not found or not updated"}), 404

# Route for creating a new flashcard set
@app.route("/create_set", methods=["POST"])
@cross_origin()
def create_flashcard_set():
    data = request.json
    username = data.get("username")
    set_name = data.get("set_name")

    if not username or not set_name:
        return jsonify({"error": "Username and set name are required"}), 400

    success = create_set(username, set_name)
    if success:
        return jsonify({"message": "Flashcard set created successfully"})
    else:
        return jsonify({"error": "User not found or set creation failed"}), 404


# Main entry point of the application
if __name__ == "__main__":
    # Enable CORS for all routes
    cors = CORS(app)
    # Run the Flask app on host 0.0.0.0 (accessible from any network interface)
    app.run(host='0.0.0.0')
