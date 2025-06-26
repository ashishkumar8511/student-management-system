import tkinter as tk
from tkinter import messagebox
import json

# ------------------ Student Class ------------------
class Student:
    def __init__(self, roll, name, course):
        self.roll = roll
        self.name = name
        self.course = course

    def to_dict(self):
        return {"roll": self.roll, "name": self.name, "course": self.course}

# ------------------ File Functions ------------------
def load_data():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)

# ------------------ Add Student ------------------
def add_student():
    roll = roll_entry.get()
    name = name_entry.get()
    course = course_entry.get()

    if not (roll and name and course):
        messagebox.showerror("Error", "All fields are required!")
        return

    data = load_data()
    for s in data:
        if s["roll"] == roll:
            messagebox.showwarning("Duplicate", "Roll number already exists!")
            return

    s = Student(roll, name, course)
    data.append(s.to_dict())
    save_data(data)

    messagebox.showinfo("Success", "Student added successfully!")

    # Clear fields
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

# ------------------ Show Students ------------------
def show_students():
    data = load_data()
    result_text.delete(1.0, tk.END)
    if not data:
        result_text.insert(tk.END, "⚠️ No student data found.")
    else:
        for s in data:
            result_text.insert(tk.END, f"Roll: {s['roll']}, Name: {s['name']}, Course: {s['course']}\n")

# ------------------ GUI Window ------------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("500x500")

# Entry Fields
tk.Label(root, text="Roll No:").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Course:").pack()
course_entry = tk.Entry(root)
course_entry.pack()

# Buttons
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="Show All Students", command=show_students).pack(pady=5)

# Result Output Box
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

root.mainloop()
