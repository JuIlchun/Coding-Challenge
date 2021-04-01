cnt=1
x=1

def tri(k):
    ans=0
    for i in range(1,k+1):
        ans+=i
    return ans

while 1:
    L=[]
    for i in range(1,x+1):
        if x%i==0:
            L.append(i)
    my_set = set(L) #집합set으로 변환
    L = list(my_set) #list로 변환
    if len(L)>=500:
        #print(x)
        break
    cnt+=1
    x=tri(cnt)