import string 
Small_list=list(string.ascii_lowercase)
big_list=list(string.ascii_uppercase)
# print(big_list)
# print(Small_list)
n=input()
n=list(n)
for i in range(0,len(n)):
    if(n[i] in Small_list):
        k=Small_list.index(n[i])
        n[i]=big_list[k]
    elif(n[i] in big_list):
        k=big_list.index(n[i])
        n[i]=Small_list[k]
    else:
        continue
print(''.join(n))
