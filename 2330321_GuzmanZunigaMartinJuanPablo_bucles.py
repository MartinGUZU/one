# ============================================================
# File: 2330321_GuzmanZunigaMartinJuanPablo.py
# Student: Martin Juan Pablo Guzman Zuñiga
# ============================================================


# ------------------------------------------------------------
# Problem 1: Sum of integers in a range
# Description: Sums integers from 1 to n and also sums only the even numbers in that range using a for loop.
# Inputs:
# - n (int)
# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>
# Validations:
# - n must be int and n >= 1
# Test cases:
# 1) Normal: n = 10
# 2) Edge case: n = 1
# 3) Error: n = 0
# ------------------------------------------------------------
n_text = input("Enter n (int >= 1): ").strip()

try:
    n = int(n_text)
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum = total_sum + i
            if i % 2 == 0:
                even_sum = even_sum + i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 2: Multiplication table with for
# Description: Prints the multiplication table for a base number from 1 to m using a for loop.
# Inputs:
# - base (int)
# - m (int)
# Outputs:
# - "<base> x <i> = <product>"
# Validations:
# - base and m must be int
# - m >= 1
# Test cases:
# 1) Normal: base = 5, m = 4
# 2) Edge case: base = 0, m = 3
# 3) Error: m = 0
# ------------------------------------------------------------
base_text = input("\nEnter base (int): ").strip()
m_text = input("Enter m (int >= 1): ").strip()

try:
    base = int(base_text)
    m = int(m_text)

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            product = base * i
            print(f"{base} x {i} = {product}")
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
# Description: Reads non-negative numbers until sentinel (-1). Calculates count and average. Rejects negatives (not sentinel).
# Inputs:
# - number (float, repeated)
# Outputs:
# - "Count:" <count>
# - "Average:" <average_value>
# - or "Error: no data"
# Validations:
# - Input must convert to float, otherwise show "Error: invalid input" and ask again
# - Accept only number >= 0, ignore other negatives (except sentinel)
# Test cases:
# 1) Normal: 10, 20, 30, -1
# 2) Edge case: -1 (no data)
# 3) Error: "abc", 10, -1
# ------------------------------------------------------------
SENTINEL_VALUE = -1.0
count = 0
total = 0.0

print("\nEnter numbers (>= 0). Type -1 to finish.")

while True:
    number_text = input("Number: ").strip()

    try:
        number = float(number_text)
    except:
        print("Error: invalid input")
        continue

    if number == SENTINEL_VALUE:
        break

    if number < 0:
        print("Error: invalid input")
        continue

    total = total + number
    count = count + 1

if count == 0:
    print("Error: no data")
else:
    average_value = total / count
    print("Count:", count)
    print("Average:", average_value)


# ------------------------------------------------------------
# Problem 4: Password attempts with while
# Description: User has MAX_ATTEMPTS tries to enter the correct password. Shows success or account locked.
# Inputs:
# - user_password (string)
# Outputs:
# - "Login success" OR "Account locked"
# Validations:
# - MAX_ATTEMPTS > 0
# Test cases:
# 1) Normal: wrong, admin123 (success on second try)
# 2) Edge case: admin123 on first try
# 3) Error: wrong, wrong, wrong (locked)
# ------------------------------------------------------------
MAX_ATTEMPTS = 3
correct_password = "admin123"

attempts = 0
logged_in = False

if MAX_ATTEMPTS <= 0:
    print("Error: invalid input")
else:
    while attempts < MAX_ATTEMPTS:
        user_password = input("\nEnter password: ")
        if user_password == correct_password:
            logged_in = True
            break
        attempts = attempts + 1

    if logged_in:
        print("Login success")
    else:
        print("Account locked")


# ------------------------------------------------------------
# Problem 5: Simple menu with while
# Description: Repeats a menu until user selects 0. Has a counter that can be shown and incremented.
# Inputs:
# - option (int)
# Outputs:
# - Greeting, Counter value, Increment message, Bye, or invalid option error
# Validations:
# - option must convert to int, only 0-3 are valid
# Test cases:
# 1) Normal: 1, 3, 2, 0
# 2) Edge case: 2, 0
# 3) Error: "x", 9, 0
# ------------------------------------------------------------
counter_value = 0
option = -1

while option != 0:
    print("\n1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_text = input("Select option: ").strip()

    try:
        option = int(option_text)
    except:
        print("Error: invalid option")
        continue

    if option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter_value)
    elif option == 3:
        counter_value = counter_value + 1
        print("Counter incremented")
    elif option == 0:
        print("Bye!")
    else:
        print("Error: invalid option")


# ------------------------------------------------------------
# Problem 6: Pattern printing with nested loops
# Description: Prints a right triangle pattern of '*' using nested for loops (also prints an inverted pattern).
# Inputs:
# - n (int)
# Outputs:
# - Triangle pattern lines and inverted triangle lines
# Validations:
# - n must convert to int and n >= 1
# Test cases:
# 1) Normal: n = 4
# 2) Edge case: n = 1
# 3) Error: n = 0
# ------------------------------------------------------------
n_text = input("\nEnter n for pattern (int >= 1): ").strip()

try:
    n = int(n_text)
    if n < 1:
        print("Error: invalid input")
    else:
        # Normal triangle
        for i in range(1, n + 1):
            line = ""
            for j in range(i):
                line = line + "*"
            print(line)

        # Inverted triangle
        for i in range(n, 0, -1):
            line = ""
            for j in range(i):
                line = line + "*"
            print(line)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# GitHub repository
# ------------------------------------------------------------
# Repository URL: https://github.com/MartinGUZU/one
