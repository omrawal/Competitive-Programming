import copy
n1=int(input())
n=int(input())
a=[]
for i in range(0,n):
    a.append(list(map(int,input().split())))
k=int(input())
c=list(map(int,input().split()))
aa=copy.deepcopy(a)
final=[]
fam=[]
temp=[]
for i in aa:
    
# it=0
# while(it<k):
#     key=c[it]
#     for j in a:
#         if(key in j):
#             if(j[0]==key):
#                 key=j[1]
#                 final.append(j[0]);final.append(j[1])
#                 a.pop(a.index(j))
#             elif(j[1]==key):
#                 # key=j[0]
#                 # final.append(j[0]);final.append(j[1])
#                 # a.pop(a.index(j))
#                 break
#     it+=1
# print(set(final))