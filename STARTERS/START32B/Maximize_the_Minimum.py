try:
    for _ in range(int(input())):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        l.sort()
        if k<n-1:
            print(l[k])
        else:
            print(l[n-1])
except:
    pass