import pymongo as pym
import bcrypt

client = pym.MongoClient("mongodb://localhost:27017")

# Selecting the database and collection
db = client["FlashCard_Ai"]
users = db["Users"]

def hash_function(password):
    """
    Hashes the provided password using bcrypt.

    Args:
    - password (str): Plain text password to be hashed.

    Returns:
    - bytes: Hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password

def register_User(username, password, email):
    
    if users.find_one({"username": username}):
        return False

    # Hash the password before storing it
    hashed_password = hash_function(password)

    user = {
        "username": username,
        "email": email,
        "password":  hashed_password,
        "sets": [],
        "performances": []
    }

    result = users.insert_one(user)
    return result.inserted_id


register_User("hayden","213456ja","123@abc.com")

