#import DB here
from dataclasses import fields
from mainapp.database.db import DB

from marshmallow import Schema, fields

class Counties(object):
    #county constructor taking in values
    def __init__(self, name, population, governor, countyhq):
        self.name = name
        self.population = population
        self.governor = governor
        self.countyhq = countyhq
        
    #method to insert county object into the database
    def insert(self):
        #inserts into mongo db counties collection
        return DB.insert(collection='counties',data=self.json())

    
    #turn given data into json
    def json(self):
        return {
            'name': self.name,
            'population': self.population,
            'governor': self.governor,
            'countyhq': self.countyhq
        }

    #return all counties in the database collection
    def get_all():
        return DB.find_all(collection='counties')
    

class CountiesSchema(Schema):
    _id = fields.Str()
    name = fields.Str()
    population = fields.Str()
    governor = fields.Str()
    countyhq = fields.Str()