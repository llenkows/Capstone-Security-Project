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
                    if "strncpy" in line.lower():
                        lines_with_keywords.append((idx + 1, "strncpy", line.strip()))
                    if "strncat" in line.lower():
                        lines_with_keywords.append((idx + 1, "strncat", line.strip()))

                if lines_with_keywords:
                    display_results(lines_with_keywords)
                else:
                    messagebox.showinfo("Result", 'No security issues found.')

        except Exception as e:
            messagebox.showerror("Error", f"Could not open or read the file: {e}")


# Function to open a browser to a specified URL
def open_url(url):
    webbrowser.open(url)


# Function to display a message and a clickable link for "test"
def show_strncpy_message():
    message_window = tk.Toplevel()
    message_window.title("strncpy() issue")

    label = tk.Label(message_window, text="When using strncpy(), use the more secure strncpy_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/"))


# Function to display a message for "capstone"
def show_strncat_message():
    message_window = tk.Toplevel()
    message_window.title("strncat() issue")

    label = tk.Label(message_window, text="When using strncat(), use the more secure strncat_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/"))


# Function to display results in a new window with clickable and hoverable lines
def display_results(lines_with_keywords):
    result_window = tk.Toplevel()
    result_window.title("Lines Containing Potential Security Vulnerabilities'")

    # Instruction label to let the user know the lines are clickable
    instruction_label = tk.Label(result_window, text="Click a line below to get more information.")
    instruction_label.pack(pady=5)

    # Scrollable text area for showing lines
    text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=80, height=20)
    text_area.pack(pady=10, padx=10)

    # Add a tag to highlight the hovered line
    text_area.tag_configure("highlight", background="yellow")

    # Insert the lines into the text widget with tags
    for line_num, keyword, line in lines_with_keywords:
        text_area.insert(tk.END, f"Line {line_num}: {line}\n", keyword)

    text_area.configure(state='disabled')  # Make the text area read-only

    # Store the current highlighted line index
    current_line_idx = None

    # Highlight the line the cursor is hovering over
    def on_hover(event):
        nonlocal current_line_idx
        text_area.configure(state='normal')

        # Get the line index at the cursor position
        line_idx = text_area.index(f"@{event.x},{event.y}").split(".")[0]

        if line_idx != current_line_idx:
            # Remove highlight from the previous line
            if current_line_idx:
                text_area.tag_remove("highlight", f"{current_line_idx}.0", f"{current_line_idx}.end")

            # Highlight the new line
            current_line_idx = line_idx
            text_area.tag_add("highlight", f"{line_idx}.0", f"{line_idx}.end")

        text_area.configure(state='disabled')

    # Bind hovering over text to show the highlight
    text_area.bind("<Motion>", on_hover)

    # Bind clicking on the text to show the appropriate message based on the keyword
    def on_click(event):
        # Get the line index at the cursor position
        line_idx = text_area.index(f"@{event.x},{event.y}").split(".")[0]
        line_text = text_area.get(f"{line_idx}.0", f"{line_idx}.end").strip()

        # Check if the line contains "test" or "capstone"
        if "strncpy" in line_text.lower():
            show_strncpy_message()
        elif "strncat" in line_text.lower():
            show_strncat_message()

    # Bind clicking on the text area to the on_click function
    text_area.bind("<Button-1>", on_click)


# Create a basic GUI window
def create_gui():
    root = tk.Tk()
    root.title("C Security Tester")

    label = tk.Label(root,
                     text="Click the button to select a text file and analyze your C code.")
    label.pack(pady=10)

    button = tk.Button(root, text="Select File", command=select_file_and_display_lines)
    button.pack(pady=10)

    root.geometry("600x200")
    root.mainloop()


if __name__ == "__main__":
    create_gui()
