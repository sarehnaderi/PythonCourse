#Average & Status

print("Please enter required data and recieve your final status")

fname = input("First name:")
lname = input("Last name:")

lesson1 = float(input("Math's final grade:"))
lesson2 = float(input("Physics' final grade:"))
lesson3 = float(input("Chemistry's final grade:"))

avg = float((lesson1+lesson2+lesson3)/3)

if avg>=17:
    sts = "Great"

if 12<=avg<17:
    sts = "Normal"

if avg<12:
    sts = "Failed"

print("")
print("Name:",fname,lname)
print("Total average:",avg)
print("Status:",sts)