### all correct

def calculate(a,n):
  num=len(a)-1
  asum=0
  while(num>0):
    asum+=(abs(a[num]-a[num-1])-1)
    num-=1
  return asum

t=int(input())
for _ in range(t):
  n=int(input())
  q=list(map(int,input().split()))
  ans=calculate(q,n)
  print(ans)
