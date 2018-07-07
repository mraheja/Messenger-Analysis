from fbchat import log, Client
from fbchat.models import *

def login(email,password):
    return Client(email,password)

def inputCredentials():
    email = str(input("Email \n"))
    password = str(input("Password \n"))
    return email,password

def logout(client):
    client.logout()
    
def idList(client):
    ids = {}
    for e in client.fetchAllUsers():
        ids[str(e.name)] = str(e.uid)
    return ids

def mostCommonWords(messengerID):
    data = {}
    for e in client.fetchThreadMessages(messengerID,limit=10000):
        try:
            words = [x.lower() for x in e.text.split(" ")]
            for word in words:
                if word in data:
                    data[word] = data[word]+1
                else:
                    data[word] = 1
        except:
            p = 1
        
    return sorted([(data[e],e) for e in data])[::-1]

email,password = inputCredentials()
client = login(email, password)

ids = idList(client)
while(True):
    name = str(input("Enter Name \n"))
    messengerID = int(ids[name])
    
    mostCommon = mostCommonWords(messengerID)

    for i in range(min(len(mostCommon),100)):
        try:
            print(str(mostCommon[i][1]) + " " + str(mostCommon[i][0]))
        except:
            lol = 1
    print()

logout(client)
