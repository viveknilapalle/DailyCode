# Day 02 --- Variables and Data Types (Python)

**Track:** DailyCode\
**Topic:** Python Fundamentals\
**Level:** Beginner

## Learning objectives

By the end of this lesson, you should be able to:

-   Explain variables and Python's dynamic typing.
-   Follow Python variable naming rules and conventions.
-   Identify `int`, `float`, `str`, `bool`, and `NoneType` values.
-   Inspect types using `type()` and `isinstance()`.
-   Convert values using `int()`, `float()`, `str()`, and `bool()`.
-   Accept and convert user input.
-   Build a marks and percentage calculator.

------------------------------------------------------------------------

## 1. Variables

### 1.1 What is a variable?

A variable is a name that refers to an object (a value) in a Python
program.

``` python
name = "Vivek"
age = 23
percentage = 85.5
```

Python does not require a separate variable declaration or a type
declaration before assignment.

### 1.2 Names refer to objects

In Python, variables are references (names bound to objects). Assigning
a new value to a variable rebinds the name; it does not change the
original object.

``` python
a = 100
b = a

a = 200

print(a)  # 200
print(b)  # 100
```

After `b = a`, both names initially refer to the integer object `100`.
Reassigning `a` does not reassign `b`.

### 1.3 Variable naming rules

-   A name must start with a letter (`A-Z`, `a-z`) or underscore (`_`).
-   It may contain letters, digits, and underscores.
-   It cannot start with a digit.
-   Names are case-sensitive: `age`, `Age`, and `AGE` are different
    names.
-   A Python keyword (such as `if`, `for`, or `class`) cannot be used as
    a variable name.
-   Spaces and punctuation such as `-`, `@`, and `$` are not allowed.

  Name             Valid?   Reason
  ---------------- -------- ----------------------------------------------
  `name`           Yes      Starts with a letter
  `_age`           Yes      Starts with underscore
  `student1`       Yes      Digits are allowed after the first character
  `1student`       No       Starts with a digit
  `student-name`   No       Hyphen is not allowed
  `student name`   No       Contains a space
  `class`          No       Python keyword

### 1.4 Naming convention: `snake_case`

Use descriptive names and lowercase words separated by underscores.

``` python
student_name = "Rahul"
total_marks = 450
average_percentage = 90.0
is_passed = True
```

Prefer `total_marks` over unclear names such as `x` or `a` when the
variable represents total marks.

### 1.5 Dynamic typing

Python is dynamically typed: the type is associated with the object, and
a name can be rebound to objects of different types while the program
runs.

``` python
value = 100
print(type(value))  # <class 'int'>

value = 45.5
print(type(value))  # <class 'float'>

value = "Python"
print(type(value))  # <class 'str'>
```

Python also supports optional type annotations:

``` python
age: int = 23
name: str = "Vivek"
```

Annotations help communicate intended types and support tools such as
type checkers. They do not generally enforce types at runtime.

**Dynamic vs. static typing (simplified):**

  -----------------------------------------------------------------------
  Dynamic typing                      Static typing
  ----------------------------------- -----------------------------------
  Types are checked primarily at      Types are checked primarily before
  runtime                             execution

  Explicit declarations are generally Type declarations are commonly used
  not required                        or required

  Example: Python                     Examples: Java, C#
  -----------------------------------------------------------------------

Python is also strongly typed: it does not silently combine incompatible
types in many operations. For example, `"Age: " + 23` raises a
`TypeError`.

------------------------------------------------------------------------

## 2. Fundamental built-in data types

A data type describes the kind of value an object represents and the
operations that can be performed on it.

### 2.1 Integer --- `int`

Represents whole numbers, including positive numbers, negative numbers,
and zero.

``` python
age = 23
marks = 95
temperature = -10
population = 1_000_000
```

Python integers can grow beyond fixed 32-bit or 64-bit ranges, subject
to available memory.

Common operations:

``` python
a = 20
b = 10

print(a + b)   # 30
print(a - b)   # 10
print(a * b)   # 200
print(a // b)  # 2: floor division
print(a % b)   # 0: remainder
```

### 2.2 Floating-point --- `float`

Represents numbers with a fractional component.

``` python
price = 99.99
percentage = 87.5
temperature = -3.14
```

Example:

``` python
length = 10.5
width = 5.2
area = length * width

print(area)  # 54.6
```

**Floating-point precision:** Many decimal fractions cannot be
represented exactly in binary floating-point.

``` python
print(0.1 + 0.2)
# 0.30000000000000004
```

For decimal arithmetic requiring exact decimal representation (such as
some financial calculations), consider Python's `decimal` module.

### 2.3 String --- `str`

Represents text: a sequence of Unicode characters.

Strings can use single, double, or triple quotes.

``` python
name = "Vivek"
language = 'Python'
message = """Welcome to Python programming."""
```

Common string operations:

``` python
first_name = "Vivek"
last_name = "Nilapalle"

full_name = first_name + " " + last_name  # Concatenation

print("Hi! " * 3)       # Repetition
print(len(full_name))  # Length
print(first_name[0])   # Indexing: V
print(first_name[0:3]) # Slicing: Viv
```

Important properties:

-   Strings are ordered.
-   They support indexing and slicing.
-   Strings are immutable: individual characters cannot be changed in
    place.

### 2.4 Boolean --- `bool`

Represents one of two logical values: `True` or `False`. Their first
letters must be uppercase.

``` python
is_passed = True
is_absent = False

print(is_passed)        # True
print(type(is_passed))  # <class 'bool'>
```

Booleans commonly result from comparisons:

``` python
marks = 75
is_passed = marks >= 35

print(is_passed)  # True
```

Comparison operators:

  Operator   Meaning                    Example
  ---------- -------------------------- ------------
  `==`       Equal to                   `10 == 10`
  `!=`       Not equal to               `10 != 5`
  `>`        Greater than               `10 > 5`
  `<`        Less than                  `5 < 10`
  `>=`       Greater than or equal to   `10 >= 10`
  `<=`       Less than or equal to      `5 <= 10`

### 2.5 None --- `NoneType`

`None` represents the absence of a value or a value that is not
currently available.

``` python
result = None

print(result)        # None
print(type(result))  # <class 'NoneType'>
```

Common uses include:

-   Initializing a variable before a value is available.
-   Representing a missing or optional value.
-   Returning no meaningful result from a function.

`None` is different from `0`, `False`, and an empty string (`""`).

  Value     Type
  --------- ------------
  `None`    `NoneType`
  `0`       `int`
  `False`   `bool`
  `""`      `str`

When checking for `None`, use identity comparison:

``` python
if result is None:
    print("No result is available")
```

------------------------------------------------------------------------

## 3. Checking types: `type()` and `isinstance()`

### 3.1 The `type()` function

`type()` returns the exact type of an object.

``` python
name = "Vivek"
age = 23
percentage = 89.5
is_student = True
result = None

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(percentage))  # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(result))      # <class 'NoneType'>
```

### 3.2 The `isinstance()` function

`isinstance(object, type)` checks whether an object is an instance of a
specified type or its subclass.

``` python
age = 23

print(isinstance(age, int))    # True
print(isinstance(age, float))  # False
```

### 3.3 `type()` vs. `isinstance()`

``` python
print(type(True) == int)      # False
print(isinstance(True, int))  # True
```

This happens because `bool` is a subclass of `int` in Python. Use
`type()` when you need the exact type; use `isinstance()` when checking
type compatibility, including inheritance.

------------------------------------------------------------------------

## 4. Type conversion

Type conversion changes a value from one type to another.

There are two broad forms:

1.  **Implicit conversion:** Python performs a conversion automatically
    in certain operations.
2.  **Explicit conversion (type casting):** The programmer requests
    conversion using a function such as `int()` or `float()`.

### 4.1 Implicit conversion

In some numeric operations, Python promotes an integer to a float.

``` python
a = 10       # int
b = 5.5      # float

result = a + b

print(result)        # 15.5
print(type(result))  # <class 'float'>
```

The integer is used as a float for the operation, and the result is a
float.

### 4.2 Explicit conversion with `int()`

Converts compatible values to integers. When converting a float, the
fractional part is discarded (truncated toward zero); it is not rounded.

``` python
a = int(10.8)    # 10
b = int("250")   # 250
c = int(-5.9)    # -5

print(a, b, c)
```

A string such as `"25.5"` cannot be passed directly to `int()`:

``` python
# int("25.5")  # ValueError

value = int(float("25.5"))
print(value)  # 25
```

### 4.3 Explicit conversion with `float()`

Converts compatible values to floating-point numbers.

``` python
a = float(10)       # 10.0
b = float("25.75")  # 25.75
c = float("100")    # 100.0

print(a, b, c)
```

### 4.4 Explicit conversion with `str()`

Creates a string representation of a value.

``` python
age = 23
percentage = 89.5
is_passed = True

print(str(age))        # "23"
print(str(percentage)) # "89.5"
print(str(is_passed))  # "True"
```

This is useful when combining values with text.

``` python
age = 23

print("My age is " + str(age))
print(f"My age is {age}")  # f-string alternative
```

### 4.5 Explicit conversion with `bool()`

Converts a value according to Python's truth-value rules.

Common false values:

``` python
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(""))      # False
print(bool(None))    # False
print(bool(False))   # False
print(bool([]))      # False
print(bool({}))      # False
print(bool(()))      # False
```

Common true values:

``` python
print(bool(1))         # True
print(bool(-10))       # True
print(bool(10.5))      # True
print(bool("Python"))  # True
print(bool("False"))   # True
print(bool([1, 2]))    # True
```

**Important:** `bool("False")` is `True` because the string is
non-empty. `bool()` does not interpret the text `"False"` as the Boolean
value `False`.

### 4.6 Common conversion results and errors

  Expression          Result
  ------------------- --------------
  `int("100")`        `100`
  `int("Hello")`      `ValueError`
  `int("10.5")`       `ValueError`
  `int(10.9)`         `10`
  `float("12.5")`     `12.5`
  `float("Python")`   `ValueError`
  `str(100)`          `"100"`
  `bool("")`          `False`
  `bool("0")`         `True`

Invalid conversions commonly raise `ValueError` or `TypeError`. Validate
or handle input when values come from users.

------------------------------------------------------------------------

## 5. User input and data types

### 5.1 The `input()` function

`input()` displays an optional prompt and reads a line from the user. It
always returns a string.

``` python
name = input("Enter your name: ")
print("Welcome", name)
```

Even if the user enters `23`, the returned value is `"23"` (a string).

``` python
age = input("Enter your age: ")

print(age)
print(type(age))  # <class 'str'>
```

### 5.2 Convert input before calculations

Convert input to the required type before performing numeric operations.

``` python
age = int(input("Enter your age: "))
print(age + 5)
```

For decimal input:

``` python
percentage = float(input("Enter percentage: "))
print(percentage + 5)
```

### 5.3 Taking multiple inputs

``` python
name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

print("\nStudent Details")
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
```

### 5.4 Handling invalid input with `try-except`

Direct conversion can fail if a user enters text that is not a valid
number.

``` python
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Please enter a valid whole number.")
```

`try-except` allows the program to handle the conversion error instead
of terminating with an unhandled exception.

------------------------------------------------------------------------

## 6. Practical program: Marks and percentage calculator

### 6.1 Problem statement

Create a program that accepts a student's name and marks in five
subjects, calculates the total and percentage, and displays the result.

**Requirements:**

-   Accept the student's name.
-   Accept marks for five subjects.
-   Each subject has a maximum of 100 marks.
-   Calculate total marks.
-   Calculate percentage.
-   Display the student details and result.

### 6.2 Formula

Let the five subject marks be (M_1, M_2, M_3, M_4, M_5).

**Total marks:**

``` text
Total = M1 + M2 + M3 + M4 + M5
```

**Maximum marks:**

``` text
Maximum = 5 × 100 = 500
```

**Percentage:**

``` text
Percentage = (Total / Maximum) × 100
```

### 6.3 Basic implementation

``` python
# Student Marks and Percentage Calculator

name = input("Enter student name: ")

subject1 = float(input("Enter Subject 1 marks: "))
subject2 = float(input("Enter Subject 2 marks: "))
subject3 = float(input("Enter Subject 3 marks: "))
subject4 = float(input("Enter Subject 4 marks: "))
subject5 = float(input("Enter Subject 5 marks: "))

total_marks = (
    subject1 + subject2 + subject3 +
    subject4 + subject5
)

maximum_marks = 500
percentage = (total_marks / maximum_marks) * 100

print("\n------ STUDENT RESULT ------")
print(f"Student Name: {name}")
print(f"Total Marks: {total_marks}/{maximum_marks}")
print(f"Percentage: {percentage:.2f}%")
```

### 6.4 Sample run

``` text
Enter student name: Vivek
Enter Subject 1 marks: 90
Enter Subject 2 marks: 85
Enter Subject 3 marks: 92
Enter Subject 4 marks: 88
Enter Subject 5 marks: 95

------ STUDENT RESULT ------
Student Name: Vivek
Total Marks: 450.0/500
Percentage: 90.00%
```

### 6.5 Concepts used

  Concept                Application
  ---------------------- --------------------------------------------
  Variables              Store student details and marks
  `str`                  Store the student's name
  `float`                Store subject marks
  `input()`              Accept user input
  `float()`              Convert input into numeric values
  Arithmetic operators   Calculate total marks
  Division               Calculate percentage
  f-strings              Display formatted output
  `:.2f`                 Display two digits after the decimal point

### 6.6 Improved implementation using a list and loop

This version reduces repetition. It introduces lists, loops, and
`sum()`, which can be studied in more detail in later lessons.

``` python
name = input("Enter student name: ")

subjects = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "English",
    "Computer Science"
]

marks = []

for subject in subjects:
    mark = float(input(f"Enter {subject} marks: "))
    marks.append(mark)

total_marks = sum(marks)
maximum_marks = len(subjects) * 100
percentage = (total_marks / maximum_marks) * 100

print("\n------ STUDENT RESULT ------")
print(f"Name: {name}")
print(f"Total: {total_marks}/{maximum_marks}")
print(f"Percentage: {percentage:.2f}%")
```

**Note:** Both examples assume valid marks between 0 and 100. Add input
validation as an extension.

------------------------------------------------------------------------

## 7. Additional practice exercises

Try implementing these without referring to solutions first.

### Exercise 1 --- Basic variable operations

Create variables for your name, age, city, and programming language.
Print them with appropriate labels.

**Concepts:** Variables, strings, integers.

### Exercise 2 --- Type identification

Create five variables with different data types. Use `type()` to display
their data types.

**Concepts:** Data types, `type()`.

### Exercise 3 --- Type conversion

Take two numbers as input. Convert them into integers and calculate
their sum, difference, product, and division.

**Concepts:** `input()`, `int()`, arithmetic operators.

### Exercise 4 --- Temperature converter

Accept temperature in Celsius and convert it into Fahrenheit.

Formula:

``` text
F = (C × 9 / 5) + 32
```

**Concepts:** `float()`, arithmetic operations.

### Exercise 5 --- Simple shopping bill

Accept a product name, quantity, and price per item. Calculate and
display the total bill.

**Concepts:** Variables, strings, integers, floats.

### Exercise 6 --- Boolean practice

Create variables representing whether a student is present, whether fees
are paid, and whether the student is eligible for an examination. Print
their values and types.

**Concepts:** `bool`, Boolean values.

------------------------------------------------------------------------

## 8. Interview questions

1.  What is a variable in Python?
2.  What is dynamic typing?
3.  What are the rules for naming variables?
4.  What is the difference between `int` and `float`?
5.  Is Python dynamically typed? Is it strongly typed?
6.  What is the difference between mutable and immutable objects?
7.  What does the `type()` function do?
8.  What is the difference between `type()` and `isinstance()`?
9.  What is type conversion?
10. What is the difference between implicit and explicit conversion?
11. Why does `input()` return a string?
12. What happens when you execute `int("10.5")`?
13. What is the difference between `None` and `False`?
14. Why does `bool("False")` return `True`?
15. What is the difference between `==` and `is`?

------------------------------------------------------------------------

## 9. Quick revision sheet

  Topic            Key point
  ---------------- -----------------------------------------------------
  Variable         A name bound to an object
  Dynamic typing   A name can be rebound to objects of different types
  `int`            Whole numbers
  `float`          Floating-point numbers
  `str`            Text
  `bool`           `True` or `False`
  `None`           Represents absence of a value
  `type()`         Returns an object's exact type
  `isinstance()`   Checks type compatibility
  `int()`          Converts compatible values to integers
  `float()`        Converts compatible values to floats
  `str()`          Creates a string representation
  `bool()`         Converts according to truth-value rules
  `input()`        Reads user input as a string

### Key takeaways

-   Python is dynamically typed and strongly typed.
-   Variable names are case-sensitive.
-   Use `snake_case` for variable names.
-   `input()` always returns a string.
-   `int()` truncates a float; it does not round it.
-   Strings are immutable.
-   `None` is not the same as `0`, `False`, or `""`.
-   `bool(0)` is `False`, while `bool("0")` is `True`.
-   Python supports implicit and explicit type conversion.

-----------------------------------------------------------------------