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

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* Run the extension
* Select a file to scan through the popup window
* View and interact with detected vulnerability list
* There will be recommendations

## Help

Make sure the file you are reading is correctly labeled with the respective .c or .sql tag.

## Authors

We are a Villanova undergraduate student team developing this project for our Senior Design Capstone.
Contact us with our info below:

Layne Lenkowski
[@Tag](https://linkedin)
Connor Redman
James DiBiasi
Chiwikem Orji

## Version History

FINISH COMPREHENSIVE VERSION HISTORY

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is not yet licensed.

## Acknowledgments

This project was developed through research and supplementation from the below resources:
* [ChatGPT](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [TEXTBOOK NAME](https://github.com/dbader/readme-template)
