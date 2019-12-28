import pickle
import scipy.io as scio
import csv

with open("rightrss.txt","rb") as f:
    rss = pickle.load(f)
#print("rss",rss)

with open("rightloc.txt","rb") as f:
    loc = pickle.load(f)
#print("loc",loc)

with open("keysFormat.txt","rb") as f:
    keys = pickle.load(f)
#print("len",len(keys))

for i,j in zip(loc,rss):
    #print(i,j)
    pass
scio.savemat('filename.mat', mdict={"loc":loc})

with open("keysFormat.txt","rb") as f:
    macKeys = pickle.load(f)
#print("macKeys",macKeys)

with open('birth_weight.csv', "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows([keys])
    f.close()
with open('birth_weight.csv', "a+", newline='') as f:
    writer = csv.writer(f)
    for i in rss:
        temp = ["0"]*165
        for ikey,ivalue in i.items():
            index = keys.index(ikey)
            if index == -1:
                pass
            else:

                temp[index] = ivalue
        writer.writerow(temp)
    f.close()