from tkinter import filedialog, messagebox
from result_window import display_results

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

                if lines_with_keywords:
                    display_results(lines_with_keywords)
                else:
                    messagebox.showinfo("Result", 'No security issues found.')

        except Exception as e:
            messagebox.showerror("Error", f"Could not open or read the file: {e}")
