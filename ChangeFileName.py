from pymongo import MongoClient
import os
path = "H:\AppInfor2"
client = MongoClient('192.168.2.169',27017)
db = client.mongoQueue
myset = db.TestList1

for file in os.listdir(path):
    if '_' in file:
        continue
    else:
       for i in myset.find({'_id':file}):
           apkname = i.get("apkname")
           apkversion = i.get("apkversion")
           apknum = i.get("num")
           filenewname = apkname+'_'+apkversion+'__'+str(apknum)
           list=[]
           for filename in os.listdir(path):
               list.append(filename)
           if filenewname not in list:
               os.rename(path+'\\'+file,path+'\\'+filenewname)




