# Password Strength Checker

A simple Python program that analyzes a password and rates its strength as Weak, Medium, or Strong. It also gives feedback on how to make the password more secure.

## Features

- Checks minimum password length
- Verifies use of uppercase and lowercase letters
- Verifies use of digits and special characters
- Rates the password as Weak, Medium, or Strong
- Suggests improvements for weak passwords

## Requirements

- Python 3.8 or higher
- No external libraries required

## Installation

```bash
git clone https://github.com/<your-username>/password-strength-checker.git
cd password-strength-checker
```

## Usage

```bash
python password_checker.py
```

Enter a password when prompted. The program prints the strength rating and suggestions.

## Example

```
Enter a password: hello123
Strength: Weak
Suggestions:
- Add at least one uppercase letter
- Add at least one special character
- Use at least 12 characters
```

## How It Works

The program assigns a score based on the following criteria:

| Criteria                         | Points |
|----------------------------------|--------|
| Length of 8 or more characters   | 1      |
| Length of 12 or more characters  | 1      |
| Contains uppercase letter        | 1      |
| Contains lowercase letter        | 1      |
| Contains a digit                 | 1      |
| Contains a special character     | 1      |

The total score maps to the final rating.

## Project Structure

```
password-strength-checker/
|-- password_checker.py
|-- README.md
```

## Future Improvements

- Check against a list of commonly used passwords
- Add a GUI using Tkinter or Streamlit
- Detect repeated or sequential characters

## Author

Kalpana
MCA Student, Galgotias College
GitHub: https://github.com/<your-username>

## License

This project is licensed under the MIT License.
