# ============================================================
# File: 2330321_GuzmanZunigaMartinJuanPablo_t_strings.py
# Student: Martin Juan Pablo Guzman Zuñiga
# Purpose: Practice basic string handling in Python
# ============================================================


# ------------------------------------------------------------
# Problem 1: Full name formatter
# Description:
# Formats a full name in Title Case and shows the initials.
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - Formatted name
# - Initials
#
# Validation:
# - Must not be empty
# - Must contain at least two words
#
# Test cases:
# 1) Normal: "martin juan pablo guzman zuñiga"
# 2) Edge case: " martin   guzman "
# 3) Error: "   "
# ------------------------------------------------------------
full_name = input("Enter full name: ").strip()

if full_name == "":
    print("Error: invalid input")
else:
    full_name = " ".join(full_name.split())
    parts = full_name.split(" ")

    if len(parts) < 2:
        print("Error: invalid input")
    else:
        formatted_name = full_name.title()
        initials = ""

        for word in parts:
            initials += word[0].upper() + "."

        print("Formatted name:", formatted_name)
        print("Initials:", initials)


# ------------------------------------------------------------
# Problem 2: Simple email validator
# Description:
# Checks if an email has a basic valid structure and shows the domain.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - Valid email: True / False
# - Domain (if valid)
#
# Validation:
# - Must not be empty
# - Must contain one '@'
# - Must not contain spaces
#
# Test cases:
# 1) Normal: "martin.guzman@mail.com"
# 2) Edge case: "juan@g.mx"
# 3) Error: "martin @mail.com"
# ------------------------------------------------------------
email_text = input("\nEnter email: ").strip()

if email_text == "":
    print("Error: invalid input")
elif " " in email_text:
    print("Valid email: False")
elif email_text.count("@") != 1:
    print("Valid email: False")
else:
    at_index = email_text.find("@")
    domain = email_text[at_index + 1:]

    if "." not in domain or domain == "":
        print("Valid email: False")
    else:
        print("Valid email: True")
        print("Domain:", domain)


# ------------------------------------------------------------
# Problem 3: Palindrome checker
# Description:
# Checks if a phrase is a palindrome ignoring spaces and case.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - Is palindrome: true / false
#
# Validation:
# - Must not be empty
# - Must have at least 3 characters after cleaning
#
# Test cases:
# 1) Normal: "ana lava lana"
# 2) Edge case: "a a"
# 3) Error: "   "
# ------------------------------------------------------------
phrase = input("\nEnter phrase: ").strip()

if phrase == "":
    print("Error: invalid input")
else:
    clean_phrase = phrase.lower().replace(" ", "")

    if len(clean_phrase) < 3:
        print("Error: invalid input")
    else:
        if clean_phrase == clean_phrase[::-1]:
            print("Is palindrome: true")
        else:
            print("Is palindrome: false")


# ------------------------------------------------------------
# Problem 4: Sentence word statistics
# Description:
# Shows word count, first, last, shortest and longest word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Word count
# - First word
# - Last word
# - Shortest word
# - Longest word
#
# Validation:
# - Must not be empty
#
# Test cases:
# 1) Normal: "Martin likes programming"
# 2) Edge case: "Guzman"
# 3) Error: "   "
# ------------------------------------------------------------
sentence = input("\nEnter sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    sentence = " ".join(sentence.split())
    words = sentence.split(" ")

    print("Word count:", len(words))
    print("First word:", words[0])
    print("Last word:", words[-1])

    shortest = words[0]
    longest = words[0]

    for w in words:
        if len(w) < len(shortest):
            shortest = w
        if len(w) > len(longest):
            longest = w

    print("Shortest word:", shortest)
    print("Longest word:", longest)


# ------------------------------------------------------------
# Problem 5: Password strength classifier
# Description:
# Classifies a password as weak, medium or strong.
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - Password strength
#
# Validation:
# - Must not be empty
# - Minimum length check
#
# Test cases:
# 1) Normal: "Martin123!"
# 2) Edge case: "Guzman123"
# 3) Error: ""
# ------------------------------------------------------------
password = input("\nEnter password: ").strip()

if password == "":
    print("Error: invalid input")
elif len(password) < 8:
    print("Password strength: weak")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for c in password:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        else:
            has_symbol = True

    if has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    elif (has_upper or has_lower) and has_digit:
        print("Password strength: medium")
    else:
        print("Password strength: weak")


# ------------------------------------------------------------
# Problem 6: Product label formatter
# Description:
# Creates a fixed-width product label of 30 characters.
#
# Inputs:
# - product_name (string)
# - price_value (number)
#
# Outputs:
# - Label with exactly 30 characters
#
# Validation:
# - Product name not empty
# - Price must be positive
#
# Test cases:
# 1) Normal: "Notebook Martin", "45.5"
# 2) Edge case: "Pen Pablo", "1"
# 3) Error: "Book Juan", "-10"
# ------------------------------------------------------------
product_name = input("\nEnter product name: ").strip()
price_value = input("Enter price: ").strip()

if product_name == "":
    print("Error: invalid input")
else:
    try:
        price = float(price_value)

        if price <= 0:
            print("Error: invalid input")
        else:
            label = "Product: " + product_name + " | Price: $" + str(price)

            if len(label) > 30:
                label = label[:30]
            else:
                label = label + " " * (30 - len(label))

            print('Label:', '"' + label + '"')
            print("Length:", len(label))

    except:
        print("Error: invalid input")


# ------------------------------------------------------------
# GitHub repository
# ------------------------------------------------------------
# Repository URL: https://github.com/MartinGUZU/one
