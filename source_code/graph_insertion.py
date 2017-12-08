
import sys
#choosing the directory of packages , based in your python version change the number ,
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')
import json
from py2neo import Graph,Relationship,Node

your_Database_port_that_running="7474" # in my case , thats the port , be assure that the port is running from neo4js
Password="neo4j"
user_name="neo4j"
local_host="127.0.0.1/"



graph = Graph()
remote_graph = Graph(local_host+your_Database_port_that_running, user_name, Password)

## use the Data_handler module to fill , nodes , it's already return dictonary
## loop through keys , for each key extract it's value and fill it in each ndoe 

alice = Node("person", name = "alice")
bob = Node("person", name = "Bob")
alice_knows_Bob = Relationship(alice, "knows", bob)



graph.create(alice_knows_Bob)
