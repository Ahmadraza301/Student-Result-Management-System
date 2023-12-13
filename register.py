from tkinter import*
import tkinter as tk
import os
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#ADEAEA")
        
        #==================================
        #self.bg=ImageTk.PhotoImage(file="images/rbg.jpg")
        #bg=Label(self.root, image=self.bg).place()
        
#=Background Images for register pages =======================================================================     
        self.bg_img=Image.open("images/rbg.jpg")
        self.bg_img=self.bg_img.resize((1350, 700), Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=0, y=0, relwidth=1, relheight=1)
    
#=========registration ==========================================
        frame1=Frame(self.root, bg="lightgrey")
        frame1.place(x=250, y=100, width=800, height=500)
        
        #==Title=========================================
        title=Label(frame1, text="Register Here", font=("times new roman", 20, "bold"), bg="lightgrey", fg="green").place(x=300, y=30)
        #=row 1 =======================================================================================
        f_name=Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=50, y=80)
        self.txt_fname=Entry(frame1, font=("times new roman", 15))
        self.txt_fname.place(x=50, y=110, width=250)
        
        l_name=Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=450, y=80)
        self.txt_lname=Entry(frame1, font=("times new roman", 15))
        self.txt_lname.place(x=450, y=110, width=250)
        #= row 2===================================================================================
        
        contact=Label(frame1, text="Contact", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=50, y=150)
        self.txt_contact=Entry(frame1, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=180, width=250)
        
        email=Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=450, y=150)
        self.txt_email=Entry(frame1, font=("times new roman", 15))
        self.txt_email.place(x=450, y=180, width=250)
        #=row 3 ==================================================================================
        
        question=Label(frame1, text="Security question", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=50, y=220)
        self.cmb_question=ttk.Combobox(frame1, font=("times new roman", 15), state='readonly', justify=CENTER)
        self.cmb_question['values']=("Select", "your Favourite book", "your mother name", "childhood friend")
        self.cmb_question.place(x=50, y=250, width=250)
        self.cmb_question.current(0)
        
        answer=Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=450, y=220)
        self.txt_answer=Entry(frame1, font=("times new roman", 15))
        self.txt_answer.place(x=450, y=250, width=250)
        
        #=row 4 ====================================================================================
        password=Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=50, y=300)
        self.txt_password=Entry(frame1, font=("times new roman", 15))
        self.txt_password.place(x=50, y=330, width=250)
        
        confirm_password=Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black").place(x=450, y=300)
        self.txt_confirm_password=Entry(frame1, font=("times new roman", 15))
        self.txt_confirm_password.place(x=450, y=330, width=250)
        
        #=Terms and Conditions===============================================================================================
        self.var_chk=IntVar()
        chk=Checkbutton(frame1, text="Agree our Terms and Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 13)).place(x=200, y=380)
        #=============button
        btn_register=Button(frame1, text="Register", font=("times new roman", 20,"bold"), bg="green", fg="white", cursor="hand2", command=self.register_data).place(x=200, y=430, width=120, height=40)
    
        btn_login=Button(frame1, text="Login", font=("times new roman", 20,"bold"), bg="green", fg="white", cursor="hand2", command=self.login_window).place(x=500, y=430, width=120, height=40)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")
    
    
    
    
    
    
#=======to clear the functions======================================================================
    def clear(self):
            self.txt_fname.delete(0,END)
            self.txt_lname.delete(0,END)
            self.txt_contact.delete(0,END)
            self.txt_email.delete(0,END)
            self.txt_answer.delete(0, END)
            self.txt_password.delete(0,END)
            self.txt_confirm_password.delete(0,END)
            self.cmb_question.current(0)
    
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_confirm_password.get()=="" :
                messagebox.showerror("Error","All Fields Are required", parent=self.root)
        elif  self.txt_password.get()!= self.txt_confirm_password.get():
                messagebox.showerror("Error","Password doesn't match", parent=self.root)
        elif self.var_chk.get()==0:
                messagebox.showerror("Error","Agree our terms and Conditions First", parent=self.root)

                
        else:
             try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?", (self.txt_email.get(), ))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                        messagebox.showerror("Error","User Already Present try different email ", parent=self.root)
                else:
                        cur.execute("insert into employee (f_name, l_name, contact, email, question, answer, password) values(?, ? ,? ,? ,? ,? ,?)",
                            (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.cmb_question.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()
                                ))
                con.commit()
                con.close()       
                messagebox.showinfo("Success","Registration has been done", parent=self.root) 
                self.clear()
                self.login_window()   
             except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}", parent=self.root)

        
root=Tk()
obj=register(root)
mainloop()
