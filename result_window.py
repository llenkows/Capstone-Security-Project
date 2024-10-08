import tkinter as tk
import re
from tkinter import scrolledtext
from message_windows import (show_strncpy_message, show_strncat_message, show_strcat_message, show_strcpy_message,
                             show_strlen_message, show_strsafe_message, show_gets_message, show_off_by_one_message,
                             show_format_string_message, show_memcpy_message, show_memmove_message, show_dynamic_query_message,
                             show_fixed_size_buffer_message)

# Function to display results in a new window with clickable and hoverable lines
def display_results(lines_with_keywords):
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
        if "strncpy" in line_text:
            error_functions.append(show_strncpy_message)
        if "strncat" in line_text:
            error_functions.append(show_strncat_message)
        if "strcpy" in line_text:
            error_functions.append(show_strcpy_message)
        if "strcat" in line_text:
            error_functions.append(show_strcat_message)
        if "strlen" in line_text:
            error_functions.append(show_strlen_message)
        if "strsafe" in line_text:
            error_functions.append(show_strsafe_message)
        if "gets(" in line_text and "fgets" not in line_text:
            error_functions.append(show_gets_message)
        if "<=" in line_text and "for" in line_text:
            error_functions.append(show_off_by_one_message)
        if "printf" in line_text or "fprintf" in line_text or "sprintf" in line_text:
            error_functions.append(show_format_string_message)
        if "memcpy" in line_text:
            error_functions.append(show_memcpy_message)
        if "memmove" in line_text:
            error_functions.append(show_memmove_message)
        if any(keyword in line_text for keyword in ["select", "insert", "update", "delete"]):
            error_functions.append(show_dynamic_query_message)

        # Check for fixed-size buffer declarations
        if re.search(r'\bchar\s+\w+\s*\[\s*\d+\s*\]', line_text):
            error_functions.append(show_fixed_size_buffer_message())

        # Open a message window for each error
        for func in error_functions:
            func()

    # Bind clicking on the text area to the on_click function
    text_area.bind("<Button-1>", on_click)