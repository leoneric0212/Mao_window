import tkinter as tk
from tkinter import ttk

class CitySelectionWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("台湾城市选择")
        self.geometry("300x400")
        
        # 创建主要框架
        mainframe = ttk.Frame(self, padding="10")
        mainframe.pack(expand=True, fill='both')
        
        # 城市列表
        self.cities = [
            "台北", "新北", "桃园", "台中", "台南", "高雄",
            "基隆", "新竹", "嘉义", "苗栗", "彰化", "南投",
            "云林", "屏东", "宜兰", "花莲", "台东", "澎湖",
            "金门", "马祖"
        ]
        
        # 用于存储城市选择的变量
        self.city_vars = {city: tk.BooleanVar() for city in self.cities}
        
        # 创建城市选择框
        city_frame = ttk.Labelframe(mainframe, text="选择城市")
        city_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        for city in self.cities:
            check = ttk.Checkbutton(city_frame, text=city, variable=self.city_vars[city])
            check.pack(anchor=tk.W)
        
        # 添加一个按钮来显示选择结果
        show_button = ttk.Button(mainframe, text="显示选择", command=self.show_selection)
        show_button.pack(pady=10)
        
    def show_selection(self):
        selected_cities = [city for city, var in self.city_vars.items() if var.get()]
        message = "已选择城市:\n" + "\n".join(selected_cities)
        print(message)
        tk.messagebox.showinfo("选择结果", message)

def main():
    app = CitySelectionWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
