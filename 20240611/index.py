import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
from tools import CustomMessagebox

class Window(ThemedTk):
    def __init__ (self,theme:str|None,**kwargs):        #設定自己的init，其中的theme沒有預設值，需要被設定
        super().__init__(**kwargs)  #找ThemedTk的宣告，得知要繼承的太多，就用**kwargs
        self.title("BMI計算機")
        self.configure(bg="#ff8cc6")        #設定整個window的顏色
        # self.geometry("300x100+100+50")   #不建議設定大小，由內容來決定大小，後面的+用來設定視窗位置
        self.resizable(False,False)
        style=ttk.Style()
        style.configure("input.TFrame",background='#2C497F')   #設定一種style，必須要先自訂名稱
        style.configure("press.TButton",background='#2C4900',font=('標楷體',10))


        title_Frame = ttk.Frame(self)     #用來設定視窗
        title_label=ttk.Label(self,text="BMI計算器",font=("arial",20))  #tk可以設定背景顏色，ttk不行
        title_label.pack(pady=10)
        title_Frame.pack(padx=100,pady=(0,20))  #設定上面距離0，下面距離20

        #按鈕設定

        input_frame= ttk.Frame(self,width=100,height=5,style='input.TFrame')   #套用前面的設定
        #姓名
        label_name = ttk.Label(input_frame, text="姓名:")
        label_name.grid(row=0, column=0, padx=5, pady=5,sticky=tk.E)

        self.name_value=tk.StringVar()  #用於讓ttk.Entry能接收，這兩行是為了讓資料能在之後被更改
        self.name_value.set('')         #將其重設為空
        entry_name = ttk.Entry(input_frame,textvariable=self.name_value)
        entry_name.grid(row=0, column=1, padx=5, pady=5)

        # 身高體重
        label_height = ttk.Label(input_frame, text="身高 (cm):")
        label_height.grid(row=1, column=0, padx=5, pady=5,sticky=tk.E)

        self.height_value=tk.StringVar()
        self.height_value.set('')
        entry_height = ttk.Entry(input_frame,textvariable=self.height_value)
        entry_height.grid(row=1, column=1, padx=5, pady=5)

        label_weight = ttk.Label(input_frame, text="體重 (kg):")
        label_weight.grid(row=2, column=0, padx=5, pady=5,sticky=tk.E)

        self.weight_value=tk.StringVar()
        self.weight_value.set('')
        entry_weight = ttk.Entry(input_frame,textvariable=self.weight_value)
        entry_weight.grid(row=2, column=1, padx=5, pady=5)

        input_frame.pack(padx=30,pady=10)

        button_frame=ttk.Frame(self)
        button_calculate=ttk.Button(button_frame,text="計算",command=self.show_bmi_result,style="press.TButton")
        button_calculate.pack(side=tk.LEFT,expand=True,fill=tk.X)
        button_close=ttk.Button(button_frame,text="關閉",command=self.destroy,style="press.TButton")
        button_close.pack(side=tk.RIGHT,expand=True,fill=tk.X)
        button_frame.pack(padx=20,fill=tk.X,pady=(0,15))

   

    def show_bmi_result(self):
        try:
            name:str = self.name_value.get()
            height:int = int(self.height_value.get())
            weight:int = int(self.weight_value.get())
        except ValueError:
            messagebox.showwarning("Warning","格式錯誤或欄位未填寫")
        except Exception:
            messagebox.showwarning("Warning","發生不知名的錯誤")
        else:
            self.show_result(name=name,height=height,weight=weight)

    def show_result(self,name:str,height:int,weight:int):
        bmi = weight / (height / 100) ** 2
        if bmi < 18.5:
            status = "體重過輕"
            ideal_weight = 18.5 * (height / 100) ** 2
            weight_change = ideal_weight - weight
            status_color = "red"
            advice = f"您需要至少增加 {abs(weight_change):.2f} 公斤才能達到正常體重。"
        elif 18.5 <= bmi <= 24.9:
            status = "正常"
            status_color = "blue"
            advice = "您的體重正常，請保持！"
        else:
            status = "體重過重"
            ideal_weight = 24.9 * (height / 100) ** 2
            weight_change = weight - ideal_weight
            status_color = "red"
            advice = f"您需要至少減少 {abs(weight_change):.2f} 公斤才能達到正常體重。"
        CustomMessagebox(self,title="bmi",name=name,bmi=bmi,status=status,advice=advice,status_color=status_color)    #self對應的是CustomMessagebox裡面的parent

    def __repr__(self):
        return "我是window的實體"
        
        


def main():
    window=Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()