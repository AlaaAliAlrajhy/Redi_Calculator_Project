import tkinter as tk
from tkinter import *
from function import *
from style import *
from app import App

# Create the window for the calculator:
root = tk.Tk()
root.title("My First Calculator")
root.geometry("570x700+400+400")
root.configure(bg="#FFFDD0")
root.resizable(False,False)

# Create the result label
label_result = create_result_label(root)

# Create an instance of the App class
calculator_app = App(root=root, label_result=label_result)

root.mainloop()
