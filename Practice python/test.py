"""
Test PY
"""

NUM = input("Give me a number,please: ")
if int(NUM) / 2 == float(NUM) / 2:
    if int(NUM) /4 == float(NUM) / 4:
        print("You chose %r, a multiple of 4.I wonder why." %NUM)
    else:
        print("You chose %r, an even number. I wonder why." %NUM)
else:
    print("You chose %r, an odd number. I wonder why." %NUM)

CHECK = input("Give me another number,please: ")
if int(NUM) / int(CHECK) == float(NUM) / float(CHECK):
    print("The second number you gave me is a divisor of the first.")
else:
    print("The second number you gave me is not a divisor of the first.")
