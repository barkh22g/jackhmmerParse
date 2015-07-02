#! /usr/bin/python

# Created by G. Barkhuff
# June 2015
# Method to parse jackhmmer hmm3-text result, after
# Manually deleting file to only contain final iteration results.

def jackhmmerParse(domain, jackhmmerFile):
    #dictionary to hold all hits and info
    resultingDict = {}
    #temp hit
    currentHit = {"gi":"x"}
    #temp sequence
    currentSequence = ""
    #temp currentGI
    currentGI = "$"

    
    #open file for reading only
    f = open(jackhmmerFile, "r")

    #read line by line
    lineList = f.readlines()
    for line in lineList:
        #strip, split to use later
        strippedLine = line.strip().split()

        if line.startswith(">>"):
            #hold GI
            currentGI = strippedLine[1]

        if line.strip().startswith("=="):
            #save last sequence to currentHit dict
            currentHit["sequence"] = currentSequence.replace("-", "").upper()
            #save last hit to resultingDict
            resultingDict[currentHit["gi"]] = currentHit

            #empty currentHit except domain
            currentHit = {"domain": domain}
            #empty seq variable
            currentSequence = ""

            #update domain number
            currentHit["gi"] = currentGI + "_" + strippedLine[2]
            #update bit score
            currentHit["score"] = strippedLine[4]

        if line.strip().startswith(currentGI):
            #if start is empty
            if "start" not in currentHit:
                currentHit["start"] = strippedLine[1]
            #update end value
            currentHit["end"] = strippedLine[3]
            #append sequence
            currentSequence += strippedLine[2]
    #del temp hit
    del resultingDict["x"]
    print "Done parsing."
    return resultingDict

