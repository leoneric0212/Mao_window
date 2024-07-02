import tkinter as tk
from tkinter import ttk

def get_names() -> list[str]:
    with open('names.txt',encoding='utf-8') as file:    
        content:str=file.read()      
    names:list[str]=content.split()
    return names

class Window(tk.Tk):
    def __init__(self,title:str='Hello',**kwargs):
        super().__init__(**kwargs)
        self.title(title)
        label:ttk.Label=ttk.Label(self,
                                  text='Hello World',
                                  font=('Arial',40,'bold'),
                                  foreground='#ae1')
        label.pack(padx=100,pady=40)

if __name__=='__main__':
    names:list[str]=get_names()
    window:Window= Window(title='拍森')
    window.mainloop()

    