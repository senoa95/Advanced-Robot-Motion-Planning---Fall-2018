#!/usr/bin/env python

import  read_file as rf
import matplotlib.pyplot as plt
import numpy as np
import contextlib

totNumVert, startVert, goalVert, adjacencyList, edgeCost = rf.read_file()
vertexList = sorted(list(adjacencyList.keys()))
costList = {vertex:np.inf for vertex in vertexList}
backPointer = {}
pointer = []
optimalList = []

costList[startVert] = 0

for i in range(totNumVert-1):
    for j in range(totNumVert):
            currVertex = vertexList[j]
            if costList[currVertex] == np.inf:
                continue
            for adjecentVertex in adjacencyList[currVertex]:
                edgeWeight = edgeCost[tuple([currVertex,adjecentVertex])]
                tempCost = edgeWeight + costList[currVertex]
                print(adjacencyList[currVertex])
                raw_input()
                if costList[adjecentVertex] > tempCost:
                    costList[adjecentVertex] = tempCost
                    backPointer[adjecentVertex] = currVertex
                    optimalList.append(costList[adjecentVertex])

tempPointer = goalVert
pointer.append(tempPointer)
# print(len(backPointer))
while tempPointer != startVert:
    tempPointer = backPointer[tempPointer]
    pointer.append(tempPointer)

pointer = sorted(pointer)
