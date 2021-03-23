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


def getBanter():
    f = open("banter.txt", "r")
    banter = []
    for line in f:
        banter.append(line.strip())
    f.close()
    return banter


def reloadEpic():
    f = open("shitpost.txt", "r")
    epic = []
    for line in f:
        epic.append(line.strip())
    f.close()
    return epic


def makeCumbank():
    f = open("cum.txt", "r")
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


def makeStr(n, adj, verb, adv, noun, epic, conj, log):
    if n < 10:
        string, epic = makeRandPop(epic)
    elif n == 11:
        string = ("%s %s %s %s %s %s %s." % (
            makeRand(adj), makeRand(adj), makeRand(adj), makeRand(verb),
            makeRand(noun), makeRand(conj), makeRand(noun)))
    elif n == 12:
        string = ("%s %s %s %s %s." % (makeRand(noun), makeRand(adv), makeRand(verb), makeRand(adj), makeRand(noun)))
    elif n == 13:
        string = ("%s %s %s %s %s." % (makeRand(conj), makeRand(noun), makeRand(verb), makeRand(adj), makeRand(noun)))
    else:
        if len(log) == 0:
            string, epic = makeRandPop(epic)
        else:
            string = makeRand(log)

    return string, epic


def makeSmart(adj, adv, verb, noun, conj):
    n = randrange(1, 3)
    if n == 1:
        string = ("%s %s %s %s %s %s %s." % (
            makeRand(adj), makeRand(adj), makeRand(adj), makeRand(verb),
            makeRand(noun), makeRand(conj), makeRand(noun)))
    if n == 2:
        string = ("%s %s %s %s %s." % (makeRand(noun), makeRand(adv), makeRand(verb), makeRand(adj), makeRand(noun)))
    if n == 3:
        string = ("%s %s %s %s %s." % (makeRand(conj), makeRand(noun), makeRand(verb), makeRand(adj), makeRand(noun)))
    return string


def makeBanter(banter, u):
    if len(banter) == 0:
        banter = getBanter()
    x = randrange(len(banter))
    phrase = banter[x]
    banter.pop(x)
    if '%' in phrase:
        phrase = phrase.replace('%', u)
    return phrase, banter


def cumCheck(s, cumBank):
    orgasm = False
    for phrase in cumBank:
        if phrase in s:
            print(phrase)
            orgasm = True
    return orgasm


def chat(sock, CHAN, msg):
    m = "PRIVMSG {} :{}\r\n".format(CHAN, msg).encode("utf-8")
    sock.send(m)
    return


def storeResponse(m):
    f = open('banter.txt', 'r')
    repeat = False
    for line in f:
        if m in line:
            repeat = True
    if not repeat:
        f.close()
        f = open('banter.txt', 'a')
        f.write(m + '\n')
    f.close()
    return repeat


def deleteDictionary(m):
    words = m.replace('.', '').split(' ')
    print(words)
    files = ['conj.txt', 'nouns.txt', 'adverbs.txt', 'adjectives.txt', 'verbs.txt']
    for file in files:
        l = []
        f = open(file, 'r')
        for line in f:
            found = False
            for word in words:
                if word == line.replace('\n', ''):
                    print("word %s" % word)
                    print("matches line %s" % line)
                    print("in file %s" % file)
                    words.remove(word)
                    found = True
            if not found:
                l.append(line)
        f.close()
        f = open(file, 'w')
        for line in l:
            f.write(line)
        f.close()
    if len(words) <= 0:
        return True
    return False


def deletePhrase(m):
    files = ['chat.txt', 'shitpost.txt', 'banter.txt']
    found = False
    for file in files:
        l = []
        f = open(file, 'r')
        for line in f:
            if line.replace('\n', '') == m:
                print("Message %s \n" % m)
                print("Matches %s." % line.replace('\n', ''))
                found = True
            else:
                l.append(line)
        f.close()
        if found:
            print("Word was found in file %s." % file)
            f = open(file, 'w')
            for line in l:
                f.write(line)
            f.close()
            return file
    bool = deleteDictionary(m)
    if bool:
        print("words found in dictionary deleted.")
        return True
    print("Word in file not found.")
    return False


def makeAbout(phrase):
    files = ['chat.txt', 'shitpost.txt', 'banter.txt']
    found = False
    mbank = []
    for file in files:
        l = []
        f = open(file, 'r')
        for line in f:
            if phrase in line:
                found = True
                print("%s was found \nin %s" % (phrase, line))
                mbank.append(line.replace('\n', ''))
    if not found:
        m = "I dont know anything about %s" % phrase
    else:
        m = mbank[randrange(len(mbank))]
    return m


def phraseMutator(nPhrases):
    punctuation = ['.', ',', '?', '!', '\n']
    files = ['chat.txt', 'shitpost.txt']
    wordbank = []
    i = 0
    while i <= nPhrases:
        file = files[randrange(0, 2)]
        f = open(file, 'r')
        lines = f.readlines()
        phrase = lines[randrange(len(lines))]
        if '\x00' not in phrase:
            for x in punctuation:
                phrase = phrase.replace(x, '')
            words = phrase.split(" ")
            if len(words) > 1:
                print(words)
                for word in words:
                    wordbank.append(word)
                i += 1
    n = randrange(len(wordbank))
    newPhrase = wordbank[n]
    wordbank.pop(n)
    while len(wordbank) > 0:
        n = randrange(len(wordbank))
        toMerge = (newPhrase, wordbank[n])
        newPhrase = " ".join(toMerge)
        wordbank.pop(n)
    return newPhrase


def phraseInList(ls, phrase):
    result = False
    for element in ls:
        if element in phrase:
            result = True
    return result


def cheembisParser(s, nick, sock, channel, adj, adv, verb, noun, conj, banter, u, m, count):
    cumBank = makeCumbank()
    cumResponse = ['*cums*', '*ejaculates*', '*cries*', '*orgasms*']
    bedBank = ['time for bed %s' % nick, '%s time for bed' % nick]
    delBank = ['do not say that again %s' % nick, '%s do not say that again' % nick]
    promptBank = ['say something %s' % nick, '%s say something' % nick]
    smartBank = ['say something smart %s' % nick, '%s say something smart' % nick]
    aboutBank = ['%s say something about ' % nick, 'say something about ']
    newBank = ['%s say something new' % nick, 'say something new %s' % nick]
    detect = True
    q = False
    if phraseInList(bedBank, s):
        q = True
        chat(sock, channel, "cya nerds")
    elif phraseInList(newBank, s):
        m = phraseMutator(2)
        chat(sock, channel, m)
    elif phraseInList(delBank, s):
        chat(sock, channel, "ok libtard.")
        deletePhrase(m)
    elif phraseInList(smartBank, s):
        m = makeSmart(adj, adv, verb, noun, conj)
        chat(sock, channel, m)
    elif phraseInList(aboutBank, s):
        phrase = s.replace('%s say something about ' % nick, '').replace('say something about ', '')
        m = makeAbout(phrase)
        chat(sock, channel, m)
    elif phraseInList(promptBank, s):
        count = 0
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
    else:
        detect = False
    return m, detect, q, count


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
