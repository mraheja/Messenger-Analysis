from fbchat import log, Client
from fbchat.models import *
import sys

try:
    file = open("credentials.txt",'r')
    x = file.read().split("\n")
    email = x[0]
    passs = x[1]
    client = Client(str(email), str(passs))

ids = {}
for e in client.fetchAllUsers():
    ids[str(e.name)] = str(e.uid)

name = sys.argv[1]
curid = int(ids[name])

words = {}
text = ""
for e in client.fetchThreadMessages(curid,limit=10000):
    try:
        text += e.text
        text += '\n'
	#	author = e.author
        curwords = e.text.split(" ")
        lowerwords = [x.lower() for x in curwords]
        for f in lowerwords:
            if f in words:
                words[f] = words[f]+1
            else:
                words[f] = 1
    except:
        p = 1
    
temp = []
for e in words:
    temp.append((words[e],e))

temp = sorted(temp)[::-1]

for i in range(0,min(len(temp),100)): print(str(temp[i][1]) + " " + str(temp[i][0]))

client.logout()

