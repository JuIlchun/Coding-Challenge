cnt=0
num=1
while cnt<20:
    cnt=0
    for i in range(1,21):
        if num%i==0:
            cnt+=1
    num+=1
print(num-1)