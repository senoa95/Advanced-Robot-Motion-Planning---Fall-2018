#!/usr/bin/env python

import  read_input_files as rif
import test
import matplotlib.pyplot as plt
import numpy as np
import contextlib

algorithmNames = {'Dijkstra', 'A*'}
numiters =  np.zeros((3,2))
totalCost = np.zeros((3,2))

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
        openList = []
        closedList = set()

        openList.append(startVert)
        costList[startVert] = 0

        while goalVert not in closedList:

            bestCurrVertex = sorted(costList.iteritems(),
                key=lambda (k,v): (v,k))
            currVertex = bestCurrVertex[0][0]
            if currVertex in closedList:
                openList.remove(currVertex)
                del costList[currVertex]
                continue

            for adjacentVertex in adjacencyList[currVertex]:
                if adjacentVertex not in openList:
                    openList.append(adjacentVertex)
                costList[adjacentVertex] =\
                 edgeCost[tuple([currVertex,adjacentVertex])]\
                + costList[currVertex] + gamma*euclideanDist[adjacentVertex]
                # print(costList)
                # raw_input()
                if currVertex == goalVert:
                    totalCost[fileNum][algorithm] = costList[currVertex]
            openList.remove(currVertex)
            closedList.add(currVertex)
            del costList[currVertex]
        print([currAlgorithm] + ['Number of Iterations'])
        print(len(closedList))
        # print(totalCost)
        numiters[fileNum][algorithm] = len(closedList)

file = open("output_numiters.txt","w")
np.savetxt('output_numiters.txt',numiters,fmt='%4d')
file.close()

file = open("output_costs.txt","w")
np.savetxt('output_costs.txt',totalCost,fmt='%4d')
file.close()
