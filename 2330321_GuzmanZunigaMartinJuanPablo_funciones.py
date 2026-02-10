# ============================================================
# File: 2330321_GuzmanZunigaMartinJuanPablo.py
# Student: Martin Juan Pablo Guzman Zuñiga
# ============================================================


# ------------------------------------------------------------
# Problem 1: Rectangle area and perimeter (basic functions)
# Description: Uses two functions to calculate area and perimeter of a rectangle.
# Inputs:
# - width (float)
# - height (float)
# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>
# Validations:
# - width > 0 and height > 0
# Test cases:
# 1) Normal: width=5, height=2
# 2) Edge case: width=0.1, height=0.1
# 3) Error: width=0, height=3
# ------------------------------------------------------------
def calculate_area(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


width_text = input("Enter width (float): ").strip()
height_text = input("Enter height (float): ").strip()

try:
    width = float(width_text)
    height = float(height_text)

    if width <= 0 or height <= 0:
        print("Error: invalid input")
    else:
        area_value = calculate_area(width, height)
        perimeter_value = calculate_perimeter(width, height)

        print("Area:", area_value)
        print("Perimeter:", perimeter_value)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 2: Grade classifier (function with return string)
# Description: Classifies a numeric score (0-100) into a letter grade.
# Inputs:
# - score (float)
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
# Validations:
# - 0 <= score <= 100
# Test cases:
# 1) Normal: score=85
# 2) Edge case: score=90
# 3) Error: score=120
# ------------------------------------------------------------
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


score_text = input("\nEnter score (0-100): ").strip()

try:
    score = float(score_text)

    if score < 0 or score > 100:
        print("Error: invalid input")
    else:
        grade_letter = classify_grade(score)
        print("Score:", score)
        print("Category:", grade_letter)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 3: List statistics function (min, max, average)
# Description: Builds a list from comma-separated text and returns min, max and average in a dictionary.
# Inputs:
# - numbers_text (string like "10,20,30")
# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>
# Validations:
# - numbers_text not empty
# - list not empty
# - all items must convert to float
# Test cases:
# 1) Normal: "10,20,30"
# 2) Edge case: "5"
# 3) Error: "10,a,30"
# ------------------------------------------------------------
def summarize_numbers(numbers_list):
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {"min": min_value, "max": max_value, "average": average_value}


numbers_text = input("\nEnter numbers (comma separated): ").strip()

if numbers_text == "":
    print("Error: invalid input")
else:
    parts = numbers_text.split(",")
    numbers_list = []
    valid = True

    for p in parts:
        p = p.strip()
        if p == "":
            valid = False
            break
        try:
            numbers_list.append(float(p))
        except:
            valid = False
            break

    if (not valid) or len(numbers_list) == 0:
        print("Error: invalid input")
    else:
        summary = summarize_numbers(numbers_list)
        print("Min:", summary["min"])
        print("Max:", summary["max"])
        print("Average:", summary["average"])


# ------------------------------------------------------------
# Problem 4: Apply discount list (pure function)
# Description: Applies a discount rate to a list of prices and returns a new list (does not modify original).
# Inputs:
# - prices_text (string like "100,200,300")
# - discount_rate (float 0..1)
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
# Validations:
# - prices list not empty
# - all prices > 0
# - 0 <= discount_rate <= 1
# Test cases:
# 1) Normal: prices="100,200,300", rate=0.10
# 2) Edge case: prices="50", rate=0
# 3) Error: prices="100,-20", rate=0.10
# ------------------------------------------------------------
def apply_discount(prices_list, discount_rate):
    discounted_list = []
    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted_list.append(discounted_price)
    return discounted_list


prices_text = input("\nEnter prices (comma separated): ").strip()
discount_rate_text = input("Enter discount rate (0..1): ").strip()

try:
    discount_rate = float(discount_rate_text)
except:
    discount_rate = None

if prices_text == "" or discount_rate is None:
    print("Error: invalid input")
elif discount_rate < 0 or discount_rate > 1:
    print("Error: invalid input")
else:
    parts = prices_text.split(",")
    original_list = []
    valid = True

    for p in parts:
        p = p.strip()
        if p == "":
            valid = False
            break
        try:
            price = float(p)
            if price <= 0:
                valid = False
                break
            original_list.append(price)
        except:
            valid = False
            break

    if (not valid) or len(original_list) == 0:
        print("Error: invalid input")
    else:
        discounted_list = apply_discount(original_list, discount_rate)
        print("Original prices:", original_list)
        print("Discounted prices:", discounted_list)


# ------------------------------------------------------------
# Problem 5: Greeting function with default parameters
# Description: Greets a person, optionally using a title. Shows positional and named argument calls.
# Inputs:
# - name (string)
# - title (string, optional)
# Outputs:
# - "Greeting:" <message>
# Validations:
# - name not empty after strip()
# Test cases:
# 1) Normal: name="Martin", title="Eng."
# 2) Edge case: name="Juan", title=""
# 3) Error: name="   "
# ------------------------------------------------------------
def greet(name, title=""):
    name_clean = name.strip()
    title_clean = title.strip()

    if title_clean != "":
        full_name = f"{title_clean} {name_clean}"
    else:
        full_name = name_clean

    return f"Hello, {full_name}!"


name_input = input("\nEnter name: ").strip()
title_input = input("Enter title (optional): ").strip()

if name_input == "":
    print("Error: invalid input")
else:
    greeting_message_1 = greet(name_input, title_input)          # positional
    greeting_message_2 = greet(name=name_input, title=title_input)  # named

    print("Greeting:", greeting_message_1)
    print("Greeting:", greeting_message_2)


# ------------------------------------------------------------
# Problem 6: Factorial function (iterative)
# Description: Calculates n! using an iterative for-loop (chosen to keep it simple and avoid recursion).
# Inputs:
# - n (int)
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
# Validations:
# - n must be int
# - 0 <= n <= 20
# Test cases:
# 1) Normal: n=5
# 2) Edge case: n=0
# 3) Error: n=25
# ------------------------------------------------------------
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


n_text = input("\nEnter n for factorial (0..20): ").strip()

try:
    n = int(n_text)
    if n < 0 or n > 20:
        print("Error: invalid input")
    else:
        factorial_value = factorial(n)
        print("n:", n)
        print("Factorial:", factorial_value)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# GitHub repository
# ------------------------------------------------------------
# Repository URL: https://github.com/MartinGUZU/one
