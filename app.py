import tkinter as tk
from tkinter import filedialog, Text
import platform
import os

root = tk.Tk()
apps = []
filetype = ()

if platform.system == 'Windows':
    filetype = ("executables", "*.exe")
else:
    filetype = ("executables", "*.sh")
    

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps= tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def add_app():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/', title='Select file', filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)

    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

def run_apps():
    for app in apps:
        os.startfile(app);

canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text='Open File', padx=10, pady=5, fg='white', bg='#263D42', command=add_app)
openFile.pack()

runApps = tk.Button(root, text='Run Apps', padx=10, pady=5, fg='white', bg='#263D42', command=run_apps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',\n')