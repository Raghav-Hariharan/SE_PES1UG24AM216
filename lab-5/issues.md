
# Lab 5 – Static Code Analysis: Issues and Fixes

## Issue Documentation

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Weak MD5 hashing (B324) | Security – High | 16 | MD5 is a weak hashing algorithm and is unsuitable for security-sensitive use. | Replaced MD5 with SHA-256. |
| Shell command execution (B605) | Security – High | 56 | `os.system()` constructs a shell command using user-controlled input, creating command-injection risk. | Replaced it with `subprocess.run()` using an argument list and `shell=False`; validated the hostname. |
| Hardcoded password (B105) | Security – Low | 11 | A proctor password was stored directly in the source code and was not used by the program. | Removed the unused hardcoded credential. |
| Insecure random generator (B311) | Security – Low | 20 | `random.choice()` uses a pseudo-random generator that is not intended for security-sensitive selection. | Replaced it with `secrets.choice()`. |
| Mutable default argument (W0102) | Code Quality | 23 | Using `{}` as a default argument shares the same dictionary across function calls. | Changed the default to `None` and initialized a new dictionary inside the function. |
| Missing module and function docstrings (C0114, C0116) | Code Quality | Multiple | The module and functions lacked documentation. | Added descriptive module and function docstrings. |
| Invalid naming conventions (C0103) | Code Quality | Multiple | Functions and parameters used camelCase instead of Python's snake_case convention. | Renamed functions and parameters using snake_case and updated their callers. |
| Inefficient loop (C0200) | Code Quality | 25 | The code used `range(len(QUESTIONS))` to iterate over a list. | Replaced it with `enumerate()`. |
| Unnecessary elif (R1705) | Code Quality | 37 | An `elif` followed a branch that already returned a value. | Replaced the unnecessary `elif` with `if`. |
| Missing whitespace (E225) | Style | 67 | An assignment operator lacked surrounding whitespace. | Added spaces around the assignment operator. |
| Missing blank line (E302) | Style | 54 | A top-level function did not have the required two blank lines before it. | Added the required blank line. |
| Inline comment spacing (E261) | Style | 69 | An inline comment did not have sufficient spacing before it. | Added the required spacing. |
| Line too long (E501) | Style | 70 | A line exceeded Flake8's 79-character limit. | Split the statement across multiple lines. |

## Verification Notes

- Pylint improved from 5.65/10 to 10.00/10.
- Flake8 reported no remaining style violations.
- Bandit reported no remaining high-severity findings.
- Bandit still reports three low-severity warnings related to subprocess usage (B404, B607 and B603). These were retained and documented rather than suppressed.
- The program was executed successfully after the changes.
