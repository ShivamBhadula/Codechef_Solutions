import math
try:

    def msb(num):
        k=int(math.log(num,2))
        return 1<<k

    for _ in range(int(input())):
        n=int(input())
        l1=list(map(int,input().split()))
        q=int(input())
        l2=[]
        for val in l1:
            l2.append(msb(val)) 
        for a in range(q):
            l,r,x=map(int,input().split())
            l3=l2[l-1:r]
            count=l3.count(msb(x))
            ans=len(l3)-count
            print(count)
except:
    pass