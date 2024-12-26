from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

file = None

def new_file() :
    global file
    text.delete("1.0", END)
    window.title("Untitled - Notepad")

def open_file() :
    global file
    file = filedialog.askopenfilename(initialdir="C:\\Users\\nitesh kumavat\\Desktop - Copy\\Tkinter",
                                          title="Open file okay?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))
    if file == "" :
        file = None
    else :
        window.title(f"{os.path.basename(file)} - Notepad")

        read_file = open(file=file, mode="r")
        text.insert("1.0", read_file.read())
        read_file.close()



def save_file():
    global file
    if not file:
        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
        )
        if not file:
            return

    try:
        with open(file, "w") as write_file:
            write_file.write(text.get("1.0", END).rstrip())
        window.title(f"{os.path.basename(file)} - Notepad")
    except Exception as e:
        print(f"Error saving file: {e}")


def copy() :
    text.event_generate("<<Copy>>")

def cut() :
    text.event_generate("<<Cut>>")

def paste() :
    text.event_generate("<<Paste>>")

def info() :
    messagebox.showinfo("Notepad", "It is created by Nitesh Kumavat")



window = Tk()
menubar = Menu(window)
window.config(menu=menubar)
window.title("Untitled - Notepad")


filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)

aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="Notepad info", command=info)

scroll = Scrollbar(window)
scroll.pack(side=RIGHT, fill=Y)
text = Text(window, yscrollcommand=scroll.set, font=("Arial", 10))
text.pack(side=LEFT, fill=BOTH)



window.mainloop()