# ==========================================
# BASIC LEVEL (VARIABLES)
# ==========================================

# Task 1. Input and Output
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")

# Task 2. Simple Calculations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")

# Task 3. Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C is {fahrenheit}°F")

# Task 4. Swap Variables
a = 5
b = 10
a, b = b, a
print(f"Swapped: a = {a}, b = {b}")

# ==========================================
# INTERMEDIATE LEVEL (CONDITIONS)
# ==========================================

# Task 5. Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Task 6. Age Category
user_age = int(input("Enter age: "))
if 0 <= user_age <= 12:
    print("Child")
elif 13 <= user_age <= 17:
    print("Teenager")
elif user_age >= 18:
    print("Adult")

# Task 7. Maximum of Three Numbers
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
print(f"Largest: {max(n1, n2, n3)}")

# Task 8. Calculator
val1 = float(input("First number: "))
val2 = float(input("Second number: "))
op = input("Operation (+, -, *, /): ")
if op == "+":
    print(val1 + val2)
elif op == "-":
    print(val1 - val2)
elif op == "*":
    print(val1 * val2)
elif op == "/" and val2 != 0:
    print(val1 / val2)
else:
    print("Invalid operation or division by zero")

# ==========================================
# ADVANCED LEVEL (CONDITIONS + LOGIC)
# ==========================================

# Task 9. Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Task 10. Grade System
score = int(input("Enter score (0-100): "))
if 90 <= score <= 100:
    print("A")
elif 75 <= score <= 89:
    print("B")
elif 50 <= score <= 74:
    print("C")
else:
    print("F")

# Task 11. Bank Withdrawal
balance = 1000
amount = float(input("Withdrawal amount: "))
if amount <= balance:
    balance -= amount
    print(f"Success. Remaining: {balance}")
else:
    print("Error: Insufficient funds")

# Task 12. Login System
stored_login = "admin"
stored_pass = "1234"
u_login = input("Login: ")
u_pass = input("Password: ")
if u_login == stored_login and u_pass == stored_pass:
    print("Access granted")
else:
    print("Access denied")

# ==========================================
# CHALLENGE LEVEL
# ==========================================

# Task 13. Discount System
purchase = float(input("Enter purchase amount: "))
if purchase >= 10000:
    purchase *= 0.90
elif purchase >= 5000:
    purchase *= 0.95
print(f"Final amount: {purchase}")

# Task 14. Triangle Checker
s1 = float(input("Side 1: "))
s2 = float(input("Side 2: "))
s3 = float(input("Side 3: "))
if s1+s2 > s3 and s1+s3 > s2 and s2+s3 > s1:
    if s1 == s2 == s3:
        print("Equilateral Triangle")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Triangle does not exist")

# Task 15. Traffic Light
color = input("Enter color: ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")

# ==========================================
# EXPERT LEVEL (MOODLE ASSESSMENT)
# ==========================================

# Task 16. Number Range Analyzer
num_analyze = int(input("Enter number: "))
# Pos/Neg/Zero
if num_analyze > 0: pos = "Positive"
elif num_analyze < 0: pos = "Negative"
else: pos = "Zero"
# Even/Odd
parity = "Even" if num_analyze % 2 == 0 else "Odd"
# Range
in_range = "Inside 1-100" if 1 <= num_analyze <= 100 else "Outside range"
print(f"{pos}, {parity}, {in_range}")

# Task 17. Advanced Calculator
try:
    calc1 = float(input("Num 1: "))
    calc2 = float(input("Num 2: "))
    calc_op = input("Op (**, %, +, -, *, /): ")
    if calc_op == "**": print(calc1 ** calc2)
    elif calc_op == "%": print(calc1 % calc2)
    elif calc_op == "/": print(calc1 / calc2)
    # ... other standard ops ...
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except:
    print("Invalid operation")

# Task 18. Password Strength Checker
pw = input("Enter password: ")
has_digit = any(char.isdigit() for char in pw)
has_upper = any(char.isupper() for char in pw)
if len(pw) >= 8 and has_digit and has_upper:
    print("Strong")
elif len(pw) >= 8:
    print("Medium")
else:
    print("Weak")

# Task 19. ATM Simulation
atm_balance = 5000
choice = input("1. Balance, 2. Deposit, 3. Withdraw: ")
if choice == "1":
    print(f"Balance: {atm_balance}")
elif choice == "2":
    dep = float(input("Amount: "))
    atm_balance += dep
    print(f"New balance: {atm_balance}")
elif choice == "3":
    wit = float(input("Amount: "))
    if wit <= atm_balance:
        atm_balance -= wit
        print(f"New balance: {atm_balance}")
    else:
        print("Insufficient funds")

# Task 20. Number Guessing (No loops)
secret = 7
guess = int(input("Guess the number: "))
if guess > secret: print("Too high")
elif guess < secret: print("Too low")
else: print("Correct")

# Task 21. Multi-Condition Grading
ex_score = int(input("Exam score: "))
att = int(input("Attendance %: "))
if ex_score < 50 or att < 60:
    print("Fail")
else:
    if ex_score >= 90: print("Grade: A")
    elif ex_score >= 75: print("Grade: B")
    else: print("Grade: C")

# Task 22. Delivery Cost Calculator
order_amt = float(input("Order amount: "))
dist = float(input("Distance (km): "))
delivery = 1000
if order_amt > 15000:
    delivery = 0
elif dist > 5:
    delivery += (dist - 5) * 200 # Assuming 200 per km for excess distance
print(f"Total delivery cost: {delivery}")

# Task 23. Simple Loan Approval
salary = float(input("Salary: "))
history = input("Credit history (good/bad): ").lower()
if salary > 200000 and history == "good":
    print("Approved")
else:
    print("Rejected")

# Task 24. Login Attempts (No loops)
u1 = input("Attempt 1 Login: ")
p1 = input("Attempt 1 Pass: ")
if u1 == "admin" and p1 == "1234":
    print("Welcome")
else:
    u2 = input("Attempt 2 Login: ")
    p2 = input("Attempt 2 Pass: ")
    if u2 == "admin" and p2 == "1234":
        print("Welcome")
    else:
        print("Access Blocked")

# Task 25. Menu-Based Program
print("Menu: Add, Subtract, Multiply, Exit")
m_choice = input("Choice: ").lower()
if m_choice != "exit":
    ma = float(input("A: "))
    mb = float(input("B: "))
    if m_choice == "add": print(ma + mb)
    elif m_choice == "subtract": print(ma - mb)
    elif m_choice == "multiply": print(ma * mb)