l1=[1,2,3,4,5]
print(type(l1))
l2=[1,2.3,True,3+4j,'MySirg']
print(type(l2))
l3=[]
print(type(l3))


print(l1[0],l1[4])
print(l2[1],l2[4])
#Negative indexing
print(l2[-1],l2[-5])
for x in l2:
    print(x,end=' ')
i=0
while i<5:
    print(l2[i],end='   ')
    i=i+1
l1.append(6)
print(l1)
l2.insert(1,'Hamid')
print(l2)
