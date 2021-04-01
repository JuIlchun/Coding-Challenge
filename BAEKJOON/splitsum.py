num=int(input())
ans=0
l=[]
start=num-(9*len(str(num)))
if (start<1):
    start=1
for i in range(start,num):
    x=sum(map(int, str(i)))
    if (num==x+int(i)):
        ans=i
        break
print(ans)