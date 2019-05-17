import tkinter as tk
from src.menubar.menubar import Menu
from src.frame.tagframe import TagFrame

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title("Image Viewer")
        self.master.geometry("640x480")

        self.master["menu"] = Menu()
        
        self.pack(fill="x")

        self.tag1 = TagFrame(self)
        self.tag1.pack(side="left")

        self.tag2 = TagFrame(self)
        self.tag2.pack(side="left")


def Main():
    window = Window()
    window.pack()
    window.mainloop()

if __name__ == "__main__":
    Main()
