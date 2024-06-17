from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox
import data,tools
from data import FilterData     #引入自製的StaticMethod
from data import Info


class Window(ThemedTk):
    def __init__(self,theme:str='arc',**kwargs):
        super().__init__(theme=theme,**kwargs)      #不可以加self,因為是呼叫父類別的引數值或引數名稱
        try:
            self.__data=data.load_data()                #如果不加self，作為實體被用完會消失，加了就變attribute
        except Exception as e:
            messagebox.showwarning(title="警告",message=str(e))
        self._display_interface()
        
    @property                                       #為避免data被修改，以此設定
    def data(self) -> list[dict]:
        return self.__data      
        
    def _display_interface(self):
        # mainframe=ttk.Frame(width=500,height=800)     #若有內容，將以內容寬高為主
        mainframe=ttk.Frame(borderwidth=1,relief='raised')      #設定邊框寬度及造型
        ttk.Label(mainframe,text="台北市U敗即時資料",font=('標楷體',25)).pack(pady=(20,10))    #master代表誰是父類別
        tableFrame=ttk.Frame(mainframe)
        columns=('sna','sarea','mday','ar','total','rent_bikes','retuen_bikes')
        tree=ttk.Treeview(tableFrame,columns=columns,show='headings',selectmode='browse')   #browse為設定單選
        # define headings
        tree.heading('sna', text='站點')
        tree.heading('sarea', text='行政區')
        tree.heading('mday', text='時間')
        tree.heading('ar', text='地址')
        tree.heading('total', text='總數')
        tree.heading('rent_bikes', text='可借')
        tree.heading('retuen_bikes', text='可還')
    
        #定義欄位寬度
        tree.column('sarea',width=50,anchor=tk.CENTER)
        tree.column('mday',width=150,anchor=tk.CENTER)
        tree.column('sarea',width=50,anchor=tk.CENTER)
        tree.column('total',width=50,anchor=tk.CENTER)
        tree.column('rent_bikes',width=50,anchor=tk.CENTER)
        tree.column('retuen_bikes',width=50,anchor=tk.CENTER)
        
        #bind事件
        tree.bind('<<TreeviewSelect>>', self.item_selected)     #當作出選擇時，觸發後面的行動(self.item_selected)
                
        # add data to the treeview
        for site in self.data:
            tree.insert('', tk.END,
                        values=(site['sna'],site['sarea'],site['mday'],site['ar'],site['total'],site['rent_bikes'],site['retuen_bikes']))
            
        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        tableFrame.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)
        mainframe.pack(expand=True,fill=tk.BOTH,padx=10,pady=10)
    
    def item_selected(self,event):      
        tree=event.widget                   #用於設定事件的功能
        print(isinstance(tree,ttk.Treeview))       #用於確認點到的位置是否為treeview的實體
        for selected in tree.selection():   #selection代表按下的那個欄位
            item=tree.item(selected)        #tree.item代表按下的物件
            record:list=item['values']      #由於上一行出來的是list，所以匯出其中的values部分
            site_data:Info=FilterData.get_selected_site(sna=record[0],data=self.data)
            tools.CustomMessagebox(self,title=site_data.sna,site=site_data)
    
                        
        
def main():
    window=Window(theme='Breeze')
    window.mainloop()

if __name__=='__main__':
    main()