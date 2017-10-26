from tkinter import *
import time
import threading
import socket
# import test_client


# class login(tk.Frame):

def login():
    def loginsent():
        mySocket.send(entry1.get().encode())
        check = mySocket.recv(1024).decode()
        if  check== 'username exist':
            var2.set(check)
        else:
            login.destroy()
            # var2.set(check+'false')
    login = Tk();login.title("登陆")
    # f0 = Frame(login)
    f1 = Frame(login,width=500,height=300);f1.pack()
    f2 = Frame(login);f2.pack()
    f3 = Frame(login);f3.pack()
    Label(f1,text="用户名").pack(side=LEFT)
    var = StringVar()
    entry1 = Entry(f1,textvariable=var)
    entry1.pack(side=LEFT)
    var2 = StringVar()
    messagebox = Message(f3,text='请输入用户名',width=200,textvariable=var2)
    messagebox.pack()
    button = Button(f2, text='login', width = 8, command=loginsent)
    button.pack()
    login.mainloop()

    


mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySocket.connect(('10.15.85.94',5550))
mySocket.send(b'new')
print(mySocket.recv(1024).decode())

name_buff = []
massage_buff = []


def check():
    while True:
        userName = input('Enter your nickname: ')
        print(userName)
        mySocket.send(userName.encode('utf-8'))
        check = mySocket.recv(1024).decode('utf-8')
        print(check)
        if check == 'username exist':
            pass
        else:
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
            name,Massage = getMassage.split()
            name_buff.append(name)
            massage_buff.append(Massage)
            print(getMassage)
            # return getMassage
        except:
            print("fail to recv")



def mymain():
  def sendMsg():#发送消息
    strMsg = '我:' + time.strftime("%Y-%m-%d %H:%M:%S",
                                  time.localtime()) + '\n '
    txtMsgList.insert(END, strMsg, 'greencolor')
    txtMsgList.insert(END, txtMsg.get('0.0', END))
    mySocket.send(txtMsg.get('0.0', END).encode())
    txtMsg.delete('0.0', END)
      
  def cancelMsg():#取消消息
    txtMsg.delete('0.0', END)

  def sendMsgEvent(event): #发送消息事件
    if event.keysym == "Up":

      sendMsg()

  def refresh():
    # print(buff)
    if name_buff:
      strMsg = name_buff.pop()+':' + time.strftime("%Y-%m-%d %H:%M:%S",
                                  time.localtime()) + '\n '
      txtMsgList.insert(END, strMsg, 'greencolor')
      txtMsgList.insert(END,massage_buff.pop()+'\n')
    t.after(1000,refresh)

  #创建窗口 
  t = Tk()
  t.title('聊天室')
        
  #创建frame容器
#   frmMain = Frame(width=500, height=320, bg='white')



  frmLT = Frame(width=500, height=320, bg='green')
  frmLC = Frame(width=500, height=150, bg='white')
  frmLB = Frame(width=500, height=30)
  frmRT = Frame(width=200, height=500)
    
  #创建控件
  txtMsgList = Text(frmLT)
  txtMsgList.tag_config('green', foreground='#008C00')#创建tag
  txtMsg = Text(frmLC)
  txtMsg.bind("<KeyPress-Up>", sendMsgEvent)
  btnSend = Button(frmLB, text='发 送', width = 8, command=sendMsg)
  btnCancel = Button(frmLB, text='取消', width = 8, command=cancelMsg)
  imgInfo = PhotoImage(file = "python.gif")
  lblImage = Label(frmRT, image = imgInfo)
  lblImage.image = imgInfo

  #窗口布局
  frmLT.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
  frmLC.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
  frmLB.grid(row=2, column=0, columnspan=2)
  frmRT.grid(row=0, column=2, rowspan=3, padx=2, pady=3)
  #固定大小
  frmLT.grid_propagate(0)
  frmLC.grid_propagate(0)
  frmLB.grid_propagate(0)
  frmRT.grid_propagate(0)
    
  btnSend.grid(row=2, column=0)
  btnCancel.grid(row=2, column=1)
  lblImage.grid()
  txtMsgList.grid()
  txtMsg.grid()
#   for t in [btnCancel,btnSend,lblImage,txtMsgList,txtMsg]:
#       t.pack(side=LEFT)
  t.after(1000,refresh)
  
  #主事件循环
  t.mainloop()


login()
th2 = threading.Thread(target=myRecv)
th2.setDaemon(True)
th2.start()
mymain()




 
