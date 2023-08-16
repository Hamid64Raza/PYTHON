print("Enter number to check it is prime or not")
n=int(input())
i=2
while (i<=n-1):
    if (n%i==0):
        break
    i=i+1
if (i==n):
    print("Prime")
else:
    print("Not Prime")
    
