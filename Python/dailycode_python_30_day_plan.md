# Python Foundations — 30-Day Learning Roadmap

**Track:** Python fundamentals, practical programming, and standard-library modules  
**Duration:** 30 consecutive learning days  
**Primary language:** Python  
**Outcome:** Refresh core Python knowledge, learn tools commonly used in real projects, and complete a small command-line project.

## How to use this roadmap

- Follow the days in order. Each day has a defined topic and practical task.
- Mark a day complete by changing its checkbox from `[ ]` to `[x]`.
- Commit your notes and code to GitHub regularly.
- Write explanations in your own words and implement examples yourself.
- If you miss a day, continue from the next unfinished day. Do not mark work complete unless you have done it.

**Suggested daily study time:** 60–90 minutes.

## Progress tracker

Use the checkboxes below to track your 30-day consistency. GitHub will let you tick each item directly in this README.

- [ ] Day 01
- [ ] Day 02
- [ ] Day 03
- [ ] Day 04
- [ ] Day 05
- [ ] Day 06
- [ ] Day 07
- [ ] Day 08
- [ ] Day 09
- [ ] Day 10
- [ ] Day 11
- [ ] Day 12
- [ ] Day 13
- [ ] Day 14
- [ ] Day 15
- [ ] Day 16
- [ ] Day 17
- [ ] Day 18
- [ ] Day 19
- [ ] Day 20
- [ ] Day 21
- [ ] Day 22
- [ ] Day 23
- [ ] Day 24
- [ ] Day 25
- [ ] Day 26
- [ ] Day 27
- [ ] Day 28
- [ ] Day 29
- [ ] Day 30

---

## Week 1 — Python Fundamentals

- [ ] **Day 01 — Python Setup and Execution**
  - Understand Python, the interpreter, scripts and the interactive shell.
  - Check the installed Python version; run a `.py` file.
  - Learn indentation, comments, `print()` and `input()`.
  - **Practice:** Build a program that collects a name, age and city, then prints an introduction.

- [ ] **Day 02 — Variables and Data Types**
  - Variables, naming conventions and dynamic typing.
  - `int`, `float`, `str`, `bool` and `None`.
  - `type()` and type conversion using `int()`, `float()`, `str()` and `bool()`.
  - **Practice:** Create a marks and percentage calculator.

- [ ] **Day 03 — Operators and Expressions**
  - Arithmetic, comparison, assignment and logical operators.
  - Membership (`in`) and identity (`is`) operators.
  - Operator precedence and expression evaluation.
  - **Practice:** Create a basic calculator and an even/odd checker.

- [ ] **Day 04 — Conditional Statements**
  - `if`, `elif`, `else` and nested conditions.
  - Truthy and falsy values.
  - Conditional expressions.
  - **Practice:** Build a grade calculator and a greatest-of-three-numbers program.

- [ ] **Day 05 — Loops**
  - `for`, `while` and `range()`.
  - `break`, `continue`, `pass` and nested loops.
  - Loop `else`.
  - **Practice:** Write a multiplication table, factorial, prime-number checker and pattern programs.

- [ ] **Day 06 — Strings**
  - String indexing, slicing and immutability.
  - Common methods: `split()`, `join()`, `strip()`, `replace()`, `find()`, `startswith()` and `endswith()`.
  - f-strings and string formatting.
  - **Practice:** Reverse a string, count vowels, check a palindrome and normalize user input.

## Week 2 — Python Collections and Core Operations

- [ ] **Day 07 — Lists**
  - Creation, indexing, slicing, iteration and nested lists.
  - Add, update and remove elements.
  - `append()`, `extend()`, `insert()`, `remove()`, `pop()` and `sort()`.
  - **Practice:** Build an expense list and calculate its total, average, minimum and maximum.

- [ ] **Day 08 — Tuples and Sets**
  - Tuple creation, packing and unpacking.
  - Set uniqueness and union, intersection, difference and symmetric difference.
  - `frozenset` and choosing between lists, tuples and sets.
  - **Practice:** Remove duplicates and find common elements between two lists.

- [ ] **Day 09 — Dictionaries**
  - Key-value storage, lookup, insertion, update and deletion.
  - `keys()`, `values()`, `items()`, `get()`, `update()` and `setdefault()`.
  - Nested dictionaries and iteration.
  - **Practice:** Build a student marks register and a word-frequency counter.

- [ ] **Day 10 — Comprehensions and Unpacking**
  - List, set and dictionary comprehensions.
  - Generator expressions (introduction).
  - Iterable unpacking, `enumerate()` and `zip()`.
  - **Practice:** Filter and transform a collection; combine two lists into a dictionary.

- [ ] **Day 11 — Built-in Functions**
  - `len()`, `sum()`, `min()`, `max()`, `sorted()` and `reversed()`.
  - `any()`, `all()`, `map()` and `filter()`.
  - `abs()`, `round()`, `divmod()` and `isinstance()`.
  - **Practice:** Solve small data-processing tasks using built-in functions.

- [ ] **Day 12 — Mutability, References and Copying**
  - Mutable vs immutable objects.
  - Object references and aliasing.
  - Shallow copy vs deep copy using `copy`.
  - Equality (`==`) vs identity (`is`).
  - **Practice:** Demonstrate shallow and deep copying with nested lists.

## Week 3 — Functions, Modules, Errors and Files

- [ ] **Day 13 — Functions**
  - Defining and calling functions.
  - Parameters, arguments, return values and scope.
  - Positional, keyword and default arguments.
  - **Practice:** Build a calculator using reusable functions.

- [ ] **Day 14 — Advanced Function Arguments**
  - `*args` and `**kwargs`.
  - Argument unpacking, lambda expressions and docstrings.
  - Keyword-only and positional-only parameters (introduction).
  - **Practice:** Write a reusable report-summary function.

- [ ] **Day 15 — Modules, Packages and Virtual Environments**
  - Modules, packages and import styles.
  - Create and import your own modules.
  - `if __name__ == "__main__":`.
  - Standard-library vs third-party packages.
  - `pip` and virtual environments using `venv`.
  - **Practice:** Split a calculator into multiple modules and run it in a virtual environment.

- [ ] **Day 16 — Exception Handling**
  - Syntax, runtime and logical errors.
  - `try`, `except`, `else` and `finally`.
  - Catch specific exceptions and raise errors with `raise`.
  - Custom exceptions (introduction).
  - **Practice:** Handle invalid input and missing-file errors safely.

- [ ] **Day 17 — File Handling**
  - Read and write text files.
  - File modes: `r`, `w`, `a`, `x` and binary mode.
  - Use `with` to manage files safely.
  - Encoding and file paths.
  - **Practice:** Create a simple notes or expense file and read its contents.

- [ ] **Day 18 — JSON and CSV**
  - JSON and Python data conversion.
  - `json.load()`, `loads()`, `dump()` and `dumps()`.
  - Read and write CSV files with the `csv` module.
  - Handle malformed or missing data.
  - **Practice:** Save application settings as JSON and export records to CSV.

## Week 4 — Practical Python Standard-Library Modules

- [ ] **Day 19 — `os`, `pathlib` and `shutil`**
  - Work with the operating system and directories.
  - `os.getcwd()`, `os.listdir()`, `os.makedirs()` and environment variables.
  - Use `pathlib.Path` to build, join and inspect paths.
  - Use `shutil` to copy and move files.
  - **Practice:** Build a folder organizer that sorts files by extension. Test it in a temporary directory.

- [ ] **Day 20 — `datetime` and `time`**
  - Dates, times, datetimes and durations.
  - `datetime`, `timedelta`, `strptime()` and `strftime()`.
  - `time.sleep()`, `time.time()` and `time.perf_counter()`.
  - Understand when to use `datetime` versus `time`.
  - **Practice:** Build an age/date calculator and measure a program's execution time.

- [ ] **Day 21 — `random` and `secrets`**
  - `random.randint()`, `choice()`, `shuffle()` and `sample()`.
  - Reproducible results with `random.seed()`.
  - Use `secrets` for security-sensitive tokens; never use `random` for passwords or authentication tokens.
  - **Practice:** Build a number-guessing game and a random quiz selector.

- [ ] **Day 22 — `math` and `statistics`**
  - `ceil()`, `floor()`, `sqrt()`, `factorial()`, `gcd()` and constants such as `pi`.
  - Floating-point precision and rounding.
  - `statistics.mean()`, `median()`, `mode()` and `stdev()`.
  - **Practice:** Build a basic statistics calculator.

- [ ] **Day 23 — `collections`**
  - `Counter` for frequency counting.
  - `defaultdict` for grouping data.
  - `deque` for efficient operations at both ends.
  - Overview of `namedtuple` and `ChainMap`.
  - **Practice:** Build a word-frequency counter, group records and simulate a queue.

- [ ] **Day 24 — `itertools` and `functools`**
  - `itertools`: `count`, `cycle`, `repeat`, `chain`, `product`, `permutations` and `combinations`.
  - `functools`: `reduce`, `partial` and `lru_cache`.
  - Lazy iteration and memory use.
  - **Practice:** Generate combinations and use caching for a repeated calculation.

## Week 5 — Project-Ready Python

- [ ] **Day 25 — `re`, `sys` and Environment Variables**
  - Regular expressions: `search()`, `match()`, `findall()` and `sub()`.
  - `sys.argv`, `sys.exit()` and `sys.path` (overview).
  - Read configuration using `os.environ` and `os.getenv()`.
  - Keep passwords, tokens and secrets out of source code.
  - **Practice:** Validate simple input formats and load configuration from environment variables.

- [ ] **Day 26 — Logging and Command-Line Programs**
  - Why application logging is preferable to relying on `print()`.
  - Logging levels: DEBUG, INFO, WARNING, ERROR and CRITICAL.
  - Log formatting and writing logs to a file.
  - Parse command-line options with `argparse`.
  - **Practice:** Create a command-line task tracker with logging.

- [ ] **Day 27 — Object-Oriented Programming**
  - Classes, objects, attributes and methods.
  - `__init__`, `self`, instance attributes and class attributes.
  - Encapsulation, inheritance and polymorphism.
  - Composition and special methods such as `__str__` and `__repr__`.
  - **Practice:** Model a bank account or library system.

- [ ] **Day 28 — Iterators, Generators, Decorators and Context Managers**
  - Iterable vs iterator; `iter()` and `next()`.
  - Generator functions and `yield`.
  - Decorators and `functools.wraps`.
  - Context managers and the `with` statement.
  - **Practice:** Create a record generator and a simple function-timing decorator.

- [ ] **Day 29 — Type Hints, Dataclasses and Testing**
  - Type annotations for variables and functions.
  - Common types: `list`, `dict`, `tuple`, `set` and union types.
  - `dataclasses.dataclass`.
  - Basic testing with `unittest` or `pytest`.
  - Assertions, edge cases and test organization.
  - **Practice:** Add type hints and tests to an earlier utility.

- [ ] **Day 30 — Mini Project and Final Revision**
  - Build a **File-Based Expense Tracker**.
  - Add, list and delete expense records.
  - Store records in JSON or CSV.
  - Use functions, suitable data structures and separate modules.
  - Use `pathlib`, `datetime`, exception handling, `argparse` and logging.
  - Add tests for core operations.
  - **Final review:** Explain collections, mutability, copying, functions, modules, exceptions, file handling, standard-library modules, OOP, iterators and generators.
  - **Deliverable:** A working command-line project, tests and a project README.

---

## Daily completion standard

Before checking off a day, confirm that you have:

- [ ] Understood the topic and can explain it in your own words.
- [ ] Written and run examples independently.
- [ ] Completed the day's practical task.
- [ ] Recorded important notes, mistakes or questions.
- [ ] Saved relevant code and notes in this repository.

## Recommended Git commit format

```text
learn: cover Python variables and data types
learn: practice Python loops and conditions
feat: add Python file organizer
learn: explore datetime and time modules
feat: build command-line expense tracker
test: add tests for expense tracker
```

## Reference

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)

## Completion goal

By the end of this roadmap, you should be able to write small Python programs independently, use core language features confidently, structure code into modules, work with files and errors, use practical standard-library modules, and build a tested command-line application.

**Next learning track:** Data Structures and Algorithms (DSA) using Python, beginning with complexity analysis, arrays, strings, hashing, searching and sorting.
