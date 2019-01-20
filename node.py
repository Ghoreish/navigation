import os
import time


def nodedict(f):
    nodesign = f.read(1)
    mydict = {}
    counter = 0
    x = 0
    y = 0
    while nodesign:
        if nodesign == "\n":
            zum = counter
            counter = 0
            x = 0
            y += 1
        else:
            mydict.update({(x, y): nodesign})
            x += 1
            counter += 1
        nodesign = f.read(1)
    return mydict, zum


def nodeway(x):
    mydict = {}
    wall = ["#", "+", "|", "-"]
    for i in x:
        mydict.update({i: []})
        if x[i] not in wall:
            if (i[0] - 1, i[1]) in x and x[(i[0] - 1, i[1])] not in wall:
                mydict[i].append((i[0] - 1, i[1]))
            if (i[0] + 1, i[1]) in x and x[(i[0] + 1, i[1])] not in wall:
                mydict[i].append((i[0] + 1, i[1]))
            if (i[0], i[1] - 1) in x and x[(i[0], i[1] - 1)] not in wall:
                mydict[i].append((i[0], i[1] - 1))
            if (i[0], i[1] + 1) in x and x[(i[0], i[1] + 1)] not in wall:
                mydict[i].append((i[0], i[1] + 1))
        if mydict[i] == []:
            mydict.pop(i)
    return mydict


def wazer(no, dic):
    used = []
    l1 = []
    l2 = []
    used.append(no)
    for i in dic[no]:
        l2.append([no, i])
    l1 = l2
    while True:
        for i in l1:
            for j in dic[i[-1]]:
                if j not in used:
                    used.append(j)
                    l2.append(i + [j])
        if l1 == l2:
            return l2
        else:
            l1 = l2


def navig(x1, y1, x2, y2, file):
    ndict, zum = nodedict(file)
    nodew = nodeway(ndict)
    l1 = wazer((x1, y1), nodew)
    for i in l1:
        if i[-1] == (x2, y2):
            r = i
    j = 0
    for k in r:
        time.sleep(0.1)
        os.system("clear")
        for i in ndict:
            j += 1
            if i == k:
                if j % zum == 0:
                    print("X")
                else:
                    print("X", end="")
            else:
                if j % zum == 0:
                    print(ndict[i])
                else:
                    print(ndict[i], end="")

l=os.listdir()
for i in range(0,len(l)):
    print(i+1,l[i])
inp=input("enter number of map file: ")
f = open(l[int(inp)-1], "r")
node = f.read(1)
x = 0
y = 0
while node:
    if node == "s":
        x1 = x
        y1 = y
    if node == "e":
        x2 = x
        y2 = y
    x += 1
    if node == "\n":
        x = 0
        y += 1
    node = f.read(1)
f.close()
f = open(l[int(inp)-1], "r")
navig(x1, y1, x2, y2, f)
