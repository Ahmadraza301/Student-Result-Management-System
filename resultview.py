from tkinter import*
from PIL import Image, ImageTk #pip Install
from tkinter import ttk, messagebox 
import sqlite3
class resultviewClass:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Query and Notification system")
        self.root.geometry("1200x480+80+0")
        self.root.config(bg="#ADEAEA")
        self.root.focus_force()
        #=======title=========
        title=Label(self.root, text="View Query Result", font=("goudy old style",20, "bold"),bg="#033054", fg='black').place(x=10, y=15, width=1180, height=35)
#========Searching the result================================================================================================
        self.var_search=StringVar()
        self.var_id=""
        lbl_search=Label(self.root, text="search by | Roll No.:", font=("goudy old style", 20, "bold"), bg="white").place(x=350, y=70)
        txt_search=Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20), bg="white").place(x=600, y=70, width=100)
        btn_search=Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.search).place(x=350, y=120, width=100, height=35)
        btn_clear=Button(self.root, text="clear", font=("goudy old style", 15, "bold"), bg="lightgrey", fg="white", cursor="hand2", command=self.clear).place(x=480, y=120, width=100, height=35)
        
#========================================================================================================================================================================================
        lbl_roll=Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=20, y=70, width=150, height=50)
        lbl_name=Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=20, y=120, width=150, height=50)
        lbl_course=Label(self.root, text="course", font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=20, y=170, width=150, height=50)
        lbl_marks=Label(self.root, text="Query active", font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=20, y=220, width=150, height=50)
        lbl_full=Label(self.root, text="Query solved", font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=20, y=270, width=150, height=50)
        lbl_per=Label(self.root, text="Percentage", font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=20, y=320, width=150, height=50)

#==============================================================================================================================================================================================
        self.roll=Label(self.root, font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.roll.place(x=170, y=70, width=150, height=50)
        self.name=Label(self.root, font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.name.place(x=170, y=120, width=150, height=50)
        self.course=Label(self.root, font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.course.place(x=170, y=170, width=150, height=50)
        self.marks=Label(self.root, font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.marks.place(x=170, y=220, width=150, height=50)
        self.full=Label(self.root, font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.full.place(x=170, y=270, width=150, height=50)
        self.per=Label(self.root, font=("goudy old style", 15, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.per.place(x=170, y=320, width=150, height=50)
#=======Images for the windows=========================================================================================================================
        self.bg_img=Image.open("images/query2.jpg")
        self.bg_img=self.bg_img.resize((500, 300), Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=600, y=130)

#=========================================================================================================================================================================================

        btn_delete=Button(self.root, text="delete", font=("goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2", command=self.delete).place(x=120, y=400, width=100, height=35)
        
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error", "Roll No. Must be required", parent=self.root)
            else:
                cur.execute("Select * from result where roll=?", (self.var_search.get(),))   
                row=cur.fetchone()
                if row!=None:
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                     messagebox.showerror("Error", "No record found", parent=self.root) 
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
            
            
    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")
        
        
        
#===========Work On delete button================================================================        
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Result First!!!", parent=self.root)
            else:
                cur.execute("Select * from result where rid=?", (self.var_id,))   
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid result ", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?", (self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete", " deleted successfully", parent=self.root)
                        self.clear()
                    
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk()
    obj=resultviewClass(root)
    root.mainloop()      