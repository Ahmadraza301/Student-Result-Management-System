from tkinter import*
from PIL import Image, ImageTk #pip Install
from tkinter import ttk, messagebox 
import sqlite3
from matplotlib import pyplot as plt

class summaryclass:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#ADEAEA")
        self.root.focus_force()
        #=======title=========
        title=Label(self.root, text="Result's Summary", font=("goudy old style",20, "bold"),bg="#033054", fg='white').place(x=10, y=15, width=1180, height=35)
        plt.plot([1,2,3],[4,5,6])
        plt.plot('infomation')
        plt.xlabel('a axis')
        plt.ylabel('yaxix')
        
        plt.show()
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=summaryclass(root)
    root.mainloop()  