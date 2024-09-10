def check_for_error_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if 'error' in line.lower():
                    print(f"Error found on line {line_number}: {line.strip()}")
                    return
        print("No 'error' found in the file.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'sample.txt'
check_for_error_in_file(file_path)
