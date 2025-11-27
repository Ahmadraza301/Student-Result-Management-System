from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3, os, sys


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


class Result:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+200+250")
        self.root.config(bg="white")
        self.root.focus_force()

        #------------- title --------------
        title = Label(self.root, text="Manage Course Details", 
                      font=("goudy old style", 20, "bold"), 
                      bg="orange", fg="#262626").place(x=10, y=15, width=1180, height=50)

        #-------------- variables -----------------
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        #-------------- widgets -------------------
        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=340)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, 
                                        font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")

        Button(self.root, text="Search", command=self.search, font=("goudy old style", 15, "bold"), 
               bg="#03a9f4", fg="white", cursor="hand2").place(x=500, y=100, width=100, height=28)

        Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), 
              bg="lightyellow", state='readonly').place(x=280, y=160, width=320)
        Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, "bold"), 
              bg="lightyellow", state='readonly').place(x=280, y=220, width=320)
        Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, "bold"), 
              bg="lightyellow").place(x=280, y=280, width=320)
        Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, "bold"), 
              bg="lightyellow").place(x=280, y=340, width=320)

        Button(self.root, text="Submit", command=self.add, font=("goudy old style", 15), 
               bg="lightgreen", activebackground="lightgreen", cursor="hand2").place(x=300, y=420, width=120, height=35)
        Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), 
               bg="lightgray", activebackground="lightgray", cursor="hand2").place(x=430, y=420, width=120, height=35)

        #----------------- image ------------------
        try:
            image_path = resource_path("images/result.jpg")

            self.bg_img = Image.open(image_path)
            self.bg_img = self.bg_img.resize((500, 300))
            self.bg_img = ImageTk.PhotoImage(self.bg_img)

            Label(self.root, image=self.bg_img).place(x=650, y=100)
        except Exception as e:
            # Create fallback image
            fallback_img = Image.new('RGB', (500, 300), color='#f0f0f0')
            from PIL import ImageDraw
            draw = ImageDraw.Draw(fallback_img)
            draw.text((250, 150), "Result Image\nNot Available", fill="#333333", anchor="mm")
            self.bg_img = ImageTk.PhotoImage(fallback_img)
            Label(self.root, image=self.bg_img).place(x=650, y=100)

    #-----------------------------------------------------------------------------------------------------------
    def fetch_roll(self):
        con = sqlite3.connect(database=resource_path("rms.db"))
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows) > 0:
                self.roll_list = [row[0] for row in rows]
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            con.close()

    def search(self):
        con = sqlite3.connect(database=resource_path("rms.db"))
        cur = con.cursor()
        try:
            cur.execute("select name, course from student where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row is not None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            con.close()

    def add(self):
        con = sqlite3.connect(database=resource_path("rms.db"))
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Student Record not found!!!", parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?", (self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Result already present", parent=self.root)
                else:
                    per = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                    cur.execute("insert into result (roll, name, course, marks_ob, full_marks, per) values(?,?,?,?,?,?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            con.close()

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Result(root)
    root.mainloop()
