a=[1,2,3,4]
for i in a:
    print(i)
    a.pop(a.index(i))
    print(i)
print(a)