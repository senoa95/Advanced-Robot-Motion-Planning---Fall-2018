#!/usr/bin/env python

import  read_files as rf
import test
import matplotlib.pyplot as plt
import numpy as np
import contextlib

totNumVert, startVert, goalVert, adjacencyList, edgeCost, inputFile = rf.read_files(3)
vertexList = sorted(list(adjacencyList.keys()))
costList = {vertex:np.inf for vertex in vertexList}
# costList = {}
backPointer = {}
openListCost = {}
openList = []
closedList = set()
tempCost = []

openList.append(startVert)
costList[startVert] = 0

while goalVert not in closedList:

    # for currVertex in openList:
    bestCurrVertex = sorted(costList.iteritems(), key=lambda (k,v): (v,k))
    currVertex = bestCurrVertex[0][0]
    if currVertex in closedList:
        openList.remove(currVertex)
        del costList[currVertex]
        continue

    for adjacentVertex in adjacencyList[currVertex]:
        if adjacentVertex not in openList:
            openList.append(adjacentVertex)
        costList[adjacentVertex] = edgeCost[tuple([currVertex,adjacentVertex])]\
        + costList[currVertex]
    openList.remove(currVertex)
    closedList.add(currVertex)
    del costList[currVertex]
print(len(closedList))
raw_input()
# raw_input()
    # print(min(tempCost.value()))
    # raw_input()

        # print(currVertex)
        # raw_input()
        # for adjacentVertex in adjacencyList[currVertex]:
        #     edgeWeight = edgeCost[tuple([currVertex,adjacentVertex])]
        #     tempCost = edgeWeight + costList[currVertex]
        #     if costList[adjacentVertex] > tempCost:
        #         costList[adjacentVertex] = tempCost
        #         backPointer[adjacentVertex] = currVertex
        #     # print(costList[currVertex])
        #     openList.append(adjacentVertex)
        # bestVertex = sorted(costList.iteritems(), key=lambda (k,v): (v,k))
        # openList.remove(currVertex)
        # closedList.append(bestVertex[0][0])
        # print(openList)
        # raw_input()
        # bestVertex[0] = []
        # del costList[bestVertex[0][0]]
        # print(costList)
        # print(closedList)

            # elif adjacentVertex not in openList:

        # elif adjacencyList[currVertex] not in openList

        # print
        # bestVertex = sorted(costList.iteritems(), key=lambda (k,v): (v,k))
        # openList.append(adjacencyList[bestVertex[0][0]])
        # openList.remove(bestVertex[0][0])
        # openList.append(bestVertex[0][0])
        # currVertex = bestVertex[i][0]
        # del costList[bestVertex[0][0]]
        # # print(bestVertex)
        # # print(costList)
        # print(currVertex)
        # raw_input()


        # for currVertex in (openList):
        # if bestVertex[0] in openList:
        #     continue
        # else:
        #     print(bestVertex[0][0])
        #     closedList.append(bestVertex[0][0])
        #     openList.remove(bestVertex[0][0])
        #     openList.append(adjacentVertex)
        #     print(openList)
        #     print('here')
        #     raw_input()


            #     if currVertex == startVert:
            #         for adjacentVertex in adjacencyList[currVertex]:
            #             openList.append(adjacentVertex)
            #             costList[adjacentVertex] = edgeCost[tuple([currVertex,adjacentVertex])]
            #         openList.remove(currVertex)
            #         closedList.append(currVertex)
            #         continue

    # for bestVertex in bestVertex:
    #     if bestVertex[0] in openList:
    #         continue
    #     else:
    #         continue
    #         print('no')
    #         print(bestVertex)
    #         print(openList)
    #         raw_input()
    #         openList.append(adjacencyList[bestVertex[0]])
    #         openList.remove(bestVertex[0])
    #         closedList.append(bestVertex[0])
    #
    #
    #     print(openList)
    #     print(closedList)


        # print(openList)
        # raw_input()

        # print(openList)
        # print(closedList)
        # break

    # for adjacentVertex in adjacencyList[currVertex]:
    #     openList.append(adjacentVertex)
    #
    # for adjacentVertex in adjacencyList[currVertex]:
    #     costList[currVertex] = edgeCost[tuple([currVertex,adjacentVertex])]\
    #                                                 + costList[currVertex]
    # openList.remove(currVertex)
    # closedList.append(currVertex)

    # minCostVert = min(costList, key=costList.get)
    # # print('open List')
    # # print(openList)
    # # openList.remove(minCostVert)
    # # closedList.append(minCostVert)
    # # print('closed list')
    # # print(closedList)
    # # continue
    # # print(costList)
    # # print(openList)
    # raw_input()
        # openList.append(adjacencyList[minCostVert])
        # print(edgeCost)
        # openList.remove(minCostVert)
        # closedList.append(minCostVert)
# pointer = []
# optimalList = []
# costList[startVert] = 0
# costList = {vertex:np.inf for vertex in vertexList}
# backPointer = {}
# pointer = []
# optimalList = []
