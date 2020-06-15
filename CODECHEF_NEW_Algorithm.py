var=list(map(int,input().split()))
limit_count=var[1]
number=str(var[0])
num_lst=list(number)
for i in range(0,len(num_lst)):
  num_lst[i]=int(num_lst[i])
for i in range(limit_count):
    if(num_lst[-1]==0):
        num_lst.pop(-1)
    else:
        num_lst[-1]-=1
s = [str(i) for i in num_lst] 
res = int("".join(s)) 
ans=int(res)
print(ans)