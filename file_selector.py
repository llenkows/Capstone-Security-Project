from tkinter import filedialog, messagebox
from result_window import display_results
import re

# Function to detect off-by-one errors in loops
def detect_off_by_one_errors(content):
    for_loop_pattern = r"for\s*\(.*;\s*(.*<=.*|.*>=.*);.*\)"
    array_access_pattern = r"\[\s*(.*)\s*\]"
    potential_errors = []

    for i, line in enumerate(content):
        # Check if a line contains a `for` loop with potential off-by-one error
        for_match = re.search(for_loop_pattern, line)
        if for_match:
            loop_condition = for_match.group(1).strip()
            # Look for array access patterns in the same or subsequent lines
            for j in range(i, min(i + 5, len(content))):  # Check nearby lines for array access
                array_match = re.search(array_access_pattern, content[j])
                if array_match:
                    array_index = array_match.group(1).strip()
                    if array_index in loop_condition:
                        potential_errors.append((i + 1, "Potential off-by-one", line.strip()))
                    break

    return potential_errors

# Function to detect format string vulnerabilities
def detect_format_string_vulnerabilities(content):
    format_function_pattern = r"(printf|fprintf|sprintf|snprintf|vprintf|vfprintf|vsprintf)\s*\(.*\)"
    potential_vulnerabilities = []

    for i, line in enumerate(content):
        # Check if line contains a function call that may be vulnerable to format string attacks
        match = re.search(format_function_pattern, line)
        if match:
            # If the function call contains only one argument (user input passed directly)
            # It can be a vulnerability, so we flag it
            arguments = line.split('(', 1)[1].rsplit(')', 1)[0]
            if ',' not in arguments:  # No format string provided
                potential_vulnerabilities.append((i + 1, "Potential format string vulnerability", line.strip()))

    return potential_vulnerabilities

# Function to select a file and display the lines containing potential security issues
def select_file_and_display_lines():
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.readlines()

                # Find lines where security-related functions and errors appear
                lines_with_keywords = []
                for idx, line in enumerate(content):
                    if "strncpy" in line.lower():
                        lines_with_keywords.append((idx + 1, "strncpy", line.strip()))
                    if "strncat" in line.lower():
                        lines_with_keywords.append((idx + 1, "strncat", line.strip()))
                    if "strcpy_s()" in line.lower():
                        lines_with_keywords.append((idx + 1, "strcpy_s()", line.strip()))
                    if "strcat_s()" in line.lower():
                        lines_with_keywords.append((idx + 1, "strcat_s()", line.strip()))
                    if "strlen()" in line.lower():
                        lines_with_keywords.append((idx + 1, "strlen()", line.strip()))
                    if "strsafe.h" in line.lower():
                        lines_with_keywords.append((idx + 1, "strsafe.h", line.strip()))
                    if "gets(" in line.lower() and "fgets(" not in line.lower():
                        lines_with_keywords.append((idx + 1, "gets(", line.strip()))

                # Check for off-by-one errors
                off_by_one_errors = detect_off_by_one_errors(content)
                lines_with_keywords.extend(off_by_one_errors)

                # Check for format string vulnerabilities
                format_string_vulnerabilities = detect_format_string_vulnerabilities(content)
                lines_with_keywords.extend(format_string_vulnerabilities)

                if lines_with_keywords:
                    display_results(lines_with_keywords)
                else:
                    messagebox.showinfo("Result", 'No security issues found.')

        except Exception as e:
            messagebox.showerror("Error", f"Could not open or read the file: {e}")
