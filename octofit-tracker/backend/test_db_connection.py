from pymongo import MongoClient

# Test MongoDB connection
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Check collections
collections = db.list_collection_names()
print("Collections:", collections)

# Insert a test document into the users collection
test_user = {"username": "testuser", "email": "testuser@example.com", "password": "password"}
db.users.insert_one(test_user)

# Verify the document was inserted
user = db.users.find_one({"username": "testuser"})
print("Inserted User:", user)
