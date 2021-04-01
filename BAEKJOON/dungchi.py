#ERROR
man=int(input())
size=[input().split() for x in range(0,man)]
rank=[1 for x in range(man)]

for i in range(man):
    for j in range(man):
        if (rank[i]==rank[j]):
            if size[i][0]>size[j][0]:
                if size[i][1]>size[j][1]:
                    rank[j]=rank[i]+1
                elif size[i][1]<size[j][1]:
                    rank[i]=rank[j]
            elif size[i][0]<size[j][0]:
                if size[i][1]>size[j][1]:
                    rank[j]=rank[i]
                elif size[i][1]<size[j][1]:
                    rank[i]=rank[j]+1

level=1
ol=0
for i in range(man):
    for j in range(man):
        if rank[j]==level:
            ol+=1
    if ol>1:
        for j in range(man):
            if rank[j]==(level+1):
                rank[j]=(rank[j]-1)+ol
    level+=1
    ol=0

for i in range(0,man):
    print(rank[i],end=' ')