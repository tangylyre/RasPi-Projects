from keyboard import write
from keyboard import is_pressed as key
from keyboard import press_and_release as pr
from random import randrange
from time import sleep

f = open("adverbs.txt", "r")
adv = []
for line in f:
    adv.append(line.strip())
f.close()

f = open("adjectives.txt", "r")
adj = []
for line in f:
    adj.append(line.strip())
f.close()

f = open("nouns.txt", "r")
noun = []
for line in f:
    noun.append(line.strip())
f.close()

f = open("verbs.txt", "r")
verb = []
for line in f:
    verb.append(line.strip())
f.close()

print("starting spam..")
sleep(1)
q = False
while not q:
    radj = randrange(len(adj))
    radv = randrange(len(adv))
    rnoun = randrange(len(noun))
    rnoun2 = randrange(len(noun))
    rverb = randrange(len(verb))
    sleep(randrange(10))
    s = ("%s %s %s %s %s." % (noun[rnoun], adv[radv], verb[rverb], adj[radj], noun[rnoun2]))
    write(s)
    pr('Enter')
