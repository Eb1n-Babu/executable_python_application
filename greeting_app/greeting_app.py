# greeting_app.py

import tkinter as tk

def greet():
    name = entry.get()
    output_label.config(text=f"Hello, {name}! Welcome to your first UI app.")

# Set up the window
window = tk.Tk()
window.title("Greeting App")
window.geometry("300x150")

# Widgets
entry_label = tk.Label(window, text="Enter your name:")
entry_label.pack()

entry = tk.Entry(window)
entry.pack()

greet_button = tk.Button(window, text="Greet Me", command=greet)
greet_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

# Start the app
window.mainloop()