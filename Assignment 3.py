#Dice

import random

print("Welcome to the Dice game!")
print("Notice:You'll win 2 more rounds if you get 6!")     

start = int(input("Enter number 1 to start the game:"))

if start == 1:
    x = random.choice([1,2,3,4,5,6])
    print("Result: ",x)
if x == 6:
    award_1 = random.choice([1,2,3,4,5,6])
    print("Congratulation! You got 6! Here is your award roll:",award_1 )
    if award_1 == 6:
        award_2 = random.choice([1,2,3,4,5,6])
        print("Wow you got 6 again! Here is your second award roll:",award_2)
if start != 1 :
    print("Invalid choice. Please Enter number 1.")
