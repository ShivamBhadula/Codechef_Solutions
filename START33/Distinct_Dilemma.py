try:
    for _ in range(int(input())):
        l=int(input())
        l=list(map(int,input().split()))
        s=sum(l)
        i=0
        ans=0
        while i<=s:
            ans+=1
            i=i+ans
        print(ans-1)
except:
    pass