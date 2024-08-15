from Flashcard_Sets import *
from bson import ObjectId 
import pymongo as pym 

# Connecting to MongoDB
client = pym.MongoClient("mongodb://localhost:27017")

# Selecting the database and collection
db = client["FlashCard_Ai"]
Flashcards = db["Flashcards"]

def add_Flashcard(question, answer, category=None):
    flashcard = {
        "question": question,
        "answer": answer,
    }

    result = Flashcards.insert_one(flashcard)
    return result.inserted_id

def update_Flashcard(id_, question, answer, category=None):
    # Convert the string ID to an ObjectId
    object_id = ObjectId(id_)

    # Find the flashcard by ID
    card = Flashcards.find_one({"_id": object_id})  # Use the ObjectId for querying

    if card is None:
        return False  # Handle case where the flashcard isn't found

    # Update the fields
    updated_fields = {
        "question": question,
        "answer": answer,
        "category": category
    }

    # Perform the update
    result = Flashcards.update_one({"_id": object_id}, {"$set": updated_fields})

    return result.modified_count > 0  # Return True if the document was updated


#update_Flashcard("66b5064d1f61c1d83ec2d2c1", "testing", "yaaaay")