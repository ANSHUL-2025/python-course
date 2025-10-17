import tkinter as tk
from tkinter import messagebox

def multiply_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Multiply Two Numbers")

# Labels and Entry fields
label_num1 = tk.Label(root, text="Enter First Number:")
label_num1.pack(pady=5)

entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter Second Number:")
label_num2.pack(pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Button to calculate product
multiply_button = tk.Button(root, text="Calculate Product", command=multiply_numbers)
multiply_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="Product: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()
