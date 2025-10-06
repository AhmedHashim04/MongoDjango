
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ahmedha4im7_db_user:Gmc5y2fr02OjGEp2@django.hdymbzc.mongodb.net/?retryWrites=true&w=majority&appName=Django"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

documents = [
    {"name": "Product 1", "price": 10.99, "description": "Description for Product 1"},
    {"name": "Product 2", "price": 15.49, "description": "Description for Product 2"},
    {"name": "Product 3", "price": 7.99, "description": "Description for Product 3"},
    {"name": "Product 4", "price": 12.00, "description": "Description for Product 4"},
    {"name": "Product 5", "price": 20.00, "description": "Description for Product 5"},
]

def insertMany(client,documents):
    db = client["Django"]
    collection = db["products"]
    collection.insert_many(documents)

insertMany(client,documents)

def findProducts(client):
    db = client["Django"]
    collection = db["products"]
    products = collection.find()
    for product in products:
        print(product)
findProducts(client)

def readDocs(client, condition):
    db = client["Django"]
    collection = db["products"]
    products = collection.find(condition)
    for product in products:
        print(product)
readDocs(client, {"price": {"$gt": 10}})