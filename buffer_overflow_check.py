import re


def detect_buffer_overflow(c_code):
    # Regular expressions to match potentially unsafe functions
    unsafe_functions = [
        r'\bgets\s*\(',  # matches gets function
        r'\bstrcpy\s*\(',  # matches strcpy function
        r'\bstrcat\s*\(',  # matches strcat function
        r'\bsprintf\s*\(',  # matches sprintf function
        r'\bscanf\s*\(',  # matches scanf function
    ]

    # Check for fixed size buffers being used with unsafe functions
    buffer_size_pattern = r'char\s+\w+\s*\[\s*(\d+)\s*\]'

    # Searching for possible buffer overflows
    vulnerabilities = []

    # Check for unsafe functions
    for pattern in unsafe_functions:
        matches = re.findall(pattern, c_code)
        for match in matches:
            vulnerabilities.append(f"Potential buffer overflow with function: {match}")

    # Check for fixed size buffer declarations
    buffer_matches = re.findall(buffer_size_pattern, c_code)
    for match in buffer_matches:
        vulnerabilities.append(f"Fixed size buffer found with size: {match}")

    return vulnerabilities


# Sample C code to test
sample_c_code = """
#include <stdio.h>
#include <string.h>

int main() {
    char buffer[10];
    gets(buffer);  // unsafe
    strcpy(buffer, "This is a test");  // unsafe
    return 0;
}
"""

# Detect vulnerabilities in the sample C code
vulnerabilities_found = detect_buffer_overflow(sample_c_code)

# Print the results
if vulnerabilities_found:
    print("Vulnerabilities detected:")
    for vuln in vulnerabilities_found:
        print(vuln)
else:
    print("No vulnerabilities detected.")
