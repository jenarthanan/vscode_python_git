
a=int(input("Please Enter a Number="))
x=[]
for j in range(1,a+1):
    x.append(j)
y=[]
print(x)
for i in x:
    if a%i==0:
        y.append(i)
        print(i)
print("Final Answer")
print("Entered Number is ",a)
print(x)
print(y)
    
