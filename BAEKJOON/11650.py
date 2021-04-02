import sys

num=int(sys.stdin.readline())
loc=[]
for _ in range(num):
    x,y=sys.stdin.readline().split(" ")
    loc.append([int(x),int(y)])

loc.sort(key = lambda x : (x[0], x[1]))

for x in range(num):
    print(loc[x][0],loc[x][1])