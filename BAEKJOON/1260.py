import sys

def DFS(n,m,v,List=[],List1=[]):
    count=0
    for x in range(m):
        if (List[x][0] not in List1) and (List[x][1] not in List1):
            if v==List[x][0]:
                List1.append(v)
                DFS(n,m,List[x][1],List,List1)
        if x==m-1: count=1
    if count==1:
        for x in range(m):
            if (List[x][0] not in List1) and (List[x][1] not in List1):
                if v==List[x][1]:
                    List1.append(v)
                    DFS(n,m,List[x][0],List,List1)

n,m,v=sys.stdin.readline().rstrip().split(" ")
List=[]
for _ in range(int(m)):
    x,y=sys.stdin.readline().rstrip().split(" ")
    List.append([int(x),int(y)])
List.sort(key=lambda x: (x[0], x[1]))
D_List=[]
B_List=[]
DFS(int(n),int(m),int(v),List,D_List)
for i in range(1, int(n)+1):
    if i not in D_List:
        D_List.append(i)

while (len(B_List)<n):
    List
    
#not end
