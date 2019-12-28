# -*-coding = utf-8-*-
import os
import pickle
FilePath = "RSSI_DATA/"
savedDataName = "data.txt"
savedLabelName = "datalabel.txt"

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
    AP_label = lists[-1]
    #print(len(lists[12:-3]))
    for RSSI_list in lists[12:-3:2]:
        #print(RSSI_list)
        AP_names.append(RSSI_list.split(",")[0] + ' ' + RSSI_list.split(",")[2].replace('"','') + ' ' + RSSI_list.split(",")[3] + ' ' +RSSI_list.split("Mb")[1].split(",")[1])
        AP_rssis.append(RSSI_list.split(",")[5] + 'dBm')
        # AP_names.append(RSSI_list.split("(",1)[0]+'-'+RSSI_list.split("{")[1].split("}")[0])
        # AP_rssis.append(RSSI_list.split("[")[1].split("dBm")[0])
    '''pyl.plot(range(len(AP_names)), AP_rssis)
    pyl.plot(range(len(AP_names)), AP_rssis,"o")
    pyl.show()  #'''
    return AP_label, dict(zip(AP_names, AP_rssis))

def GetFileName(path):
    path_list=[]
    listdirs = os.listdir(path)
    for listdir in listdirs:
        path_list.append(listdir)
    return path_list

def SaveData(name,datas):
    # print(datas)
    with open(name,"wb") as f:
        pickle.dump(datas, f)

AllAPdata = []
AllAPlabel = []
if __name__ == '__main__':
    for path_list in GetFileName(FilePath):
        RSSI_lists = ReadTxtName(path_list)
        label, Rssidata = GetAPInfo(RSSI_lists)
        AllAPdata.append(Rssidata)
        AllAPlabel.append(label)
    SaveData(savedDataName,AllAPdata)
    SaveData(savedLabelName,AllAPlabel)