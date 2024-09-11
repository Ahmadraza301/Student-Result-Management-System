from tkinter import*
from PIL import Image, ImageTk 
#pip install pillow
from tkinter import ttk, messagebox 
import sqlite3
class courseclass:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#ADEAEA")
        self.root.focus_force()
        #=======title=========
        title=Label(self.root, text="Manage Course details", font=("goudy old style",20, "bold"),bg="#033054", fg='white').place(x=10, y=15, width=1180, height=35)
        #=================Variables ============================================================================
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        #==============widgets============
        lbl_CourseName=Label(self.root, text="Doc. Name:", font=("goudy old style", 15, "bold"), bg='white').place(x=10, y=60)
        lbl_duration=Label(self.root, text="duration:", font=("goudy old style", 15, "bold"), bg='white').place(x=10, y=100)
        lbl_Description=Label(self.root, text="Query:", font=("goudy old style", 15, "bold"), bg='white').place(x=10, y=180)
        #=============Entry fields====================================
        
        self.txt_CourseName=Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, "bold"), bg='white')
        self.txt_CourseName.place(x=150, y=60, width=500)
        txt_duration=Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"), bg='white').place(x=150, y=100, width=500)
      
        self.txt_description=Text(self.root, font=("goudy old style", 15, "bold"), bg='white')
        self.txt_description.place(x=150, y=180, width=500, height=200)
        
        #=============buttons sections======================================================================================================
        self.btn_add=Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update=Button(self.root, text="update", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete=Button(self.root, text="delete", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear=Button(self.root, text="clear", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)
        
        #================Search panel============================================================
        self.var_search=StringVar()
        lbl_search_CourseName=Label(self.root, text="Doc. Name:", font=("goudy old style", 15, "bold"), bg='white').place(x=720, y=60)
        txt_search_CourseName=Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg='white').place(x=870, y=60, width=180)
        btn_search=Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)
        #========Content=========================================================================================================
        self.c_frame=Frame(self.root, bd=2, relief=RIDGE)
        self.c_frame.place(x=720, y=100, width=470, height=340)
        
        
        
        scrolly=Scrollbar(self.c_frame, orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame, orient=HORIZONTAL)

        self.CourseTable=ttk.Treeview(self.c_frame, columns=("cid", "name", "duration", "charges", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        
        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Doc. Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Query")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=150)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#========================Exceptional Handling ========================================================================== 
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0', END)
        self.txt_CourseName.config(state=NORMAL)
        
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Document Name must be Required", parent=self.root)
            else:
                cur.execute("Select * from course where name=?", (self.var_course.get(),))   
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Plaese Slelect the Document from List ", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from Document where name=?", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Document deleted successfully", parent=self.root)
                        self.clear()
                    
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
                
    
    
    
    
    
    def get_data(self, ev):
        self.txt_CourseName.config(state='readonly')
        self.txt_CourseName
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r) 
        row=content["values"] 
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        #self.var_course.set(row[4])
        self.txt_description.delete('1.0', END)
        self.txt_description.insert(END, row[4])
        
#=================for Save button=============================================================             
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Document Name must be Required", parent=self.root)
            else:
                cur.execute("Select * from course where name=?", (self.var_course.get(),))   
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Document Name Already Exist ", parent=self.root)
                else:
                    cur.execute("Insert into course (name, duration, charges, description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)

                    ))
                    con.commit()  
                    messagebox.showinfo("success", "Document Added Successfully", parent=self.root)
                    self.show() 

                     
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
#=============================for update Button==========================================================            
    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Document Name must be Required", parent=self.root)
            else:
                cur.execute("Select * from course where name=?", (self.var_course.get(),))   
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Document from List", parent=self.root)
                else:
                    cur.execute("update course set duration=?, charges=?, description=? where name=? ",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        self.var_course.get()

                    ))
                    con.commit()  
                    messagebox.showinfo("success", "Document updated Successfully", parent=self.root)
                    self.show() 

                     
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
                        
#============To Show the Data=====================================================================            
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from course")   
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows :
                self.CourseTable.insert('', END, values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")  
#=============To search the data=======================================================================================          
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"Select * from course where name LIKE '%{self.var_search.get()}%'")   
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows :
                self.CourseTable.insert('', END, values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")                 


            
if __name__=="__main__":
    root=Tk()
    obj=courseclass(root)
    root.mainloop()        
        