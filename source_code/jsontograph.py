import json
from py2neo import Graph,Relationship,Node

graph = Graph()
remote_graph = Graph("localhost/7474", "neo4j", "yourpassword")
alice = Node("person", name = "alice")
bob = Node("person", name = "Bob")
alice_knows_Bob = Relationship(alice, "knows", bob)
graph.create(alice_knows_Bob)
