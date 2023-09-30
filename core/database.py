from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values

config = dotenv_values(".env.secret")

# Create a new client and connect to the server
dbhdl = MongoClient(config["MONGODB_URI"], server_api=ServerApi('1'))
dbclient = dbhdl[config["MONGODB_NAME"]]

# Send a ping to confirm a successful connection
try:
    dbhdl.admin.command('ping')
    print("Mongodb connection success")
except Exception as e:
    print('Database connection error', e)