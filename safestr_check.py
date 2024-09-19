import re
import sys

# function to confirm that SafeStr isn't used before its Trust flag is checked
def check_safestr_usage(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    safestr_vars = set()  # Store variables using SafeStr
    trusted_checks = set()  # Track if "safestr_istrusted" is checked

    for idx, line in enumerate(lines):
        # Check for SafeStr variable declaration (e.g. SafeStr my_var;)
        safestr_match = re.search(r'\bSafeStr\b\s+(\w+)', line)
        if safestr_match:
            var_name = safestr_match.group(1)
            safestr_vars.add(var_name)
            print(f"Found SafeStr declaration on line {idx+1}: {line.strip()}")

        # Check for safestr_istrusted check (e.g. if (safestr_istrusted(my_var))
        trusted_match = re.search(r'\bsafestr_istrusted\s*\(\s*(\w+)\s*\)', line)
        if trusted_match:
            var_name = trusted_match.group(1)
            trusted_checks.add(var_name)
            print(f"Found safestr_istrusted check on line {idx+1}: {line.strip()}")

    # Now check if there are SafeStr usages without safestr_istrusted checks
    for idx, line in enumerate(lines):
        # Look for any usage of the SafeStr variable
        for var in safestr_vars:
            if var in line and re.search(r'\b{}\b'.format(var), line):
                if var not in trusted_checks:
                    print(f"WARNING: SafeStr '{var}' used without safestr_istrusted check on line {idx+1}: {line.strip()}")