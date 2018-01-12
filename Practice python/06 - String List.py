



a=input("Please enter a String =")
b=''
j=len(a)
print(j)
print("First")
while j>1:
    b+=a[j-1]
    print(b)
    j=j-1
print(b)
b=''
print("Last")
for i in a:
    b+=i
    print(b)
