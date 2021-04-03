import sys

num=int(sys.stdin.readline())
name=[]
for _ in range(num):
    x,y=sys.stdin.readline().rstrip().split(" ")
    name.append([int(x),y])

name.sort(key=lambda x: x[0])

for x in range(num):
    print(name[x][0],name[x][1])