#!/usr/bin/env python

import  read_file as rf
import matplotlib.pyplot as plt
import numpy as np
import contextlib

totNumVert, startVert, goalVert, i, j, cost = rf.read_file()

neighborList = []
tempEdgeList = []
tempCost_j = np.zeros(len(i))
costListSize = (totNumVert,totNumVert-1)
costList = np.ones(costListSize) * np.inf

for k in range(0,totNumVert-1):
    for vertIdx in range(0,totNumVert):
        vertexNum = vertIdx
        if vertIdx == 0:
            costList[vertIdx][k] = 0
        else:
            for edgeIdx in range(0,len(j)):
                curr_i = i[edgeIdx]
                curr_j = j[edgeIdx]
                if curr_i == vertexNum:
                    curr_j = j[edgeIdx]
                    tempCost_j[edgeIdx] = cost[edgeIdx] + costList[vertIdx-1][k-1]
                else:
                    tempCost_j[edgeIdx] = float('inf')

            costList[vertIdx][k] = min(tempCost_j)

print(costList)
raw_input()
file = open("output_1.txt","w")
np.savetxt('output_1.txt',costList)
file.close()
