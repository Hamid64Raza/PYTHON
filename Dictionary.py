#How to create dict object
d1={102:'Hamid',104:'Raza',106:'Zero',108:'Seven',200:'Ten',202:'Hundried'}
r=type(d1)
print(r)
print(d1)
d2=dict(r="rahul",p="Payal")
print(d2)
#How to access dict eliments
print(d1)
print(d1[102],d1[202])
for k in d1:
    print(k,d1[k])
# As dict is mutable, so we can make changes in the dictionary
d1[204]='dilap'
for k in d1:
    print(k,d1[k],end="-")
#How to delete key value pair
del d1[202]
for k in d1:
    print(k,d1[k])
#Methods in dict
r=d1.keys()    
print(r)
s=d1.values()
print(s)
t=d1.items()
print(t)
#Another method
for k,d in d1.items():
    print(k,d)
#Built-in Methods
x=len(d1)
print(x)
y=min(d1)
print(y)
z=max(d1)
print(z)
a=sum(d1)
print(a)
b=sorted(d1)
print(b)
# dict object methods
p=d1.pop(204)
print(p)
q=d1.popitem()
print(q)

