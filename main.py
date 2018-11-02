from subprocess import STDOUT, check_output
from tkinter import *
from tkinter import filedialog, ttk
import os


class MyException(Exception):
    pass
def close():
    app.destroy()
    exit()
def browse():
    app.filename = filedialog.askopenfilename(initialdir="/", 
                                              title="Select file",
                                              filetypes=(("Python Files", "*.py"), ("Python Files (without console)", "*.pyw")))
    txt.insert("end", "\"{}\" File Selected.\n".format(app.filename))
    txt.see('end')
def getState(widget):
    if options["ext"] != widget["text"]:
        options["ext"] = widget["text"]
        txt.insert("end", "Build Setting:{}\n".format(options["ext"]))
        txt.see('end')

def start(ver=None, ext="exe"):
    if ext == "exe":
        # check_output("python{} setup.py build".format(ver), stderr=STDOUT, shell=True)
        txt.insert("end", "Building exe file from \"{}\" in that folder.\n".format(app.filename))
        txt.see('end')
    elif ext == "msi":
        txt.insert("end", "Building msi installer file from \"{}\" in that folder.\n".format(os.path.dirname(os.path.realpath(app.filename))))
        txt.see('end')
        # check_output("python{} setup.py bdist_msi".format(ver), stderr=STDOUT, shell=True)
    else:
        txt.insert("end", "You need to set build setting.\n")
        txt.see('end')

def check():
    txt.insert("end", "No update found.\n")
    txt.see('end')

options = {"ext":""}
app = Tk()
SW = app.winfo_screenwidth()
SH = app.winfo_screenheight()
WW = 0.32552083333333333333333333333333*SW
WH = 0.52083333333333333333333333333333*SH
app.geometry("{}x{}+{}+{}".format(int(WW), int(WH), int(SW/2-WW/2), int(SH/2-WH/2)))
app.title("Easy Python To Exe Converter")
app.resizable(False, False)
ttk.Style().configure("TButton", padding=1, font="Helvetica 12", relief="flat", background="#ccc")
 
lb = ttk.Button(app, text="Check for downloadable files", style="TButton", command=check)
lb.pack()
 
f1 = Frame(app)
f1.pack(fill=X, pady=10, padx=10)
entry = ttk.Entry(f1, font="Helvetica 14")
entry.pack(side="left", expand=1, fill=X)
browse = ttk.Button(f1, text="Browse", style="TButton", command=browse)
browse.pack(side="right")
 
f2 = Frame(app)
f2.pack()
 
R1 = ttk.Radiobutton(f2, text="MSI", value=1, command=lambda: getState(R1))
R2 = ttk.Radiobutton(f2, text="EXE", value=2, command=lambda: getState(R2))
 
R1.pack(side='left')
R2.pack(side='left')
B1 = ttk.Button(app, text="Start!", style="TButton", command=lambda: start(3, options["ext"].lower()))
B1.pack(pady=3)

txt = Text(app, relief='solid')
txt.pack(fill=BOTH, pady=10, padx=10)

app.mainloop()
