n=int(input())
a={}
for _ in range(n+1):
    s=input()
    s=list(s.split(" "))
    if(len(s)!=1):
        avg=(float(s[1])+float(s[2])+float(s[3]))/3
        a[s[0]]=avg
    else:
        print("%.2f"%(a[s[0]]))
