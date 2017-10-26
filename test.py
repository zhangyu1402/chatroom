from tkinter import *
tk =Tk()
frmMain = Frame(width=5000, height=5000, bg='white')
frmLT = Frame(frmMain, bg='red')
frmLC = Frame(frmMain, bg='green')
frmLB = Frame(frmLT, bg='black')
frmRT = Frame(frmLC, bg='yellow')
# frm1.pack()
# frm2.pack()
# frm3.pack()
# frm4.pack()
txtMsgList = Text(frmLT)
txtMsgList.tag_config('greencolor', foreground='#008C00')#创建tag
txtMsg = Text(frmLC)
#   txtMsg.bind("<KeyPress-Up>", sendMsgEvent)
btnSend = Button(frmLB, text='发 送', width = 8)
btnCancel = Button(frmLB, text='取消', width = 8)
imgInfo = PhotoImage(file = "python.gif")
lblImage = Label(frmRT, image = imgInfo)
lblImage.image = imgInfo

for t in [btnCancel,btnSend,lblImage,txtMsgList,txtMsg]:
    t.pack(side=LEFT)

tk.mainloop()