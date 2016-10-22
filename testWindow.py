'''everything for the window object is
created here'''

import tkinter as tk

class testWindow(tk.Tk):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        #rest goes here for the GUI
        self.widgets()
    #good containter for stuff
    def widgets(self):
        #good menu
        menubar = tk.Menu(root)
        #btw, no () on functions in these parameters
        fileMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Save")
        fileMenu.add_separator()
        fileMenu.add_command(label="Load")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.quit)
        #connections
        conMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Connections", menu=conMenu)
        conMenu.add_command(label="Add Connection")
        conMenu.add_separator()
        conMenu.add_command(label="Manage Connection")
        conMenu.add_separator()
        conMenu.add_command(label="Connection Info")

        #help

        helpMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpMenu)#if this points to the main menu, it freezes your comp
        helpMenu.add_command(label="Help Database")
        helpMenu.add_separator()
        helpMenu.add_command(label="About")
        root.config(menu=menubar)
    def quit(self):
        self.root.destroy()
if __name__ == "__main__":
    root = tk.Tk()
    root.title("RPG Aid")
    root.geometry("500x400")
    app = testWindow(root)
    root.mainloop()
