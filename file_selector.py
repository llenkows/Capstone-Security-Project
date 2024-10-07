from tkinter import filedialog, messagebox
from result_window import display_results
import re
import sys


# Function to detect off-by-one errors in loops
def detect_off_by_one_errors(content):
    for_loop_pattern = r"for\s*\(.*;\s*(.*<=.*|.*>=.*);.*\)"
    array_access_pattern = r"\[\s*(.*)\s*\]"
    potential_errors = []

    for i, line in enumerate(content):
        for_match = re.search(for_loop_pattern, line)
        if for_match:
            loop_condition = for_match.group(1).strip()
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
        match = re.search(format_function_pattern, line)
        if match:
            arguments = line.split('(', 1)[1].rsplit(')', 1)[0]
            if ',' not in arguments:  # No format string provided
                potential_vulnerabilities.append((i + 1, "Potential format string vulnerability", line.strip()))

    return potential_vulnerabilities


def detect_buffer_overflow(content):
    unsafe_functions = [
        r'\bgets\s*\(',
        r'\bstrcpy\s*\(',
        r'\bstrcat\s*\(',
        r'\bsprintf\s*\(',
        r'\bscanf\s*\(',
    ]

    buffer_size_pattern = r'char\s+\w+\s*\[\s*(\d+)\s*\]'
    vulnerabilities = []

    for i, line in enumerate(content):
        for pattern in unsafe_functions:
            if re.search(pattern, line):
                vulnerabilities.append((i + 1, "Potential buffer overflow", line.strip()))

        if re.search(buffer_size_pattern, line):
            vulnerabilities.append((i + 1, "Fixed size buffer", line.strip()))

    return vulnerabilities


def detect_dynamic_query_construction(content):
    dynamic_query_patterns = [
        r'\bsprintf\s*\(',
        r'\bstrcat\s*\(',
        r'\bstrcpy\s*\(',
        r'\bmysql_query\s*\(',
        r'\bsystem\s*\(',
    ]

    sql_keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE']
    vulnerabilities = []

    for i, line in enumerate(content):
        for pattern in dynamic_query_patterns:
            if re.search(pattern, line):
                if any(keyword in line.upper() for keyword in sql_keywords):
                    vulnerabilities.append(
                        (i + 1, "Potential SQL Injection (Dynamic Query Construction)", line.strip()))

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
                    if "memcpy()" in line.lower():
                        lines_with_keywords.append((idx + 1, "memcpy()", line.strip()))
                    if "memmove()" in line.lower():
                        lines_with_keywords.append((idx + 1, "memmove()", line.strip()))

                # Check for off-by-one errors
                off_by_one_errors = detect_off_by_one_errors(content)
                lines_with_keywords.extend(off_by_one_errors)

                # Check for format string vulnerabilities
                format_string_vulnerabilities = detect_format_string_vulnerabilities(content)
                lines_with_keywords.extend(format_string_vulnerabilities)

                # Check for buffer overflow vulnerabilities
                buffer_flow_vulnerabilities = detect_buffer_overflow(content)
                lines_with_keywords.extend(buffer_flow_vulnerabilities)

                # Check for dynamic query construction vulnerabilities
                dynamic_query_vulnerabilities = detect_dynamic_query_construction(content)
                lines_with_keywords.extend(dynamic_query_vulnerabilities)

                # Remove duplicates
                unique_lines = remove_duplicates(lines_with_keywords)

                if unique_lines:
                    display_results(unique_lines)
                else:
                    messagebox.showinfo("Result", 'No security issues found.')

        except Exception as e:
            messagebox.showerror("Error", f"Could not open or read the file: {e}")
