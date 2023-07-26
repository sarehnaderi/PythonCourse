#Calculater

op = input("Enter Your required operation (+ , - , * , / , cos , sin , tan , cot , ! , sqrt):")

if op == "+":
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))
    result = num1 + num2

if op == "-":
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))
    result = num1 - num2

if op == "*":
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))
    result = num1 * num2

if op == "/":
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))
    if num2 == 0:
        result = "NOT DEFINED"
    else:
        result = num1 / num2

import math

if op == "cos":
    num = int(input("Enter your number:"))
    result = math.Cos(num)

if op == "sin":
    num = int(input("Enter your number:"))
    result = math.sin(num)

if op == "tan":
    num = int(input("Enter your number:"))
    if math.cos(num)==0:
        result = "NOT DEFINED"
    else:
        result = math.tan(num)

if op == "cot":
    num = int(input("Enter your number:"))
    if math.sin(num)==0:
        result = "NOT DEFINED"
    else:
        result = math.cot(num)

if op == "!":
    num = int(input("Enter your number:"))
    result = math.factorial(num)

if op == "sqrt":
    num = int(input("Enter your number:"))
    result = math.sqrt(num)

print("Your answer:",result)