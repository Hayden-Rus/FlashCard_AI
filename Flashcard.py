import pymongo as pym

client = pym.MongoClient("mongodb://localhost:27017")

# Selecting the database and collection
db = client["FlashCard_Ai"]
Flashcards = db["Flashcards"]

def add_Flashcard(question, answer, category=None):
    flashcard = {
        "question": question,
        "answer": answer,
        "category": category
    }

    
    result = Flashcards.insert_one(flashcard)

    return result.inserted_id

