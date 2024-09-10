import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import webbrowser


# Function to select a file and display the lines containing the words "test" and "capstone"
def select_file_and_display_lines():
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.readlines()

                # Find lines where the words "test" or "capstone" appear
                lines_with_keywords = []
                for idx, line in enumerate(content):
                    if "test" in line.lower():
                        lines_with_keywords.append((idx + 1, "test", line.strip()))
                    if "capstone" in line.lower():
                        lines_with_keywords.append((idx + 1, "capstone", line.strip()))

                if lines_with_keywords:
                    display_results(lines_with_keywords)
                else:
                    messagebox.showinfo("Result", 'No occurrences of the words "test" or "capstone" found.')

        except Exception as e:
            messagebox.showerror("Error", f"Could not open or read the file: {e}")


# Function to open a browser to a specified URL
def open_url(url):
    webbrowser.open(url)


# Function to display a message and a clickable link for "test"
def show_remove_message():
    message_window = tk.Toplevel()
    message_window.title("Remove 'test'")

    label = tk.Label(message_window, text="Please remove the word 'test' from your code.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="Click here to search on Google", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.google.com"))


# Function to display a message for "capstone"
def show_capstone_message():
    message_window = tk.Toplevel()
    message_window.title("Capstone Message")

    label = tk.Label(message_window, text="You've found a capstone-related line!")
    label.pack(pady=10)


# Function to display results in a new window with clickable and hoverable lines
def display_results(lines_with_keywords):
    result_window = tk.Toplevel()
    result_window.title("Lines Containing 'test' or 'capstone'")

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi('C Test 1')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
