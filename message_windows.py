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
def show_strcpy_message():
    message_window = tk.Toplevel()
    message_window.title("strcpy_s() Message")

    label = tk.Label(message_window, text="You've found a line using strcpy_s()!")
    label.pack(pady=10)

def show_strcat_message():
    message_window = tk.Toplevel()
    message_window.title("strcat_s() Message")

    label = tk.Label(message_window, text="You've found a line using strcat_s()!")
    label.pack(pady=10)

def show_strlen_message():
    message_window = tk.Toplevel()
    message_window.title("strlen() Message")

    label = tk.Label(message_window, text="You've found a vulnerable line that uses strlen()!")
    label.pack(pady=10)

def show_strsafe_message():
    message_window = tk.Toplevel()
    message_window.title("strsafe Message")

    label = tk.Label(message_window, text="You've found a vulnerable line that uses strsafe.h!")
    label.pack(pady=10)

#Added buffer overflow msgs
def show_gets_message():
    message_window = tk.Toplevel()
    message_window.title("gets() Message")

    label = tk.Label(message_window, text="You've found a vulnerable line that uses gets()!")
    label.pack(pady=10)

def show_memcpy_message():
    message_window = tk.Toplevel()
    message_window.title("memcpy() Message")

    label = tk.Label(message_window, text="You've found a vulnerable line that uses memcpy()!")
    label.pack(pady=10)

def show_memmove_message():
    message_window = tk.Toplevel()
    message_window.title("memmove() Message")

    label = tk.Label(message_window, text="You've found a vulnerable line that uses memmove()!")
    label.pack(pady=10)
