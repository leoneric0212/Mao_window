import data
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self,Theme:str|None,**kwargs):
        super().__init__(**kwargs)
        try:
            ubike:list[dict]=data.load_data()
        except Exception as error:
            print(error)
        else:
            print(ubike)

def main():
    window=Window(Theme='clam')
    window.mainloop()

if __name__ == '__main__':
    main()