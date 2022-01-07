import tkinter as tk
import subprocess as sub

root = tk.Tk()
root.title("Matrix x Vector")
root.geometry("800x800")
root.resizable(True, True)


# dimensions state
dimensions_labels = []
dimensions_entries = []
dimensions_generate_button = []

def create_dimensions_state():

        dimensions_labels.append(tk.Label(root, text="Matrix A Dimensions"))
        dimensions_labels[0].pack()

        dimensions_entries.append(tk.Entry(root, textvariable=tk.StringVar()))
        dimensions_entries[0].pack()

        dimensions_entries.append(tk.Entry(root, textvariable=tk.StringVar()))
        dimensions_entries[1].pack()

        dimensions_generate_button.append(tk.Button(root, text="Generate Matrix",
                command=lambda: create_input_state(dimensions_entries[0].get(), dimensions_entries[1].get())))
        dimensions_generate_button[0].pack()

create_dimensions_state()

# input state
input_matrix = []
input_matrix_label = []
input_vector = []
input_vector_label = []
input_reset_button = []
input_solve_button = []


def create_input_state(rows, columns):
        
        clear_pack_screen()
        try:
                rows = int(rows)
                columns = int(columns)
        except:
                reset_state()

        input_matrix_label.append(tk.Label(root, text=f"Matrix A:"))
        input_matrix_label[0].grid(row=0, column=0)

        for n in range(rows):
                input_matrix_row = []
                for m in range(columns):
                        input_matrix_row.append(tk.Entry(
                                root, textvariable=tk.StringVar()))
                        input_matrix_row[m].insert('end', f'x{n+1}{m+1}')
                        input_matrix_row[m].grid(row=n+1, column=m)
                input_matrix.append(input_matrix_row)
        
        row_after_matrix = len(input_matrix) + 1

        input_vector_label.append(tk.Label(root, text=f"Vector x\u20d7:"))
        input_vector_label[0].grid(row=row_after_matrix, column=0)

        for n in range(columns):
                input_vector.append(tk.Entry(
                        root, textvariable=tk.StringVar()))
                input_vector[n].insert('end', f'x{n+1}')
                input_vector[n].grid(row=row_after_matrix+n+1, column=0)
        
        row_after_vector = row_after_matrix+len(input_vector) + 1
        
        input_reset_button.append(tk.Button(root, text="Reset", command=lambda:reset_state()))
        input_reset_button[0].grid(row=row_after_vector, column=0)

        row_after_reset = row_after_vector + len(input_reset_button)

        input_solve_button.append(tk.Button(root, text="Solve", command=lambda:create_output_state(input_matrix, input_vector)))
        input_solve_button[0].grid(row=row_after_reset, column=0)

        return

#output state
output_labels = []
output_vector = []
output_reset_button = []

def create_output_state(user_matrix, user_vector):

        clear_grid_screen()

        matrix = []
        vector = []
        solution_vector = []
        try:
                for n in user_matrix:
                        matrix_row = []
                        for m in n:
                                matrix_row.append(float(m.get()))
                        matrix.append(matrix_row)

                for n in user_vector:
                        vector.append(float(n.get()))

                for n in matrix:
                        addends = []
                        for i, v in enumerate(n):
                                product = v * vector[i]
                                addends.append(product)
                        solution_vector.append(sum(addends))

                output_labels.append(tk.Label(root, text=f"Solution y\u20d7:"))
                for v in solution_vector:
                        output_labels[0]['text'] = output_labels[0]['text'] + f'\n{v}'
                output_labels[0].pack()
                output_vector.append(output_labels[0])

                output_reset_button.append(tk.Button(root, text="Reset", command=lambda:reset_state()))
                output_reset_button[0].pack()
        except:
                reset_state()

def reset_state():

        root_widgets = root.winfo_children()
        for widget in root_widgets:
                widget.destroy()

        dimensions_labels.clear()
        dimensions_entries.clear()
        dimensions_generate_button.clear()
        input_matrix.clear()
        input_vector.clear()
        input_reset_button.clear()
        input_solve_button.clear()
        output_labels.clear()
        output_vector.clear()
        output_reset_button.clear()
        input_matrix_label.clear()
        input_vector_label.clear()

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