import tkinter as tk
import subprocess as sub

# tkinter setup
root = tk.Tk()
root.title("Linear Algebra Helper - Home")
root.geometry("800x800")
root.resizable(True, True)

title_label = tk.Label(root, text="What Linear Algebra task can we assist you with today?")
title_label.pack()

# application buttons
matrix_vector_button = tk.Button(root, text="Matrix x Vector Multiplication", command=lambda:start_file('matrix-vector.py'))
matrix_vector_button.pack()

# functions
def start_file(file_name):
        sub.run(['python3', file_name])

root.mainloop()