# Security Vulnerability Checker

This program is a Python tool for analyzing C and SQL files to detect potential security vulnerabilities. It scans for common programming mistakes and security risks, helping developers identify issues such as buffer overflows, format string vulnerabilities, and SQL injection risks.

## File Selectors

### C File Selector
The C File Selector checks C code for various security issues, including:

Off-by-One Errors: Identifies potential errors in loops by checking loop conditions and array indexing.
Format String Vulnerabilities: Detects cases where format strings may be missing, leading to possible vulnerabilities.
Buffer Overflow Vulnerabilities: Checks for the usage of unsafe functions (e.g., gets, strcpy, sprintf) and identifies fixed-size buffers, which can lead to buffer overflows.
Dynamic Query Construction Vulnerabilities: Detects unsafe dynamic query constructions involving SQL keywords, potentially leading to SQL injection.

### SQL File Selector
The SQL File Selector performs similar checks on SQL-related code. It includes:

Off-by-One Errors: Checks for potential off-by-one errors in loops and array indexing.
Format String Vulnerabilities: Checks for missing format strings in functions like printf.
Buffer Overflow Vulnerabilities: Scans for unsafe functions.
SQL Injection Detection: Analyzes SQL queries for unsafe constructions that may expose vulnerabilities, such as sprintf or strcat in query construction.

### IEEE Standards

IEEE SA - P3390
* Our project considers the impact of "User Perceived Quality of Experience (QoE) on Business Performance". Our project has a friendly user interface, and runs at a conveniently near-instantaneous speed.

ISO/IEC/IEEE 29119
* Our development follows IEEE Software Testing standards. Throughout the design process, we have rigorously tested sample files by our code, including edge cases. Our testing is also keyword-driven.

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* Run the executible, a popup will open
* Select a file to scan through the popup window
* View and interact with detected vulnerability list
* There will be recommendations

## Help

Make sure you specify the correct language (C or SQL) for the file selector to read your file. If your C code uses embedded SQL, read the file twice, once for each language.

## Authors

We are an undergraduate student team at Villanova University, developing this project for our Senior Design Capstone.

Layne Lenkowski
[www.linkedin.com/in/laynelenkowski]

Connor Redman
[www.linkedin.com/in/connorredman]

James DiBiasi
[www.linkedin.com/in/jamesdibiasi]

Chiwikem Orji
[www.linkedin.com/in/chiwuikemorji]


## Acknowledgments

This project was developed through research and supplementation from the below resources:
* [ChatGPT]
* [Secure Coding in C and C++, by Robert C. Seacord, 2006]
