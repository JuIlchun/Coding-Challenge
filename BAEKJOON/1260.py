import sys

def DFS(n,m,v,List=[]):
    count=0
    for x in range(m):
        if (List[x][0] not in D_List) and (List[x][1] not in D_List):
            if v==List[x][0]:
                D_List.append(v)
                DFS(n,m,List[x][1],List)
        if x==m-1: count=1
    if count==1:
        for x in range(m):
            if (List[x][0] not in D_List) and (List[x][1] not in D_List):
                if v==List[x][1]:
                    D_List.append(v)
                    DFS(n,m,List[x][0],List)

n,m,v=sys.stdin.readline().rstrip().split(" ")

List=[]
for _ in range(int(m)):
    x,y=sys.stdin.readline().rstrip().split(" ")
    List.append([int(x),int(y)])
List.sort(key=lambda x: (x[0], x[1]))

D_List=[]
B_List=[]

DFS(int(n),int(m),int(v),List)

for x in D_List: sys.stdout.write(f"{x} ")
sys.stdout.write("\n")

B_List.append(int(v))
index=1
while (len(B_List)<int(n)):
    count=0
    for x in range(int(m)):
        if int(v)==List[x][0]:
            if List[x][1] not in B_List:
                B_List.append(List[x][1])
        if x==int(m)-1:count=1
    for x in range(int(m)):
        if int(v)==List[x][1]:
            if List[x][0] not in B_List:
                B_List.append(List[x][0])
    v=B_List[index]
    index+=1
        
for x in B_List: sys.stdout.write(f"{x} ")
#not end
