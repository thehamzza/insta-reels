import pymongo

post = {"Username" : "wilfredburr", "ReelsUrl": "https://www.instagram.com", "EmbedCode": "cssvvbbh100001000hghghghty1-00"}

print("Updating Data to Mongodb")
# Sending Data to DataBase

client = pymongo.MongoClient("mongodb+srv://user1:123@cluster0.ruioxcd.mongodb.net/?retryWrites=true&w=majority")
db = client["test2"]

collection = db["dummy"]
collection.insert_one(post)