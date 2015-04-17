'''
Created on Mar 18, 2015

@author: erik
'''

def setDisipline(skill):
    
    strDisipline = ""
    
    lstDisipline = {  
                     # Data Mining
                     "Churn Modelling"              : "Data Mining"
                     ,"Conceptual Modeling"         : "Data Mining"
                     ,"Customer Analysis"           : "Data Mining"
                     ,"Customer Value"              : "Data Mining"
                     ,"Customer Value Modelling"    : "Data Mining"
                     ,"Data Science"                : "Data Mining"
                     ,"Churn Modelling"             : "Data Mining"
                     ,"Data Mining"                 : "Data Mining"
                     ,"Data Science"                : "Data Mining"
                     ,"Data Visualization"          : "Data Mining"
                     ,"Machine Learning"            : "Data Mining"
                     ,"Next Best Action"            : "Data Mining"
                     ,"Predictive Analytics"        : "Data Mining"
                     ,"Python"                      : "Data Mining"
                     ,"R"                           : "Data Mining"
                     ,"Text Mining"                 : "Data Mining"
                     ,"Pega DSM"                    : "Data Mining"
                     ,"Pegasystems PRPC"            : "Data Mining"
                    # Data Warehouse
                     ,"Data Analysis"               :"Data Warehousing"
                     ,"Data Integration"            :"Data Warehousing"
                     ,"Data Modeling"               :"Data Warehousing"
                     ,"Data Quality"                :"Data Warehousing"
                     ,"Data Warehouse..."           :"Data Warehousing"
                     ,"Data Warehousing"            :"Data Warehousing"
                     ,"Database Marketing"          :"Data Warehousing"
                     ,"Databases"                   :"Data Warehousing"
                     ,"Dimensional Modeling"        :"Data Warehousing"
                     ,"ETL"                         :"Data Warehousing"
                     ,"Information Management"      :"Data Warehousing"
                     ,"LGD Models"                  :"Data Warehousing"
                     ,"Master Data Management"      :"Data Warehousing"
                     ,"Real Time"                   :"Data Warehousing"
                     ,"SAS"                         :"Data Warehousing"
                     ,"SQL"                         :"Data Warehousing"
                     ,"SSIS"                        :"Data Warehousing"
                    # Reporting
                    ,"Business Objects,"            :"Reporting"
                    ,"Cognos,"                      :"Reporting"
                    ,"SSRS"                         :"Reporting"   
                    }
    
    
    for strSkill in lstDisipline:
        if skill.lower() in strSkill.lower():
            strDisipline = lstDisipline[strSkill]
    
    return strDisipline


def setFunctie (strDisipline):
    strFunctie = ""
    
    lstFuncties = {  
                     # Business Intelligence
                     "Data Mining"             : "Business Intelligence"
                   
                   }
    
    for strFunctie in lstFuncties:
        if strDisipline.lower() in strFunctie.lower():
            strFunctie = lstFuncties[strFunctie]
    
    return strFunctie


