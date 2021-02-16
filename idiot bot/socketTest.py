import socket
import time


def chat(sock, CHAN, msg):
    sock.send("PRIVMSG #{} :{}\r\n".format(CHAN, msg).encode("utf-8"))
    return


n = input("please input the text file to read from:\n")
try:
    f = open(n)
except:
    f = open("instance.txt")
instance = []
i = 0
for line in f:
    instance.append(line.split()[0])
    i += 1
    if i >= 5:
        break
f.close()
server = instance[0]
port = int(instance[1])
nick = instance[2]
token = instance[3]
channel = instance[4]
sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nick}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))
while True:
    resp = sock.recv(2048).decode('utf-8')
    l = resp.split(':')
    u = l[1].split('!')[0]
    print(u)
    s = l[2]
    if 'tmi.twitch.tv' in s or 'Welcome, GLHF!' in s:
        s = ''
    print(s)
    chat(sock, channel, "test")
    time.sleep(1)
