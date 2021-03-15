import socket
import time
import random
import tkinter
from tkinter import filedialog

from idiot import *

epic = reloadEpic()
adj = getAdj()
verb = getVerb()
noun = getNoun()
adv = getAdv()
conj = getConj()
banter = getBanter()
cumBank = makeCumbank()
cumResponse = ['*cums*', '*ejaculates*', '*cries*', '*orgasms*']

f = open(filedialog.askopenfilename(title="Select a Bot Profile",
                                    filetypes=(("Text files",
                                                "*.txt*"),
                                               ("all files",
                                                "*.*"))))
print(f)
if f == '':
    f = open("cheembisProfile.txt")

instance = []
i = 0
for line in f:
    instance.append(line.split()[0])
    i += 1
    if i >= 8:
        break
f.close()

server = instance[0]
port = int(instance[1])
nick = instance[2]
token = instance[3]
channel = instance[4]
to = int(instance[5])
countMin = int(instance[6])
countMax = int(instance[7])

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nick}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))
sock.settimeout(to)

log = open('chat.txt', 'r')
logLs = []

for line in log:
    if line != '\n':
        logLs.append(line.replace('\n', ''))
log.close()

q = False
count = random.randint(countMin, countMax)
m, epic = makeStr(randrange(20), adj, verb, adv, noun, epic, conj, logLs)
chat(sock, channel, m)
while not q:
    print(count)
    s = ''
    try:
        resp = sock.recv(2048).decode('utf-8')
    except socket.timeout:
        resp = ''
    l = resp.split(':')
    if len(l) >= 2 and '!' in l[1]:
        u = l[1].split('!')[0]
        s = l[2].replace('\n', '').replace('\r', '').lower()
        if 'twitch.tv' in s or 'Welcome, GLHF!' in s:
            s = ''
    if 'time for bed %s' % nick in s:
        q = True
        chat(sock, channel, "cya nerds")
    elif 'do not say that again %s' % nick in s:
        chat(sock, channel, "ok libtard.")
        fileRevise = deletePhrase(m)
        print('%s was found in %s' % m, fileRevise)
    elif cumCheck(s, cumBank):
        m = cumResponse[randrange(len(cumResponse))]
        chat(sock, channel, m)
    elif nick in s:
        m, banter = makeBanter(banter, u)
        rp = storeResponse(s.replace(nick, '%'))
        if rp:
            chat(sock, channel, ('come up with something new, %s' % u))
        else:
            chat(sock, channel, m)
    elif len(s) > 2:
        unique = True
        for phrase in logLs:
            if s in phrase:
                unique = False
        if unique:
            logLs.append(s)
    count -= 1
    if count <= 0:
        if len(epic) == 0:
            epic = reloadEpic()
        m, epic = makeStr(randrange(20), adj, verb, adv, noun, epic, conj, logLs)
        chat(sock, channel, m)
        count = random.randint(countMin, countMax)

print("Signing off...")
log = open('chat.txt', 'w')
for line in logLs:
    log.write(line.replace('\n', '') + '\n')
log.close()
sock.close()
print("logs written, remember to double check!")
