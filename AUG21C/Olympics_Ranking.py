

#OLYRANK

try:
    for _ in range(int(input())):
        l1=list(map(int,input().split()))
        c1=sum(l1[0:3])
        c2=sum(l1[3:])
        if c1 > c2 :
            print(1)
        else:
            print(2)
except:
    pass
