#!/usr/bin/env python

def read_file():
    import tkFileDialog
    import numpy as np
    # Declaration

    adjacencyList = {}
    edgeCost = {}
    #
    inputFilename = tkFileDialog.askopenfilename(initialdir = "/home/sena/VT-robot-motion-planning-course/F2018-HW/HW2/problem1_inputfiles",
                                    title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
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
