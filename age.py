from tkinter import *
from datetime import date

# Function to calculate age
def calculate_age():
    today = date.today()
    birth_day = int(day_entry.get())
    birth_month = int(month_entry.get())
    birth_year = int(year_entry.get())

    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    result_label.config(text=f"Your Age is: {age} years")

# Main window
root = Tk()
root.title("Age Calculator App")
root.geometry("350x300")
root.config(bg="#f0f0f0")

# Title label
Label(root, text="Age Calculator", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Frame for entries
frame = Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

# Day
Label(frame, text="Day:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
day_entry = Entry(frame, width=5)
day_entry.grid(row=0, column=1, padx=5, pady=5)

# Month
Label(frame, text="Month:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
month_entry = Entry(frame, width=5)
month_entry.grid(row=1, column=1, padx=5, pady=5)

# Year
Label(frame, text="Year:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5)
year_entry = Entry(frame, width=5)
year_entry.grid(row=2, column=1, padx=5, pady=5)

# Calculate button
Button(root, text="Calculate Age", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
       command=calculate_age).pack(pady=15)

# Result label
result_label = Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="blue")
result_label.pack(pady=10)

root.mainloop()
