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
        self.root.resizable(True, True)
        frame = ttk.Frame(self.root)
        frame.pack(expand=False, fill='both')
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame)
        scrollbar.grid(row=1, column=2, sticky="nse")
        # Listbox
        urllist = tk.Listbox(
            frame, yscrollcommand=scrollbar.set, width=90, height=20)
        urllist.grid(pady=10, padx=10)
        # Entry
        urlinput = ttk.Entry(frame, width=50)
        urlinput.grid(row=0, column=1, sticky='n', pady=10)
        # Pack
        urllist.grid(row=1, column=1)
        scrollbar.config(command=urllist.yview)
        # Button
        urlbutton = ttk.Button(
            frame, text='Add', command=lambda: self.addurl(urlinput, frame, scrollbar, urllist))
        urlbutton.grid(row=0, column=1, sticky='ne', pady=10, padx=20)

    def addurl(self, entry, frame, scrollbar, listbox):
        # Add URL
        self.urls.insert(0, entry.get())
        print(self.urls)
        # Show URL
        for url in self.urls:
            listbox.insert(END, url)
            entry.delete(0, END)


app = App()
app.root.mainloop()
