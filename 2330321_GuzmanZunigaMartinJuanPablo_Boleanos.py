# ============================================================
# File: 2330321_GuzmanZunigaMartinJuanPablo.py
# Student: Martin Juan Pablo Guzman Zuñiga
# ============================================================


# ------------------------------------------------------------
# Problem 1: Temperature converter and range flag
# Description: Converts Celsius to Fahrenheit and Kelvin, and checks if it is high temperature (>= 30.0 C).
# Inputs: temp_c (float)
# Outputs: Fahrenheit, Kelvin, High temperature (True/False)
# Validations: temp_c must be a float and temp_c >= -273.15
# Test cases:
# 1) Normal: 35.0
# 2) Edge case: -273.15
# 3) Error: -300
# ------------------------------------------------------------
temp_c_text = input("Enter temperature in Celsius: ").strip()

try:
    temp_c = float(temp_c_text)
    if temp_c < -273.15:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = (temp_c >= 30.0)

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", is_high_temperature)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 2: Work hours and overtime payment
# Description: Calculates weekly pay with overtime (>40 hours paid at 150% rate) and a has_overtime flag.
# Inputs: hours_worked (int), hourly_rate (float)
# Outputs: Regular pay, Overtime pay, Total pay, Has overtime
# Validations: hours_worked >= 0, hourly_rate > 0
# Test cases:
# 1) Normal: hours=45, rate=100.0
# 2) Edge case: hours=40, rate=50.0
# 3) Error: hours=-5, rate=80.0
# ------------------------------------------------------------
hours_worked_text = input("\nEnter hours worked (int): ").strip()
hourly_rate_text = input("Enter hourly rate (float): ").strip()

try:
    hours_worked = int(hours_worked_text)
    hourly_rate = float(hourly_rate_text)

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        has_overtime = (hours_worked > 40)

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", has_overtime)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 3: Discount eligibility with booleans
# Description: Checks discount eligibility (student OR senior OR purchase_total >= 1000) and applies 10% discount.
# Inputs: purchase_total (float), is_student_text ("YES"/"NO"), is_senior_text ("YES"/"NO")
# Outputs: Discount eligible, Final total
# Validations: purchase_total >= 0, texts must be YES or NO
# Test cases:
# 1) Normal: total=1200, student=NO, senior=NO
# 2) Edge case: total=1000, student=NO, senior=NO
# 3) Error: total=500, student=MAYBE, senior=NO
# ------------------------------------------------------------
purchase_total_text = input("\nEnter purchase total (float): ").strip()
is_student_text = input("Is student? (YES/NO): ").strip().upper()
is_senior_text = input("Is senior? (YES/NO): ").strip().upper()

try:
    purchase_total = float(purchase_total_text)

    if purchase_total < 0:
        print("Error: invalid input")
    elif (is_student_text != "YES" and is_student_text != "NO") or (is_senior_text != "YES" and is_senior_text != "NO"):
        print("Error: invalid input")
    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", discount_eligible)
        print("Final total:", final_total)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 4: Basic statistics of three integers
# Description: Reads three integers and prints sum, average, max, min, and all_even flag.
# Inputs: n1 (int), n2 (int), n3 (int)
# Outputs: Sum, Average, Max, Min, All even
# Validations: all values must convert to int
# Test cases:
# 1) Normal: 2, 5, 8
# 2) Edge case: -1, 0, 1
# 3) Error: "a", 2, 3
# ------------------------------------------------------------
n1_text = input("\nEnter integer n1: ").strip()
n2_text = input("Enter integer n2: ").strip()
n3_text = input("Enter integer n3: ").strip()

try:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 5: Loan eligibility (income and debt ratio)
# Description: Computes debt ratio and checks eligibility using income, debt ratio, and credit score.
# Inputs: monthly_income (float), monthly_debt (float), credit_score (int)
# Outputs: Debt ratio, Eligible
# Validations: monthly_income > 0, monthly_debt >= 0, credit_score >= 0
# Test cases:
# 1) Normal: income=12000, debt=3000, score=700
# 2) Edge case: income=8000, debt=3200, score=650
# 3) Error: income=0, debt=100, score=700
# ------------------------------------------------------------
monthly_income_text = input("\nEnter monthly income (float): ").strip()
monthly_debt_text = input("Enter monthly debt (float): ").strip()
credit_score_text = input("Enter credit score (int): ").strip()

try:
    monthly_income = float(monthly_income_text)
    monthly_debt = float(monthly_debt_text)
    credit_score = int(credit_score_text)

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

        print("Debt ratio:", debt_ratio)
        print("Eligible:", eligible)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# Problem 6: Body Mass Index (BMI) and category flag
# Description: Calculates BMI and prints underweight/normal/overweight boolean flags.
# Inputs: weight_kg (float), height_m (float)
# Outputs: BMI (rounded), Underweight, Normal, Overweight
# Validations: weight_kg > 0, height_m > 0
# Test cases:
# 1) Normal: weight=70, height=1.75
# 2) Edge case: weight=18.5, height=1.0
# 3) Error: weight=70, height=0
# ------------------------------------------------------------
weight_kg_text = input("\nEnter weight in kg (float): ").strip()
height_m_text = input("Enter height in meters (float): ").strip()

try:
    weight_kg = float(weight_kg_text)
    height_m = float(height_m_text)

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)

        is_underweight = (bmi < 18.5)
        is_normal = (bmi >= 18.5 and bmi < 25.0)
        is_overweight = (bmi >= 25.0)

        print("BMI:", bmi_rounded)
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)
except:
    print("Error: invalid input")


# ------------------------------------------------------------
# GitHub repository
# ------------------------------------------------------------
# Repository URL: https://github.com/MartinGUZU/one
