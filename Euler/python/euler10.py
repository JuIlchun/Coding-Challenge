ans=0
L=[2]
for i in range(2,2000001):
    for j in L:
        if i%j==0:
            break
        else:
            L.append(i)
            ans+=i
print(ans)