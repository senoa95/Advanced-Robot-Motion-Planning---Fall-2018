#!/usr/bin/env python

import  read_input_files as rif
import test
import matplotlib.pyplot as plt
import numpy as np
import contextlib

algorithmNames = {'Dijkstra', 'A*'}
numiters =  np.zeros((3,2))
totalCost = np.zeros((3,2))

print('Please replace the value of fileDir in "read_input_files.py" by the\
 full directory path of the location of this script on your machine before execution.')
raw_input()

for fileNum in range(3):
    for currAlgorithm in algorithmNames:
        if currAlgorithm == 'A*':
            gamma = 1
            algorithm = 1
        else:
            gamma = 0
            algorithm = 0
        [totNumVert,
        startVert,
        goalVert,
        adjacencyList,
        edgeCost,
        euclideanDist] = rif.read_files(fileNum)
        # print(euclideanDist)
        # raw_input()
        vertexList = sorted(list(adjacencyList.keys()))
        costList = {vertex:np.inf for vertex in vertexList}
        globalCostList = {}
        openList = []
        closedList = set()

        openList.append(startVert)
        costList[startVert] = 0
        globalCostList[startVert] = 0

        while goalVert not in closedList:

            bestCurrVertex = sorted(costList.iteritems(),
                key=lambda (k,v): (v,k))
            currVertex = bestCurrVertex[0][0]
            if currVertex in closedList:
                openList.remove(currVertex)
                del costList[currVertex]
                continue

            for adjacentVertex in adjacencyList[currVertex]:
                if adjacentVertex not in openList and adjacentVertex not in closedList:
                    openList.append(adjacentVertex)
                    edgeWeight = edgeCost[tuple([currVertex,adjacentVertex])]
                    tempCost = edgeWeight + costList[currVertex] \
                    + gamma*euclideanDist[adjacentVertex]
                    tempCost2 = edgeWeight + globalCostList[currVertex]

                    # print(adjacentVertex)
                    # raw_input()
                    if costList[adjacentVertex] > tempCost:
                        costList[adjacentVertex] = tempCost
                        globalCostList[adjacentVertex] = tempCost2
                    # backPointer[adjacentVertex] = currVertex
                # costList[adjacentVertex] =\
                #  edgeCost[tuple([currVertex,adjacentVertex])]\
                # + globalCostList[currVertex] + gamma*euclideanDist[adjacentVertex]
                # globalCostList[adjacentVertex] = costList[adjacentVertex]
                # print(costList)
                # raw_input()
                    if adjacentVertex == goalVert:
                        totalCost[fileNum][algorithm] = globalCostList[currVertex]
                        print(globalCostList[currVertex])
                else:
                    continue
            openList.remove(currVertex)
            closedList.add(currVertex)
            del costList[currVertex]
        print([currAlgorithm] + ['Number of Iterations'])
        print(len(closedList))
        numiters[fileNum][algorithm] = len(closedList)

print(totalCost)
file = open("output_numiters.txt","w")
np.savetxt('output_numiters.txt',numiters,fmt='%4d')
file.close()

file = open("output_costs.txt","w")
np.savetxt('output_costs.txt',totalCost,fmt='%4d')
file.close()
