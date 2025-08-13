import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self):
        self.todoList = []

    def addTask(self, task):
        self.todoList.append(task)

    def viewTasks(self):
        return self.todoList

    def removeTask(self, index):
        try:
            self.todoList.pop(index)
            return True
        except IndexError:
            return False

class TodoApp:
    def __init__(self, root):
        self.todo = TodoList()
        self.root = root
        self.root.title("Todo List App")

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack()

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        self.remove_btn = tk.Button(root, text="Remove Selected Task", command=self.remove_task)
        self.remove_btn.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.todo.addTask(task)
            self.entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            if self.todo.removeTask(index):
                self.update_listbox()
            else:
                messagebox.showerror("Error", "Invalid index.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for i, task in enumerate(self.todo.viewTasks()):
            self.listbox.insert(tk.END, f"{i}: {task}")

if __name__ == '__main__':
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()