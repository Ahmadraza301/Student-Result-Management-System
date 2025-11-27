import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
from datetime import datetime
import sqlite3
from math import sin, cos, radians
import threading
import os
import sys


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+110+80")
        self.root.config(bg="white")

        # Initialize counters
        self.course_count = 0
        self.student_count = 0
        self.result_count = 0

        # Image placeholders
        self.logo_dash = None
        self.bg_img = None
        self.clock_bg = None
        self.clock_img = None

        # Setup UI
        try:
            self.load_images()
            self.setup_ui()
            self.start_background_tasks()
        except Exception as e:
            messagebox.showerror("Initialization Error", f"Failed to initialize application: {str(e)}")
            self.root.destroy()

    def load_images(self):
        """Load all required images with fallback options."""
        try:
            # Use resource_path for proper path resolution
            logo_path = resource_path("images/logo_p.png")
            if os.path.exists(logo_path):
                self.logo_dash = ImageTk.PhotoImage(Image.open(logo_path))
            else:
                # Create a fallback logo
                blank_logo = Image.new('RGB', (50, 50), color='#033054')
                draw = ImageDraw.Draw(blank_logo)
                draw.text((25, 25), "SRM", fill="white", anchor="mm")
                self.logo_dash = ImageTk.PhotoImage(blank_logo)

            bg_path = resource_path("images/bg.png")
            if os.path.exists(bg_path):
                bg_img = Image.open(bg_path)
                self.bg_img = ImageTk.PhotoImage(bg_img.resize((920, 350)))
            else:
                # Create a fallback background
                blank_bg = Image.new('RGB', (920, 350), color='#f0f0f0')
                draw = ImageDraw.Draw(blank_bg)
                draw.text((460, 175), "Student Result\nManagement System", fill="#333333", anchor="mm", font=ImageFont.load_default())
                self.bg_img = ImageTk.PhotoImage(blank_bg)

            clock_bg_path = resource_path("images/c.png")
            if os.path.exists(clock_bg_path):
                self.clock_bg = Image.open(clock_bg_path).resize((300, 300))
            else:
                self.clock_bg = Image.new('RGB', (300, 300), color='#081923')

        except Exception as e:
            print(f"Image loading error: {e}")
            # Create basic fallback images
            self.create_fallback_images()

    def create_fallback_images(self):
        """Create basic fallback images when loading fails"""
        try:
            # Fallback logo
            blank_logo = Image.new('RGB', (50, 50), color='#033054')
            draw = ImageDraw.Draw(blank_logo)
            draw.text((25, 25), "SRM", fill="white", anchor="mm")
            self.logo_dash = ImageTk.PhotoImage(blank_logo)

            # Fallback background
            blank_bg = Image.new('RGB', (920, 350), color='#f0f0f0')
            draw = ImageDraw.Draw(blank_bg)
            draw.text((460, 175), "Student Result\nManagement System", fill="#333333", anchor="mm")
            self.bg_img = ImageTk.PhotoImage(blank_bg)

            # Fallback clock background
            self.clock_bg = Image.new('RGB', (300, 300), color='#081923')
        except Exception as e:
            print(f"Fallback image creation failed: {e}")

    def setup_ui(self):
        """Setup all UI components."""
        title = tk.Label(
            self.root,
            text="Student Result Management System",
            compound=tk.LEFT,
            padx=10,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=50)

        # Menu Frame
        M_Frame = tk.LabelFrame(
            self.root,
            text="Menu",
            font=("times new roman", 15),
            bg="white"
        )
        M_Frame.place(x=10, y=70, width=1330, height=80)

        buttons = [
            ("Course", self.add_course, 20),
            ("Student", self.add_student, 280),
            ("Result", self.add_result, 540),
            ("View Result", self.add_report, 800),
            ("Exit", self.exit, 1060)
        ]

        for text, command, x_pos in buttons:
            btn = tk.Button(
                M_Frame,
                text=text,
                command=command,
                font=("goudy old style", 15, "bold"),
                bg="#0b5377",
                fg="white",
                cursor="hand2"
            )
            btn.place(x=x_pos, y=5, width=250, height=40)

        # Background Image or Fallback
        if self.bg_img:
            self.lbl_bg = tk.Label(self.root, image=self.bg_img)
            self.lbl_bg.place(x=400, y=180, width=920, height=350)
        else:
            fallback_bg = tk.Frame(self.root, bg="lightgray")
            fallback_bg.place(x=400, y=180, width=920, height=350)
            tk.Label(
                fallback_bg,
                text="Application Content",
                font=("Arial", 24),
                bg="lightgray"
            ).pack(expand=True)

        # Info Labels
        self.lbl_course = tk.Label(
            self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20),
            bd=10, relief=tk.RIDGE, bg="#e43b06", fg="white"
        )
        self.lbl_course.place(x=400, y=540, width=300, height=100)

        self.lbl_student = tk.Label(
            self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20),
            bd=10, relief=tk.RIDGE, bg="#0676ad", fg="white"
        )
        self.lbl_student.place(x=710, y=540, width=300, height=100)

        self.lbl_result = tk.Label(
            self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20),
            bd=10, relief=tk.RIDGE, bg="#038074", fg="white"
        )
        self.lbl_result.place(x=1020, y=540, width=300, height=100)

        # Clock
        self.lbl = tk.Label(
            self.root,
            text="\nClock",
            font=("Book Antiqua", 25, "bold"),
            fg="white",
            compound=tk.BOTTOM,
            bg="#081923",
            bd=0
        )
        self.lbl.place(x=10, y=180, height=450, width=350)

        # Footer
        footer = tk.Label(
            self.root,
            text="Student Result Management System\nContact Us: 7058930166",
            font=("goudy old style", 12),
            bg="#262626",
            fg="white"
        )
        footer.pack(side=tk.BOTTOM, fill=tk.X)

    def start_background_tasks(self):
        self.update_clock()
        self.update_counts()

    def update_clock(self):
        try:
            now = datetime.now().time()
            hr = (now.hour % 12) * 30
            min_ = now.minute * 6
            sec_ = now.second * 6

            clock = Image.new("RGB", (400, 400), (8, 25, 35))
            draw = ImageDraw.Draw(clock)

            if self.clock_bg:
                clock.paste(self.clock_bg, (50, 50))
            else:
                draw.ellipse((50, 50, 350, 350), outline="white", width=2)

            origin = (200, 200)
            draw.line([origin, (200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr)))], fill="#DF005E", width=4)
            draw.line([origin, (200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_)))], fill="white", width=3)
            draw.line([origin, (200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_)))], fill="yellow", width=2)
            draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")

            self.clock_img = ImageTk.PhotoImage(clock)
            self.lbl.config(image=self.clock_img)

        except Exception as e:
            print(f"Clock update error: {e}")
            self.lbl.config(text=f"\n{datetime.now().strftime('%H:%M:%S')}", image='')

        self.root.after(1000, self.update_clock)

    def update_counts(self):
        def fetch_counts():
            try:
                # Use resource_path for database
                db_path = resource_path("rms.db")
                con = sqlite3.connect(database=db_path)
                cur = con.cursor()
                cur.execute("SELECT COUNT(*) FROM course")
                self.course_count = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM student")
                self.student_count = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM result")
                self.result_count = cur.fetchone()[0]
                con.close()
            except Exception as e:
                print(f"Database error: {e}")
                self.course_count, self.student_count, self.result_count = 0, 0, 0

            self.root.after(0, self.update_count_labels)

        threading.Thread(target=fetch_counts, daemon=True).start()
        self.root.after(5000, self.update_counts)

    def update_count_labels(self):
        self.lbl_course.config(text=f"Total Courses\n[{self.course_count}]")
        self.lbl_student.config(text=f"Total Students\n[{self.student_count}]")
        self.lbl_result.config(text=f"Total Results\n[{self.result_count}]")

    def add_course(self):
        try:
            from course import Course
            self.new_win = tk.Toplevel(self.root)
            self.new_obj = Course(self.new_win)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Course window: {str(e)}")

    def add_student(self):
        try:
            from student import Student
            self.new_win = tk.Toplevel(self.root)
            self.new_obj = Student(self.new_win)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Student window: {str(e)}")

    def add_result(self):
        try:
            from result import Result
            self.new_win = tk.Toplevel(self.root)
            self.new_obj = Result(self.new_win)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Result window: {str(e)}")

    def add_report(self):
        try:
            from report import Report
            self.new_win = tk.Toplevel(self.root)
            self.new_obj = Report(self.new_win)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Report window: {str(e)}")

    def exit(self):
        if messagebox.askyesno("Confirm", "Do you really want to exit?", parent=self.root):
            self.root.destroy()


if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = RMS(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Fatal Error", f"Application failed to start: {str(e)}")
