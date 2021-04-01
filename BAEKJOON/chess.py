#ERROR
y, x=input().split()
x=int(x)
y=int(y)
location=[input() for i in range(y)]

def loc(first, i,j):
    if first==0:
        if i%2==0:
            if j%2==0:
                if location[i][j]!="B":
                    return 1
            elif j%2!=0:
                if location[i][j]!="W":
                    return 1
        elif i%2!=0:
            if j%2==0:
                if location[i][j]!="W":
                    return 1
            elif j%2!=0:
                if location[i][j]!="B":
                    return 1
    elif first==1:
        if i%2==0:
            if j%2==0:
                if location[i][j]!="W":
                    return 1
            elif j%2!=0:
                if location[i][j]!="B":
                    return 1
        elif i%2!=0:
            if j%2==0:
                if location[i][j]!="B":
                    return 1
            elif j%2!=0:
                if location[i][j]!="W":
                    return 1

wrong=0
first=0 #0=black 1=white
ans=100
#1
first=1 if location[0][0]=="W" else 0
for i in range(8):
    for j in range(8):
        if loc(first,i,j)==1: wrong+=1
print(wrong)
if wrong<ans: ans=wrong
wrong=0
#2
first=1 if location[0][x-1]=="W" else 0
for i in range(8):
    for j in range(7,-1,-1):
        if loc(first,i,j)==1: wrong+=1
print(wrong)
if wrong<ans: ans=wrong
wrong=0
#3
first=1 if location[y-1][0]=="W" else 0
for i in range(7,-1,-1):
    for j in range(8):
        if loc(first,i,j)==1: wrong+=1
print(wrong)
if wrong<ans: ans=wrong
wrong=0
#4
first=1 if location[y-1][x-1]=="W" else 0
for i in range(7,-1,-1):
    for j in range(7,-1,-1):
        if loc(first,i,j)==1: wrong+=1
print(wrong)
if wrong<ans: ans=wrong
wrong=0

print (ans)