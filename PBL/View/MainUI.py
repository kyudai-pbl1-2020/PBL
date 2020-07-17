import tkinter as tk
import time
from PBL.View import addItemView as ai
from PBL.Controller import csvController
import tkinter.messagebox as mb

WID = 10

class MainUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid()
        
        #csv
        #self.csvController = csvController.CsvController()
        #self.loadItemData()
        
        #add item
        b_add = tk.Button(text=u'Add Item', command=self.add)
        
        #active
        b_active = tk.Button(text=u'Active', command=self.active)
        
        #timer(startで開始、割合が少なくなったら開始に変更予定)
        self.s1 = 3
        self.s2 = 0
        self.s3 = 0
        
        b_add.grid(row=0, column=0)
        b_active.grid(row=0, column=7)
        
        #active item(1 -> item1,...)
        active_item = 2
        
        #item1の情報(csvから得られるように変更する)
        name1 = 'water'
        max_weight1 = 10
        desired_weight1 = 3
        now_weight1 = 4
        #pic1 = 
        
        #item2の情報(csvから得られるように変更する)
        name2 = 'cup noodle'
        max_weight2 = 10
        desired_weight2 = 3
        now_weight2 = 9
        #pic2 =
        
        #item1の情報(csvから得られるように変更する)
        name3 = 'omutsu'
        max_weight3 = 10
        desired_weight3 = 3
        now_weight3 = 5
        #pic3 =
        
        
        
        #item1
        
        #picの代わり
        pic = tk.Canvas(width = 100,height = 100,bg = "grey")
        
        #name
        name = tk.Label(text=name1)
        
        #gauage
        r =  now_weight1 / max_weight1#割合
        gauage = tk.Canvas(width = 100,height = 10,bg = "grey")
        gauage.create_rectangle(0, 0,r*100, 30,fill = "blue")
              
        self.tokei=tk.Label(text=u'00:00:00')
        
        b1 = tk.Button(text='Order',command=self.order)
        b2 = tk.Button(text='Cancel',command=self.cancel)
        
        #check mark      
        check = tk.Canvas(width=20, height=20)
        if active_item == 1:
            check.create_oval(5,5,15,15, fill="blue")
        else:
            check.create_oval(5,5,15,15, tag="oval")
        
        
        check.grid(row=3, column=0)
        pic.grid(row=1, column=1, rowspan=4, columnspan=4)
        name.grid(row=2, column=6)
        gauage.grid(row=3, column=6)
        b1.grid(row=4, column=6)
        #b2.grid(row=4, column=7)
        #self.tokei.grid(row=4, column=6)
        if active_item == 1:
            b2.grid(row=4, column=7)
            self.tokei.grid(row=4, column=6)
        else:
            b1.grid(row=4, column=6)
 
        #item2
        #picの代わり
        pic2 = tk.Canvas(width = 100,height = 100,bg = "grey")
        
        #name
        name2 = tk.Label(text=name2)
        
        #gauage
        r = now_weight2 / max_weight2 #割合
        gauage2 = tk.Canvas(width = 100,height = 10,bg = "grey")
        gauage2.create_rectangle(0, 0,r*100, 30,fill = "blue")
              
        self.tokei2=tk.Label(text=u'00:00:00')
        
        b12 = tk.Button(text='Order',command=self.order)
        b22 = tk.Button(text='Cancel',command=self.cancel)
        
        #check mark       
        check2 = tk.Canvas(width=20, height=20)
        if active_item == 2:
            check2.create_oval(5,5,15,15, fill="blue")
        else:
            check2.create_oval(5,5,15,15, tag="oval")
        
        
        check2.grid(row=7, column=0)
        pic2.grid(row=5, column=1, rowspan=4, columnspan=4)
        name2.grid(row=6, column=6)
        gauage2.grid(row=7, column=6)
        if active_item == 2:
            b22.grid(row=8, column=7)
            self.tokei2.grid(row=8, column=6)
        else:
            b12.grid(row=8, column=6)
        
        
        #item3
        #picの代わり
        pic3 = tk.Canvas(width = 100,height = 100,bg = "grey")
        
        #name
        name3 = tk.Label(text=name3)
        
        #gauage
        r = now_weight3 / max_weight3 #割合
        gauage3 = tk.Canvas(width = 100,height = 10,bg = "grey")
        gauage3.create_rectangle(0, 0,r*100, 30,fill = "blue")
              
        self.tokei3=tk.Label(text=u'00:00:00')
        
        b13 = tk.Button(text='Order',command=self.order)
        b23 = tk.Button(text='Cancel',command=self.cancel)
        
        #check mark     
        check3 = tk.Canvas(width=20, height=20)
        if active_item == 3:
            check3.create_oval(5,5,15,15, fill="blue")
        else:
            check3.create_oval(5,5,15,15, tag="oval")
        
        
        check3.grid(row=11, column=0)
        pic3.grid(row=9, column=1, rowspan=4, columnspan=4)
        name3.grid(row=10, column=6)
        gauage3.grid(row=11, column=6)
        if active_item == 3:
            b23.grid(row=12, column=7)
            self.tokei3.grid(row=12, column=6)
        else:
            b13.grid(row=12, column=6)
        
        
        
        
        

    def start(self): #Startを押したときの動作(実験用　カウントダウン開始)
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
        
    def add(self):
        ai.AddItemView(self)
        
    def active(self):
        popupwindow = tk.Toplevel()
        active_number = tk.Entry(popupwindow, width=10)
        active_number.pack()
    
    def order(self):
        return 0
    def cancel(self):
        return 0
        
        
    def loadItemData(self):
        itemList = self.csvController.getItemData()
