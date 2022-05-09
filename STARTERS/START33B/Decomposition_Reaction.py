try:
    n,m=map(int,input().split())
    l1=list(map(int,input().split()))
    for i in range(m):
        a,b=map(int,input().split())
        l2=list(map(int,input().split()))
        for j in range(0,len(l2),2):
            l1[l2[j+1]-1]=(l1[l2[j+1]-1]+l2[j]*l1[a-1])%1_000_000_007
        l1[a-1]=0
    for i in l1:
        print(i)

except:
    pass