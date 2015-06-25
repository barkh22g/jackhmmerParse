#! /usr/bin/python

#Created by G. Barkhuff
#June 2015
#Method to parse jackhmmer result, after
#Manually deleting file to only contain final iteration results.

def jackhmmerParse(domain, jackhmmerFile):
	#dictionary to hold all hits and info
	resultingDict = {}
	#dict to hold currentHit,
	#to be nested inside resultingDict
	currentHit = {"gi":"x"}
	#holder for sequence
	currentSequence = ""

	#open file for reading only
	f = open(jackhmmerFile, "r")

	#read line by line
	lineList = f.readlines()
	for line in lineList:
		if line.startswith(">>"):
			#put last sequence into dictionary
			currentHit["sequence"] = currentSequence.replace("-", "")
			#save last hit to resultingDict
			resultingDict[currentHit["gi"]] = currentHit
			#empty currentHit dict except for domain
			currentHit = {"domain": domain}
			#strip extra stuff from gi
			strippedA = line.lstrip(">> ")
			strippedB = strippedA.rstrip("\n")
			strippedC = strippedB.strip()
			#put gi in dictionary
			currentHit["gi"] = strippedC
			#empty string to hold new sequence
			currentSequence = ""

		#if line is the important info line
		elif line.startswith("   1 !") or line.startswith("   1 ?"):
			#note: splits into 16 elements
			splitLine = line.split()
			#get startLocation, endLocation
			start = splitLine[9]
			end = splitLine[10]
			#put into dictionary
			currentHit["start"] = start
			currentHit["end"] = end

			#if line displaying sequence
		elif line.startswith("  " + currentHit["gi"]):
			#split line
			splitLine = line.split()
			currentSequence += splitLine[2].upper()
	return resultingDict




		




