import sys

num=int(sys.stdin.readline().rstrip())
List=[sys.stdin.readline().rstrip() for _ in range(num)]
List=set(List)
List=list(List)

List.sort(key=lambda x: (len(x),x))

for x in List:
    print(x)