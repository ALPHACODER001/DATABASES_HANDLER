import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')
import pymongo
from pymongo import MongoClient
import Data_Handler

client = MongoClient()

def read_by_nosql_engine():
    trucks_geolocation_db=client["trucks_geolocation"]
    trucks_doc=trucks_geolocation_db["trucks"]
    geo_location_doc=trucks_geolocation_db["geo_location"]
    Records_trucks=Data_Handler.get_table_rows("trucks")
    Records_geolocation=Data_Handler.get_table_rows("geolocation")
    insert(Records_trucks,trucks_doc)
    insert(Records_geolocation,geo_location_doc)

def insert(Records,doc):
    for record in Records:
        doc.insert(record)

read_by_nosql_engine()



