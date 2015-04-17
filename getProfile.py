'''
Created on Mar 19, 2015

@author: erik
'''

from pymongo import MongoClient


#Mongo connection
client = MongoClient()
#Mongo Database
db = client.LinkedIn

def getProfiles(Skill):
    
    #Mongo Collection
    Profiel = db.STG_Profielen
    
    jsonProfiles = Profiel.find({"skills_list":Skill})
        
    return jsonProfiles

def getFullName(jsonProfile):
    FullName = jsonProfile['full_name']
    
    return FullName

def getCurrentCompany(jsonProfile):
    CurrentCompany = jsonProfile["current_companies"]
    
    return CurrentCompany

def getPastCompanies(jsonProfile):
    PastCompanies = jsonProfile["past_companies"]
    
    return PastCompanies
    
def getHeadline (jsonProfile):
    headline = jsonProfile["headline"]

    return headline

def getBackgroundSummary(jsonProfile):
    
    background_summary = jsonProfile["background_summary"]
            
    return background_summary

def getBackgroundExperience(jsonProfile):
    
    background_experience = jsonProfile["background_experience"]
    
    return background_experience
    
def getBackgroundProjects(jsonProfile):
    background_projects = jsonProfile["background_projects"]
    
    return background_projects

def defSkillsList(jsonProfile):
    skills_list = jsonProfile["skills_list"]
    
    return skills_list
    


    