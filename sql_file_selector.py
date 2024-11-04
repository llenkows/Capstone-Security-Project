from tkinter import filedialog, messagebox
from sql_result_window import sql_display_results
import re
import sys

# Adjusted function to detect SQL Injection
def detect_sql_injection(content):
    injection_patterns = [
        r"\bSELECT\b.*\bFROM\b.*['\"].*['\"]",  # Pattern for SELECT with user input directly embedded
        r"\bINSERT\b.*\bVALUES\b.*['\"].*['\"]",  # Pattern for INSERT with dynamic values
        r"\bUPDATE\b.*\bSET\b.*['\"].*['\"]",  # Pattern for UPDATE with dynamic SET values
        r"\bDELETE\b.*\bWHERE\b.*['\"].*['\"]"  # Pattern for DELETE with dynamic WHERE clause
    ]
    vulnerabilities = []

    for i, line in enumerate(content):
        for pattern in injection_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                vulnerabilities.append((i + 1, "Potential SQL Injection", line.strip()))

    return vulnerabilities


# Adjusted function to detect Broken Authentication
def detect_broken_authentication(content):
    broken_auth_patterns = [
        r"SELECT\s+\*\s+FROM\s+users\s+WHERE\s+username\s*=\s*['\"]?\w*['\"]?\s*AND\s+password\s*=\s*['\"]?\w*['\"]?",
        # Check for hardcoded or concatenated password in query
        r"SELECT\s+\*\s+FROM\s+users\s+WHERE\s+username\s*=\s*['\"]?\w*['\"]?\s*AND\s+password\s*=\s*['\"]?\s*.*'?"
        # Password check that could be bypassed
    ]
    vulnerabilities = []

    for i, line in enumerate(content):
        for pattern in broken_auth_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                vulnerabilities.append((i + 1, "Potential Broken Authentication", line.strip()))

    return vulnerabilities


# Adjusted function to detect Improper Error Handling
def detect_improper_error_handling(content):
    error_handling_patterns = [
        r"Exception.*print",  # Print statement used in exception handling
        r"Exception.*log",  # Log statement used in exception handling
        r"except\s+Exception\s+as\s+.*\s*:\s*print"  # General pattern for printing exception message
    ]
    vulnerabilities = []

    for i, line in enumerate(content):
        for pattern in error_handling_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                vulnerabilities.append((i + 1, "Potential Improper Error Handling", line.strip()))

    return vulnerabilities


# Adjusted function to detect Privilege Escalation
def detect_privilege_escalation(content):
    privilege_patterns = [
        r"GRANT\s+ALL\s+ON\s+\w+\s+TO\s+['\"].*['\"]",  # Excessive privileges grant
        r"GRANT\s+\w+\s+ON\s+\w+\s+TO\s+\w+\s+WITH\s+GRANT\s+OPTION",  # WITH GRANT OPTION for privilege escalation
        r"GRANT\s+\w+\s+ON\s+.*\s+TO\s+.*"  # General pattern to detect GRANT statements
    ]
    vulnerabilities = []

    for i, line in enumerate(content):
        for pattern in privilege_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                vulnerabilities.append((i + 1, "Potential Privilege Escalation", line.strip()))

    return vulnerabilities

# Function to remove any line that appears more than once
def remove_duplicates(results):
    line_count = {}
    for result in results:
        line_number = result[0]
        if line_number not in line_count:
            line_count[line_number] = 1
        else:
            line_count[line_number] += 1

    # Only keep results with lines that appear once
    unique_results = [result for result in results if line_count[result[0]] == 1]

    return unique_results

# Testing setup
def sql_select_file_and_display_lines():
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.readlines()

                # Find security vulnerabilities in the content
                lines_with_keywords = []

                # Run vulnerability detection functions
                sql_injection_vulnerabilities = detect_sql_injection(content)
                lines_with_keywords.extend(sql_injection_vulnerabilities)

                broken_auth_vulnerabilities = detect_broken_authentication(content)
                lines_with_keywords.extend(broken_auth_vulnerabilities)

                error_handling_vulnerabilities = detect_improper_error_handling(content)
                lines_with_keywords.extend(error_handling_vulnerabilities)

                privilege_escalation_vulnerabilities = detect_privilege_escalation(content)
                lines_with_keywords.extend(privilege_escalation_vulnerabilities)

                # Remove duplicates and display results
                unique_lines = remove_duplicates(lines_with_keywords)

                if unique_lines:
                    sql_display_results(unique_lines)
                else:
                    messagebox.showinfo("Result", 'No security issues found.')

        except Exception as e:
            messagebox.showerror("Error", f"Could not open or read the file: {e}")
