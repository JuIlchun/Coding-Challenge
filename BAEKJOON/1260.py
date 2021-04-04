import sys

def DFS(n,m,v,List=[]):
    count=0
    ind_f=0
    ind_s=0
    sys.stdout.write(f"{v} ")
    for x in range(m):
        if v==List[x][0]:
            ind_f=List[x][1]
            break
    for x in range(m):
        if v==List[x][1]:
            ind_s=List[x][0]
            break
    if ind_f==0 and ind_s!=0:
        D_List.append(v)
        DFS(n,m,List[ind_s],List)
    if ind_s==0 and ind_f!=0:
        D_List.append(v)
        DFS(n,m,List[ind_f],List)
    if ind_f!=0 and ind_s!=0:
        if ind_f>ind_s:
            D_List.append(v)
            DFS(n,m,List[ind_s],List)
        elif ind_s>ind_f:
            D_List.append(v)
            DFS(n,m,List[ind_f],List)
    if ind_f==0 and ind_s==0:
        DFS(n,m,List[ind_f],List)

    

n,m,v=sys.stdin.readline().rstrip().split(" ")

List=[]
for _ in range(int(m)):
    x,y=sys.stdin.readline().rstrip().split(" ")
    List.append([int(x),int(y)])
List.sort(key=lambda x: (x[0], x[1]))

D_List=[]
B_List=[]

DFS(int(n),int(m),int(v),List)
sys.stdout.write("\n")

B_List.append(int(v))
que=[v]
index=1
while (len(que)>0):
    v=que[0]
    count=0
    for x in range(int(m)):
        if int(v)==List[x][0]:
            if List[x][1] not in B_List:
                B_List.append(List[x][1])
                que.append(List[x][1])
        if x==int(m)-1:count=1
    for x in range(int(m)):
        if int(v)==List[x][1]:
            if List[x][0] not in B_List:
                B_List.append(List[x][0])
                que.append(List[x][0])
    del que[0]
    index+=1
        
for x in B_List: sys.stdout.write(f"{x} ")
