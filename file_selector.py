from tkinter import filedialog, messagebox
from result_window import display_results
from input_validation import check_input_validation_in_c_file

# Function to select a file and display the lines containing the words "strncpy" and "strncat"
def select_file_and_display_lines():
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.readlines()

                # Find lines where the words "strncpy" or "strncat" appear
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

                    # ADDED LINES FOR BUFFER OVERFLOW / CODE INJECTION
                    if "gets()" in line.lower():
                        lines_with_keywords.append((idx + 1, "gets()", line.strip()))
                    if "memcpy()" in line.lower():
                        lines_with_keywords.append((idx + 1, "memcpy()", line.strip()))
                    if "memmove()" in line.lower():
                        lines_with_keywords.append((idx + 1, "memmove()", line.strip()))

                if lines_with_keywords:
                    display_results(lines_with_keywords)
                else:
                    messagebox.showinfo("Result", 'No security issues found.')

        except Exception as e:
            messagebox.showerror("Error", f"Could not open or read the file: {e}")
