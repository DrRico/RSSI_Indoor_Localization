'''import scipy.io as sio
a = sio.loadmat('matlabdata.mat') #加载文件
af = a['fingerprint_sim']
print(af)
with open('name.txt',"w") as f:
    f.write(str(af)) #'''
'''import scipy.io as scio
import cv2

offline_data = scio.loadmat('offline_data_random.mat')
online_data = scio.loadmat('online_data.mat')

print('offline_data key:',offline_data.keys())
print('online_data key:',online_data.keys())

offline_location, offline_rss = offline_data['offline_location'], offline_data['offline_rss']
trace, rss = online_data['trace'][0:100, :], online_data['rss'][0:100, :]

trace_x=trace[:,0]
trace_y=trace[:,1]

map = cv2.imread("map_matlab.jpg")

for i,j in zip(trace_x,trace_y):
    cv2.circle(map, (i, j), 5, (0, 255, 0),thickness=-1)

cv2.imshow("image", map)
cv2.waitKey(0)  #'''

import pickle
def SaveDataAsformat(name,datas):
    # print(datas)
    with open(name,"wb") as f:
        pickle.dump(datas, f)

keys = []
with open("rss.txt","rb") as f:
    rssdatas = pickle.load(f)
    print(rssdatas)
    print(type(rssdatas))
    for rssdata in rssdatas:
        for i in rssdata:
            keys.append(i)
            #print(i)
        #keys.append(rssdata.keys())

keys = tuple(set(keys))
print(type(keys))

SaveDataAsformat("keysFormat.txt",keys)

with open("keys.txt","w") as kf:
    kf.write(str(keys))

# import pytesseract
# from PIL import Image
#
# IMG = Image.open(r"E:\Python\Python3.6\My_shit\pycharm\TXEDU\室内定位相关\RSSI_PreProcess\1.png")
# #IMG.show()
# aa = pytesseract.image_to_string(IMG)
# #aa = pytesseract.image_to_string(IMG)
# print(aa)
