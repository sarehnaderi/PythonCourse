#Triangle or not

print("Enter a, b & c and find out if they could form a triangle or not")

a = float(input("Enter angle a:"))
b = float(input("Enter angle b:"))

c = float(input("Enter angle c:"))
if a<b+c and b<a+c and c<a+b:
    print("TRUE: Entered numbers can form a triangle")
else:
    print("FALSE: Entered numbers cannot form a triangle")


