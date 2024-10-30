import tkinter as tk
from file_selector import select_file_and_display_lines
from sql_file_selector import sql_select_file_and_display_lines


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

    root.geometry("600x300")
    root.mainloop()


if __name__ == "__main__":
    create_gui()
