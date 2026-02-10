# ============================================================
# File: 2330321_GuzmanZunigaMartinJuanPablo.py
# Student: Martin Juan Pablo Guzman Zuñiga
# ============================================================


# ------------------------------------------------------------
# Problem 1: Shopping list basics (list operations)
# Description: Creates a shopping list from text, adds a new item, counts items, and searches an item.
# Inputs: initial_items_text, new_item, search_item
# Outputs: Items list, Total items, Found item
# Validations: inputs not empty
# Test cases:
# 1) Normal: "martin:2,juan:5,pablo:1"
# 2) Edge case: "guzman:1"
# 3) Error: ""
# ------------------------------------------------------------
initial_items_text = input("Enter initial items (example apple:2,banana:5): ").strip()

if initial_items_text == "":
    print("Error: invalid input")
else:
    items_list = []

    parts = initial_items_text.split(",")

    for p in parts:
        p = p.strip().lower()
        if p != "":
            items_list.append(p)

    new_item = input("Enter new item to add: ").strip().lower()
    if new_item == "":
        print("Error: invalid input")
    else:
        items_list.append(new_item)

        search_item = input("Enter item to search: ").strip().lower()
        if search_item == "":
            print("Error: invalid input")
        else:
            is_in_list = (search_item in items_list)

            print("Items list:", items_list)
            print("Total items:", len(items_list))
            print("Found item:", is_in_list)


# ------------------------------------------------------------
# Problem 2: Points and distances with tuples
# Description: Creates two 2D points as tuples, calculates distance and midpoint.
# Inputs: x1, y1, x2, y2
# Outputs: Point A, Point B, Distance, Midpoint
# Validations: values must convert to float
# Test cases:
# 1) Normal: (0,0) and (3,4)
# 2) Edge case: (1,1) and (1,1)
# 3) Error: x1="abc"
# ------------------------------------------------------------
x1_text = input("\nEnter x1: ").strip()
y1_text = input("Enter y1: ").strip()
x2_text = input("Enter x2: ").strip()
y2_text = input("Enter y2: ").strip()

try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 3: Product catalog with dictionary
# Description: Uses a dictionary of products and calculates total price if product exists.
# Inputs: product_name, quantity
# Outputs: Unit price, Quantity, Total OR Error
# Validations: product_name not empty, quantity > 0
# Test cases:
# 1) Normal: "notebook", 2
# 2) Edge case: "pen", 1
# 3) Error: "phone", 3
# ------------------------------------------------------------
product_prices = {
    "notebook": 25.0,
    "pen": 5.0,
    "eraser": 3.0
}

product_name = input("\nEnter product name: ").strip().lower()
quantity_text = input("Enter quantity (int): ").strip()

try:
    quantity = int(quantity_text)

    if product_name == "" or quantity <= 0:
        print("Error: invalid input")
    else:
        if product_name in product_prices:
            unit_price = product_prices[product_name]
            total_price = unit_price * quantity

            print("Unit price:", unit_price)
            print("Quantity:", quantity)
            print("Total:", total_price)
        else:
            print("Error: product not found")
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 4: Student grades with dict and list
# Description: Stores student grades in a dictionary and calculates average and pass status.
# Inputs: student_name
# Outputs: Grades, Average, Passed OR Error
# Validations: student_name not empty, student must exist, grades list not empty
# Test cases:
# 1) Normal: "martin"
# 2) Edge case: "juan"
# 3) Error: "pablo"
# ------------------------------------------------------------
student_grades = {
    "martin": [90.0, 85.0, 88.0],
    "juan": [70.0, 60.0, 75.0],
    "guzman": [100.0, 95.0, 98.0]
}

student_name = input("\nEnter student name: ").strip().lower()

if student_name == "":
    print("Error: invalid input")
else:
    if student_name in student_grades:
        grades_list = student_grades[student_name]

        if len(grades_list) == 0:
            print("Error: invalid input")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = (average >= 70.0)

            print("Grades:", grades_list)
            print("Average:", average)
            print("Passed:", is_passed)
    else:
        print("Error: student not found")


# ------------------------------------------------------------
# Problem 5: Word frequency counter (list + dict)
# Description: Counts word frequency in a sentence using list and dictionary.
# Inputs: sentence
# Outputs: Words list, Frequencies, Most common word
# Validations: sentence not empty, words list not empty
# Test cases:
# 1) Normal: "martin martin juan"
# 2) Edge case: "pablo."
# 3) Error: "   "
# ------------------------------------------------------------
sentence = input("\nEnter a sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    sentence = sentence.lower()
    sentence = sentence.replace(".", "")
    sentence = sentence.replace(",", "")
    sentence = sentence.replace("!", "")
    sentence = sentence.replace("?", "")
    sentence = sentence.replace(";", "")
    sentence = sentence.replace(":", "")

    words_list = sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        most_common_word = words_list[0]
        max_count = freq_dict[most_common_word]

        for word in freq_dict:
            if freq_dict[word] > max_count:
                max_count = freq_dict[word]
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


# ------------------------------------------------------------
# Problem 6: Simple address book (dictionary CRUD)
# Description: Simple address book with ADD, SEARCH, DELETE actions using a dictionary.
# Inputs: action_text, name, phone (if ADD)
# Outputs: Saved, Phone, Deleted, or Error
# Validations: action must be valid, name not empty, phone not empty for ADD
# Test cases:
# 1) Normal: ADD martin 12345
# 2) Edge case: SEARCH juan
# 3) Error: DELETE pablo (not found)
# ------------------------------------------------------------
contacts = {
    "martin": "5551112222",
    "juan": "5553334444",
    "pablo": "5557778888"
}

action_text = input("\nEnter action (ADD/SEARCH/DELETE): ").strip().upper()

if action_text != "ADD" and action_text != "SEARCH" and action_text != "DELETE":
    print("Error: invalid input")
else:
    name = input("Enter contact name: ").strip().lower()

    if name == "":
        print("Error: invalid input")
    else:
        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()

            if phone == "":
                print("Error: invalid input")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")


# ------------------------------------------------------------
# GitHub repository
# ------------------------------------------------------------
# Repository URL: https://github.com/MartinGUZU/one
