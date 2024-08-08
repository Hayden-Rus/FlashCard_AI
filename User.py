import pymongo as pym

client = pym.MongoClient("mongodb://localhost:27017")

# Selecting the database and collection
db = client["FlashCard_Ai"]
users = db["Users"]

def add_User(username, email):
    user = {
        "username": username,
        "email": email,
    }

    
    result = users.insert_one(user)

    return result.inserted_id

