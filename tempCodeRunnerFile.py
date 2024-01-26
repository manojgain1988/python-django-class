def add(a,*b):
    print(a)
    print(b)
    c=a
    for x in b:
        c=c+x
    print(c)

add(5,10,15,20)
