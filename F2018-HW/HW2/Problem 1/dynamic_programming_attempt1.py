#!/usr/bin/env python

import  read_file as rf
import matplotlib.pyplot as plt
import numpy as np

totNumVert, startVert, goalVert, i, j, cost = rf.read_file()

neighborList = []
tempList = []
costList = np.zeros((totNumVert,totNumVert-1))

for vertIdx in range(0,len(i)-1):
    tempList.append( (j[vertIdx] )
    # tempList2.append(cost[vertIdx])
    if i[vertIdx]==i[vertIdx+1]:
        continue
    else:
        neighborList.append(tempList)
        tempList = []


for costIdx in range(0,len(neighborList)):
    costList[0,:] = 0
    costList[1:,0] = float('inf')
    currEdge = neighborList[costIdx]
    for edgeIdx in range(0,len(currEdge)):
        currNeigh = currEdge[edgeIdx]
        costList[currNeigh][0] = 
print(costList)
# V = np.matrix([])
# x = 0
# minVerCost = np.matrix([])
# # V.append(float('inf'))
# startIdx = i.index(startVert)
# # print(i[startIdx])
# V = np.zeros((len(i),len(i)-1))
# print(V)

# tempList.append(2) tempList.append(3)
#
# bigList.append(tempList)
#
# tempList = []
#
# bigList[42][0]
# bigLuist[24][2]
#
# for k in range(startIdx,len(i)-2):
#     # print([startVert])
#     # print(i[startVert])
#
#     if k==startIdx:
#         V[0,k] = 0;
#         V[1:,k] = float('inf')
#         continue
#             # V[]
#     for x_i in range(startVert,(len(i)-1)):
#         print(V[:,0])
#         if k==0:
#             # V[k].append([])
#             V[x_i,k] = (10000)
#
#         elif (k != 0) and (i[x_i] == i[x_i+1]):
#             # # print((cost[x_i+1] + V[k-1]))
#             # # print(cost[x_i])
#             # print((cost[x_i+1] + V[k-1]))
#             # x += 1
#             # print(x)
#             V[k,x_i] = min((cost[x_i] + V[x_i,k-1]),(cost[x_i+1] + V[x_i,k-1]))
            # print(V[k,:])
            # runningCost[x_i] = cost[x_i] + V[k-1]
            # print(runningCost[x_i])
        #     costFun
        # plt.plot(j)
        # print('start Vertex = ', startVert)
        # print('goal Vertex = ', goalVert)
        # print('totNumVert = ', totNumVert)
# V[k].append(min(runningCost))
        # print('total cost list',len(cost))
        # print(len(runningCost))
        # print(k)
        # print(len(i))
        # print(len(j))
        # print(len(cost))
        # print(cost[x_i])
        # print(V[k-1])

        # print(runningCost[x_i])

        # plt.plot(V)
# print(max(V[1,:]))
# i = 0
# # print(len(V))
# for horizIdx in range(0,len(V)):
#     # print(V[horizIdx,0:i+1].shape)
#     # print(V[horizIdx,:])
#     # minVerCost[horizIdx] = min(V[horizIdx,i:])
#     i = i+1
