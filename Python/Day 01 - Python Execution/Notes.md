# Python Introduction and Basics

## 1. Learning Objectives

By the end of this day, you should understand:

- What Python is and where it is used.
- How Python code is executed.
- The difference between the Python interpreter, interactive shell, and script.
- How to use `print()` and `input()`.
- What variables are and how to store values.
- Basic comments and indentation.
- How to format output using f-strings.

---

## 2. What is Python?

Python is a high-level, general-purpose programming language known for its readable syntax and simplicity.

### Key Features

- **Easy to read:** Uses simple and readable syntax.
- **Interpreted:** Python code is executed by the Python runtime.
- **Dynamically typed:** You do not need to explicitly declare variable types.
- **Object-oriented:** Supports classes, objects, inheritance, and polymorphism.
- **Cross-platform:** Runs on Windows, Linux, and macOS.
- **Large standard library:** Provides built-in modules for common tasks.

### Where is Python Used?

- Web development – Django, Flask, FastAPI.
- Data analysis – Pandas, NumPy.
- Artificial Intelligence and Machine Learning.
- Automation and scripting.
- API development.
- Testing and software development.
- Data processing.

---

## 3. How Python Code Executes

Python code is processed by the Python interpreter/runtime.

A simplified execution flow:

1. Write Python code in a `.py` file.
2. The Python runtime processes the code.
3. Python generally compiles source code into bytecode.
4. The Python Virtual Machine (PVM) executes that bytecode.

**Example:**

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

### Python Interpreter

The interpreter is the program/runtime responsible for executing Python code.

Check the installed Python version:

```bash
python --version
```

or:

```bash
python -V
```

---

## 4. Ways to Execute Python Code

### A. Interactive Shell

Allows you to execute Python statements directly, one at a time.

Start it using:

```bash
python
```

Example:

```python
>>> print("Hello")
Hello

>>> 10 + 20
30
```

Exit using:

```python
exit()
```

**Use case:** Quickly testing small expressions and code snippets.

### B. Python Script

A Python script is a file containing Python code, usually saved with the `.py` extension.

Example: `hello.py`

```python
print("Hello, Python!")
print("I am learning programming.")
```

Execute it using:

```bash
python hello.py
```

**Use case:** Writing programs, applications, and reusable code.

---

## 5. The print() Function

The `print()` function displays information on the standard output, normally the terminal.

### Basic Syntax

```python
print(value)
```

### Examples

```python
print("Hello World")
print(100)
print(10.5)
print(True)
```

Output:

```text
Hello World
100
10.5
True
```

### Printing Multiple Values

```python
print("Name:", "Rahul", "Age:", 24)
```

Output:

```text
Name: Rahul Age: 24
```

### Understanding the print() Parameters

```python
print(*values, sep=" ", end="\n", file=None, flush=False)
```

| Parameter | Purpose | Default |
|---|---|---|
| `*values` | Accepts multiple values to display | No values |
| `sep` | Defines the separator between values | Space |
| `end` | Defines what is printed at the end | Newline |
| `file` | Specifies the output destination | Standard output |
| `flush` | Controls immediate flushing of buffered output | `False` |

### A. sep – Separator

Defines what appears between multiple values.

```python
print("Hello", "Python", "World")
```

Output:

```text
Hello Python World
```

Custom separator:

```python
print("Hello", "Python", "World", sep="-")
```

Output:

```text
Hello-Python-World
```

### B. end – Ending Character

By default, `print()` adds a newline after displaying the output.

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

Using a custom ending:

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

### C. file – Output Destination

By default, output goes to the terminal. You can redirect it to a file.

```python
with open("output.txt", "w") as file:
    print("Hello Python", file=file)
```

This writes the message into `output.txt`.

### D. flush – Immediate Output

Controls whether buffered output is immediately sent to its destination.

```python
print("Processing...", flush=True)
```

Useful for progress indicators and real-time output.

### E. Return Type

The `print()` function returns `None`.

```python
result = print("Hello")

print(result)
```

Output:

```text
Hello
None
```

**Remember:** `print()` displays information; it does not return the displayed text.

---

## 6. The input() Function

The `input()` function collects information from the user.

### Syntax

```python
variable = input("Enter something: ")
```

Example:

```python
name = input("Enter your name: ")

print(name)
```

Output:

```text
Enter your name: Rahul
Rahul
```

### Important: input() Returns a String

Even if the user enters a number, `input()` returns it as a string.

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

### Converting User Input

Use `int()` to convert input into an integer.

```python
age = int(input("Enter your age: "))

print(age)
print(type(age))
```

Use `float()` for decimal values.

```python
height = float(input("Enter your height: "))

print(height)
```

**Important:** Converting invalid input can raise a `ValueError`. You will learn how to handle this with exceptions later.

---

## 7. Variables in Python

A variable is a name used to refer to a value stored in memory.

Example:

```python
name = "Rahul"
age = 24
city = "Hyderabad"
```

Here:

- `name` refers to the string `"Rahul"`.
- `age` refers to the integer `24`.
- `city` refers to the string `"Hyderabad"`.

Python does not require explicit type declarations.

```python
value = 100
value = "Python"

print(value)
```

Output:

```text
Python
```

This is possible because Python is dynamically typed.

### Variable Naming Rules

1. A variable name can contain letters, numbers, and underscores.
2. It cannot start with a number.
3. Variable names are case-sensitive.
4. Python keywords cannot be used as variable names.
5. Use meaningful names.

Valid examples:

```python
name = "Rahul"
user_age = 24
total_marks = 450
```

Invalid examples:

```python
# 1name = "Rahul"
# user-age = 24
# class = "Python"
```

### Multiple Variable Assignment

```python
name, age, city = "Rahul", 24, "Hyderabad"

print(name, age, city)
```

You can also assign the same value to multiple variables:

```python
a = b = c = 10
```

---

## 8. Basic Data Types

Python provides different built-in data types.

| Data Type | Description | Example |
|---|---|---|
| `int` | Integer numbers | `25` |
| `float` | Decimal numbers | `25.5` |
| `str` | Text | `"Python"` |
| `bool` | True or False | `True` |
| `NoneType` | Absence of a value | `None` |

Use `type()` to identify a value's type.

```python
name = "Rahul"
age = 24
height = 5.8
is_student = True
result = None

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(result))
```

---

## 9. Type Conversion

Type conversion means converting a value from one data type to another.

Common conversion functions:

| Function | Conversion |
|---|---|
| `int()` | Converts to integer |
| `float()` | Converts to float |
| `str()` | Converts to string |
| `bool()` | Converts to Boolean |

Examples:

```python
age = "24"
age = int(age)

price = "99.50"
price = float(price)

number = 100
text = str(number)

print(age, type(age))
print(price, type(price))
print(text, type(text))
```

---

## 10. Comments in Python

Comments are notes written in code that Python does not execute as statements.

### Single-line Comments

Use `#`.

```python
# This is a comment
name = "Rahul"
```

### Multi-line Explanatory Text

Python does not have a dedicated multiline comment syntax. Multiple `#` lines are commonly used.

```python
# This program collects user information.
# It displays a personal introduction.
# It is a Day 01 practice program.
```

Triple-quoted strings are often used for documentation strings (docstrings), not as a dedicated comment syntax.

---

## 11. Indentation in Python

Indentation means the spaces at the beginning of a line.

Python uses indentation to define code blocks.

Example:

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

The indented statement belongs to the `if` block.

Incorrect indentation can cause an `IndentationError`.

**Best practice:** Use four spaces for each indentation level.

---

## 12. String Formatting – f-strings

f-strings allow you to insert variables and expressions directly into strings.

Place `f` before the opening quotation mark.

Example:

```python
name = "Rahul"
age = 24

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Rahul and I am 24 years old.
```

You can also perform expressions inside f-strings.

```python
a = 10
b = 20

print(f"Sum: {a + b}")
```

Output:

```text
Sum: 30
```

---

## 13. Practical Exercise – Personal Introduction Program

### Objective

Build a program that collects a user's name, age, and city, then displays a formatted introduction.

### Requirements

1. Ask the user for their name.
2. Ask the user for their age.
3. Ask the user for their city.
4. Convert age into an integer.
5. Display the information using f-strings.
6. Format the output neatly.

### Expected Output

```text
Enter your name: Rahul
Enter your age: 24
Enter your city: Hyderabad

--------- Personal Introduction ---------

Hello! My name is Rahul.
I am 24 years old.
I live in Hyderabad.

Nice to meet you!
```



## 14. Common Mistakes to Avoid

| Mistake | Explanation |
|---|---|
| Forgetting quotation marks | Text must be enclosed in quotes. |
| Treating input as an integer | `input()` always returns a string. |
| Incorrect indentation | Python uses indentation to define blocks. |
| Using `=` instead of `==` in comparisons | `=` assigns; `==` compares. |
| Invalid variable names | Variable names must follow Python naming rules. |
| Forgetting f-string prefix | Variables inside `{}` need an f-string for interpolation. |

---

## 15. Quick Revision Questions

Try answering these without looking at the notes.

1. What is Python, and where is it used?
2. What is the role of the Python interpreter?
3. What is the difference between an interactive shell and a Python script?
4. What is the purpose of `print()`?
5. What are `sep` and `end` in `print()`?
6. What does `print()` return?
7. What is the purpose of `input()`?
8. Why do we use `int()` and `float()`?
9. What is a variable?
10. What does dynamically typed mean?
11. What is indentation, and why is it important?
12. What is an f-string?

---

**Next: Day 02 – Variables, Data Types, and Type Conversion in Greater Detail.**