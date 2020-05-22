import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
import webbrowser


class App(object):

    urls = []

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Autostart Browser Windows")
        self.root.geometry('600x300')
        self.root.resizable(False, False)
        frm = ttk.Frame(self.root)
        frm.pack(expand=False, fill='both')
        scrollbar = ttk.Scrollbar(frm)
        scrollbar.pack(side=RIGHT, fill=Y)
        urlinput = ttk.Entry(frm, width=80)
        urlinput.grid(row=0, column=1, sticky=W, padx=10)
        urlbutton = ttk.Button(
            frm, text='Add', command=lambda: self.addurl(urlinput, frm, scrollbar))
        urlbutton.grid(row=0, column=2, sticky=W)

    def addurl(self, input, frame, scrollbar):
        # Add URL
        self.urls.insert(0, input.get())
        print(self.urls)
        # Show URL
        listurl = Listbox(frame, yscrollcommand=scrollbar.set)
        for url in self.urls:
            listurl.insert(END, url)
        listurl.pack()
        scrollbar.config(command=listurl.yview)


app = App()
app.root.mainloop()
