import tkinter as tk
from browser_helpers import open_url

# Function to display a message and a clickable link for "strncpy"
def show_strncpy_message():
    message_window = tk.Toplevel()
    message_window.title("strncpy() issue")

    label = tk.Label(message_window, text="When using strncpy(), use the more secure strncpy_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/"))

# Function to display a message for "strncat"
def show_strncat_message():
    message_window = tk.Toplevel()
    message_window.title("strncat() issue")

    label = tk.Label(message_window, text="When using strncat(), use the more secure strncat_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/"))
