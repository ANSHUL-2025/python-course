import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("Length Converter App")

# Set window size (width x height)
root.geometry("400x400")

# Optional: prevent resizing (you can comment this if you want to allow resizing)
root.resizable(False, False)

# Add a sample widget (label)
label = tk.Label(root, text="Welcome to the Length Converter App!", font=("Arial", 12))
label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
