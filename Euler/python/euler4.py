ans=0
for i in range(999):
    for j in range(999):
        x=i*j
        k=str(x)
        rk=k[::-1]
        if len(k)==6:
            if k[0:3]==rk[0:3]:
                if x>ans:
                    ans=x
print(ans)