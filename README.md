# Email Checker (Python)

A simple Python program that validates email addresses based on multiple conditions such as correct format, allowed characters, proper use of the `@` symbol, and domain structure.

This project demonstrates **basic input validation, string handling, and conditional logic in Python**. It is designed as a beginner-friendly project for learning Python and understanding how email validation works.

---

## Features

* Checks if the email contains exactly **one `@` symbol**
* Ensures the **first character is valid**
* Validates **email length**
* Detects **invalid special characters**
* Prevents **spaces in the email**
* Confirms the **email domain format**

---

## Technologies Used

* Python 3
* Basic Python concepts:

  * Loops
  * Conditional statements
  * String methods

---

## Project Structure

```
email-checker/

├── email_checker.py
└── README.md
```

---

##  How to Run the Program

1. Clone the repository

```
git clone https://github.com/your-username/email-checker.git
```

2. Navigate to the project folder

```
cd email-checker
```

3. Run the Python program

```
python email_checker.py
```

---

## Example

### Input

```
Enter email: user123@gmail.com
```

### Output

```
user123@gmail.com is a valid email address.
```

### Invalid Example

```
Enter email: user@@gmail.com
Invalid email. The '@' symbol is missing or used more than once.
```

---

## Learning Goals

This project helps beginners understand:

* Input validation
* String manipulation
* Python loops and conditions
* Writing simple command-line programs

---

## Future Improvements

* Add **regex-based validation**
* Support for **multiple email domains**
* Build a **GUI version using Tkinter**
* Create a **web-based email validator**

---

##  License

This project is open-source and available for learning and educational purposes.
