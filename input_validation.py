import re
from tkinter import filedialog, messagebox
from result_window import display_results

# Function to check for input validation in the provided C file
def check_input_validation_in_c_file():
    file_path = filedialog.askopenfilename(title="Select a C File", filetypes=[("C files", "*.c"), ("All files", "*.*")])

    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()

                # Regex to match functions without input length validation
                # Match a function that uses strlen(arg), without any validation of buffer size.
                function_pattern = re.compile(
                    r"\bint\s+\w+\s*\(.*?\)\s*\{[^}]*?\bchar\s+(\w+)\[.*?\];[^}]*?\bstrlen\((\w+)\)[^}]*?if\s*\(.*?\)\s*{[^}]*?\}",
                    re.DOTALL
                )

                matches = function_pattern.findall(content)

                lines_with_issues = []
                if matches:
                    for match in matches:
                        buffer_name, arg_name = match
                        # Check if the function has an input validation for buffer size
                        # Look for a comparison of strlen(arg) with sizeof(buffer) and proper handling.
                        validation_check = re.search(
                            rf"if\s*\(strlen\({arg_name}\)\s*<\s*sizeof\({buffer_name}\)\)", content, re.DOTALL
                        )

                        if not validation_check:
                            # Get the line number where the issue occurs
                            for line_num, line in enumerate(content.splitlines(), start=1):
                                if buffer_name in line or arg_name in line:
                                    lines_with_issues.append((line_num, line.strip()))
                                    break

                if lines_with_issues:
                    display_results(lines_with_issues)
                else:
                    messagebox.showinfo("Result", "No issues found related to input validation.")

        except Exception as e:
            messagebox.showerror("Error", f"Could not open or read the file: {e}")
