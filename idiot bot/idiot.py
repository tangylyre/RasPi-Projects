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

f = open("adverbs.txt", "r")
conj = []
for line in f:
    conj.append(line.strip())
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


def makeRand(lis):
    return lis[randrange(len(lis))]
def makeDelay():
    return randrange(150)/1000

def makeStr(n, adj, verb, adv, noun):
    if n < 1:
        string = "crikey!"
    elif n == 1:
        string = ("%s %s %s %s %s %s %s." % (
            makeRand(adj), makeRand(adj), makeRand(adj), makeRand(verb),
            makeRand(noun), makeRand(conj), makeRand(noun)))
    elif n == 2:
        string = ("%s %s %s %s %s." % (makeRand(noun), makeRand(adv), makeRand(verb), makeRand(adj), makeRand(noun)))
    elif n == 3:
        string = ("%s %s %s %s %s." % (makeRand(conj), makeRand(noun), makeRand(verb), makeRand(adj), makeRand(noun)))

    return string


while not q:
    if key('q'):
        write('\n')
        print("Stopping!")
        q = True
    sleep(randrange(50))
    s = makeStr(randrange(3), adj, verb, adv, noun)
    write(s, makeDelay())
    pr('Enter')
