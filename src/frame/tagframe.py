import tkinter as tk

class TagFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        

        self.bt1 = tk.Button(self)
        self.bt1["text"] = "button"
        self.bt1.pack(side="left")
