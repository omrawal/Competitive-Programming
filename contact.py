'''
t=int(input("Enter the numbver of instances: "))
for i in range(0,t):
    text=input("Enter contact number: ")
    lst=list(text)
    num=int(text)
    if(1111111111<=num<=9999999999):
        ans="+91 "+text
        print(ans)
    elif(len(lst)>10):
        lst=lst[::-1]
        lst=lst[0:10]
        lst=lst[::-1]
        ans="+91 "
        for ele in lst:
            ans=ans+ele
        print(ans)
    else:
        print("Invalid input")
'''

def decor(fun):
    def inner():
        t=fun()
        for i in range(0,t):
            text=input("Enter contact number: ")
            lst=list(text)
            num=int(text)
            if(1111111111<=num<=9999999999):
                ans="+91 "+text
                print(ans)
                #return 1
                #yield 1
            elif(len(lst)>10):
                lst=lst[::-1]
                lst=lst[0:10]
                lst=lst[::-1]
                ans="+91 "
                for ele in lst:
                    ans=ans+ele
                print(ans)
                #return 1
                #yield 1
            else:
                print("Invalid input")
                #return 1
                #yield 1
    return inner
    #yield inner

@decor
def num():
    t=int(input("Enter the number of instances: "))
    return t

num()