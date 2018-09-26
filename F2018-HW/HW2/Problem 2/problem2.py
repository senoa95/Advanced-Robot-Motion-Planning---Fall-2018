#!/usr/bin/env python

import  read_input_files as rif
import test
import matplotlib.pyplot as plt
import numpy as np
import contextlib

for fileNum in range(3):
    totNumVert, startVert, goalVert, adjacencyList, edgeCost, euclideanDist = rif.read_files(0)
    print(euclideanDist)
    raw_input()
    vertexList = sorted(list(adjacencyList.keys()))
    costList = {vertex:np.inf for vertex in vertexList}
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
    print('Dijkstra Number of Iterations')
    print(len(closedList))
