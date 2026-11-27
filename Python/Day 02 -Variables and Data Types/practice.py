# ============================================================
# PYTHON PRACTICE PROGRAMS
# Exercises 1 to 6
# ============================================================


# ------------------------------------------------------------
# Exercise 1: Basic variable operations
# Create variables for name, age, city, and programming language.
# Print them with appropriate labels.
# Concepts: Variables, strings, integers
# ------------------------------------------------------------

def exercise_1():
    print("=== Exercise 1: Basic Variable Operations ===")

    name = "Rahul"
    age = 20
    city = "Mumbai"
    programming_language = "Python"

    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Programming Language:", programming_language)
    print()


# ------------------------------------------------------------
# Exercise 2: Type identification
# Create five variables with different data types.
# Use type() to display their data types.
# Concepts: Data types, type()
# ------------------------------------------------------------

def exercise_2():
    print("=== Exercise 2: Type Identification ===")

    number = 25                  # int
    price = 99.99                # float
    student_name = "Aarav"       # str
    is_present = True            # bool
    subjects = ["Math", "Python"]  # list

    print("Value:", number, "| Type:", type(number))
    print("Value:", price, "| Type:", type(price))
    print("Value:", student_name, "| Type:", type(student_name))
    print("Value:", is_present, "| Type:", type(is_present))
    print("Value:", subjects, "| Type:", type(subjects))
    print()


# ------------------------------------------------------------
# Exercise 3: Type conversion
# Take two numbers as input. Convert them into integers and
# calculate sum, difference, product, and division.
# Concepts: input(), int(), arithmetic operators
# ------------------------------------------------------------

def exercise_3():
    print("=== Exercise 3: Type Conversion ===")

    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    addition = number1 + number2
    difference = number1 - number2
    product = number1 * number2

    print("Sum:", addition)
    print("Difference:", difference)
    print("Product:", product)

    if number2 != 0:
        division = number1 / number2
        print("Division:", division)
    else:
        print("Division is not possible because second number is 0.")
    print()


# ------------------------------------------------------------
# Exercise 4: Temperature converter
# Accept temperature in Celsius and convert it to Fahrenheit.
# Formula: F = (C * 9 / 5) + 32
# Concepts: float(), arithmetic operations
# ------------------------------------------------------------

def exercise_4():
    print("=== Exercise 4: Temperature Converter ===")

    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32

    print("Temperature in Fahrenheit:", fahrenheit)
    print()


# ------------------------------------------------------------
# Exercise 5: Simple shopping bill
# Accept product name, quantity, and price per item.
# Calculate and display the total bill.
# Concepts: Variables, strings, integers, floats
# ------------------------------------------------------------

def exercise_5():
    print("=== Exercise 5: Simple Shopping Bill ===")

    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price_per_item = float(input("Enter price per item: "))

    total_bill = quantity * price_per_item

    print("Product Name:", product_name)
    print("Quantity:", quantity)
    print("Price per Item:", price_per_item)
    print("Total Bill:", total_bill)
    print()


# ------------------------------------------------------------
# Exercise 6: Boolean practice
# Create variables representing whether a student is present,
# whether fees are paid, and whether the student is eligible
# for an examination. Print their values and types.
# Concepts: bool, Boolean values
# ------------------------------------------------------------

def exercise_6():
    print("=== Exercise 6: Boolean Practice ===")

    is_present = True
    fees_paid = False
    is_eligible_for_exam = True

    print("Student Present:", is_present, "| Type:", type(is_present))
    print("Fees Paid:", fees_paid, "| Type:", type(fees_paid))
    print("Eligible for Examination:", is_eligible_for_exam, "| Type:", type(is_eligible_for_exam))
    print()


# ------------------------------------------------------------
# Run all exercises
# ------------------------------------------------------------

if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()