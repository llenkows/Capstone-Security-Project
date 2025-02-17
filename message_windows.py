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
    message_window.title("strcpy() Message")

    label = tk.Label(message_window, text="When using strcpy(), use the more secure strcpy_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/"))

def show_strcat_message():
    message_window = tk.Toplevel()
    message_window.title("strcat() Message")

    label = tk.Label(message_window, text="When using strcat(), use the more secure strcat_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/"))

def show_strlen_message():
    message_window = tk.Toplevel()
    message_window.title("strlen() Message")

    label = tk.Label(message_window, text="When using strlen(), ensure that a string is null terminated before passing it"
                                          "to strlen() by inserting a null character in the last byte of the array or"
                                          " use the strnlen() function that accepts a maximum size.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://rules.sonarsource.com/c/tag/cwe/RSPEC-5813/"))
def show_strsafe_message():
    message_window = tk.Toplevel()
    message_window.title("strsafe Message")

    label = tk.Label(message_window, text="Strsafe will add a lot of security to your code. Just remember that"
                                          "Strsafe works differently to functions like strcpy_s(), so make sure you"
                                          "choose the best one that fits your needs.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://learn.microsoft.com/en-us/windows/win32/menurc/strsafe-ovw"))
def show_gets_message():
    message_window = tk.Toplevel()
    message_window.title("gets Message")

    label = tk.Label(message_window, text="gets() is a highly vulnerable function. Change to fgets() to limit "
                                          "the message to a certain amount of characters. ")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/gets-is-risky-to-use/"))
def show_off_by_one_message():
    message_window = tk.Toplevel()
    message_window.title("Off-by-one issue")

    label = tk.Label(message_window, text="When using <= in a loop to fill an array, there is potential for a buffer "
                                          "overflow by one. Make sure to use either < or one number below the array "
                                          "size.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://cwe.mitre.org/data/definitions/193.html"))

def show_format_string_message():
    message_window = tk.Toplevel()
    message_window.title("Format string issue")

    label = tk.Label(message_window, text="When using a form of printf, make sure to explicitly specify the format string "
                                          "using '%s'.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/format-string-vulnerability-and-prevention-with-example/"))

def show_memcpy_message():
    message_window = tk.Toplevel()
    message_window.title("memcpy() Message")

    label = tk.Label(message_window, text="When using memcpy(), use the more secure memcpy_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.ctfrecipes.com/pwn/stack-exploitation/stack-buffer-overflow/dangerous-functions/memcpy"))

def show_memmove_message():
    message_window = tk.Toplevel()
    message_window.title("memmove() issue")

    label = tk.Label(message_window, text="When using memmove(), use the more secure memmove_s() instead.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.ctfrecipes.com/pwn/stack-exploitation/stack-buffer-overflow/dangerous-functions/memcpy"))

def show_dynamic_query_message():
    message_window = tk.Toplevel()
    message_window.title("SQL Dynamic Query issue")

    label = tk.Label(message_window, text="This code could potentially be used for SQL injection. Make sure user input is seperated from the SQL query.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html"))

def show_fixed_size_buffer_message():
    message_window = tk.Toplevel()
    message_window.title("Fixed Sized Buffer issue")

    label = tk.Label(message_window, text="Using a fixed size buffer, it could lead to potential buffer overflow depending on the data size or function. "
                                            "It is a better idea to use dynamic memory allocation to prevent this.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/"))


def show_signed_to_unsigned_message():
    message_window = tk.Toplevel()
    message_window.title("Signed to unsigned issue")

    label = tk.Label(message_window,
                     text="Using a signed number in a function could convert it into an unsigned integer which can cause potential problems.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>",
              lambda e: open_url("https://www.geeksforgeeks.org/difference-between-unsigned-int-and-signed-int-in-c/"))

def show_scanf_message():
    message_window = tk.Toplevel()
    message_window.title("Scanf issue")

    label = tk.Label(message_window,
                     text="Scanf doesn't have set input bounds, so overflow vulnerabilities are possible. Use a different function like fgets() or sscanf().")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>",
              lambda e: open_url("https://stackoverflow.com/questions/35734927/vulnerability-using-printf-scanf-and-s"))