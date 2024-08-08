import pymongo as pym
client = pym.MongoClient("mongodb://localhost:27017")

# Selecting the database and collection
db = client["FlashCard_Ai"]
UserFlashcards = db["UserFlashcards"]

#create datetime objects for last_reviewed

def add_UserFlashcard(user_id, flashcard_id, last_reviewed, interval, ease_factor, correct_streak):
    user_flashcard = {
        "User_Id": user_id,
        "Flashcard_Id": flashcard_id,
        "last_reviewed": last_reviewed,
        "iterval": interval,
        "ease_factor": ease_factor,
        "correct_streak": correct_streak
    }

    
    result = UserFlashcards.insert_one(user_flashcard)
    
    return result.inserted_id

# Example test data
user_id = "user_123"  # Replace with a valid user ID
flashcard_id = "flashcard_456"  # Replace with a valid flashcard ID
last_reviewed = "xx,xx,xxxx" # Current date and time
interval = 5  # Review interval in days
ease_factor = 2.5  # Ease factor of the flashcard
correct_streak = 3  # Number of consecutive correct answers

# Call the function with the test data
inserted_id = add_UserFlashcard(user_id, flashcard_id, last_reviewed, interval, ease_factor, correct_streak)
print(f"UserFlashcard entry added with ID: {inserted_id}")