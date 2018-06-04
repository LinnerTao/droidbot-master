from pymongo import MongoClient

def MongoConn(add):
    client = MongoClient(add,27017)
    return client

def Insert(my_set,Nodes):
    my_set.insert(Nodes)
