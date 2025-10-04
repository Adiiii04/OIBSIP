import tkinter as tk
from tkinter import messagebox, ttk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        if weight <= 0:
            messagebox.showwarning("Invalid Input", "Weight must be positive")
            return

        if unit_var.get() == "Meters":
            height = float(height_m.get())
            if height <= 0:
                messagebox.showwarning("Invalid Input", "Height must be positive")
                return
        else:
            feet = float(height_ft.get())
            inches = float(height_in.get())
            if feet < 0 or inches < 0:
                messagebox.showwarning("Invalid Input", "Height must be positive")
                return
            height = (feet*12 + inches) * 0.0254

        bmi = weight / (height**2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "High BMI"

        result_label.config(text=f"BMI: {bmi:.2f}\n{category}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numeric values")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="BMI CALCULATOR", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

unit_var = tk.StringVar(value="Meters")
unit_menu = ttk.Combobox(root, textvariable=unit_var, values=["Meters", "Feet & Inches"], state="readonly")
unit_menu.pack(pady=5)

height_frame = tk.Frame(root)
height_frame.pack(pady=5)

height_m = tk.Entry(height_frame)
height_ft = tk.Entry(height_frame, width=5)
height_in = tk.Entry(height_frame, width=5)

def switch_units(event=None):
    for widget in height_frame.winfo_children():
        widget.pack_forget()
    if unit_var.get() == "Meters":
        tk.Label(height_frame, text="Height (m):").pack(side="left")
        height_m.pack(side="left")
    else:
        tk.Label(height_frame, text="Feet:").pack(side="left")
        height_ft.pack(side="left")
        tk.Label(height_frame, text="Inches:").pack(side="left")
        height_in.pack(side="left")

unit_menu.bind("<<ComboboxSelected>>", switch_units)
switch_units()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
