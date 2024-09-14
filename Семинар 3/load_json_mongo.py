from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)

db = client['books_shop']
books = db.books

with open(r"books.json") as f:
    data = json.load(f)

if isinstance(data, list):
    books.insert_many(data)
else:
    books.insert_one(data)