import pymongo as pym
import bcrypt

client = pym.MongoClient("mongodb://localhost:27017")

# Selecting the database and collection
db = client["FlashCard_Ai"]
users = db["Users"]

def hash_function(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password

def register_User(username, password, email):
    if users.find_one({"username": username}):
        return False

    hashed_password = hash_function(password)

    user = {
        "username": username,
        "email": email,
        "password": hashed_password,
        "sets": [],
        "performances": []
    }

    result = users.insert_one(user)
    return result.acknowledged

def login(password, username):
    user = users.find_one({"username": username})

    if user:
        hashed_password = user["password"]
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
    return False
