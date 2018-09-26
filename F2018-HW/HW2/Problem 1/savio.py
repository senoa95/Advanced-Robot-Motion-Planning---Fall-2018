#!/usr/bin/env python

import  read_file as rf
import matplotlib.pyplot as plt
import numpy as np
import contextlib

totNumVert, startVert, goalVert, i, j, cost = rf.read_file()

neighborList = []
tempEdgeList = []
tempCost_j = np.zeros(len(i))
# costList = np.zeros([len(neighborList)][len(neighborList)-1])
costListSize = (totNumVert,totNumVert-1)
costList = np.zeros(costListSize)
# a = (2,2)
# costList = np.zeros(a)

# s = (2,2)
# p = np.zeros(s)

# for vertIdx in range(0,totNumVert-1):
#     tempEdgeList.append( (i[vertIdx], j[vertIdx], cost[vertIdx]) )
#     if i[vertIdx]==i[vertIdx+1]:
#         # print(i[vertIdx+1])
#         continue
#     else:
#         # neighborList = []
#         neighborList.append(tempEdgeList)
#         tempEdgeList = []
for k in range(0,totNumVert-2 ):
    print('curr k')
    print(k)
    # raw_input()
    for vertIdx in range(0,totNumVert-1):
        vertexNum = vertIdx
        # print('start')
        # print(vertexNum)
        # raw_input()
        # currEdge = neighborList[i]
        if vertIdx == 0:
            costList[vertIdx][k] = 0
        elif vertIdx != 0 and k == 0:
            costList[vertIdx:,k] = float('inf')
            print('costList Inf')
            print(costList)
            raw_input()
            break
        else:
            for edgeIdx in range(0,len(j)-1):
                curr_i = i[edgeIdx]
                curr_j = j[edgeIdx]
                print('curr i')
                print(curr_i)
                print('vertexNum')
                print(vertexNum)
                print('edgeIdx')
                print(edgeIdx)
                # raw_input()
                if curr_i == vertexNum:
                    curr_j = j[edgeIdx]
                    tempCost_j[edgeIdx] = cost[edgeIdx] + costList[vertIdx-1][k-1]
                    print('curr cost')
                    print(tempCost_j)
                    # print('prev cost')
                    # print(costList[vertIdx-1][k-1])
                    raw_input()
                else:
                    tempCost_j[edgeIdx] = float('inf')
                    # print('inf')
                    # print(tempCost_j)
                    # raw_input()
            costList[vertIdx][k] = min(tempCost_j)
            print('cost list currunt num edges')
            np.printoptions(precision=3, suppress=False)
                print(costList[:][k])
            raw_input()
# file = open("output_1.txt","w")
# np.savetxt('output_1.txt',costList)
# file.close()
            # print(costList)
            # raw_input(0)
        #
        # print(currEdge)
        # raw_input()
        #
        # # if edgeIdx == 0:
        # #     costList[0:len(neighborList)-1][len(neighborList)-1] = float('inf')
        # #
        # #     continue
        # runningCost = []
        # for neighborIdx in range(0,len(currEdge)):
        #     currVertex = currEdge[neighborIdx][0]
        #     currNeighbor = currEdge[neighborIdx][1]
        #     currCostToNeighbor = currEdge[neighborIdx][2]
        #
        #     if currVertex == startVert:
        #         costList[currVertex,:] = 0
        #     runningCost.append(currCostToNeighbor + costList[currVertex][edgeIdx-1])
        #     # neighborList[(costIdx-1)][(neighborIdx-1)][1])
        #     costList[currNeighbor,edgeIdx] =  min(runningCost)
        #     # print(currNeighbor)
        #     # raw_input()
# print(costList)



# print(currNeighbor)
# print(edgeIdx)
# print(currVertex)
# # print(costList[currNeighbor,edgeIdx])
# print(costList[currVertex][edgeIdx-1])
# raw_input()
# costList[currNeighbor,edgeIdx] =


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
