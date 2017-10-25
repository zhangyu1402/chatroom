import socket
import time
import threading

mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


mySocket.connect(('localhost',5550))
mySocket.send(b'new')
print(mySocket.recv(1024).decode())



def check():
    while True:
        userName = input('Enter your nickname: ')
        print(userName)
        mySocket.send(userName.encode('utf-8'))
        check = mySocket.recv(1024).decode('utf-8')
        print(check)
        if check == 'username exist':
            # print("1")
            pass
        else:
            # print("success")
            break

def mySent():
    while True:
        try:
            myWord = input()
            mySocket.send(myWord.encode('utf-8'))
        except:
            print("fail to send")


def myRecv():
    while True:
        try:
            getMassage = mySocket.recv(1024).decode()
            print(getMassage)
        except:
            print("fail to recv")

check()

th1 = threading.Thread(target=mySent)
th2 = threading.Thread(target=myRecv)
threads = [th1, th2]

for t in threads:
    t.setDaemon(True)
    t.start()
t.join()