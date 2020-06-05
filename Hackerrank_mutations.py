a=input()
a=list(a)
var=list(map(str,input().split()))
pos=int(var[0])
cha=var[1]
a[pos]=cha
print(''.join(a))