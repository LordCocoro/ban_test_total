
def fibb(a):
    i=0
    b=1
    c=0
    for f in range(a):
        c = i + b
        i = b
        b = c
    print(i)

fibb(0)

