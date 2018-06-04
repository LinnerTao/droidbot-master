from pymongo import MongoClient
from bson.objectid import ObjectId
import json
def InsertMongo(Nodes):
    client = MongoClient('192.168.2.169', 27017)
    db = client.MultiApp
    collection = db.test1
    collection.insert(Nodes)

def ReadFiles(name,path,list1):
    #name:MongoDB中_id 的前缀，这里是app名称+版本号+num
    #path:
    #list1:json文件列表，一个json代表一个界面
    for i in list1:
        with open(path+'\\'+i,'r') as f:
            temp = json.loads(f.read())#json文件
            KeyNode = {
                '_id' : name+'_'+i,
                'states':temp
            }
            InsertMongo(KeyNode)

            #print (type(temp))
            #InsertMongo(temp)


import os

def ReadOnekindFiles(string):#读取一种文件格式的文件
    path = string #'D:\ExData\\air.com.tencent.qqfarmios_3.3.4__27\\states'
    list=[]
    filelist = os.listdir(path)
    for i in filelist:
        if os.path.splitext(i)[1]=='.json':#这里读取所有.json文件
            list.append(i)
    return list


