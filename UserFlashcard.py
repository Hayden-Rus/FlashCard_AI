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


# update user flashcard
def search_performance(username, flashcard_id):
    user = users.find_one({"username": username})
    for x in user["performances"]:
        if x["Flashcard_Id"] == flashcard_id:
            return x
    return None

def update_last_reviewed(username, flashcard, date):
    user = users.find_one({"username": username})
    perf = search_performance(username, flashcard)
    if perf:
        perf["last_reviewed"] = date
        users.update_one(
            {"username": username, "performances.Flashcard_Id": flashcard},
            {"$set": {"performances.$.last_reviewed": date}}
        )

def increase_streak(username, flashcard):
    user = users.find_one({"username": username})
    perf = search_performance(username, flashcard)
    if perf:
        perf["correct_streak"] += 1
        users.update_one(
            {"username": username, "performances.Flashcard_Id": flashcard},
            {"$set": {"performances.$.correct_streak": perf["correct_streak"]}}
        )

def reset_count(username, flashcard):
    user = users.find_one({"username": username})
    perf = search_performance(username, flashcard)
    if perf:
        perf["correct_streak"] = 0
        users.update_one(
            {"username": username, "performances.Flashcard_Id": flashcard},
            {"$set": {"performances.$.correct_streak": 0}}
        )

def increase_ease_factor(username, flashcard):
    user = users.find_one({"username": username})
    perf = search_performance(username, flashcard)
    if perf:
        perf["ease_factor"] += 0.1
        users.update_one(
            {"username": username, "performances.Flashcard_Id": flashcard},
            {"$set": {"performances.$.ease_factor": perf["ease_factor"]}}
        )

def decrease_ease_factor(username, flashcard):
    user = users.find_one({"username": username})
    perf = search_performance(username, flashcard)
    if perf:
        perf["ease_factor"] -= 0.2
        users.update_one(
            {"username": username, "performances.Flashcard_Id": flashcard},
            {"$set": {"performances.$.ease_factor": perf["ease_factor"]}}
        )



