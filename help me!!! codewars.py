n1=int(input())
n=int(input())
a=[]
for i in range(0,n):
    a.append(list(map(int,input().split())))
k=int(input())
c=list(map(int,input().split()))
final=[]
for i in c:
    final.append(i)
for i in a:
    for j in i:
        if(j in c and i[1]==j):
            final.append(j)
            final.append(i[0])
        elif(j in c and i[0]==j):
            final.append(j)
            final.append(i[1])
# print(final)
final=list(set(final))
# print(final)
print(len(final))   

