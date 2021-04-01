x=1000000
y=1000000
cnt=0
cnt1=0
L=[]
def nodd(num):
    num=((3*num)+1)
    return num

def neven(num):
    num=num/2
    return num

while x>1:
    if y!=1:
        if y%2==0:
            y=neven(y)
            cnt1+=1
        else:
            y=nodd(y)
            cnt1+=1
    else:
        if (cnt1>cnt):
            cnt=cnt1
            cnt1=0
            L.clear()
            L.append(x)
        x-=1
        y=x
print(L)