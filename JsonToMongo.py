from WriteMongoData import *
path1 = 'H:\AppInfor2'
#path = 'D:\ExData\\air.com.tencent.qqfarmios_3.3.4__27\\states'
#name = 'air.com.tencent.qqfarmios_3.3.4__27'

for file in os.listdir(path1):
    path2 = path1+'\\'+file+'\\'+'states'
    list1 = ReadOnekindFiles(path2)
    ReadFiles(file,path2,list1)
#InsertMongo(Nodes)

