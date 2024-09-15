import tkinter as tk
from tkinter import scrolledtext
from message_windows import show_strncpy_message, show_strncat_message

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

        # Check if the line contains "strncpy" or "strncat"
        if "strncpy" in line_text.lower():
            show_strncpy_message()
        elif "strncat" in line_text.lower():
            show_strncat_message()

    # Bind clicking on the text area to the on_click function
    text_area.bind("<Button-1>", on_click)
