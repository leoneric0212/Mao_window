from pprint import pprint
import tools
import tkinter as tk
from tkinter import Event, Frame, Misc, ttk    
from ttkthemes import ThemedTk     
from tkinter import messagebox
from tkinter.simpledialog import Dialog
from datetime import datetime
class Window(ThemedTk):             
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("空氣品質指標AQQIII顯示")   
        
        style=ttk.Style()           
        style.configure('Top.TFrame')  
        style.configure('Top.TLabel',font=('Helvetica',25,'bold'))   
        title_frame=ttk.Frame(self,style='Top.TFrame',borderwidth=2,relief='groove')  
        ttk.Label(title_frame,text="全台空氣品值指標",style='Top.TLabel').pack(expand=True,fill='y')  
        title_frame.pack(ipadx=100,ipady=30,padx=10,pady=10) 
        func_frame=ttk.Frame(self,style='Top.TFrame',borderwidth=1,relief='groove')    
        ttk.Button(func_frame,text="aqi品質最好的5個",command=self.click1).pack(side='left',expand=True)
        ttk.Button(func_frame,text="aqi品質最差的5個",command=self.click2).pack(side='left',expand=True)
        ttk.Button(func_frame,text="pm2.5品質最好的5個",command=self.click3).pack(side='left',expand=True)
        ttk.Button(func_frame,text="pm2.5品質最差的5個",command=self.click4).pack(side='left',expand=True)
        func_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)
    
    def download_parse_data(self) ->list[dict] |None:   #設定公共功能，讓後面按鈕可以一起套用
        try:              #去抓資料
            all_data:dict[any]=tools.download_json()
        except Exception as error:
            messagebox.showwarning("出現錯誤","出現大bug，請稍後再試")
            return     #將錯誤回傳，或是回傳None
        else:   #try
            data:list[dict]=tools.get_data(all_data)
            return data     #data為區域變數
            
    def update_data(self):
        if (tools.AQI.aqi_records) is None or (tools.AQI.update_time) is None:  #當沒有資料時，去下載資料
            tools.AQI.aqi_records=self.download_parse_data()
            tools.AQI.update_time=datetime.now()
        elif((datetime.now()-tools.AQI.update_time).seconds>=60*60): #將現在時間減去資料時間，得到timedelta，並用這參數計算，當間隔超過一小時時下載資料
            tools.AQI.aqi_records=self.download_parse_data()
            tools.AQI.update_time=datetime.now()

    def click1(self):
        self.update_data()  #呼叫確認資料更新
        data:list[dict]=tools.AQI.aqi_records
        sorted_data:list[dict]=sorted(data,key=lambda value:value['aqi'])
        best_aqi:list[dict]=sorted_data[:5]
        def abc(value:dict) -> str:
            return f"{value['county']}{value['site_name']} aqi:{value['aqi']}、pm2.5：{value['pm25']}-狀況：{value['status']}-時段-{value['date']}"
        message_data:list[dict]=list(map(abc,best_aqi))
        message="\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="全台aqi最佳前5名",message=message)

    def click2(self):
        self.update_data()  #呼叫確認資料更新
        data:list[dict]=tools.AQI.aqi_records
        sorted_data:list[dict]=sorted(data,key=lambda value:value['aqi'],reverse=True)
        best_aqi:list[dict]=sorted_data[:5]
        def abc(value:dict) -> str:
            return f"{value['county']}{value['site_name']} aqi:{value['aqi']}、pm2.5：{value['pm25']}-狀況：{value['status']}-時段-{value['date']}"
        message_data:list[dict]=list(map(abc,best_aqi))
        message="\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="全台aqi最差前5名",message=message)

    def click3(self):
        self.update_data()  #呼叫確認資料更新
        data:list[dict]=tools.AQI.aqi_records
        sorted_data:list[dict]=sorted(data,key=lambda value:value['pm25'])
        best_aqi:list[dict]=sorted_data[:5]
        def abc(value:dict) -> str:
            return f"{value['county']}{value['site_name']} aqi:{value['aqi']}、pm2.5：{value['pm25']}-狀況：{value['status']}-時段-{value['date']}"
        message_data:list[dict]=list(map(abc,best_aqi))
        message="\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="全台pm2.5最佳前5名",message=message)
        
    def click4(self):
        self.update_data()  #呼叫確認資料更新
        data:list[dict]=tools.AQI.aqi_records
        sorted_data:list[dict]=sorted(data,key=lambda value:value['pm25'],reverse=True)
        best_aqi:list[dict]=sorted_data[:5]
        def abc(value:dict) -> str:
            return f"{value['county']}{value['site_name']} aqi:{value['aqi']}、pm2.5：{value['pm25']}-狀況：{value['status']}-時段-{value['date']}"
        message_data:list[dict]=list(map(abc,best_aqi))
        message="\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="全台pm2.5最差前5名",message=message)

class ShowInfo(Dialog):
    def __init__(self,parent:Misc,title:str|None,message:str=""):
        self.message=message        #要寫在super上面!!
        super().__init__(parent=parent,title=title)

    def body(self,master:Frame):    #按下按鈕後顯示的資料
        text=tk.Text(self,height=5,font=('標楷體',12))
        text.pack(padx=10,pady=10)  
        text.insert(tk.INSERT,self.message)
        text.config(state='normal')
        return None

    def apply(self) -> None:            #設定使用者按下ok按鈕後內建會執行的動作
        print("使用者按下ok")

    def buttonbox(self) -> None:        #自訂按鈕(取代內建的ok,cancel)
        box = tk.Frame(self)
        self.ok_button= tk.Button(box,text="ok!!!",width=10,command=self.ok,default=tk.ACTIVE)  #default為設定按鈕預設狀態 
        self.ok_button.pack(pady=(30,30),ipady=10)           #設定呈現ok按鈕，ipady設定按鈕高度
        box.pack()                      #設定呈現整個對話框

    def ok(self) -> None:   #覆寫原有的ok功能
        print("按下了OK按鈕")
        super().ok()



def main():
    window=Window(theme="arc")
    window.mainloop()

if __name__=='__main__':
    main()