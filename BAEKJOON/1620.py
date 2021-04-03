import sys

num,num2=sys.stdin.readline().rstrip().split()

poke=[]
for _ in range(int(num)):
    poke.append(sys.stdin.readline().rstrip())
quest=[]
for _ in range(int(num2)):
    quest.append(sys.stdin.readline().rstrip())

for i in range(int(num2)):
    if quest[i].isdigit():
        print(poke[int(quest[i])+1])
    if quest[i].isaplha():
        for j in range(int(num)):
            if poke[j]==quset[i]:
                print(j+1)