#Calculater

import math

op = input("Enter Your required operation (+ , - , * , / , cos , sin , tan , cot , ! , sqrt):")

if op == "+":
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))
    result = num1 + num2

if op == "-":
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))
    result = num1 - num2

if op == "*":
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))
    result = num1 * num2

if op == "/":
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))
    if num2 == 0:
        result = "NOT DEFINED"
    else:
        result = num1 / num2

if op == "cos":
    degrees = float(input("Enter your angle in degrees:"))
    radian = degrees * math.pi/180
    result = math.cos(radian)

if op == "sin":
    degrees = float(input("Enter your angle in degrees:"))
    radian = degrees * math.pi/180
    result = math.sin(radian)

if op == "tan":
    degrees = float(input("Enter your angle in degrees:"))
    radian = degrees * math.pi/180
    if math.cos(radian)==0:
        result = "NOT DEFINED"
    else:
        result = math.tan(radian)

if op == "cot":
    degrees = float(input("Enter your angle in degrees:"))
    radian = degrees * math.pi/180
    if math.sin(radian)==0:
        result = "NOT DEFINED"
    else:
        result = math.cot(radian)

if op == "!":
    num = int(input("Enter your number:"))
    result = math.factorial(num)

if op == "sqrt":
    num = float(input("Enter your number:"))
    if num >= 0 :
        result = math.sqrt(num)
    else:
        result = "Error! Enter a non-negative number."

else:
    print("Error! Please enter a defined operation")

print("Your answer:",result)
