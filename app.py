import tkinter as tk
import subprocess as sub

root = tk.Tk()
root.title("Linear Algebra Helper - Home")
root.geometry("800x800")
root.resizable(True, True)

title_label = tk.Label(root, text="What Linear Algebra task can we assist you with today?")
title_label.pack()

root.mainloop()