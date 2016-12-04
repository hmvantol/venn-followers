import itertools, collections, json

d = "/github/followers/"


poliList = ["JustinTrudeau", "pmharper", "ThomasMulcair", "ElizabethMay"]
label = ["Justin Trudeau", "Stephen Harper", "Thomas Mulcair", "Elizabeth May"]

poliDict = {}

x = 0
for name in poliList:
	with open(d + name + ".txt", "r") as inFile:
		followers = inFile.read().split(",")
	del followers[-1]
	x += 1
	poliDict[x] = followers



sets = []

for x in range(1,5):
	combo = itertools.combinations(range(4), x)
	sets.append([list(i) for i in combo])

sets = list(itertools.chain.from_iterable(item if isinstance(item,collections.Iterable) and not isinstance(item, basestring) else [item] for item in sets))



size = []

for x in range(4):
	size.append(len(poliDict[sets[x][0]+1]))

for y in range(4,10):
	size.append(len(set(poliDict[sets[y][0]+1]).intersection(poliDict[sets[y][1]+1])))

for z in range(10,14):
	size.append(len(set(poliDict[sets[z][0]+1]).intersection(poliDict[sets[z][1]+1], poliDict[sets[z][2]+1])))

for a in range(14, 15):
	size.append(len(set(poliDict[sets[a][0]+1]).intersection(poliDict[sets[a][1]+1], poliDict[sets[a][2]+1], poliDict[sets[a][3]+1])))




print 'var sets = ['
for i in range(4):
	print '         {"sets": ' + str(sets[i]) + ', "label": "' + label[i] + '", "size": ' + str(size[i]) + '},'
for i in range(4,len(sets)):
	print '         {"sets": ' + str(sets[i]) + ', "size": ' + str(size[i]) + '},'
print '];'

