t=int(input())
for num in range(t):
    var=list(map(int,input().split()))
    max_val=var[1]
    a=list(map(int,input().split()))
    loss=0
    for i in a:
        if(i>max_val):
            loss=loss+(i-max_val)
    print(loss)