import pymongo

class DB(object):
  #using online mongo db database 
  #this is not a safe implementation
  DATABASE_URL = "mongodb+srv://aptitudeadmin:aptitudenyunyizi@aptitude.5x5on6f.mongodb.net/?retryWrites=true&w=majority"
  def init():
    client = pymongo.MongoClient(DB.DATABASE_URL)
    DB.DATABASE = client["govt"]

  def insert(collection, data):
      #insert data into given collection
      DB.DATABASE[collection].insert_one(data)

  def find_all(collection):
    #return all entries in the given collection
    return DB.DATABASE[collection].find()
    

