import pymongo as pym
from User import *
client = pym.MongoClient("mongodb://localhost:27017")

# Selecting the database and collection
db = client["FlashCard_Ai"]
UserFlashcards = db["UserFlashcards"]

#create datetime objects for last_reviewed

def add_UserFlashcard(user_id, flashcard_id, last_reviewed, interval, ease_factor, correct_streak):
    user_flashcard = {
        "User_Id": user_id, #may or may not need this
        "Flashcard_Id": flashcard_id,
        "last_reviewed": last_reviewed,
        "interval": interval,  
        "ease_factor": ease_factor,
        "correct_streak": correct_streak
    }

    user = users.find_one({"username": user_id})
    if user is None:
        return False 
    
    user["performances"].append(user_flashcard)  

    return users.update_one({"username": user_id}, {"$set": {"performances": user["performances"]}})

    

    
    
