
#BUS

# cook your dish here
try:
    for _ in range(int(input())):
        n,m,q=map(int,input().split())
        Consistent="Consistent"
        l2=[]
        for i in range(q):
            l1=list(input().split())
            ch=l1[0]
            val=int(l1[1])
            if ch=='-' and val not in l2:
                Consistent="Inconsistent"
                continue
            if ch=='+' and len(l2)>=m:
                Consistent="Inconsistent"
                continue
            if ch=='+' and val not in l2 and (len(l2)<m):
                l2.append(val)
            if ch=='-' and val in l2:
                l2.remove(val)
        print(Consistent)
except:
    pass
