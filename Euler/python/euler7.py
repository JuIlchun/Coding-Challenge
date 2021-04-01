cnt=0
num=2
while (cnt<10001):
    cnt1=0
    for i in range(1,num):
        if num%i==0:
            cnt1+=1
    if (cnt1==1):
        cnt+=1
    num+=1
print(cnt,num-1)