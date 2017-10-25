import socket
import threading

socket_dic ={}

mySocket =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mySocket.bind(("localhost",5550))
mySocket.listen(5)


def broadcast(myName,content):
    for sockName in socket_dic.keys():
        if sockName != myName:
            try:
                socket_dic[sockName].sendall(whatToSay.encode())
            except:
                pass

def init(mySocket):
    global userName
    while True:
        userName = mySocket.recv(1024).decode()
        if userName in socket_dic:
            mySocket.send(b'username exist')
            # print("username exist")
        else:
            mySocket.send(b'username accept')
            # print("break")
            break
    socket_dic[userName] = mySocket

def addThreadIn(mySocket):
    
    init(mySocket)

    print(userName+"jion")
    broadcast(userName,userName+'join')
    while True:
        try:
            massage = mySocket.recv(1024).decode()
            if massage:
                
                broadcast(userName,massage)
                print(userName+"say"+massage)
        except:
            try:
                socket_dic.remove(userName)
            except:
                pass
            # print(mydict[connNumber],'has exited,',len(mylist), ' person left')
            print("shuo hua")
            broadcast(userName,userName+'leaved')
            mySocket.close()
while True:
    connection, addr = mySocket.accept()
    try:
        buf = connection.recv(1024).decode()
        print(buf)
        if buf == 'new':
            connection.sendall(b'welcome to server!')

            #new thread
            mythread = threading.Thread(target=addThreadIn, args=(connection,))
            mythread.setDaemon(True)
            mythread.start()

        else:
            connection.send(b'please go out!')
            connection.close()
    
    except:
        pass