try:
    for _ in range(int(input())):
        l=int(input())
        l1=list(map(int,input().split()))
        l2=list(map(int,input().split()))
        ans=0
        for i in l1:
            for j in l2:
                ans+=max(i^j,i&j)
        print(ans)
except:
    pass