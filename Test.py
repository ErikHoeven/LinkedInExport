'''
Created on Apr 2, 2015

@author: erik
'''
from pymongo import MongoClient


#Mongo connection
client = MongoClient()
#Mongo Database
db = client.LinkedIn
#Mongo Collection
Profiel = db.STG_Profielen
jsonProfiles = Profiel.find({"skills_list":"ETL"})

print "background_projects" in jsonProfiles[3].keys()


  
        
    