# this type of array operation always creates problems so use a duplicate array or 
# use while loop and increment by 2 just like we did in scheduling algorithms
a=[1,2,3,4]
for i in a:
    print(i)
    a.pop(a.index(i))
    print(i)
print(a)
