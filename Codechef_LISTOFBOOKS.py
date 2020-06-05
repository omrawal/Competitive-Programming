n=int(input())
a=[]
var=list(map(int,input().split()))
t=int(input())
for i in range(t):
    k=int(input())
    k-=1
    aa=var.pop(k)
    a.append(aa)
for i in a:
    print(i)