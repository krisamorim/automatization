from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title("Caminho dos arquivos")
        self.root.configure(background= '#1e3743')
        self.root.geometry('400x300')
        self.root.resizable(True, True)
        self.root.maxsize(width=500, height=500)
        self.root.minsize(width=300, height=300)


Application()