print("Enter 1st number")
a=int(input())
print("Enter 2nd number")
b=int(input())
try:
    c=a/b
    print("result is =",c)
except:
    print("Can not devide by 0")
else:
    print("Keep going on")
