from tkinter import *

def create_result_label(root):
    # Create a label widget to display the result:
    label_result = Label(root, width=25, height=2, text="", font=('Arial', 30,), bg="#F5F5DC")
    label_result.pack()
    return label_result

