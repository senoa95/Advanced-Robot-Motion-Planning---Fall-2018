#!/usr/bin/env python

import numpy as np

def read_files(graphNumber):
    fileDir = "/home/sena/VT-robot-motion-planning-course/F2018-HW/HW2-Submission/Problem2/"
    input_1Dir = fileDir + "input_1.txt"
    input_2Dir = fileDir + "input_2.txt"
    input_3Dir = fileDir + "input_3.txt"
    coords_1Dir = fileDir + "coords_1.txt"
    coords_2Dir = fileDir + "coords_2.txt"
    coords_3Dir = fileDir + "coords_3.txt"

    if graphNumber == 0:
        coordFile = open(coords_1Dir,"r")
        coordFileContent = coordFile.readlines()
        totNumVert, startVert, goalVert, adjacencyList, edgeCost = read_input(input_1Dir)
        euclideanDist = euclidean_distance(adjacencyList,coordFileContent,goalVert)

    elif graphNumber == 1:
        coordFile = open(coords_2Dir,"r")
        coordFileContent = coordFile.readlines()
        totNumVert, startVert, goalVert, adjacencyList, edgeCost = \
        read_input(input_2Dir)
        euclideanDist = euclidean_distance(adjacencyList,coordFileContent,goalVert)
    elif graphNumber == 2:
        coordFile = open(coords_3Dir,"r")
        coordFileContent = coordFile.readlines()
        totNumVert, startVert, goalVert, adjacencyList, edgeCost = \
        read_input(input_3Dir)
        euclideanDist = euclidean_distance(adjacencyList,coordFileContent,goalVert)

    return totNumVert, startVert, goalVert, adjacencyList, edgeCost, euclideanDist

def read_input(inputFilename):
    # Declaration

    adjacencyList = {}
    edgeCost = {}

    inputFile = open(inputFilename,"r")
    inputFileContent = inputFile.readlines()

    totNumVert = int(inputFileContent[0])
    startVert = int(inputFileContent[1])
    goalVert = int(inputFileContent[2])
    for counter in range(3,len(inputFileContent)):
        curr = inputFileContent[counter].split()
        if int(curr[0]) not in adjacencyList:
            adjacencyList[int(curr[0])] = []
        adjacencyList[int(curr[0])].append(int(curr[1]))
        edgeCost[tuple([int(curr[0]),int(curr[1])])] = float(curr[2])

    return totNumVert, startVert, goalVert, adjacencyList, edgeCost


def euclidean_distance(adjacencyList,coordFileContent, goalVert):
    euclideanDist = {}
    vertexList = sorted(list(adjacencyList.keys()))
    goal = coordFileContent[goalVert].split()

    for counter in range(len(coordFileContent)):
        currCoord = coordFileContent[counter].split()
        goalX = float(goal[0])
        goalY = float(goal[1])
        currX = float(currCoord[0])
        currY = float(currCoord[1])
        # if vertexList[counter] not in euclideanDist:
        #     euclideanDist[vertexList[counter]] = []
        euclideanDist[vertexList[counter]] = np.sqrt(np.square(goalX - currX) + np.square(goalY - currY))
    return euclideanDist
