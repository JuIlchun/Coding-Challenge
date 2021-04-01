import sys
List=[0 for x in range(10000)]
num=int(sys.stdin.readline())
for i in range(num):
    x=int(sys.stdin.readline())
    List[x-1]+=1
for i in range(10000):
    if List[i]>0:
        for j in range(List[i]):
            print(i+1)