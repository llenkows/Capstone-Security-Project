import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


# Function to select a file and display the lines containing the word "test"
def select_file_and_display_lines():
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.readlines()

                # Find lines where the word "test" appears
                lines_with_test = [f"Line {idx + 1}: {line.strip()}" for idx, line in enumerate(content) if
                                   "test" in line.lower()]

                if lines_with_test:
                    display_results("\n".join(lines_with_test))
                else:
                    messagebox.showinfo("Result", 'No occurrences of the word "test" found.')

        except Exception as e:
            messagebox.showerror("Error", f"Could not open or read the file: {e}")


# Function to display results in a new window with scrollable text
def display_results(result_text):
    result_window = tk.Toplevel()
    result_window.title("Lines Containing 'test'")

    text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=80, height=20)
    text_area.pack(pady=10, padx=10)
    text_area.insert(tk.END, result_text)
    text_area.configure(state='disabled')  # Make the text area read-only


# Create a basic GUI window
def create_gui():
    root = tk.Tk()
    root.title("Word Finder")

    label = tk.Label(root, text="Click the button to select a text file and search for the word 'test'.")
    label.pack(pady=10)

    button = tk.Button(root, text="Select File", command=select_file_and_display_lines)
    button.pack(pady=10)

    root.geometry("400x200")
    root.mainloop()


if __name__ == "__main__":
    create_gui()
