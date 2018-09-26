#!/usr/bin/env python

import read_input_file as rif

def read_files(graphNumber):
    fileDir = "/home/sena/VT-robot-motion-planning-course/F2018-HW/HW2/Problem 2/problem2_inputfiles/"
    input_1Dir = fileDir + "input_1.txt"
    input_2Dir = fileDir + "input_2.txt"
    input_3Dir = fileDir + "input_3.txt"
    coords_1Dir = fileDir + "coords_1.txt"
    coords_2Dir = fileDir + "coords_2.txt"
    coords_3Dir = fileDir + "coords_3.txt"

    if graphNumber == 0:
        coordFile = open(coords_1Dir,"r")
        coordFileContent = coordFile.readlines()
        totNumVert, startVert, goalVert, adjacencyList, edgeCost = rif.read_input(input_1Dir)
    elif graphNumber == 1:
        coordFile = open(coords_2Dir,"r")
        coordFileContent = coordFile.readlines()
        totNumVert, startVert, goalVert, adjacencyList, edgeCost = \
        rif.read_input(input_2Dir)
    elif graphNumber == 2:
        coordFile = open(coords_3Dir,"r")
        coordFileContent = coordFile.readlines()
        totNumVert, startVert, goalVert, adjacencyList, edgeCost = \
        rif.read_input(input_3Dir)

    return totNumVert, startVert, goalVert, adjacencyList, edgeCost, coordFileContent

def euclidean_distance(adjacencyList,coordFileContent):
    for counter in range(len(coordFileContent)):
        currCoord = coordFileContent[counter].split()
        currX = currCoord[0]
        currY = currCoord[1]
        euclideanDist =
    vertexList = sorted(list(adjacencyList.keys()))
    print(fileContent[1])
