from keyboard import write
from keyboard import is_pressed as key
from keyboard import press_and_release as pr
from keyboard import add_hotkey as hk
from random import randrange
from random import randint
from time import sleep


def getAdv():
    f = open("adverbs.txt", "r")
    adv = []
    for line in f:
        adv.append(line.strip())
    f.close()
    return adv


def getConj():
    f = open("adverbs.txt", "r")
    conj = []
    for line in f:
        conj.append(line.strip())
    f.close()
    return conj


def getAdj():
    f = open("adjectives.txt", "r")
    adj = []
    for line in f:
        adj.append(line.strip())
    f.close()
    return adj


def getNoun():
    f = open("nouns.txt", "r")
    noun = []
    for line in f:
        noun.append(line.strip())
    f.close()
    return noun


def getVerb():
    f = open("verbs.txt", "r")
    verb = []
    for line in f:
        verb.append(line.strip())
    f.close()
    return verb


def reloadEpic():
    f = open("shitpost.txt", "r")
    epic = []
    for line in f:
        epic.append(line.strip())
    f.close()
    return epic


def makeRand(lis):
    return lis[randrange(len(lis))]


def makeRandPop(lis):
    x = randrange(len(lis))
    string = lis[x]
    lis.pop(x)
    return string, lis


def makeDelay(d):
    return randrange(d) / 1000


def makeStr(n, adj, verb, adv, noun, epic, conj):
    if n < 2:
        string, epic = makeRandPop(epic)
    elif n == 3:
        string = ("%s %s %s %s %s %s %s." % (
            makeRand(adj), makeRand(adj), makeRand(adj), makeRand(verb),
            makeRand(noun), makeRand(conj), makeRand(noun)))
    elif n == 4:
        string = ("%s %s %s %s %s." % (makeRand(noun), makeRand(adv), makeRand(verb), makeRand(adj), makeRand(noun)))
    elif n == 5:
        string = ("%s %s %s %s %s." % (makeRand(conj), makeRand(noun), makeRand(verb), makeRand(adj), makeRand(noun)))

    return string, epic


def main():
    try:
        tn = int(input("choose sleep time min:\n"))
    except:
        tn = 30
    try:
        tx = int(input("choose sleep time max:\n"))
    except:
        tx = 180
    try:
        td = int(input("choose typing delay (ms):\n"))
    except:
        td = 180
    epic = reloadEpic()
    adj = getAdj()
    verb = getVerb()
    noun = getNoun()
    adv = getAdv()
    conj = getConj()
    print("beginning spam..")
    q = False
    while not q:
        t = randint(tn, tx)
        print("waiting %d" % t)
        sleep(t)
        if len(epic) == 0:
            epic = reloadEpic()
        s, epic = makeStr(randrange(5), adj, verb, adv, noun, epic, conj)
        write(s, makeDelay(td))
        pr('Enter')
        if key('Shift'):
            # hold shift to end loop.
            write('\n')
            print("Stopping!")
            q = True
    sleep(10)
    ip = input("(q)uit or (r)estart?\n")
    if ip == 'r':
        main()
    else:
        return


if __name__ == "__main__":
    main()
