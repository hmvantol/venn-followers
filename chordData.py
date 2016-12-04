from itertools import product

d = "/github/followers/"


poliList = ["JustinTrudeau", "pmharper", "ThomasMulcair", "ElizabethMay", "GillesDuceppe"]
label = ["Justin Trudeau", "Stephen Harper", "Thomas Mulcair", "Elizabeth May", "Gilles Duceppe"]

poliDict = {}

x = 0
for name in poliList:
	with open(d + name + ".txt", "r") as inFile:
		followers = inFile.read().split(",")
	del followers[-1]
	poliDict[label[x]] = followers
	x += 1

JT = []
for x in range(len(poliList)):
	if x != 0:
		JT.append(len(set(poliDict[label[0]]).intersection(poliDict[label[x]])))
	if x == 0:
		JT.append(len(set(poliDict[label[0]]).difference(set(poliDict[label[1]]) | set(poliDict[label[2]]) | set(poliDict[label[3]]) | set(poliDict[label[4]]))))
print JT


SH = []
for x in range(len(poliList)):
	if x != 1:
		SH.append(len(set(poliDict[label[1]]).intersection(poliDict[label[x]])))
	if x == 1:
		SH.append(len(set(poliDict[label[1]]).difference(set(poliDict[label[0]]) | set(poliDict[label[2]]) | set(poliDict[label[3]]) | set(poliDict[label[4]]))))
print SH

TM = []
for x in range(len(poliList)):
	if x != 2:
		TM.append(len(set(poliDict[label[2]]).intersection(poliDict[label[x]])))
	if x == 2:
		TM.append(len(set(poliDict[label[2]]).difference(set(poliDict[label[0]]) | set(poliDict[label[1]]) | set(poliDict[label[3]]) | set(poliDict[label[4]]))))
print TM

EM = []
for x in range(len(poliList)):
	if x != 3:
		EM.append(len(set(poliDict[label[3]]).intersection(poliDict[label[x]])))
	if x == 3:
		EM.append(len(set(poliDict[label[3]]).difference(set(poliDict[label[0]]) | set(poliDict[label[1]]) | set(poliDict[label[2]]) | set(poliDict[label[4]]))))
print EM

GD = []
for x in range(len(poliList)):
	if x != 4:
		GD.append(len(set(poliDict[label[4]]).intersection(poliDict[label[x]])))
	if x == 4:
		GD.append(len(set(poliDict[label[4]]).difference(set(poliDict[label[0]]) | set(poliDict[label[1]]) | set(poliDict[label[2]]) | set(poliDict[label[3]]))))
print GD
