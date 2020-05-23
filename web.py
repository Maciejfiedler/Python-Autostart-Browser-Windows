import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import webbrowser
import os


class App(object):

    urls = []
    

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Start Browser Windows")
        self.root.resizable(False, False)
        self.root.iconbitmap('./assets/open_in_browser-24px.ico')
        itemselected = IntVar()
        frame = ttk.Frame(self.root)
        frame.pack(expand=False, fill='both')
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame)
        scrollbar.grid(row=1, column=2, sticky="nse")
        # Listbox
        urllist = tk.Listbox(
            frame, selectmode=MULTIPLE, yscrollcommand=scrollbar.set, width=90, height=20)
        urllist.grid(pady=10, padx=10)
        # Entry
        urlinput = ttk.Entry(frame, width=50)
        urlinput.grid(row=0, column=1, sticky='n', pady=10)
        # Checkbox
        cleartextcheckbox = ttk.Checkbutton(frame, text = "Clear Text", variable = itemselected,command = lambda:  print(itemselected.get()))
       
        cleartextcheckbox.grid(row=0, column=1, sticky='nw', pady=10, padx = 50)
        # Pack
        urllist.grid(row=1, column=1)
        scrollbar.config(command=urllist.yview)
        # Add Button
        addbutton = ttk.Button(
            frame, text='Add', command=lambda: self.addurl(urlinput, frame, scrollbar, urllist,itemselected))
        addbutton.grid(row=0, column=1, sticky='ne', pady=10, padx=20)
        # Start Button
        startbuttoon = ttk.Button(
            frame, text='Start', command=lambda: self.starturl())
        startbuttoon.grid(row=2, column=1, sticky='ne', pady=10, padx=20)
        # Clear Button
        startbuttoon = ttk.Button(
            frame, text='Clear', command=lambda: self.clearlist(urllist))
        startbuttoon.grid(row=2, column=0, sticky='ne', pady=10, padx=20)
        # Delete Button
        deleteButton = ttk.Button(
            frame, text='Delete',command=lambda: self.deleteurl(urllist))
        deleteButton.grid(row=0, column=0, sticky='ne', pady=10, padx=20)

        if os.path.isfile('urls.txt'):
            with open('urls.txt', 'r') as f:
                tempApps = f.read()
                tempApps = tempApps.split(',')
                apps = [x for x in tempApps if x.strip()]
                self.urls.clear()
                for app in apps:
                    self.urls.insert(0, app)
                    urllist.insert(END, app)
                    urlinput.delete(0, END)

    def addurl(self, entry, frame, scrollbar, listbox,itemselected):
        if entry.get().strip():
            # Add URL
            with open('urls.txt', 'w') as file:
                for url in self.urls:
                    file.write(url + ',')
            self.urls.insert(0, entry.get())
            print(self.urls)
            # Open URL
            for url in self.urls:
                listbox.insert(END, url)
                if  itemselected.get() == 1:
                    print("1")
                    entry.delete(0, END)
                
                break

    def starturl(self):
        for url in self.urls:
            webbrowser.open(url)

    def clearlist(self, listbox):
        if tk.messagebox.askyesno(title="Delete All?", default=NO, icon=WARNING, message="Do you want to delete all URLs from the list?",):
            # Clear List
            listbox.delete(0, END)
            self.urls.clear()
            open('urls.txt', 'w').close()
    def deleteurl(self,listbox):
        for url in listbox.curselection():
            listbox.delete(url)
            self.urls.pop(url)
            print(url)


app = App()
app.root.mainloop()

