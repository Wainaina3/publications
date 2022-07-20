import pymongo
from mainapp.configs.appconfigs import Appconfig

class DB(object):
  #using online mongo db database 
  def init():

    #load database credentials
      database_url = Appconfig.read_configs("database_url")
      #initiate a connection
      client = pymongo.MongoClient(database_url)
      DB.DATABASE = client['govt']

  def insert(collection, data):
      #insert data into given collection
      DB.DATABASE[collection].insert_one(data)

  def find_all(collection):
    #return all entries in the given collection
    return DB.DATABASE[collection].find()
    

