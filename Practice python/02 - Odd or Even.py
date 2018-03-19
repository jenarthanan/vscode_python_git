"""
Changed Something
"""

a = int(input("Please enter a Number"))
'''
if a%2==0 and a%4!=0 :
    print("Given Number is a Even Number")
elif a%4==0 :
    print("Given Number is a multiple of 4.")
elif  a%2!=0 :
    print("Given Number is a odd number")
'Extra
b=int(input("enter a number="))
c=int(input("Enter another Number="))

if b%c==0 :
    print("b can be divided by c.")
else:
    print("b cannot be divided by c.")
'Alternate Method:
'''
dev = (a / 2 * 2)
if a == dev:
    print("{} is an odd number." .format(a))
    print("it's even")
    print(dev)
else:

    print("it's not even")
