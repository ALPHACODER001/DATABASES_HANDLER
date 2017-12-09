import sys, csv
from py2neo import neo4j, authenticate, Graph

def main():

    sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')

    graph = Graph("127.0.0.1/7474","oawajan","80302170812")

    graph.execute("load csv with headers from F:\\Users\\oawajan\\Documents\\Courses\\data-science\\BigData\\hw1\\DATABASES_HANDLER-master\\source_code\\geolocation.csv \
                              as geolocation create (a1:geolocation {truckid:geolocation.truckid,driverid:geolocation.driverid,event:geolocation.event \
                              latitude:geolocation.latitude,longitude:geolocation.longitude,city:geolocation.city,velocity:geolocation.velocity, \
                              event:geolocation.event,idling_ind:geolocation.idling_ind})")
    graph.execute("load csv with headers from F:\\Users\\oawajan\\Documents\\Courses\\data-science\\BigData\\hw1\\DATABASES_HANDLER-master\\source_code\\geolocation.csv \
        as trucks create (a1:truks {driverid:trucks.driverid,truckid:trucks.truckid,model:trucks.model})")

    with open("geolocation.csv", newline ='') as gelocation:
        with open("trucks.csv",newline='') as trucks:

            ReadGeolocation = csv.DictReader(gelocation)
            ReadTrucks = csv.DictReader(trucks)

            for row in ReadGeolocation:
                print(row['truckid'],row['driverid'],row['event'],row['latitude'],row['longitude'],row['city'],row['velocity'],
                    row['event_ind'],row['idling_ind'])

            for row in ReadTrucks:
                print(row['truckid'], row['driverid'], row['event'], row['latitude'], row['longitude'], row['city'],
                      row['velocity'], row['event_ind'], row['idling_ind'])

if __name__ == '__main__':
    main()
