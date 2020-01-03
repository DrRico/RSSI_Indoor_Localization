import pickle
import scipy.io as scio
import csv
import numpy as np

with open("PRE_RSS.txt","rb") as f:
    predicerss = pickle.load(f)
#print('predicerss',predicerss)

with open("PRE_LAB.txt","rb") as f:
    PRE_LOC = pickle.load(f)
#print('predicerss',predicerss)

with open("OFF_RSS.txt","rb") as f:
    rss = pickle.load(f)
#print("rss",rss)

with open("OFF_LOC.txt","rb") as f:
    loc = pickle.load(f)
#print("loc",loc)

with open("keysFormat.txt","rb") as f:
    keys = pickle.load(f)
#print("len",len(keys))


scio.savemat('loc.mat', mdict={"loc":loc})
scio.savemat('PRE_LOC.mat', mdict={"PRE_LOC":PRE_LOC})

with open("keysFormat.txt","rb") as f:
    macKeys = pickle.load(f)
#print("macKeys",macKeys)

# with open('birth_weight.csv', "w", newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows([keys])
#     f.close()
# with open('birth_weight.csv', "a+", newline='') as f:
#     writer = csv.writer(f)
datas = []
for i in rss:
    temp = [0]*165
    for ikey,ivalue in i.items():
        index = keys.index(ikey)
        sum = 0
        if index == -1:
            pass
        else:
            for value in ivalue:
                sum = sum + int(value)
            temp[index] = sum/len(ivalue)
    datas.append(np.array(temp))
#print(datas)
scio.savemat('OFF_RSS.mat', mdict={"csv": datas})


datas = []
for i in predicerss:
    temp = [0]*165
    for ikey,ivalue in i.items():
        index = keys.index(ikey)
        if index == -1:
            pass
        else:
            temp[index] = int(ivalue)
    datas.append(temp)
    #print(temp)
#print(datas)
scio.savemat('PRE_RSS.mat', mdict={"predict": datas})
