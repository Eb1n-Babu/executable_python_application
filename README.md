📦 1. Install PyInstaller

pip install pyinstaller


📝 2. Prepare Your GUI Script
Save this as app.py:

"""pip install pyinstaller
pyinstaller --onefile main.py"""

import tkinter as tk

def greet():
    label.config(text=f"Hello, {entry.get()}!")

root = tk.Tk()
root.title("Greeting App")
root.geometry("300x150")  # Optional: Set window size

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Greet", command=greet)
button.pack()

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
🎨 3. Add Your Icon

Make sure you have an .ico file (example: app_icon.ico) in the same directory or provide the full path.

🛠️ 4. Build Executable (Suppress CMD + Icon)
Run this in your terminal or command prompt:

pyinstaller --onefile --windowed --icon=app_icon.ico app.py

🔍 Explanation:
- --onefile: Packs everything into one .exe
- --windowed: No CMD window (ideal for GUI apps)
- --icon: Sets custom icon

📁 5. Find and Run Your App

- Navigate to the dist folder.
- You’ll find app.exe. Double-click it—no console, just your interface!

💡 Optional bonus: If you're building many apps, I can help create a reusable CLI shortcut or wrapper script to automate this entire flow. Just say the word.
#   e x e c u t a b l e _ p y t h o n _ a p p l i c a t i o n  
 