



import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')

from collections import Counter

import Data_Handler
trucks=Data_Handler.get_table_rows("trucks","dictonary")
geolocations=Data_Handler.get_table_rows("geolocation","dictonary")

import redis
r=redis.StrictRedis(host="localhost",port=6379,charset="utf-8", decode_responses=True,db=0)

# building id's initial
AN=1
driver_id_string_code="driver_id:" # +AN

#building hash map for trucks
for truck in trucks :
    key_for_el=driver_id_string_code+'A'+str(AN)
    r.hmset(key_for_el,truck)
    AN=AN+1

#building hash map for geo_location

## getting value example
#print(r.hget("driver_id:A1","model"))
#truck_id:driver_id:AN  lists
trip_id="t:"
driver_id_string_code=":driver_id:"
familar_IDs=Counter()

for geolocation in geolocations:

    driver_id_based_on_dic=geolocation["driverid"]
    familar_IDs[driver_id_based_on_dic]+=1
    form_the_key=trip_id+str(familar_IDs[driver_id_based_on_dic])+driver_id_string_code+driver_id_based_on_dic
    r.hmset(form_the_key,geolocation)
