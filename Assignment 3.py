#Dice

import random

print("Welcome to the Dice game!")
print("Notice:You'll win 2 more rounds if you get 6!")     

start = int(input("Enter number 1 to start the game:"))

if start == 1:
    x = random.choice([1,2,3,4,5,6])
    print("Result: ",x)
    if x == 6:
        print("Congratulation! You got 6! Here are your award's results:" )
        for i in range(2):
            x = random.choice([1,2,3,4,5,6])
            print(x)

if start != 1 :
    print("Invalid choice. Please Enter number 1.")
