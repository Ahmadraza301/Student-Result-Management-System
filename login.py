from tkinter import*
import os
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import sqlite3
from PIL import Image, ImageTk

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Pages")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#ADEAEA")
        
        
        
        self.bg_img=Image.open("images/rbg.jpg")
        self.bg_img=self.bg_img.resize((1350, 700), Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        #=========Login Frame ==========================
        frame1=Frame(self.root, bg="lightgrey")
        frame1.place(x=250, y=100, width=800, height=500)
        
        #==Title=========================================
        title=Label(frame1, text="Login Here", font=("times new roman", 30, "bold"), bg="lightgrey", fg="red").place(x=250, y=30)
        #==========================================================================================================================
        email=Label(frame1, text="Email Id", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=250, y=120)
        self.txt_email=Entry(frame1, font=("times new roman", 15))
        self.txt_email.place(x=250, y=150, width=250)
        #===============================================================================================================
        password=Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=250, y=210)
        self.txt_password=Entry(frame1, font=("times new roman", 15))
        self.txt_password.place(x=250, y=240, width=250)
        
        
        
        btn_registration=Button(frame1, text="Register New Account", font=("times new roman",14),bg="lightgrey", bd=0, fg="red", cursor="hand2", command=self.register_window).place(x=310, y=270, width=200, height=20)
        btn_login=Button(frame1, text="Login", font=("times new roman", 20,"bold"), bg="green", fg="white", cursor="hand2", command=self.login).place(x=315, y=300, width=120, height=40)

    
    def register_window(self):
        self.root.destroy()
        import register
        
    
    
    
    
    
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error", "All field are mandetory", parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(), self.txt_password.get()))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error", "Invalid username and password", parent=self.root)
                    

                else:
                    messagebox.showinfo("Success", f"Welcome to Student Query and Notification System:\n {self.txt_email.get()}", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                    con.close()
                    
                    
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
    



root=Tk()
obj=login(root)
mainloop()
    