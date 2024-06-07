from pprint import pprint
import tools
import tkinter as tk
from tkinter import ttk     #製作視窗
from ttkthemes import ThemedTk      #外觀套件
from tkinter import messagebox
from tkinter.simpledialog import Dialog

class Window(ThemedTk):             #套用外觀套件
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("空氣品質指標AQQIII顯示")    #設定標題
        style=ttk.Style()           #tk直接設定background，而ttk則是設定frame及style
        style.configure('Top.TFrame')  #設定容器，老師也是上網查，設定名稱是網站建議命名為TFrame，背景色為background="色號"
        style.configure('Top.TLabel',font=('Helvetica',25,'bold'))    #設定文字，及字底下顏色
        title_frame=ttk.Frame(self,style='Top.TFrame',borderwidth=2,relief='groove')     #設定容器造型，borderwidth是邊框粗細；若裡面有pack，則此設定無效
        ttk.Label(title_frame,text="全台空氣品值指標",style='Top.TLabel').pack(expand=True,fill='y')      #選擇樣式為title_frame的TopLable，pack設定容器的延伸；最後要包再title_frame.pack
        title_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)   #設定尺寸，ipadx,ipady會將內文推開，padx,pady會從框外推開
        #ttk.Button(self,text="離開",command=self.destroy).pack()    #設定關閉按鈕
        func_frame=ttk.Frame(self,style='Top.TFrame',borderwidth=1,relief='groove')    
        ttk.Button(func_frame,text="aqi品質最好的5個",command=self.click1).pack(side='left',expand=True)    #side='left'設定靠左
        ttk.Button(func_frame,text="aqi品質最差的5個",command=self.click2).pack(side='left',expand=True)    #全部都用expand左右擴張才能平均分配空間
        ttk.Button(func_frame,text="pm2.5品質最好的5個",command=self.click3).pack(side='left',expand=True)  #command連接到下面的click設定
        ttk.Button(func_frame,text="pm2.5品質最差的5個",command=self.click4).pack(side='left',expand=True)
        func_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)
        ttk.Button(func_frame,text="pm2.5品質最差的5個",command=self.click5).pack(side='left',expand=True)
        func_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)
    
    def click1(self):   #設定功能讓按鍵套用
        messagebox.showinfo("安安","吃大便")
    def click2(self):
        messagebox.showerror("錯誤","你就是錯誤")
    def click3(self):
        messagebox.showwarning("請注意","你成為第一百萬用戶")
    '''def click4(self):
        answer:bool=messagebox.askyesno("繼續ㄇ?",message="你確定嗎")
        print(answer)'''
    def click4(self):
        Dialog(self,title="這是戴噁羅格")   #dialog用於自訂內容，但由於內文(body)已被寫死不能改，所以要繼承再自訂
    def click5(self):
        ShowInfo(parent=self,title="這是新的Dialog")    #由於class設定中，有使用**kwargs，所以這邊要寫出引述名稱parent

class ShowInfo(Dialog):     #用來繼承dialog，並修改內容
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def body(self,master):
        text=tk.Text(self,height=5,font=('Helvetica',12)) 
        text.pack(padx=10,pady=10)  
        text.insert(tk.INSERT,"測試文字")
        text.config(state='normal')     #state用於讓使用者無法在裡面輸入
        return None

def main():
    window=Window(theme="arc")  #利用套件，設定顏色
    window.mainloop()

if __name__=='__main__':
    main()