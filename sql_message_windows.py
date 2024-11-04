import tkinter as tk
from browser_helpers import open_url

# Function to display a message and a clickable link for "strncpy"
def show_sql_injection_message():
    message_window = tk.Toplevel()
    message_window.title("sql injection issue")

    label = tk.Label(message_window, text="When using strncpy(), use the more secure strncpy_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/"))

# Function to display a message for "strncat"
def show_broken_authentication_message():
    message_window = tk.Toplevel()
    message_window.title("broken authentication issue")

    label = tk.Label(message_window, text="When using strncat(), use the more secure strncat_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/"))
def show_improper_error_handling_message():
    message_window = tk.Toplevel()
    message_window.title("improper error handling Message")

    label = tk.Label(message_window, text="When using strcpy(), use the more secure strcpy_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/"))

def show_privilege_escalation_message():
    message_window = tk.Toplevel()
    message_window.title("privilege escalation Message")

    label = tk.Label(message_window, text="When using strcat(), use the more secure strcat_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/"))