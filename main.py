import tkinter as tk
from tkinter import messagebox
from file_selector import select_file_and_display_lines
from sql_file_selector import sql_select_file_and_display_lines


# Function to open a popup displaying the content of README.md
def show_readme():
    try:
        with open("README.md", "r") as file:
            readme_content = file.read()
        # Create a new Toplevel window to display the README content
        popup = tk.Toplevel()
        popup.title("README.md")

        # Create a Text widget to display the file content
        text_widget = tk.Text(popup, wrap='word', width=60, height=20)
        text_widget.insert("1.0", readme_content)
        text_widget.config(state="disabled")  # Make it read-only
        text_widget.pack(padx=10, pady=10)

        # Add a close button
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)
    except FileNotFoundError:
        messagebox.showerror("Error", "README.md file not found.")


# Create a basic GUI window
def create_gui():
    root = tk.Tk()
    root.title("Security Tester")

    # Variable to hold the selected mode
    mode = tk.StringVar(value="C")

    label = tk.Label(root, text="Click the button to select a text file and analyze your C code.")
    label.pack(pady=10)

    # Label and radio buttons for mode selection
    label = tk.Label(root, text="Choose Analysis Mode:")
    label.pack(pady=10)

    c_mode_radio = tk.Radiobutton(root, text="C Mode", variable=mode, value="C")
    sql_mode_radio = tk.Radiobutton(root, text="SQL Mode", variable=mode, value="SQL")
    c_mode_radio.pack()
    sql_mode_radio.pack()

    # Function to call the appropriate function based on the selected mode
    def select_file():
        if mode.get() == "C":
            select_file_and_display_lines()
        elif mode.get() == "SQL":
            sql_select_file_and_display_lines()

    # Button to select file
    button = tk.Button(root, text="Select File", command=select_file)
    button.pack(pady=10)

    # Button to open README.md popup
    readme_button = tk.Button(root, text="Open README.md", command=show_readme)
    readme_button.pack(pady=10)

    root.geometry("600x300")
    root.mainloop()


if __name__ == "__main__":
    create_gui()
