import json
from MongoOperation import *
import os
path1 = 'H:\AppInfor2'
client = MongoConn('192.168.2.169')
my_set1 = client.MultiApp.AppList
#JSPath = "H:\\AppInfor2\\COM.Bangso.FitMiss_1.1__16\\utg.js"
#JSonPath = "H:\\AppInfor2\\COM.Bangso.FitMiss_1.1__16\\APPFiles.json"
#AppName = 'COM.Bangso.FitMiss_1.1__16'
for file in os.listdir(path1):
    JSPath = path1+'\\'+file+'\\'+'utg.js'
    JSonPath = path1+'\\'+file+'\\'+'APPFiles.json'
    AppName = file
    k = AppName.split('_')
    if len(k)==5:
        appn = k[0]+'.'+k[1]
        appver = k[2]
        num = int(k[4])
    else:
        appn = k[0]
        appver = k[1]
        num = int(k[3])
    f = open(JSPath, 'r')
    f2 = open(JSonPath, 'w')
    line = f.readline()
    while line:
        line = f.readline()
        f2.write(line)
        # print (type(k))
    f2.close()


    f3 = open(JSonPath, 'r')
    temp = json.loads(f3.read())
    key_node = {
        '_id': AppName,
        'AppName': appn,
        'AppVersion': appver,
        'num': num,
        'OtherThing': temp
    }
    Insert(my_set1, key_node)

