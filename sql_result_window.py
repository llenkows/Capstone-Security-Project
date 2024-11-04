import tkinter as tk
import re
from tkinter import scrolledtext
from sql_message_windows import (show_sql_injection_message, show_broken_authentication_message,
                             show_improper_error_handling_message, show_privilege_escalation_message)

# Function to display results in a new window with clickable and hoverable lines
def sql_display_results(lines_with_keywords):
    result_window = tk.Toplevel()
    result_window.title("Lines Containing Potential Security Vulnerabilities")

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
        line_text = text_area.get(f"{line_idx}.0", f"{line_idx}.end").strip().lower()

        # List to store functions to be called for each detected error
        error_functions = []

        # Check for multiple errors in the same line

        # SQL-specific checks
        if "select" in line_text and "from" in line_text:
            error_functions.append(show_sql_injection_message)
        if "where username" in line_text and "password" in line_text:
            error_functions.append(show_broken_authentication_message)
        if "exception" in line_text and ("print" in line_text or "log" in line_text):
            error_functions.append(show_improper_error_handling_message)
        if "grant" in line_text:
            error_functions.append(show_privilege_escalation_message)

        # Open a message window for each error
        for func in error_functions:
            func()

    # Bind clicking on the text area to the on_click function
    text_area.bind("<Button-1>", on_click)
