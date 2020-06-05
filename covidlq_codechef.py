def getIndexPositions(listOfElements, element):
    indexPosList = []
    indexPos = 0
    while True:
        try:
            indexPos = listOfElements.index(element, indexPos)
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
    return indexPosList


t=int(input())
for ti in range(0,t):
    n=int(input())
    li=list(map(int,input().split()))
    li_len=len(li)
    one_count=li.count(1)
    flag=0
    preflag=0
    # gap_len=0
    if(li_len<=6 and one_count==1):
        print("YES")
        preflag=1
    elif(li_len<=6 and one_count>1):
        print("NO")
        preflag=1
    elif(li_len>6 and one_count==1):
        print("YES")
        preflag=1
    else:
        a=getIndexPositions(li,1)
        for i in range(0,(len(a)-1)):
            j=i+1
            if(a[j]-a[i]<6):
                print("NO")
                preflag=1
                break
    if(flag==0 and preflag==0):
        print("YES")

