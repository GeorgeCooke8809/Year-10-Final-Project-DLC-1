import os
from tkinter import *
from tkinter import filedialog

def select():
    global path
    path = filedialog.askdirectory(initialdir = "/", title = "Select Main Game Folder")
    
def contin():
    global path
    
    if path != "":
        frame_1.pack_forget()
        loading = Label(root, text = "Loading...", font = ("Monoton", 15))
        loading.pack(anchor = "center")

path = ""

root = Tk()
root.geometry("500x150")
root.title("Install DLC 1")

frame_1 = Frame(root, padx = 10, pady = 10)
frame_1.rowconfigure(0)
frame_1.rowconfigure(1)
frame_1.rowconfigure(2)

install_txt = Label(frame_1, text = "Install DLC To:", font = ("Monoton", 15, "bold"))
install_txt.pack(anchor = "w", expand = True, fill = "x")

select_path = Button(frame_1, text = "Select Folder", command = select, font = ("Monoton", 10), anchor = "center", justify = "center")
select_path.pack(anchor = "center", expand = True, fill = "x", pady = 10)

cont = Button(frame_1, text = "Continue", command = contin, font = ("Monoton", 10), anchor = "center", justify = "center")
cont.pack(anchor = "center", expand = True, fill = "x")

frame_1.pack(fill = "x")

root.mainloop()