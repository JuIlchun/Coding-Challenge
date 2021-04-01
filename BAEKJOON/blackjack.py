n,m=map(int,input().split())
card=[int(x) for x in input().split()]
ans=0
for i in range(n):
    for j in range(n):
        if (i<j):
            for k in range(n):
                if (k>j):
                    x=card[i]+card[j]+card[k]
                    if (x>=ans and m>=x):
                        ans=x
print(ans)