from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['books_shop']
books = db.books

#Чтение данных
doc = books.find_one({"title": "A Light in the Attic"})
print(doc)

print("________________________________")

#Чтение с условием
docs = books.find({"stock": {"$gt": 19}})
for doc in docs:
    print(doc)

print("_______________________________")

#Обновление данных
books.update_one(
    {"title": "A Light in the Attic"},
    {"$set": {"stock": 99999}}
)

#Подсчет документов
count = books.count_documents({"stock": {"$gt": 19}})
print(count)