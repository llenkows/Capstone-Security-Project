import tkinter as tk
from file_selector import select_file_and_display_lines

# Create a basic GUI window
def create_gui():
    root = tk.Tk()
    root.title("C Security Tester")

    label = tk.Label(root, text="Click the button to select a text file and analyze your C code.")
    label.pack(pady=10)

    button = tk.Button(root, text="Select File", command=select_file_and_display_lines)
    button.pack(pady=10)

    root.geometry("600x200")
    root.mainloop()

if __name__ == "__main__":
    create_gui()
