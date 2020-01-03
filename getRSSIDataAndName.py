# -*-coding = utf-8-*-
import os
import pickle,collections
import numpy as np
FilePath = "RSS数据/"
savedDataName = "OFF_RSS.txt"
savedLabelName = "OFF_LOC.txt"

def ReadTxtName(rootdir):
    lines = []
    with open(FilePath+rootdir, 'r',encoding='utf-8') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines

def GetAPInfo(lists):
    AP_names = []
    AP_rssis = []
    dicts = {}
    #print(len(lists[12:-3]))
    for RSSI_list in lists[12:-3:2]:
        #print(RSSI_list)
        if(RSSI_list.split(",")[3] == '6' or RSSI_list.split(",")[3] == '11'):  #筛选出信道为6和11的数据，扔掉
            continue
        #mac = RSSI_list.split(",")[0] + ' ' + RSSI_list.split(",")[2].replace('"','') + ' ' + RSSI_list.split(",")[3] + ' ' +RSSI_list.split("Mb")[1].split(",")[1]
        #mac = RSSI_list.split(",")[0] + '_' + RSSI_list.split("Mb")[1].split(",")[1]
        mac = RSSI_list.split("Mb")[1].split(",")[1]
        val = RSSI_list.split(",")[5]

        AP_names.append(mac)
        AP_rssis.append(val)

    for i, j in zip(AP_names, AP_rssis):          #这是正确的办法
        if i not in dicts.keys():
            dicts[i] = [j]
        else:
            dicts[i].append(j)

    #AP_label = dict(zip(tuple(AP_names), tuple(AP_rssis)))
    return dicts

def GetFileName(path):
    path_list=[]
    listdirs = os.listdir(path)
    for listdir in listdirs:
        path_list.append(listdir)
    return path_list

def SaveDataAsformat(name,datas):
    # print(datas)
    with open(name,"wb") as f:
        pickle.dump(datas, f)

def SaveDataAsTXT(name,datas):
    # print(datas)
    with open(name,"w") as f:
        f.write(str(datas))


AllAPdata = []
AllAPlabel = []
if __name__ == '__main__':
    for path_list in GetFileName(FilePath):
        RSSI_lists = ReadTxtName(path_list)
        dicts  = GetAPInfo(RSSI_lists)
        AllAPdata.append(dicts)
        AllAPlabel.append([int(path_list.split('_')[1]),int(path_list.split('_')[2])])
    SaveDataAsformat(savedDataName,AllAPdata)
    SaveDataAsformat(savedLabelName,np.array(AllAPlabel))