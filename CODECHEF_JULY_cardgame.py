##### All Correct
def find_winner(a,b,n):
  a_score=0
  b_score=0
  for i in range(n):
    if(a[i]>b[i]):
      a_score+=1
    elif(a[i]<b[i]):
      b_score+=1
    elif(a[i]==b[i]):
      a_score+=1
      b_score+=1
  if(a_score>b_score):
    return(0,a_score)
  elif(a_score<b_score):
    return(1,b_score)
  else:
    return(2,a_score)
def sumDigits(no): 
      return 0 if no == 0 else int(no%10) + sumDigits(int(no/10))

t=int(input())
for _ in range(t):
  n=int(input())
  a=[]# a is chef 0
  b=[]# b is morty 1

  for i in range(n):
    a1,b1=(map(int,input().split()))
    
    a.append(sumDigits(a1))
    b.append(sumDigits(b1))
  winner,score=find_winner(a,b,n)
  print(winner,score)
  
