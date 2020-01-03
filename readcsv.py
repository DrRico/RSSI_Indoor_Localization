# -*-coding = utf-8-*-
# 导入数据
import numpy as np
import scipy.io as scio
from sklearn import neighbors
import matplotlib.pyplot as plt
import cv2

loc = scio.loadmat('loc.mat')
rss = scio.loadmat('OFF_RSS.mat')
predict = scio.loadmat('PRE_RSS.mat')
#predict_loc = scio.loadmat('PRE_LOC.mat')

# print('loc key:',loc.keys())
# print('rss key:',rss.keys())
# print('predict key:',predict.keys())

# offline_location, offline_rss = offline_data['offline_location'], offline_data['offline_rss']
# trace, rss = online_data['trace'][0:100, :], online_data['rss'][0:100, :]
trace, rss, predict = loc['loc'], rss['csv'], predict['predict']

trace_x = trace[:,0]
trace_y = trace[:,1]

# 定位准确度
def accuracy(predictions, labels):
    return np.mean(np.sqrt(np.sum((predictions - labels)**2, 1)))

knn_reg = neighbors.KNeighborsRegressor(1, weights='uniform', metric='euclidean')  #参数为33时最优
predictions = knn_reg.fit(rss, trace).predict(predict)  #通过实际测量的rssi值进行预测
acc = accuracy(predictions, trace)
print("knn回归精度: ", acc/100, "m")  #

predictions_x,predictions_y = predictions[:,0],predictions[:,1]

# #plt.plot(trace)
# plt.scatter(trace_x,trace_y,color='blue')
# plt.scatter(predictions[:,0],predictions[:,1],color='red')
# plt.plot([trace_x,predictions[:,0]],[trace_y,predictions[:,1]],linestyle='dotted')
# plt.show()                  

map = cv2.imread("map_matlab.jpg")
for i, j, x, y in zip(trace_x, trace_y, predictions_x, predictions_y):
    cv2.line(map, (i, j), (int(x), int(y)), (0, 0, 255), 1)
    # cv2.circle(map, (i, j), 8, (0, 255, 0),thickness=-1)
    # cv2.circle(map, (int(x), int(y)), 4, (0, 0, 255),thickness=-1)
    cv2.circle(map, (i, j), 8, (0, 255, 0),2)
    cv2.circle(map, (int(x), int(y)), 4, (0, 0, 255),2)
cv2.imshow("map", map)
cv2.waitKey(0)              #'''
