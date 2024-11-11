import tkinter as tk
from browser_helpers import open_url

# Function to display a message and a clickable link for "strncpy"
def show_sql_injection_message():
    message_window = tk.Toplevel()
    message_window.title("Potential SQL Injection Vulnerability")

    label = tk.Label(message_window, text="This line of code may have the ability for the user to inject unintended inputs.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.w3schools.com/sql/sql_injection.asp"))

# Function to display a message for "strncat"
def show_broken_authentication_message():
    message_window = tk.Toplevel()
    message_window.title("Potential Broken Authentication Vulnerability")

    label = tk.Label(message_window, text="This line of code has the potential to bypass authentication mechanisms.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://brightsec.com/blog/broken-authentication-impact-examples-and-how-to-fix-it/"))
def show_improper_error_handling_message():
    message_window = tk.Toplevel()
    message_window.title("Potential Improper Error Handling Vulnerability")

    label = tk.Label(message_window, text="This line of code has improper error handling mechanisms.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://www.geeksforgeeks.org/what-is-improper-error-handling/"))

def show_privilege_escalation_message():
    message_window = tk.Toplevel()
    message_window.title("Potential Privilege Escalation Vulnerability")

    label = tk.Label(message_window, text="This line of code could potentially be used to escalate privileges above their intended value.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://knowledge-base.secureflag.com/vulnerabilities/broken_authorization/privilege_escalation_sql.html"))
def show_dynamic_query_message():
    message_window = tk.Toplevel()
    message_window.title("Potential Dynamic Query Construction Vulnerability")

    label = tk.Label(message_window, text="This line has a dynamic query construction vulnerability.")
    label.pack(pady=10)

    link = tk.Label(message_window, text="More information on the vulnerability.", fg="blue", cursor="hand2")
    link.pack(pady=5)

    # Make the label a clickable link
    link.bind("<Button-1>", lambda e: open_url("https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#safest-use-of-dynamic-sql-generation-discouraged"))
