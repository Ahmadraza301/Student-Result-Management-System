from tkinter import*
from PIL import Image, ImageTk #pip Install  
from course import courseclass
from student import StudentClass
from result import Resultclass
import sqlite3
import os
from resultview import resultviewClass
from summary import summaryclass
from tkinter import messagebox

#=Starting with class and constructor=====================================================
class CMS:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#ADEAEA")
        #=======icons=========
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        #=======title=========
        title=Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash, font=("goudy old style",20, "bold"),bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)
        #=========Menu=========
        M_Frame=LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=250, height=500)
        
        #===========Frame for View Count==============================================
        
        
        btn_course=Button(M_Frame, text="Add Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student=Button(M_Frame, text="Add Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=20, y=75, width=200, height=40)
        btn_result=Button(M_Frame, text=" Add Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=20, y=145, width=200, height=40)
        btn_view=Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.view_result).place(x=20, y=215, width=200, height=40)
        btn_summary=Button(M_Frame, text="View Summary", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.view_summary).place(x=20, y=285, width=200, height=40)

        btn_logout=Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.logout).place(x=20, y=355, width=200, height=40)
        btn_exit=Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit).place(x=20, y=425, width=200, height=40)
        #============content_window==========
        self.bg_img=Image.open("images/cms.png")
        self.bg_img=self.bg_img.resize((900, 500), Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=250, y=100, width=920, height=420)
        #self.lbl_bg=Label(self.root, image=self.bg_img).place(x=300, y=180, width=920, height=350)
        
        #===Another Frame============================
        u_Frame=LabelFrame(self.root, text="Updates", font=("times new roman", 15), bg="white")
        u_Frame.place(x=1020, y=70, width=250, height=500)
        
        self.lbl_course=Label(self.root, text="Total Course\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#033054", fg="white")
        self.lbl_course.place(x=1050, y=100, width=200, height=80)
        
        self.lbl_student=Label(self.root, text="Total Student\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#033054", fg="white")
        self.lbl_student.place(x=1050, y=280, width=200, height=80)
        
        self.lbl_result=Label(self.root, text="Total Result\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#033054", fg="white")
        self.lbl_result.place(x=1050, y=460, width=200, height=80)
        
        
        #Dtabasese Connections=============
        
        footer=Label(self.root, text="Student Result Management System\nContact Us for any Technical Issue: 9876543210", font=("goudy old style",12),bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from course")   
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Course\n[{str(len(cr))}]")
            
            cur.execute("Select * from student")   
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total student\n[{str(len(cr))}]")
            
            
            cur.execute("Select * from result")   
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Result\n[{str(len(cr))}]")
            
            
            self.lbl_course.after(200, self.update_details)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")  
        
    
    
    
    
    
    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=courseclass(self.new_win)
        
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
        
        
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Resultclass(self.new_win)
        
        
    def view_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultviewClass(self.new_win)
        
        
        
    def view_summary(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=summaryclass(self.new_win)
        
    
    
    def logout(self):
        op=messagebox.askyesno("confirm", "Do really wanna logout?", parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
    
    
    def exit(self):
        op=messagebox.askyesno("confirm", "Do really wanna Exit?", parent=self.root)
        if op==True:
            self.root.destroy()       
        
if __name__=="__main__":
    root=Tk()
    obj=CMS(root)
    root.mainloop()        