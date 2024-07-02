import tkinter as tk
from tkinter import ttk
from tkinter import Misc    #用於做自訂的init
from PIL import Image,ImageTk

class Excample(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)    #繼承不用寫self,後面寫法是常見寫法
        master.title("LLLine")
        self.configure({'borderwidth':2,'relief':'groove'})
        '''以下三種寫法都一樣  都可以
        # self.configure({'borderwidth':2,'relief':'groove'})
        # self.config({'borderwidth':2,'relief':'groove'})
        # self['borderwidth']=20
        # self['relief']='groove'
        '''
        canvas=tk.Canvas(self)                  #用於繪製內容
        canvas.create_line(15,30,200,30)        #畫線，(x0,y0,x1,y1...)
        canvas.create_line(300,35,300,200,dash=(4,2))   #dash設定虛線樣式
        canvas.create_line(55,85,155,85,105,180,55,85)
        canvas.pack(expand=True,fill='both')
        
        self.pack(expand=True,fill='both')
        
class Excample1(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)    #繼承不用寫self,後面寫法是常見寫法
        master.title("cCcolors")
        self.configure({'borderwidth':2,'relief':'groove'})
        canvas=tk.Canvas(self)                  
        canvas.create_rectangle(30,10,150,80,outline='#a78',fill='#079')
        canvas.create_text(40,40,text="中文測試",anchor='nw',fill='#fff',font=('標楷體',18,'bold','italic'))
        canvas.create_oval(150,10,200,60,outline='#723',fill='#ccc',width=3)    #設定圓形的方法為設定一個矩形的長寬，並用圓塞滿
        self.img=Image.open('20240617\\tvdi.png')                   #這兩行都要加上self，不然執行完圖片就被消滅了，不會顯示也不會出錯
        self.tvdi=ImageTk.PhotoImage(self.img)
        canvas.create_image(210,10,anchor='nw',image=self.tvdi)
        
        
        canvas.pack(expand=True,fill='both')
        self.pack(expand=True,fill='both')

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #將圖表用在canvas
class Excample2(ttk.Frame):
       
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)    #繼承不用寫self,後面寫法是常見寫法
        master.title("cCchart")
        self.configure({'borderwidth':2,'relief':'groove'})
        figure=plt.figure(figsize=(5,4),dpi=30)
        axes=figure.add_subplot()
        axes.plot([1,2,3,4,5],[2,3,5,7,11])     #x與y的數量要一致
        axes.set_title("Sssample Char")
        axes.set_xlabel("X-sasix")
        axes.set_ylabel("Y-axis")
        
        canvas=FigureCanvasTkAgg(figure,self)
        canvas.draw()       #要加上draw
        canvas.get_tk_widget().pack(expand=True,fill='both',padx=30,pady=30)    #要這樣pack才能運作    
        
        self.pack(expand=True,fill='both')

def main():
    window=tk.Tk()
    
    Excample2(window)                #master就是window
    
    window.geometry("600x500")
    window.mainloop()

if __name__=='__main__':
    main()