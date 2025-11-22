"""
Topic: Integer (floor) division //, Modulus %, and Absolute value abs()
Goal: Understand what each operator/function does with clear examples.
Author: You :)
"""

# -----------------------------
# Basic integer variables
# -----------------------------
num1 = 10
num2 = 5

# -----------------------------
# 1) Integer (Floor) Division //
# -----------------------------
# Meaning: Divides and returns the floor of the quotient (rounded down to nearest integer).
# For positive numbers, it's the same as normal division then dropping decimals.
result1 = num1 // num2  # 10 // 5 = 2
print("Integer Division (10 // 5):", result1)

# Example with non-even division
print("Integer Division (7 // 3):", 7 // 3)   # 7 / 3 = 2.333... -> floor is 2

# Example with negatives (important! floors toward -infinity)
print("Integer Division (-7 // 3):", -7 // 3)  # -2.333... -> floor is -3 (NOT -2)

# If one operand is float, result is float but still floored
print("Floor Division with float (7.0 // 2):", 7.0 // 2)  # 3.0

# -----------------------------
# 2) Modulus (Remainder) %
# -----------------------------
# Meaning: Gives the remainder after division.
result2 = num1 % num2  # 10 % 5 = 0 (since 10 is divisible by 5)
print("Modulus (Remainder) (10 % 5):", result2)

# Common cases
print("Modulus (7 % 3):", 7 % 3)      # remainder = 1
print("Modulus (14 % 4):", 14 % 4)    # remainder = 2

# With negatives (Python's rule keeps this identity true: a == (a // b) * b + (a % b))
print("Modulus with negative (-7 % 3):", -7 % 3)  # 2, because -7 = (-3 * 3) + 2

# -----------------------------
# 3) Absolute Value abs()
# -----------------------------
# Meaning: Returns the non-negative magnitude of a number.
print("Absolute Value of -7:", abs(-7))     # 7
print("Absolute Value of -3.5:", abs(-3.5)) # 3.5

# For complex numbers, abs() returns the magnitude (sqrt(a^2 + b^2))
z = 3 + 4j
print("Absolute Value of complex (3+4j):", abs(z))  # 5.0

# -----------------------------
# Bonus: Practical patterns
# -----------------------------

# Even/Odd check using %
n = 17
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")

# Relationship between // and % always holds (for b != 0):
a, b = 23, 5
q = a // b
r = a % b
print(f"{a} == ({a} // {b}) * {b} + ({a} % {b})  ->  {a} == {q}*{b} + {r}  ->", a == q * b + r)

# Safety: Division/modulus by zero raises an error
# Uncomment the next line to see the exception:
# print(10 // 0)  # ZeroDivisionError