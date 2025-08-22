# -------------------------------
# Employee Management System (with Tkinter UI + SQLite + CSV Export)
# -------------------------------

import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
import csv

# ---------- STEP 1: Database Setup ----------
def init_db():
    """
    Initializes the database and creates the 'employees' table if it doesn't exist.
    """
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  department TEXT,
                  salary REAL)''')
    conn.commit()
    conn.close()

# ---------- STEP 2: CRUD Operations ----------
def add_employee():
    """
    Adds a new employee into the database.
    """
    name = simpledialog.askstring("Input", "Enter Name")
    dept = simpledialog.askstring("Input", "Enter Department")
    salary = simpledialog.askstring("Input", "Enter Salary")
    if name and dept and salary:
        conn = sqlite3.connect("employees.db")
        c = conn.cursor()
        c.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", 
                  (name, dept, float(salary)))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Employee added successfully!")

def view_employees():
    """
    Fetches all employee records and shows them in a popup.
    """
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    records = c.fetchall()
    conn.close()
    
    if records:
        data = "\n".join([f"ID: {r[0]}, Name: {r[1]}, Dept: {r[2]}, Salary: {r[3]}" for r in records])
    else:
        data = "No records found."
    
    messagebox.showinfo("Employees", data)

def update_employee():
    """
    Updates employee details (name, department, salary) by ID.
    """
    emp_id = simpledialog.askstring("Input", "Enter Employee ID to Update")
    name = simpledialog.askstring("Input", "Enter New Name")
    dept = simpledialog.askstring("Input", "Enter New Department")
    salary = simpledialog.askstring("Input", "Enter New Salary")
    
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute("UPDATE employees SET name=?, department=?, salary=? WHERE id=?", 
              (name, dept, float(salary), emp_id))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Employee updated successfully!")

def delete_employee():
    """
    Deletes an employee by ID.
    """
    emp_id = simpledialog.askstring("Input", "Enter Employee ID to Delete")
    
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Employee deleted successfully!")

def export_csv():
    """
    Exports all employee data to employees.csv (Excel readable).
    """
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    records = c.fetchall()
    conn.close()
    
    with open("employees.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Salary"])
        writer.writerows(records)
    
    messagebox.showinfo("Export", "Data exported to employees.csv")

# ---------- STEP 3: GUI ----------
init_db()  # Call DB setup at the start

root = tk.Tk()
root.title("Employee Management System")
root.geometry("600x500")
root.configure(bg="#f0f8ff")  # Light background

# Heading
heading = tk.Label(root, 
                   text="Employee Management System", 
                   font=("Arial", 22, "bold"), 
                   fg="white", 
                   bg="#4682B4", 
                   pady=15)
heading.pack(fill="x")

# Frame for buttons
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=40)

# Button Styling
button_style = {
    "font": ("Arial", 14, "bold"),
    "width": 20,
    "height": 2,
    "relief": "raised",
    "bd": 3,
    "bg": "#4682B4",
    "fg": "white",
    "activebackground": "#5F9EA0",
    "activeforeground": "yellow"
}

# Buttons
tk.Button(frame, text="Add Employee", command=add_employee, **button_style).pack(pady=10)
tk.Button(frame, text="View Employees", command=view_employees, **button_style).pack(pady=10)
tk.Button(frame, text="Update Employee", command=update_employee, **button_style).pack(pady=10)
tk.Button(frame, text="Delete Employee", command=delete_employee, **button_style).pack(pady=10)
tk.Button(frame, text="Export to CSV", command=export_csv, **button_style).pack(pady=10)

# Run the app
root.mainloop()


# ---- (Optional) Old Console Menu ----
"""
while True:
    print("\n==== Employee Management System ====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")
    print("6. Export Employees to CSV")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        add_employee(id, name, dept, salary)

    elif choice == "2":
        view_employees()

    elif choice == "3":
        id = int(input("Enter Employee ID to update: "))
        dept = input("Enter new Department: ")
        salary = float(input("Enter new Salary: "))
        update_employee(id, dept, salary)

    elif choice == "4":
        id = int(input("Enter Employee ID to delete: "))
        delete_employee(id)

    elif choice == "5":
        print("Exiting program... Goodbye!")
        break

    elif choice == "6":
        export_to_csv()

    else:
        print("Invalid choice. Please try again.")
"""
