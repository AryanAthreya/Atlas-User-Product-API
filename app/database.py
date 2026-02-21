from pymongo import MongoClient

MONGO_URL = "mongodb+srv://Aryan_Cluster:Aryan1234@cluster0.tjuz4os.mongodb.net/"

client = MongoClient(MONGO_URL)

database = client["atlas_user_product_db"]

users_collection = database["users"]
products_collection = database["products"]
