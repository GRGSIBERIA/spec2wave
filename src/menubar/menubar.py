import tkinter as tk 

class Menu(tk.Menu):
    def __init__(self, master=None):
        tk.Menu.__init__(self, master)
        self.CreateFileMenu()
        self.CreateHelpMenu()
    
    def CreateFileMenu(self):
        filemenu = tk.Menu(self)
        filemenu.add_command(label="Update Files")
        filemenu.add_command(label="Import Directory")
        filemenu.add_command(label="Exit")
        self.add_cascade(menu=filemenu, label="File")

    def CreateHelpMenu(self):
        helpmenu = tk.Menu(self)
        helpmenu.add_command(label="Version")
        self.add_cascade(menu=helpmenu, label="Help")
