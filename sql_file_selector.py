import re
from tkinter import filedialog, messagebox
from sql_result_window import sql_display_results

# Adjusted function to detect SQL Injection with more flexible patterns
def detect_sql_injection(content):
    injection_patterns = [
        r"\bSELECT\b.*\bFROM\b.*(\+|\|\||[{].*?[}]|['\"].*['\"])",  # SELECT statement with dynamic user input
        r"\bINSERT\b.*\bVALUES\b.*(\+|\|\||[{].*?[}]|['\"].*['\"])",  # INSERT with potential user input
        r"\bUPDATE\b.*\bSET\b.*(\+|\|\||[{].*?[}]|['\"].*['\"])",  # UPDATE with dynamic user input
        r"\bDELETE\b.*\bWHERE\b.*(\+|\|\||[{].*?[}]|['\"].*['\"])"  # DELETE with dynamic WHERE clause
    ]
    vulnerabilities = []

    for i, line in enumerate(content):
        for pattern in injection_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                vulnerabilities.append((i + 1, "Potential SQL Injection", line.strip()))

    return vulnerabilities

# Adjusted function to detect Broken Authentication with flexible matching
def detect_broken_authentication(content):
    broken_auth_patterns = [
        r"SELECT\s+\*\s+FROM\s+users\s+WHERE\s+username\s*=\s*['\"].*['\"]?\s*AND\s+password\s*=\s*['\"].*['\"]?",  # Explicit password in query
        r"SELECT\s+\*\s+FROM\s+users\s+WHERE\s+username\s*=\s*\w+\s*AND\s+password\s*=\s*\w+"  # Username and password in WHERE clause without explicit strings
    ]
    vulnerabilities = []

    for i, line in enumerate(content):
        for pattern in broken_auth_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                vulnerabilities.append((i + 1, "Potential Broken Authentication", line.strip()))

    return vulnerabilities

# UPDATED  Improper Error Handling per testing cases
def detect_improper_error_handling(content):
    vulnerabilities = []
    improper_error_handling_patterns = [
        r"except(\s+Exception|\s*):",
        r"print\s+ERROR_MESSAGE\(\)",
        r"IS\s+NULL",
        r"INSERT\s+INTO\s+logs.*?ERROR_MESSAGE\(\)",
        r"Database\s+error:\s*[']?\s*\|\|\s*ERROR_MESSAGE\(\)",
        r"information_schema",
        r"@@version"
    ]

    for i, line in enumerate(content):
        for pattern in improper_error_handling_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                vulnerabilities.append((i + 1, "Potential Improper Error Handling", line.strip()))
    return vulnerabilities

# Adjusted function to detect Privilege Escalation with broader GRANT detection
def detect_privilege_escalation(content):
    privilege_patterns = [
        r"GRANT\s+\w+\s+ON\s+.*\s+TO\s+.*",  # General GRANT statement pattern
        r"SELECT\s+.*?FROM\s+users.*?password",
        r"SET\s+role\s*=\s*'admin'",
        r"ADD\s+admin_role",
        r"SET\s + is_admin",
    ]
    vulnerabilities = []

    for i, line in enumerate(content):
        for pattern in privilege_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                vulnerabilities.append((i + 1, "Potential Privilege Escalation", line.strip()))

    return vulnerabilities

# Function to remove duplicates based on line number
# Function to remove duplicates based on line number while preserving vulnerability information
def remove_duplicates(results):
    unique_results = {}

    # Loop through each result to collect unique line numbers with combined vulnerability descriptions
    for line_num, vulnerability_type, line_text in results:
        if line_num not in unique_results:
            unique_results[line_num] = (line_num, vulnerability_type, line_text)
        else:
            # Append additional vulnerability type to existing entry, if it's different
            if vulnerability_type not in unique_results[line_num][1]:
                unique_results[line_num] = (
                    line_num,
                    f"{unique_results[line_num][1]}, {vulnerability_type}",
                    line_text
                )

    # Return the results as a sorted list by line number
    return sorted(unique_results.values(), key=lambda x: x[0])


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