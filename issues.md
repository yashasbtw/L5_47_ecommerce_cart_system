# Lab 5: Static Analysis Findings

**Student:** Yashas  
**SRN:** PES2UG24CS609  
**Program:** E-Commerce Cart System

Findings below come from the baseline Pylint, Bandit, and Flake8 reports. High and medium severity security findings are listed first.

| Issue | Type / tool | Baseline line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Weak MD5 digest | High / Bandit B324 | 49 | MD5 is unsuitable where collision resistance is expected. | Replaced MD5 with SHA-256. |
| Shell command with a filename | High / Bandit B605 | 60 | A filename was concatenated into a shell command, creating command-injection risk. | Removed shell execution; receipt writing now uses `pathlib` and the saved path is printed normally. |
| Dynamic `eval` | Medium / Bandit B307, Pylint W0123 | 44 | A discount string was evaluated as arbitrary Python code. | Replaced expression evaluation with a validated numeric discount rate in the inclusive range 0–1. |
| Mutable default and global state | Pylint W0102, W0603 | 15–16 | A shared list default and a global sales counter could leak state between calls. | Removed the unused shared audit-log parameter and stopped mutating a global counter. |
| Broad exception handling | Low / Bandit B110, Pylint W0702, Flake8 E722 | 28 | A bare `except` hid errors while deleting an item. | Replaced the `try`/`except` with `dict.pop(..., None)` and an explicit success result. |
| Predictable checkout PIN | Low / Bandit B311 | 53 | `random.randint` is not suitable for security-related PIN generation. | Switched to `secrets.randbelow` and retained the four-digit range. |
| Style, unused code, and names | Pylint / Flake8 | 1–76 | The baseline had unused imports/locals, naming and documentation issues, and formatting violations. | Removed unused code, used `snake_case`, added docstrings, simplified conditions, and formatted long lines. |
| Hard-coded gateway-looking value | Manual review | 70 | A credential-like value was embedded in the demo and printed. | Removed the value and its output; secrets should be supplied through a protected runtime configuration. |

## Verification

- Baseline Pylint: 4.04/10.
- Final Pylint: 10.00/10.
- Baseline Bandit: 5 findings (2 high, 1 medium, 2 low).
- Final Bandit: 0 findings.
- Final Flake8: exit code 0 with no reported violations.
- The updated program ran successfully and wrote its receipt in the Lab 5 working folder.
