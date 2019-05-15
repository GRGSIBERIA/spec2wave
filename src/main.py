import tkinter as tk

window = tk.Tk()
window.title("Spec2Wave")
window.geometry("640x480")

menubar = tk.Menu(window)
window.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

window.mainloop()
