from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox,Misc
import data
from data import FilterData,Info
from tools import CustomMessagebox



class Window(ThemedTk):
    def __init__(self,theme:str='arc',**kwargs):
        super().__init__(theme=theme,**kwargs)
        self.title('台北市YouBike2.0及時資料')
        try:
            self.__data = data.load_data()
        except Exception as e:
            messagebox.showwarning(title='警告',message=str(e))
        
        self._display_interface()
        
    @property
    def data(self)->list[dict]:
        return self.__data
    

    def _display_interface(self):
        mainFrame = ttk.Frame(borderwidth=1,relief='groove')
        ttk.Label(mainFrame,text="台北市YouBike2.0及時資料",font=('arial',25)).pack(pady=(20,10))
        #=================================
        tableFrame = ttk.Frame(mainFrame)
        columns = ('sna', 'sarea', 'mday','ar','total','rent_bikes','retuen_bikes')
        tree = ttk.Treeview(tableFrame, columns=columns, show='headings')
        # define headings
        tree.heading('sna', text='站點')
        tree.heading('sarea', text='行政區')
        tree.heading('mday', text='時間')
        tree.heading('ar', text='地址')
        tree.heading('total', text='總數')
        tree.heading('rent_bikes', text='可借')
        tree.heading('retuen_bikes', text='可還')

        # 定義欄位寬度
        tree.column('sarea',width=70,anchor=tk.CENTER)
        tree.column('mday',width=120,anchor=tk.CENTER)
        tree.column('ar',minwidth=100)
        tree.column('total',width=50,anchor=tk.CENTER)
        tree.column('rent_bikes',width=50,anchor=tk.CENTER)
        tree.column('retuen_bikes',width=50,anchor=tk.CENTER)

        # bind使用者的事件
        tree.bind('<<TreeviewSelect>>', self.item_selected)

    
        
        
        # add data to the treeview
        for site in self.data:
            tree.insert('', tk.END,
                        values=(site['sna'],site['sarea'],site['mday'],site['ar'],site['total'],site['rent_bikes'],site['retuen_bikes']))
        
        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        tableFrame.pack(padx=20,pady=20)
        #======================================
        self.piechartframe=PieChartFrame(mainFrame)
        self.piechartframe.pack(expand=True,fill=tk.BOTH)
        mainFrame.pack(padx=10,pady=10)
        
        



    def item_selected(self,event):
        tree = event.widget
        print(tree.selection())
        records:list[list]=[]
        for selected_item in tree.selection()[:3]:          #後面的[:3]用於只顯示前三項
            item = tree.item(selected_item)
            record:list = item['values']
            records.append(record)
        self.piechartframe.infos=records
            
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #將圖表用在canvas

class PieChartFrame(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)    #繼承不用寫self,後面寫法是常見寫法
        # master.title("LLLine")                      #不是window不能寫title
        self.configure({'borderwidth':2,'relief':'groove'})
        '''以下三種寫法都一樣  都可以
        # self.configure({'borderwidth':2,'relief':'groove'})
        # self.config({'borderwidth':2,'relief':'groove'})
        # self['borderwidth']=20
        # self['relief']='groove'
        '''
        '''
        canvas=tk.Canvas(self)                  #用於繪製內容
        canvas.create_line(15,30,200,30)        #畫線，(x0,y0,x1,y1...)
        canvas.create_line(300,35,300,200,dash=(4,2))   #dash設定虛線樣式
        canvas.create_line(55,85,155,85,105,180,55,85)
        canvas.pack(expand=True,fill='both')
        '''
        style=ttk.Style()                                   #設定主要Frame的外觀
        style.configure('abc.TFrame',background='#fff')
        self.configure(style='abc.TFrame')

    @property                           #確保進來的資料不會被改
    def infos(self) -> None:
        return None
    

    
    @infos.setter
    def infos(self,datas:list[list]) -> None:       #讓資料傳進來，但不傳出去，顯示在視窗內
        for w in self.winfo_children():             #由於資料進來後不會被處理，只會越堆越多，因此用這個
            w.destroy()
        for data in datas:
            sitename:str=data[0]
            area:str=data[1]
            info_timer:str=data[2]
            address:str=data[3]
            total:int=data[4]
            rent:int=data[5]
            returns:int=data[6]
            oneFrame=ttk.Frame(self,style='abc.TFrame')
            ttk.Label(oneFrame,text='行政區:').grid(row=0,column=0,sticky='e')
            ttk.Label(oneFrame,text=area).grid(row=0,column=1,sticky='w')
            ttk.Label(oneFrame,text='站點名稱:').grid(row=1,column=0,sticky='e')
            ttk.Label(oneFrame,text=sitename).grid(row=1,column=1,sticky='w')
            ttk.Label(oneFrame,text='時間:').grid(row=2,column=0,sticky='e')
            ttk.Label(oneFrame,text=info_timer).grid(row=2,column=1,sticky='w')
            ttk.Label(oneFrame,text='地址:').grid(row=3,column=0,sticky='e')
            ttk.Label(oneFrame,text=address).grid(row=3,column=1,sticky='w')
            ttk.Label(oneFrame,text='總車輛數:').grid(row=4,column=0,sticky='e')
            ttk.Label(oneFrame,text=total).grid(row=4,column=1,sticky='w')
            ttk.Label(oneFrame,text='可借:').grid(row=5,column=0,sticky='e')
            ttk.Label(oneFrame,text=rent).grid(row=5,column=1,sticky='w')
            ttk.Label(oneFrame,text='可還:').grid(row=6,column=0,sticky='e')
            ttk.Label(oneFrame,text=returns).grid(row=6,column=1,sticky='w')
            
            def func(pct,allvals):
                absolute = int(np.round(pct/100.*np.sum(allvals)))
                return f"{absolute:d}pcs - {pct:.1f}%"

            value=[rent,returns]
            labels=['rent','return']
            colors=['green','red']
            figure=plt.figure(figsize=(5,5),dpi=72)
            axes=figure.add_subplot()
            #製作圓餅圖
            axes.pie(value,labels=labels,           
                    colors=colors,
                    shadow=True,
                    startangle=180,
                    labeldistance=1.2,
                    autopct=lambda pct:func(pct,value),
                    textprops=dict(color="red"))         #設顏色
            
            axes.legend(title="rate",
                        loc="center left",bbox_to_anchor=(0,0,0,2))
            
            canvas=FigureCanvasTkAgg(figure,oneFrame)
            canvas.draw()       #要加上draw
            canvas.get_tk_widget().grid(row=6,column=0,columnspan=2)    #要這樣pack才能運作
            
            oneFrame.pack(side='left',expand=True,fill='both')
    


    

def main():
    def on_closing():           #由於關閉視窗不會停止終端機，所以要加上這個
        print("手動關閉視窗")
        window.destroy()
        
    window = Window(theme='breeze')
    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.mainloop()

if __name__ == '__main__':
    main()