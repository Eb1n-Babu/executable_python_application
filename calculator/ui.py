import tkinter as tk
from tkinter import messagebox
from operation import operation

def launch_ui():
    def calculate():
        try:
            x = int(entry_x.get())
            y = int(entry_y.get())
            z = op_var.get()
            result = operation(x, y, z)
            result_label.config(text=f"Result: {result}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "You cannot divide by zero")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception:
            messagebox.showerror("Error", "Something went wrong")

    root = tk.Tk()
    root.title("Simple Calculator")

    tk.Label(root, text="First Number").grid(row=0, column=0)
    entry_x = tk.Entry(root)
    entry_x.grid(row=0, column=1)

    tk.Label(root, text="Second Number").grid(row=1, column=0)
    entry_y = tk.Entry(root)
    entry_y.grid(row=1, column=1)

    tk.Label(root, text="Operation").grid(row=2, column=0)
    op_var = tk.StringVar(root)
    op_var.set("+")
    tk.OptionMenu(root, op_var, "+", "-", "*", "/").grid(row=2, column=1)

    tk.Button(root, text="Calculate", command=calculate).grid(row=3, columnspan=2, pady=10)
    result_label = tk.Label(root, text="Result: ")
    result_label.grid(row=4, columnspan=2)

    root.mainloop()