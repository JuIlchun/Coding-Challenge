x=1
y=2
L=[1,2]
while y<=4000000:
    k=y
    y=x+y
    L.append(y)
    x=k

ans=0
for i in L:
    if i%2==0:
        ans+=i
print(ans)