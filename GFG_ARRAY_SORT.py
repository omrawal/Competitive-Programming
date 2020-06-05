n=int(input())
for _ in range(n):
    t=int(input())
    var=list(map(int,input().split()))
    var=sorted(var)
    for i in var:
        print(str(i),end=" ")
    print()