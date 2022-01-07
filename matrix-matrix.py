import tkinter as tk
import numpy as np

# tkinter setup
root = tk.Tk()
root.title("Matrix x Matrix")
root.geometry("800x800")
root.resizable(True, True)

# dimensions state
dimensions_labels = []
dimensions_entries = []
dimensions_generate_button = []
dimensions_quit_button = []

def create_dimensions_state():

        dimensions_labels.append(tk.Label(root, text="Matrix A Dimensions"))
        dimensions_labels[0].pack()

        dimensions_entries.append(tk.Entry(root, textvariable=tk.StringVar()))
        dimensions_entries[0].pack()

        dimensions_entries.append(tk.Entry(root, textvariable=tk.StringVar()))
        dimensions_entries[1].pack()

        dimensions_labels.append(tk.Label(root, text="Matrix B Dimensions"))
        dimensions_labels[1].pack()

        dimensions_entries.append(tk.Entry(root, textvariable=tk.StringVar()))
        dimensions_entries[2].pack()

        dimensions_entries.append(tk.Entry(root, textvariable=tk.StringVar()))
        dimensions_entries[3].pack()

        dimensions_generate_button.append(tk.Button(root, text="Generate Matricies",
                command=lambda: create_input_state(dimensions_entries[0].get(), dimensions_entries[1].get(), dimensions_entries[2].get(), dimensions_entries[3].get())))
        dimensions_generate_button[0].pack()

        dimensions_quit_button.append(tk.Button(root, text="Quit",
                command=lambda: root.destroy()))
        dimensions_quit_button[0].pack()

create_dimensions_state()

# input state
input_m1 = []
input_m1_label = []
input_m2 = []
input_m2_label = []
input_reset_button = []
input_solve_button = []


def create_input_state(m1_rows, m1_columns, m2_rows, m2_columns):
        
        clear_pack_screen()
        try:
                m1_rows = int(m1_rows)
                m1_columns = int(m1_columns)
                m2_rows = int(m2_rows)
                m2_columns = int(m2_columns)
        except:
                reset_state()

        input_m1_label.append(tk.Label(root, text=f"Matrix A:"))
        input_m1_label[0].grid(row=0, column=0)

        for n in range(m1_rows):
                input_m1_row = []
                for m in range(m1_columns):
                        input_m1_row.append(tk.Entry(
                                root, textvariable=tk.StringVar()))
                        input_m1_row[m].insert('end', f'x{n+1}{m+1}')
                        input_m1_row[m].grid(row=n+1, column=m)
                input_m1.append(input_m1_row)
        
        row_after_m1 = len(input_m1) + 1

        input_m2_label.append(tk.Label(root, text=f"Matrix B:"))
        input_m2_label[0].grid(row=row_after_m1, column=0)


        for n in range(m2_rows):
                input_m2_row = []
                for m in range(m2_columns):
                        input_m2_row.append(tk.Entry(
                                root, textvariable=tk.StringVar()))
                        input_m2_row[m].insert('end', f'x{n+1}{m+1}')
                        input_m2_row[m].grid(row=row_after_m1+n+1, column=m)
                input_m2.append(input_m2_row)

        
        row_after_m2 = row_after_m1 +len(input_m2) + 1
        
        input_reset_button.append(tk.Button(root, text="Reset", command=lambda:reset_state()))
        input_reset_button[0].grid(row=row_after_m2, column=0)

        row_after_reset = row_after_m2 + len(input_reset_button)

        input_solve_button.append(tk.Button(root, text="Solve", command=lambda:create_output_state(input_m1, input_m2)))
        input_solve_button[0].grid(row=row_after_reset, column=0)

# output state
output_labels = []
output_matrix = []
output_reset_button = []

def create_output_state(m1, m2):

        clear_grid_screen()

        m1_temp = []
        m2_temp= []
        solution_matrix = []
        try:
                for n in m1:
                        m1_row = []
                        for m in n:
                                m1_row.append(float(m.get()))
                        m1_temp.append(m1_row)

                for n in m2:
                        m2_row = []
                        for m in n:
                                m2_row.append(float(m.get()))
                        m2_temp.append(m2_row)

                solution_matrix = np.dot(m1_temp,m2_temp)

                output_labels.append(tk.Label(root, text=f"Solution C:\n"))
                for row in solution_matrix:
                        output_labels[0]['text'] = output_labels[0]['text'] + '['
                        for value in row:
                                output_labels[0]['text'] = output_labels[0]['text'] + f' {value}'
                        output_labels[0]['text'] = output_labels[0]['text'] + ']\n'

                output_labels[0].pack()

                output_reset_button.append(tk.Button(root, text="Reset", command=lambda:reset_state()))
                output_reset_button[0].pack()
        except:
                reset_state()

# other functions
def reset_state():

        root_widgets = root.winfo_children()
        for widget in root_widgets:
                widget.destroy()

        dimensions_labels.clear()
        dimensions_entries.clear()
        dimensions_generate_button.clear()
        dimensions_quit_button.clear()
        input_m1.clear()
        input_m1_label.clear()
        input_m2.clear()
        input_m2_label.clear()
        input_reset_button.clear()
        input_solve_button.clear()
        output_labels.clear()
        output_matrix.clear()
        output_reset_button.clear()

        create_dimensions_state()

def clear_pack_screen():
        root_widgets = root.winfo_children()
        for widget in root_widgets:
                widget.pack_forget()

def clear_grid_screen():
        root_widgets = root.winfo_children()
        for widget in root_widgets:
                widget.grid_remove()

root.mainloop()