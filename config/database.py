from multiprocessing import connection
#Import statements
from pymongo import mongo_client
#Create a DB connection
connection = mongo_client("mongodb://localhost:27017/test")