#!/usr/bin/env python

def read_file():
    import tkFileDialog
    import numpy as np
    # Declaration

    adjecencyList = {}
    edgeCost = {}
    #
    inputFilename = tkFileDialog.askopenfilename(initialdir = "/home/sena/VT-robot-motion-planning-course/F2018-HW/HW2/problem1_inputfiles",
                                    title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    inputFile = open(inputFilename,"r")
    inputFileContent = inputFile.readlines()
    #print(len(inputFileContent))
    totNumVert = int(inputFileContent[0])
    startVert = int(inputFileContent[1])
    goalVert = int(inputFileContent[2])
    for counter in range(3,len(inputFileContent)):
        curr = inputFileContent[counter].split()
        adjecencyList[int(curr[0])] = {int(curr[1])}
        costList[adjecencyList[int(curr[0])]] = {float(curr[2])}
        # i.append(int(float(curr[0])))
        # j.append(int(float(curr[1])))
        # cost.append(int(float(curr[2])))

    return [totNumVert, startVert, goalVert, i, j, cost]
# read_file()
