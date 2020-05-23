import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
import webbrowser
import os


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

        if os.path.isfile('urls.txt'):
            with open('urls.txt', 'r') as f:
                tempApps = f.read()
                tempApps = tempApps.split(',')
                apps = [x for x in tempApps if x.strip()]
                self.urls.clear()
                for app in apps:
                    self.urls.insert(0,app)
                    urllist.insert(END, app)
                    urlinput.delete(0, END)

    def addurl(self, entry, frame, scrollbar, listbox):
        if entry.get().strip():
            # Add URL
            with open('urls.txt', 'w') as file:
                for url in self.urls:
                    file.write(url + ',')
            self.urls.insert(0, entry.get())
            print(self.urls)
            # Show URL
            for url in self.urls:
                listbox.insert(END, url)
                entry.delete(0, END)
                break;


app = App()
app.root.mainloop()
