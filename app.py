from tkinter import *
from function import *


class App():
    def __init__(self, root, label_result):
        self.root = root
        self.label_result = label_result


        # Create the buttons functions:
        Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#e61736", command=lambda: clear(label_result)).place(x=10, y=100)
        Button(root, text="÷", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda:show("/", label_result)).place(x=150, y=100)
        Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("*0.01", label_result)).place(x=290, y=100)
        Button(root, text="X", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("*", label_result)).place(x=430, y=100)
        Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("7", label_result)).place(x=10, y=200)
        Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("8", label_result)).place(x=150, y=200)
        Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("9", label_result)).place(x=290, y=200)
        Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#7FFF00", bg="#17183d", command=lambda: show("+", label_result)).place(x=430, y=200)
        Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("4", label_result)).place(x=10, y=300)
        Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("5", label_result)).place(x=150, y=300)
        Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("6", label_result)).place(x=290, y=300)
        Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("1", label_result)).place(x=10, y=400)
        Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("2", label_result)).place(x=150, y=400)
        Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("3", label_result)).place(x=290, y=400)
        Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#e61736", bg="#17183d", command=lambda: calculate(label_result)).place(x=430, y=410)
        Button(root, text="00", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("00", label_result)).place(x=10, y=500)
        Button(root, text="0", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("0", label_result)).place(x=150, y=500)
        Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show(".", label_result)).place(x=290, y=500)
        Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("-", label_result)).place(x=430, y=300)