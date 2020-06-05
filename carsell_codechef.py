import copy
def decrement(li):
    for i in range(0,len(li)):
        if(li[i]==0):
            li[i]=0
        else:
            li[i]-=1
    return li
t=int(input())
for ti in range(0,t):
    n=int(input())
    lit=list(map(int,input().split()))
    li=copy.deepcopy(lit)
    total_profit=0
    li.sort()
    li=li[::-1]
    while(len(li)>0):
        # print(li)
        total_profit+=li[0]
        li=decrement(li)
        li.pop(0)
    print(total_profit)
