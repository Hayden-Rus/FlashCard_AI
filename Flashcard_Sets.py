from User import *
import pymongo as pym

def create_set(username, set_name):
    new_set = {
        "set_name": set_name,
        "set": []
    }

    user = users.find_one({"username": username})
    if user is None:
        return False
    
    user["sets"].append(new_set)

    users.update_one({"username": username}, {"$set": {"sets": user["sets"]}})

    return True

    
#create_set("hayden","balh")