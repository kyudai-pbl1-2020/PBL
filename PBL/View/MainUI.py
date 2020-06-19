import tkinter as tk
import time

WID = 10

class MainUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid()
        
        #picの代わり
        pic = tk.Canvas(width = 100,height = 100,bg = "grey")
        pic.grid(row = 1, column = 1)
        
        #name
        name = tk.Label(self, text=u'name')
        name.grid(row = 1, column =3)

        #timer(startで開始、割合が少なくなったら開始に変更予定)
        self.s1 = 3
        self.s2 = 0
        self.s3 = 0
        
        #gauage
        r = 70 #割合
        gauage = tk.Canvas(width = 100,height = 10,bg = "grey")
        gauage.grid(row = 2, column = 3)
        gauage.create_rectangle(0, 0,r, 30,fill = "blue")
              
        self.tokei=tk.Label(self,text=u'00:00:00',font='Arial, 25')
        
        self.tokei.grid(row=3, column=3)
 
        b1 = tk.Button(self,text='Start',command=self.start)
        b2 = tk.Button(self,text='Cancel',command=self.stop)
 
        b1.grid(row=4, column=3)
        b2.grid(row=10, column=10)

 
    def start(self): #Startを押したときの動作(実験用)
        self.started=True
        self.kake()
        self.finish = time.time() + self.s4
        self.count()
 
    def count(self):
        if self.started:
            t = self.finish - time.time()
            if t < 0:
                self.tokei.config(text="Order")#注文処理
 
            else:
                self.tokei.config(text='%02d:%02d:%02d'%(t/3600,(t/60)%60,t%60)) #表示時間を1秒毎に書き換え
                self.after(100, self.count)
 
 
    def stop(self): #停止処理
        self.started=False
        self.tokei.config(text='00:00:00')
 
    def kake(self): #入力した分＋秒を秒に換算
        ss1=self.s1
        ss2=self.s2
        ss3=self.s3
        c1=int(ss1)
        c2=int(ss2)
        c3=int(ss3)
        self.s4=c1*60*60+c2*60+c3
        